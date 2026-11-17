/* =====================================================================
   AT-Integra | Programacao de Banco de Dados
   Stored procedure transacional de abertura de chamado.
   SGBD: Microsoft SQL Server 2022
   ===================================================================== */
CREATE OR ALTER PROCEDURE dbo.sp_AbrirChamado
    @ClienteId      UNIQUEIDENTIFIER,
    @ContratoId     UNIQUEIDENTIFIER,
    @Titulo         VARCHAR(120),
    @Descricao      VARCHAR(4000),
    @Prioridade     TINYINT,
    @UsuarioLogin   VARCHAR(100),
    @ChamadoId      UNIQUEIDENTIFIER OUTPUT,
    @Protocolo      VARCHAR(20)      OUTPUT
AS
BEGIN
    SET NOCOUNT ON;
    SET XACT_ABORT ON;                        -- desfaz a transacao em erro grave
    SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

    DECLARE @NivelSla   CHAR(6),
            @PrazoSla   DATETIME2(0),
            @Abertura   DATETIME2(0) = SYSUTCDATETIME();

    BEGIN TRY
        BEGIN TRANSACTION;

        /* Bloqueio de linha do contrato: impede que uma renegociacao
           concorrente altere o nivel de SLA durante o calculo do prazo. */
        SELECT @NivelSla = NivelSla
          FROM dbo.Contrato WITH (UPDLOCK, ROWLOCK)
         WHERE ContratoId = @ContratoId
           AND ClienteId  = @ClienteId
           AND Ativo      = 1
           AND @Abertura BETWEEN VigenciaInicio AND VigenciaFim;

        IF @NivelSla IS NULL
            THROW 50010, 'Contrato inexistente, inativo ou fora de vigencia.', 1;

        IF @Prioridade NOT BETWEEN 1 AND 4
            THROW 50011, 'Prioridade invalida. Valores aceitos: 1 a 4.', 1;

        SET @ChamadoId = NEWID();
        SET @Protocolo = CONCAT('AT', FORMAT(@Abertura, 'yyyyMMdd'), '-',
                                UPPER(LEFT(CONVERT(VARCHAR(36), @ChamadoId), 6)));

        -- Funcao escalar reaproveitada pela API e pelos relatorios gerenciais.
        SET @PrazoSla = dbo.fn_CalcularPrazoSla(@Abertura, @NivelSla, @Prioridade);

        INSERT INTO dbo.Chamado
              (ChamadoId, Protocolo, ClienteId, ContratoId, Titulo, Descricao,
               Prioridade, Status, PrazoSla, CriadoEm, CriadoPor, Ativo)
        VALUES (@ChamadoId, @Protocolo, @ClienteId, @ContratoId, @Titulo, @Descricao,
               @Prioridade, 1, @PrazoSla, @Abertura, @UsuarioLogin, 1);

        INSERT INTO dbo.ChamadoHistorico
              (ChamadoId, StatusAnterior, StatusNovo, Observacao, RegistradoEm, RegistradoPor)
        VALUES (@ChamadoId, NULL, 1, 'Abertura via portal corporativo',
               @Abertura, @UsuarioLogin);

        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        IF XACT_STATE() <> 0 ROLLBACK TRANSACTION;

        INSERT INTO dbo.LogErro (Procedimento, Mensagem, NumeroErro, OcorridoEm, Usuario)
        VALUES (ERROR_PROCEDURE(), ERROR_MESSAGE(), ERROR_NUMBER(),
                SYSUTCDATETIME(), @UsuarioLogin);

        THROW;                                 -- repassa o erro a camada .NET
    END CATCH
END;
GO

/* ---------------------------------------------------------------------
   Consulta paginada do painel operacional (keyset/OFFSET-FETCH).
   Evita SELECT * e devolve somente as colunas usadas pela interface.
   --------------------------------------------------------------------- */
CREATE OR ALTER PROCEDURE dbo.sp_ListarPainelOperacional
    @ClienteId      UNIQUEIDENTIFIER,
    @Pagina         INT = 1,
    @TamanhoPagina  INT = 20
AS
BEGIN
    SET NOCOUNT ON;

    SELECT  c.ChamadoId,
            c.Protocolo,
            c.Titulo,
            c.Prioridade,
            c.Status,
            c.PrazoSla,
            t.Nome AS Tecnico,
            CASE WHEN ISNULL(c.ResolvidoEm, SYSUTCDATETIME()) > c.PrazoSla
                 THEN 1 ELSE 0 END AS SlaViolado
      FROM  dbo.Chamado      AS c
      LEFT  JOIN dbo.Tecnico AS t ON t.TecnicoId = c.TecnicoId
     WHERE  c.ClienteId = @ClienteId
       AND  c.Ativo     = 1
       AND  c.Status   IN (1, 2, 3)
     ORDER  BY c.Prioridade DESC, c.PrazoSla ASC
    OFFSET (@Pagina - 1) * @TamanhoPagina ROWS
     FETCH NEXT @TamanhoPagina ROWS ONLY
    OPTION (RECOMPILE);                        -- evita parameter sniffing
END;
GO
