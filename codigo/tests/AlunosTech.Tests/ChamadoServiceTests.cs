using System;
using AlunosTech.Domain.Entidades;
using AlunosTech.Domain.Servicos;
using Xunit;

namespace AlunosTech.Tests
{
    /// <summary>
    /// Testes de unidade do agregado Chamado. Cobrem as regras de SLA, o
    /// ciclo de vida do atendimento e as invariantes de validacao.
    /// </summary>
    public class ChamadoServiceTests
    {
        private static Chamado NovoChamado(PrioridadeChamado p = PrioridadeChamado.Alta) =>
            new(Guid.NewGuid(), "Falha no servidor de arquivos",
                "Compartilhamento indisponivel na filial Sul", p, Guid.NewGuid());

        [Fact]
        public void DefinirSla_ContratoGold_PrioridadeCritica_Deve_Reservar_2_Horas()
        {
            var chamado = NovoChamado(PrioridadeChamado.Critica);

            chamado.DefinirSla(SlaStrategyFactory.Criar("GOLD"));

            Assert.Equal(chamado.CriadoEm.AddHours(2), chamado.PrazoSla);
        }

        [Theory]
        [InlineData(PrioridadeChamado.Critica, 4)]
        [InlineData(PrioridadeChamado.Alta, 8)]
        [InlineData(PrioridadeChamado.Media, 24)]
        public void DefinirSla_ContratoSilver_Deve_Contar_Apenas_Horas_Uteis(
            PrioridadeChamado prioridade, int horasUteis)
        {
            var chamado = NovoChamado(prioridade);

            chamado.DefinirSla(SlaStrategyFactory.Criar("SILVER"));

            Assert.True(chamado.PrazoSla > chamado.CriadoEm.AddHours(horasUteis - 1));
        }

        [Fact]
        public void Resolver_Sem_Tecnico_Atribuido_Deve_Lancar_Excecao()
        {
            var chamado = NovoChamado();

            var erro = Assert.Throws<InvalidOperationException>(
                () => chamado.Resolver("Servico reiniciado"));

            Assert.Equal("Chamado sem tecnico responsavel.", erro.Message);
        }

        [Fact]
        public void Resolver_Dentro_Do_Prazo_Nao_Deve_Violar_Sla()
        {
            var chamado = NovoChamado();
            chamado.DefinirSla(SlaStrategyFactory.Criar("GOLD"));
            chamado.Atribuir(Guid.NewGuid());

            chamado.Resolver("Reindexacao do volume concluida");

            Assert.Equal(StatusChamado.Resolvido, chamado.Status);
            Assert.False(chamado.SlaViolado);
        }

        [Fact]
        public void Titulo_Com_Menos_De_5_Caracteres_Deve_Ser_Rejeitado()
        {
            Assert.Throws<ArgumentException>(() =>
                new Chamado(Guid.NewGuid(), "ERRO", "descricao",
                            PrioridadeChamado.Baixa, Guid.NewGuid()));
        }
    }
}
