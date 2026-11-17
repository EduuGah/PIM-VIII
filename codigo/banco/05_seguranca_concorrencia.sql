/* =====================================================================
   AT-Integra | Seguranca, controle de concorrencia e otimizacao
   ===================================================================== */

/* ---------- 1. Controle de acesso baseado em papeis ---------- */
CREATE ROLE rl_atendimento;
CREATE ROLE rl_supervisao;
CREATE ROLE rl_relatorios;

-- Principio do menor privilegio: nenhum papel recebe acesso direto as tabelas.
GRANT EXECUTE ON dbo.sp_AbrirChamado            TO rl_atendimento;
GRANT EXECUTE ON dbo.sp_ListarPainelOperacional TO rl_atendimento, rl_supervisao;
GRANT SELECT   ON dbo.vw_IndicadoresSla         TO rl_relatorios;

DENY  SELECT   ON dbo.Cliente (CpfCnpj)         TO rl_atendimento;
GO

/* ---------- 2. Seguranca em nivel de linha (RLS) ---------- */
CREATE FUNCTION seg.fn_FiltroCliente(@ClienteId UNIQUEIDENTIFIER)
RETURNS TABLE
WITH SCHEMABINDING
AS
RETURN SELECT 1 AS Permitido
        WHERE @ClienteId = CAST(SESSION_CONTEXT(N'ClienteId') AS UNIQUEIDENTIFIER)
           OR IS_MEMBER('rl_supervisao') = 1;
GO

CREATE SECURITY POLICY seg.pol_ChamadoPorCliente
ADD FILTER PREDICATE seg.fn_FiltroCliente(ClienteId) ON dbo.Chamado
WITH (STATE = ON);
GO

/* ---------- 3. Mascaramento dinamico e criptografia ---------- */
ALTER TABLE dbo.Cliente
ALTER COLUMN CpfCnpj ADD MASKED WITH (FUNCTION = 'partial(3,"*****",2)');

ALTER TABLE dbo.Usuario
ALTER COLUMN SenhaHash VARBINARY(256)
ENCRYPTED WITH (COLUMN_ENCRYPTION_KEY = cek_AtIntegra,
                ENCRYPTION_TYPE = DETERMINISTIC,
                ALGORITHM = 'AEAD_AES_256_CBC_HMAC_SHA_256');
GO

/* ---------- 4. Controle de concorrencia otimista ---------- */
/* A coluna rowversion e comparada no UPDATE: se outra sessao alterou a
   linha, nenhuma linha e afetada e a aplicacao recebe o erro de conflito. */
CREATE OR ALTER PROCEDURE dbo.sp_AtualizarStatusChamado
    @ChamadoId  UNIQUEIDENTIFIER,
    @StatusNovo TINYINT,
    @Versao     ROWVERSION
AS
BEGIN
    SET NOCOUNT ON;

    UPDATE dbo.Chamado
       SET Status = @StatusNovo,
           AtualizadoEm = SYSUTCDATETIME()
     WHERE ChamadoId = @ChamadoId
       AND Versao    = @Versao;

    IF @@ROWCOUNT = 0
        THROW 50030,
              'Registro alterado por outro usuario. Recarregue o chamado.', 1;
END;
GO

/* Controle pessimista pontual: a distribuicao automatica de chamados usa
   bloqueio de aplicacao para que duas instancias do servico em nuvem nao
   atribuam o mesmo chamado simultaneamente. */
CREATE OR ALTER PROCEDURE dbo.sp_DistribuirProximoChamado
    @TecnicoId UNIQUEIDENTIFIER
AS
BEGIN
    SET NOCOUNT ON;
    BEGIN TRANSACTION;

    EXEC sp_getapplock @Resource = 'fila_distribuicao',
                       @LockMode = 'Exclusive',
                       @LockTimeout = 5000;

    UPDATE TOP (1) dbo.Chamado
       SET TecnicoId = @TecnicoId, Status = 2
     OUTPUT inserted.ChamadoId, inserted.Protocolo
     WHERE TecnicoId IS NULL AND Status = 1;

    EXEC sp_releaseapplock @Resource = 'fila_distribuicao';
    COMMIT TRANSACTION;
END;
GO

/* ---------- 5. Otimizacao de consultas ---------- */
/* Indice composto com colunas incluidas: atende integralmente a consulta do
   painel operacional (covering index), eliminando operacoes de Key Lookup. */
CREATE NONCLUSTERED INDEX IX_Chamado_Painel
    ON dbo.Chamado (ClienteId, Status, Prioridade DESC)
    INCLUDE (Protocolo, Titulo, PrazoSla, TecnicoId, ResolvidoEm)
    WHERE Ativo = 1;                           -- indice filtrado
GO

/* Visao indexada para o painel gerencial de SLA, materializando a
   agregacao mensal consultada com alta frequencia pelo dashboard. */
CREATE OR ALTER VIEW dbo.vw_IndicadoresSla
WITH SCHEMABINDING
AS
SELECT  ClienteId,
        DATEFROMPARTS(YEAR(CriadoEm), MONTH(CriadoEm), 1) AS Competencia,
        COUNT_BIG(*)                                      AS TotalChamados,
        SUM(CASE WHEN ResolvidoEm > PrazoSla THEN 1 ELSE 0 END) AS Violacoes
  FROM  dbo.Chamado
 GROUP  BY ClienteId, DATEFROMPARTS(YEAR(CriadoEm), MONTH(CriadoEm), 1);
GO

CREATE UNIQUE CLUSTERED INDEX IX_vw_IndicadoresSla
    ON dbo.vw_IndicadoresSla (ClienteId, Competencia);
GO
