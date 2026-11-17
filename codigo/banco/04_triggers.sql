/* =====================================================================
   AT-Integra | Gatilhos de auditoria e integridade
   ===================================================================== */

/* AFTER UPDATE: trilha de auditoria imutavel das mudancas de status.
   Escrito em logica de conjunto (set-based) para suportar atualizacoes
   em lote sem degradar o desempenho. */
CREATE OR ALTER TRIGGER dbo.trg_Chamado_AuditarStatus
ON dbo.Chamado
AFTER UPDATE
AS
BEGIN
    SET NOCOUNT ON;

    IF NOT UPDATE(Status) RETURN;

    INSERT INTO dbo.ChamadoHistorico
          (ChamadoId, StatusAnterior, StatusNovo, Observacao, RegistradoEm, RegistradoPor)
    SELECT  i.ChamadoId,
            d.Status,
            i.Status,
            CONCAT('Transicao automatica ', d.Status, ' -> ', i.Status),
            SYSUTCDATETIME(),
            SUSER_SNAME()
      FROM  inserted AS i
      INNER JOIN deleted AS d ON d.ChamadoId = i.ChamadoId
     WHERE  i.Status <> d.Status;
END;
GO

/* INSTEAD OF DELETE: converte a exclusao fisica em exclusao logica,
   preservando o historico exigido pela politica de retencao e pela LGPD. */
CREATE OR ALTER TRIGGER dbo.trg_Chamado_ExclusaoLogica
ON dbo.Chamado
INSTEAD OF DELETE
AS
BEGIN
    SET NOCOUNT ON;

    UPDATE  c
       SET  c.Ativo        = 0,
            c.AtualizadoEm = SYSUTCDATETIME()
      FROM  dbo.Chamado AS c
     INNER JOIN deleted AS d ON d.ChamadoId = c.ChamadoId;

    INSERT INTO dbo.ChamadoHistorico
          (ChamadoId, StatusAnterior, StatusNovo, Observacao, RegistradoEm, RegistradoPor)
    SELECT  d.ChamadoId, d.Status, d.Status,
            'Exclusao logica solicitada', SYSUTCDATETIME(), SUSER_SNAME()
      FROM  deleted AS d;
END;
GO

/* AFTER INSERT/UPDATE: regra de negocio que impede atribuir chamado a
   tecnico sem a certificacao exigida pela categoria do servico. */
CREATE OR ALTER TRIGGER dbo.trg_Chamado_ValidarCertificacao
ON dbo.Chamado
AFTER INSERT, UPDATE
AS
BEGIN
    SET NOCOUNT ON;

    IF EXISTS (
        SELECT 1
          FROM inserted AS i
          INNER JOIN dbo.Tecnico AS t ON t.TecnicoId = i.TecnicoId
         WHERE i.Prioridade = 4
           AND t.CertificadoNivel2 = 0)
    BEGIN
        ROLLBACK TRANSACTION;
        THROW 50020,
              'Chamado critico exige tecnico com certificacao de nivel 2.', 1;
    END
END;
GO
