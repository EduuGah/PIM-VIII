using System;
using System.Collections.Generic;
using AlunosTech.Domain.Servicos;

namespace AlunosTech.Domain.Entidades
{
    public enum PrioridadeChamado { Baixa = 1, Media = 2, Alta = 3, Critica = 4 }

    public enum StatusChamado { Aberto = 1, EmAtendimento = 2, Pendente = 3, Resolvido = 4, Encerrado = 5 }

    /// <summary>
    /// Raiz de agregacao do modulo de Service Desk. Concentra as regras de
    /// negocio do ciclo de vida do chamado e do calculo de SLA.
    /// </summary>
    public class Chamado : EntidadeBase
    {
        private readonly List<ApontamentoHoras> _apontamentos = new();

        protected Chamado() { }   // exigido pelo Entity Framework Core

        public Chamado(Guid clienteId, string titulo, string descricao,
                       PrioridadeChamado prioridade, Guid contratoId)
        {
            ClienteId = clienteId;
            ContratoId = contratoId;
            Titulo = titulo;
            Descricao = descricao;
            Prioridade = prioridade;
            Status = StatusChamado.Aberto;
            Protocolo = GerarProtocolo();
            Validar();
        }

        public string Protocolo { get; private set; } = string.Empty;
        public Guid ClienteId { get; private set; }
        public Guid ContratoId { get; private set; }
        public Guid? TecnicoId { get; private set; }
        public string Titulo { get; private set; } = string.Empty;
        public string Descricao { get; private set; } = string.Empty;
        public PrioridadeChamado Prioridade { get; private set; }
        public StatusChamado Status { get; private set; }
        public DateTime? PrazoSla { get; private set; }
        public DateTime? ResolvidoEm { get; private set; }

        public IReadOnlyCollection<ApontamentoHoras> Apontamentos => _apontamentos.AsReadOnly();

        /// <summary>Indica se o chamado violou o prazo contratado.</summary>
        public bool SlaViolado =>
            PrazoSla.HasValue && (ResolvidoEm ?? DateTime.UtcNow) > PrazoSla.Value;

        /// <summary>
        /// Define o prazo de atendimento delegando o calculo a estrategia
        /// correspondente ao nivel de servico do contrato (padrao Strategy).
        /// </summary>
        public void DefinirSla(ICalculoSlaStrategy estrategia)
        {
            if (estrategia is null) throw new ArgumentNullException(nameof(estrategia));
            PrazoSla = estrategia.CalcularPrazo(CriadoEm, Prioridade);
            MarcarAtualizacao();
        }

        public void Atribuir(Guid tecnicoId)
        {
            if (Status is StatusChamado.Resolvido or StatusChamado.Encerrado)
                throw new InvalidOperationException("Chamado encerrado nao pode ser reatribuido.");

            TecnicoId = tecnicoId;
            Status = StatusChamado.EmAtendimento;
            MarcarAtualizacao();
        }

        public void Resolver(string solucao)
        {
            if (TecnicoId is null)
                throw new InvalidOperationException("Chamado sem tecnico responsavel.");
            if (string.IsNullOrWhiteSpace(solucao))
                throw new ArgumentException("A solucao aplicada deve ser informada.");

            Descricao += Environment.NewLine + "[SOLUCAO] " + solucao;
            Status = StatusChamado.Resolvido;
            ResolvidoEm = DateTime.UtcNow;
            MarcarAtualizacao();
        }

        public void RegistrarApontamento(ApontamentoHoras apontamento)
        {
            if (Status == StatusChamado.Encerrado)
                throw new InvalidOperationException("Chamado encerrado nao aceita apontamentos.");
            _apontamentos.Add(apontamento);
            MarcarAtualizacao();
        }

        public override void Validar()
        {
            if (string.IsNullOrWhiteSpace(Titulo) || Titulo.Length < 5)
                throw new ArgumentException("Titulo deve possuir ao menos 5 caracteres.");
            if (ClienteId == Guid.Empty)
                throw new ArgumentException("Chamado deve estar vinculado a um cliente.");
            if (ContratoId == Guid.Empty)
                throw new ArgumentException("Chamado deve estar vinculado a um contrato.");
        }

        private static string GerarProtocolo()
        {
            var sufixo = Guid.NewGuid().ToString("N").Substring(0, 6).ToUpperInvariant();
            return string.Concat("AT", DateTime.UtcNow.ToString("yyyyMMdd"), "-", sufixo);
        }
    }
}
