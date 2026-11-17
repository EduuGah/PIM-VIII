using System;
using System.Threading.Tasks;
using AlunosTech.Application.DTOs;
using AlunosTech.Domain.Entidades;
using AlunosTech.Domain.Interfaces;
using AlunosTech.Domain.Servicos;
using Microsoft.Extensions.Logging;

namespace AlunosTech.Application.Servicos
{
    public interface IChamadoService
    {
        Task<ChamadoRespostaDto> AbrirAsync(AberturaChamadoDto dto);
        Task AtribuirAsync(Guid chamadoId, Guid tecnicoId);
    }

    /// <summary>
    /// Servico de aplicacao que orquestra o caso de uso "Abrir chamado".
    /// As dependencias sao recebidas por injecao de construtor, mantendo a
    /// camada desacoplada da infraestrutura (Inversao de Dependencia).
    /// </summary>
    public class ChamadoService : IChamadoService
    {
        private readonly IUnitOfWork _uow;
        private readonly IContratoRepositorio _contratos;
        private readonly INotificacaoService _notificacao;
        private readonly ILogger<ChamadoService> _logger;

        public ChamadoService(IUnitOfWork uow,
                              IContratoRepositorio contratos,
                              INotificacaoService notificacao,
                              ILogger<ChamadoService> logger)
        {
            _uow = uow;
            _contratos = contratos;
            _notificacao = notificacao;
            _logger = logger;
        }

        public async Task<ChamadoRespostaDto> AbrirAsync(AberturaChamadoDto dto)
        {
            var contrato = await _contratos.ObterPorIdAsync(dto.ContratoId)
                ?? throw new InvalidOperationException("Contrato inexistente ou inativo.");

            var chamado = new Chamado(dto.ClienteId, dto.Titulo, dto.Descricao,
                                      dto.Prioridade, dto.ContratoId);

            // A estrategia de SLA varia conforme o nivel do contrato (Gold/Silver).
            var estrategia = SlaStrategyFactory.Criar(contrato.NivelSla);
            chamado.DefinirSla(estrategia);

            try
            {
                await _uow.Chamados.AdicionarAsync(chamado);
                await _uow.ConfirmarAsync();
            }
            catch (Exception ex)
            {
                await _uow.DescartarAsync();
                _logger.LogError(ex, "Falha ao persistir o chamado do cliente {Cliente}", dto.ClienteId);
                throw;
            }

            await _notificacao.EnviarAsync(contrato.EmailResponsavel,
                "Chamado " + chamado.Protocolo + " registrado",
                "Prazo de atendimento: " + chamado.PrazoSla);

            _logger.LogInformation("Chamado {Protocolo} aberto com SLA {Nivel}",
                                   chamado.Protocolo, estrategia.Nivel);

            return ChamadoRespostaDto.De(chamado);
        }

        public async Task AtribuirAsync(Guid chamadoId, Guid tecnicoId)
        {
            var chamado = await _uow.Chamados.ObterPorIdAsync(chamadoId)
                ?? throw new InvalidOperationException("Chamado nao localizado.");

            chamado.Atribuir(tecnicoId);
            _uow.Chamados.Atualizar(chamado);
            await _uow.ConfirmarAsync();
        }
    }
}
