using System;
using System.Collections.ObjectModel;
using System.Threading.Tasks;
using System.Windows.Input;
using AlunosTech.Application.DTOs;
using AlunosTech.Application.Servicos;

namespace AlunosTech.Desktop.ViewModels
{
    /// <summary>
    /// ViewModel do modulo desktop (WPF) utilizado pela central de operacoes
    /// da Alunos Tech. O modulo roda em estacoes internas e consome os mesmos
    /// servicos de aplicacao da API, reaproveitando as regras de negocio.
    /// </summary>
    public class PainelOperacoesViewModel : ViewModelBase
    {
        private readonly IChamadoService _chamadoService;
        private readonly IRelatorioService _relatorioService;
        private ChamadoRespostaDto _selecionado;
        private int _slaViolados;

        public PainelOperacoesViewModel(IChamadoService chamadoService,
                                        IRelatorioService relatorioService)
        {
            _chamadoService = chamadoService;
            _relatorioService = relatorioService;

            AtualizarComando = new ComandoRelay(async _ => await AtualizarAsync());
            AtribuirComando  = new ComandoRelay(async p => await AtribuirAsync((Guid)p),
                                                _ => Selecionado is not null);
        }

        public ObservableCollection<ChamadoRespostaDto> Fila { get; } = new();

        public ChamadoRespostaDto Selecionado
        {
            get => _selecionado;
            set { _selecionado = value; NotificarMudanca(); }
        }

        public int SlaViolados
        {
            get => _slaViolados;
            private set { _slaViolados = value; NotificarMudanca(); }
        }

        public ICommand AtualizarComando { get; }
        public ICommand AtribuirComando { get; }

        private async Task AtualizarAsync()
        {
            var painel = await _relatorioService.ObterFilaPrioritariaAsync();

            Fila.Clear();
            foreach (var chamado in painel) Fila.Add(chamado);

            SlaViolados = await _relatorioService.ContarSlaVioladoAsync(
                DateTime.Today.AddDays(-30), DateTime.Today);
        }

        private async Task AtribuirAsync(Guid tecnicoId)
        {
            await _chamadoService.AtribuirAsync(Selecionado.Id, tecnicoId);
            await AtualizarAsync();
        }
    }
}
