/* =====================================================================
   AT-Integra | Esquema fisico (recorte das tabelas centrais)
   SGBD: Microsoft SQL Server 2022 | Collation: Latin1_General_CI_AI
   ===================================================================== */
CREATE TABLE dbo.Cliente
(
    ClienteId     UNIQUEIDENTIFIER NOT NULL CONSTRAINT PK_Cliente PRIMARY KEY,
    RazaoSocial   VARCHAR(150)     NOT NULL,
    CpfCnpj       VARCHAR(18)      NOT NULL CONSTRAINT UQ_Cliente_Documento UNIQUE,
    Segmento      VARCHAR(60)      NULL,
    CriadoEm      DATETIME2(0)     NOT NULL CONSTRAINT DF_Cliente_Criado DEFAULT SYSUTCDATETIME(),
    Ativo         BIT              NOT NULL CONSTRAINT DF_Cliente_Ativo  DEFAULT 1
);

CREATE TABLE dbo.Contrato
(
    ContratoId      UNIQUEIDENTIFIER NOT NULL CONSTRAINT PK_Contrato PRIMARY KEY,
    ClienteId       UNIQUEIDENTIFIER NOT NULL,
    NivelSla        CHAR(6)          NOT NULL,
    ValorMensal     DECIMAL(12,2)    NOT NULL,
    EmailResponsavel VARCHAR(120)    NOT NULL,
    VigenciaInicio  DATE             NOT NULL,
    VigenciaFim     DATE             NOT NULL,
    Ativo           BIT              NOT NULL CONSTRAINT DF_Contrato_Ativo DEFAULT 1,
    CONSTRAINT FK_Contrato_Cliente FOREIGN KEY (ClienteId)
        REFERENCES dbo.Cliente (ClienteId),
    CONSTRAINT CK_Contrato_Nivel  CHECK (NivelSla IN ('GOLD', 'SILVER')),
    CONSTRAINT CK_Contrato_Vigencia CHECK (VigenciaFim > VigenciaInicio)
);

CREATE TABLE dbo.Tecnico
(
    TecnicoId         UNIQUEIDENTIFIER NOT NULL CONSTRAINT PK_Tecnico PRIMARY KEY,
    Nome              VARCHAR(120)     NOT NULL,
    Especialidade     VARCHAR(60)      NOT NULL,
    CertificadoNivel2 BIT              NOT NULL CONSTRAINT DF_Tecnico_Cert DEFAULT 0,
    Ativo             BIT              NOT NULL CONSTRAINT DF_Tecnico_Ativo DEFAULT 1
);

CREATE TABLE dbo.Chamado
(
    ChamadoId    UNIQUEIDENTIFIER NOT NULL CONSTRAINT PK_Chamado PRIMARY KEY,
    Protocolo    VARCHAR(20)      NOT NULL CONSTRAINT UQ_Chamado_Protocolo UNIQUE,
    ClienteId    UNIQUEIDENTIFIER NOT NULL,
    ContratoId   UNIQUEIDENTIFIER NOT NULL,
    TecnicoId    UNIQUEIDENTIFIER NULL,
    Titulo       VARCHAR(120)     NOT NULL,
    Descricao    VARCHAR(4000)    NULL,
    Prioridade   TINYINT          NOT NULL,
    Status       TINYINT          NOT NULL,
    PrazoSla     DATETIME2(0)     NULL,
    ResolvidoEm  DATETIME2(0)     NULL,
    CriadoEm     DATETIME2(0)     NOT NULL CONSTRAINT DF_Chamado_Criado DEFAULT SYSUTCDATETIME(),
    CriadoPor    VARCHAR(100)     NOT NULL,
    AtualizadoEm DATETIME2(0)     NULL,
    Ativo        BIT              NOT NULL CONSTRAINT DF_Chamado_Ativo DEFAULT 1,
    Versao       ROWVERSION       NOT NULL,
    CONSTRAINT FK_Chamado_Cliente  FOREIGN KEY (ClienteId)  REFERENCES dbo.Cliente (ClienteId),
    CONSTRAINT FK_Chamado_Contrato FOREIGN KEY (ContratoId) REFERENCES dbo.Contrato (ContratoId),
    CONSTRAINT FK_Chamado_Tecnico  FOREIGN KEY (TecnicoId)  REFERENCES dbo.Tecnico (TecnicoId),
    CONSTRAINT CK_Chamado_Prioridade CHECK (Prioridade BETWEEN 1 AND 4),
    CONSTRAINT CK_Chamado_Status     CHECK (Status BETWEEN 1 AND 5)
)
/* Particionamento por competencia: distribui o historico em filegroups
   distintos, acelerando a purga e as consultas por periodo. */
ON ps_ChamadoPorCompetencia (CriadoEm);

CREATE TABLE dbo.ApontamentoHoras
(
    ApontamentoId UNIQUEIDENTIFIER NOT NULL CONSTRAINT PK_Apontamento PRIMARY KEY,
    ChamadoId     UNIQUEIDENTIFIER NOT NULL,
    TecnicoId     UNIQUEIDENTIFIER NOT NULL,
    Inicio        DATETIME2(0)     NOT NULL,
    Fim           DATETIME2(0)     NOT NULL,
    Atividade     VARCHAR(400)     NOT NULL,
    CONSTRAINT FK_Apontamento_Chamado FOREIGN KEY (ChamadoId)
        REFERENCES dbo.Chamado (ChamadoId) ON DELETE CASCADE,
    CONSTRAINT CK_Apontamento_Periodo CHECK (Fim > Inicio)
);

CREATE TABLE dbo.ChamadoHistorico
(
    HistoricoId    BIGINT IDENTITY(1,1) CONSTRAINT PK_Historico PRIMARY KEY,
    ChamadoId      UNIQUEIDENTIFIER NOT NULL,
    StatusAnterior TINYINT          NULL,
    StatusNovo     TINYINT          NOT NULL,
    Observacao     VARCHAR(400)     NULL,
    RegistradoEm   DATETIME2(0)     NOT NULL,
    RegistradoPor  VARCHAR(100)     NOT NULL
);

CREATE TABLE dbo.LogErro
(
    LogErroId     BIGINT IDENTITY(1,1) CONSTRAINT PK_LogErro PRIMARY KEY,
    Procedimento  VARCHAR(150) NULL,
    Mensagem      VARCHAR(2000) NOT NULL,
    NumeroErro    INT NULL,
    OcorridoEm    DATETIME2(0) NOT NULL,
    Usuario       VARCHAR(100) NULL
);
GO
