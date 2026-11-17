using System;

namespace AlunosTech.Domain.Entidades
{
    /// <summary>
    /// Classe abstrata que concentra o estado comum a todas as entidades
    /// persistentes da plataforma AT-Integra. Aplica encapsulamento (setters
    /// protegidos) e serve de ponto de extensao para heranca e polimorfismo.
    /// </summary>
    public abstract class EntidadeBase
    {
        public Guid Id { get; protected set; } = Guid.NewGuid();
        public DateTime CriadoEm { get; protected set; } = DateTime.UtcNow;
        public DateTime? AtualizadoEm { get; protected set; }
        public bool Ativo { get; protected set; } = true;

        /// <summary>Token de concorrencia otimista mapeado na coluna rowversion.</summary>
        public byte[] Versao { get; protected set; } = Array.Empty<byte>();

        /// <summary>Cada entidade concreta define suas proprias regras de validacao.</summary>
        public abstract void Validar();

        public void MarcarAtualizacao() => AtualizadoEm = DateTime.UtcNow;

        public void Inativar()
        {
            Ativo = false;
            MarcarAtualizacao();
        }
    }
}
