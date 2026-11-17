using System;
using System.ComponentModel.DataAnnotations;
using AlunosTech.Domain.Entidades;

namespace AlunosTech.Application.DTOs
{
    /// <summary>Dados de entrada do caso de uso de abertura de chamado.</summary>
    public class AberturaChamadoDto
    {
        [Required] public Guid ClienteId { get; set; }
        [Required] public Guid ContratoId { get; set; }

        [Required, StringLength(120, MinimumLength = 5)]
        public string Titulo { get; set; } = string.Empty;

        [Required, StringLength(4000)]
        public string Descricao { get; set; } = string.Empty;

        [Range(1, 4)] public PrioridadeChamado Prioridade { get; set; }
    }

    /// <summary>Projecao de saida; evita expor a entidade de dominio na API.</summary>
    public class ChamadoRespostaDto
    {
        public Guid Id { get; set; }
        public string Protocolo { get; set; } = string.Empty;
        public string Titulo { get; set; } = string.Empty;
        public string Status { get; set; } = string.Empty;
        public string Prioridade { get; set; } = string.Empty;
        public DateTime? PrazoSla { get; set; }
        public bool SlaViolado { get; set; }

        public static ChamadoRespostaDto De(Chamado c) => new()
        {
            Id = c.Id,
            Protocolo = c.Protocolo,
            Titulo = c.Titulo,
            Status = c.Status.ToString(),
            Prioridade = c.Prioridade.ToString(),
            PrazoSla = c.PrazoSla,
            SlaViolado = c.SlaViolado
        };
    }
}
