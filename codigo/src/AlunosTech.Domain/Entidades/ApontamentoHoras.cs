using System;

namespace AlunosTech.Domain.Entidades
{
    /// <summary>
    /// Registro de horas tecnicas consumidas no atendimento de um chamado.
    /// Utilizado tanto no faturamento quanto no indicador de produtividade.
    /// </summary>
    public class ApontamentoHoras : EntidadeBase
    {
        protected ApontamentoHoras() { }

        public ApontamentoHoras(Guid chamadoId, Guid tecnicoId,
                                DateTime inicio, DateTime fim, string atividade)
        {
            ChamadoId = chamadoId;
            TecnicoId = tecnicoId;
            Inicio = inicio;
            Fim = fim;
            Atividade = atividade;
            Validar();
        }

        public Guid ChamadoId { get; private set; }
        public Guid TecnicoId { get; private set; }
        public DateTime Inicio { get; private set; }
        public DateTime Fim { get; private set; }
        public string Atividade { get; private set; } = string.Empty;

        public decimal HorasTrabalhadas => (decimal)(Fim - Inicio).TotalHours;

        public override void Validar()
        {
            if (Fim <= Inicio)
                throw new ArgumentException("A hora final deve ser posterior a inicial.");
            if (HorasTrabalhadas > 12)
                throw new ArgumentException("Apontamento unico nao pode exceder 12 horas.");
            if (string.IsNullOrWhiteSpace(Atividade))
                throw new ArgumentException("A atividade executada deve ser descrita.");
        }
    }
}
