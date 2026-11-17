using System;
using System.Collections.ObjectModel;
using System.Threading.Tasks;
using System.Windows.Input;
using AlunosTech.Mobile.Servicos;
using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;

namespace AlunosTech.Mobile.ViewModels
{
    /// <summary>
    /// ViewModel do aplicativo .NET MAUI usado pelo tecnico em campo.
    /// Implementa o padrao MVVM e a estrategia offline-first: as alteracoes
    /// sao gravadas em SQLite local e sincronizadas quando ha conectividade.
    /// </summary>
    public partial class ChamadoViewModel : ObservableObject
    {
        private readonly IApiAtIntegra _api;
        private readonly IRepositorioLocal _local;
        private readonly IConnectivity _conectividade;

        public ChamadoViewModel(IApiAtIntegra api,
                                IRepositorioLocal local,
                                IConnectivity conectividade)
        {
            _api = api;
            _local = local;
            _conectividade = conectividade;
        }

        [ObservableProperty] private bool carregando;
        [ObservableProperty] private string filtroStatus = "EmAtendimento";

        public ObservableCollection<ChamadoItem> Chamados { get; } = new();

        [RelayCommand]
        private async Task CarregarAsync()
        {
            if (Carregando) return;
            Carregando = true;

            try
            {
                var online = _conectividade.NetworkAccess == NetworkAccess.Internet;

                var itens = online
                    ? await _api.ObterChamadosDoTecnicoAsync(FiltroStatus)
                    : await _local.ListarChamadosAsync(FiltroStatus);

                if (online) await _local.SalvarEmCacheAsync(itens);

                Chamados.Clear();
                foreach (var item in itens) Chamados.Add(item);
            }
            catch (Exception ex)
            {
                await Shell.Current.DisplayAlert("Atencao",
                    "Nao foi possivel atualizar a lista: " + ex.Message, "OK");
            }
            finally
            {
                Carregando = false;
            }
        }

        /// <summary>
        /// Conclui o atendimento em campo. Sem conexao, o registro entra na
        /// fila de sincronizacao e e reenviado pelo servico em segundo plano.
        /// </summary>
        [RelayCommand]
        private async Task ConcluirAsync(ChamadoItem item)
        {
            item.Status = "Resolvido";
            item.ResolvidoEm = DateTime.UtcNow;

            if (_conectividade.NetworkAccess == NetworkAccess.Internet)
                await _api.ResolverChamadoAsync(item.Id, item.SolucaoAplicada);
            else
                await _local.EnfileirarSincronizacaoAsync(item);

            await CarregarAsync();
        }
    }
}
