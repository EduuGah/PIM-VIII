using System;
using System.Collections.Generic;
using System.Linq.Expressions;
using System.Threading.Tasks;
using AlunosTech.Domain.Entidades;

namespace AlunosTech.Domain.Interfaces
{
    /// <summary>Contrato generico do padrao Repository.</summary>
    public interface IRepositorio<T> where T : EntidadeBase
    {
        Task<T> ObterPorIdAsync(Guid id);
        Task<IEnumerable<T>> ListarAsync(Expression<Func<T, bool>> filtro);
        Task AdicionarAsync(T entidade);
        void Atualizar(T entidade);
    }

    /// <summary>Repositorio especializado do agregado Chamado.</summary>
    public interface IChamadoRepositorio : IRepositorio<Chamado>
    {
        Task<IEnumerable<Chamado>> ObterPainelOperacionalAsync(Guid clienteId, int pagina, int tamanho);
        Task<int> ContarSlaVioladoAsync(DateTime inicio, DateTime fim);
    }

    /// <summary>Padrao Unit of Work: garante atomicidade entre repositorios.</summary>
    public interface IUnitOfWork : IDisposable
    {
        IChamadoRepositorio Chamados { get; }
        Task<int> ConfirmarAsync();
        Task DescartarAsync();
    }
}
