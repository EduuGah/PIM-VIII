using System;
using AlunosTech.Domain.Entidades;

namespace AlunosTech.Domain.Servicos
{
    /// <summary>Contrato do padrao Strategy para o calculo de prazo de SLA.</summary>
    public interface ICalculoSlaStrategy
    {
        string Nivel { get; }
        DateTime CalcularPrazo(DateTime abertura, PrioridadeChamado prioridade);
    }

    /// <summary>SLA Gold: cobertura 24x7, sem desconto de horario comercial.</summary>
    public sealed class SlaGoldStrategy : ICalculoSlaStrategy
    {
        public string Nivel => "GOLD";

        public DateTime CalcularPrazo(DateTime abertura, PrioridadeChamado prioridade) =>
            prioridade switch
            {
                PrioridadeChamado.Critica => abertura.AddHours(2),
                PrioridadeChamado.Alta    => abertura.AddHours(4),
                PrioridadeChamado.Media   => abertura.AddHours(12),
                _                         => abertura.AddHours(24)
            };
    }

    /// <summary>SLA Silver: prazos contados apenas em horario comercial (8h-18h).</summary>
    public sealed class SlaSilverStrategy : ICalculoSlaStrategy
    {
        public string Nivel => "SILVER";

        public DateTime CalcularPrazo(DateTime abertura, PrioridadeChamado prioridade)
        {
            var horas = prioridade switch
            {
                PrioridadeChamado.Critica => 4,
                PrioridadeChamado.Alta    => 8,
                PrioridadeChamado.Media   => 24,
                _                         => 48
            };
            return AdicionarHorasUteis(abertura, horas);
        }

        private static DateTime AdicionarHorasUteis(DateTime inicio, int horas)
        {
            var atual = inicio;
            while (horas > 0)
            {
                atual = atual.AddHours(1);
                var diaUtil = atual.DayOfWeek != DayOfWeek.Saturday
                           && atual.DayOfWeek != DayOfWeek.Sunday;
                if (diaUtil && atual.Hour >= 8 && atual.Hour < 18) horas--;
            }
            return atual;
        }
    }

    /// <summary>
    /// Fabrica que resolve a estrategia a partir do nivel de servico registrado
    /// no contrato do cliente (padrao Factory Method).
    /// </summary>
    public static class SlaStrategyFactory
    {
        public static ICalculoSlaStrategy Criar(string nivelContrato)
        {
            var nivel = (nivelContrato ?? string.Empty).Trim().ToUpperInvariant();
            return nivel switch
            {
                "GOLD"   => new SlaGoldStrategy(),
                "SILVER" => new SlaSilverStrategy(),
                _ => throw new NotSupportedException("Nivel de SLA nao suportado: " + nivel)
            };
        }
    }
}
