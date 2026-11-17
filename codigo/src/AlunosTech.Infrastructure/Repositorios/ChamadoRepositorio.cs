using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Linq.Expressions;
using System.Threading.Tasks;
using AlunosTech.Domain.Entidades;
using AlunosTech.Domain.Interfaces;
using AlunosTech.Infrastructure.Data;
using Dapper;
using Microsoft.EntityFrameworkCore;

namespace AlunosTech.Infrastructure.Repositorios
{
    /// <summary>
    /// Implementacao do repositorio de chamados. Operacoes transacionais usam
    /// Entity Framework Core; consultas analiticas de alto volume usam Dapper
    /// sobre stored procedures, evitando o custo do change tracker.
    /// </summary>
    public class ChamadoRepositorio : IChamadoRepositorio
    {
        private readonly AtIntegraDbContext _contexto;

        public ChamadoRepositorio(AtIntegraDbContext contexto) => _contexto = contexto;

        public async Task<Chamado> ObterPorIdAsync(Guid id) =>
            await _contexto.Chamados
                           .Include(c => c.Apontamentos)
                           .FirstOrDefaultAsync(c => c.Id == id && c.Ativo);

        public async Task<IEnumerable<Chamado>> ListarAsync(Expression<Func<Chamado, bool>> filtro) =>
            await _contexto.Chamados.AsNoTracking().Where(filtro).ToListAsync();

        public async Task AdicionarAsync(Chamado entidade) =>
            await _contexto.Chamados.AddAsync(entidade);

        public void Atualizar(Chamado entidade) =>
            _contexto.Chamados.Update(entidade);

        /// <summary>
        /// Consulta paginada do painel operacional. A procedure encapsula a
        /// regra de ordenacao por criticidade e devolve apenas as colunas
        /// necessarias, reduzindo o trafego de rede.
        /// </summary>
        public async Task<IEnumerable<Chamado>> ObterPainelOperacionalAsync(
            Guid clienteId, int pagina, int tamanho)
        {
            var conexao = _contexto.Database.GetDbConnection();
            var parametros = new DynamicParameters();
            parametros.Add("@ClienteId", clienteId, DbType.Guid);
            parametros.Add("@Pagina", pagina, DbType.Int32);
            parametros.Add("@TamanhoPagina", tamanho, DbType.Int32);

            return await conexao.QueryAsync<Chamado>(
                "dbo.sp_ListarPainelOperacional",
                parametros,
                commandType: CommandType.StoredProcedure);
        }

        public async Task<int> ContarSlaVioladoAsync(DateTime inicio, DateTime fim) =>
            await _contexto.Chamados
                           .AsNoTracking()
                           .CountAsync(c => c.CriadoEm >= inicio
                                         && c.CriadoEm <= fim
                                         && c.PrazoSla != null
                                         && c.ResolvidoEm > c.PrazoSla);
    }
}
