/* =====================================================================
   AT-Integra | Funcoes definidas pelo usuario
   ===================================================================== */

/* Funcao escalar: converte nivel de contrato + prioridade em prazo limite.
   Centraliza a regra para que API, relatorios e procedures usem o mesmo
   calculo, eliminando divergencia de resultados entre camadas. */
CREATE OR ALTER FUNCTION dbo.fn_CalcularPrazoSla
(
    @Abertura   DATETIME2(0),
    @NivelSla   CHAR(6),
    @Prioridade TINYINT
)
RETURNS DATETIME2(0)
WITH SCHEMABINDING
AS
BEGIN
    DECLARE @Horas INT;

    SET @Horas =
        CASE @NivelSla
            WHEN 'GOLD'   THEN CASE @Prioridade WHEN 4 THEN 2  WHEN 3 THEN 4
                                                WHEN 2 THEN 12 ELSE 24 END
            WHEN 'SILVER' THEN CASE @Prioridade WHEN 4 THEN 4  WHEN 3 THEN 8
                                                WHEN 2 THEN 24 ELSE 48 END
            ELSE 72
        END;

    RETURN DATEADD(HOUR, @Horas, @Abertura);
END;
GO

/* Funcao com valor de tabela em linha (inline TVF): o otimizador expande o
   corpo na consulta chamadora, permitindo uso dos indices das tabelas base.
   Alternativa de melhor desempenho em relacao a TVF multi-statement. */
CREATE OR ALTER FUNCTION dbo.fn_ProdutividadeTecnico
(
    @Inicio DATE,
    @Fim    DATE
)
RETURNS TABLE
AS
RETURN
(
    SELECT  t.TecnicoId,
            t.Nome,
            COUNT(DISTINCT c.ChamadoId)                         AS ChamadosAtendidos,
            SUM(DATEDIFF(MINUTE, a.Inicio, a.Fim)) / 60.0       AS HorasApontadas,
            AVG(DATEDIFF(MINUTE, c.CriadoEm, c.ResolvidoEm)) / 60.0 AS TempoMedioHoras,
            SUM(CASE WHEN c.ResolvidoEm > c.PrazoSla THEN 1 ELSE 0 END) AS SlaViolados
      FROM  dbo.Tecnico            AS t
      INNER JOIN dbo.Chamado       AS c ON c.TecnicoId = t.TecnicoId
      INNER JOIN dbo.ApontamentoHoras AS a ON a.ChamadoId = c.ChamadoId
     WHERE  c.ResolvidoEm IS NOT NULL
       AND  CAST(c.ResolvidoEm AS DATE) BETWEEN @Inicio AND @Fim
     GROUP  BY t.TecnicoId, t.Nome
);
GO
