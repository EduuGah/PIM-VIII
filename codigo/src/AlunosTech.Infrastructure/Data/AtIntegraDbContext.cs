using AlunosTech.Domain.Entidades;
using Microsoft.EntityFrameworkCore;

namespace AlunosTech.Infrastructure.Data
{
    /// <summary>
    /// Contexto de persistencia da plataforma. O mapeamento declara indices,
    /// o token de concorrencia (rowversion) e o filtro global de exclusao
    /// logica aplicado a todas as consultas.
    /// </summary>
    public class AtIntegraDbContext : DbContext
    {
        public AtIntegraDbContext(DbContextOptions<AtIntegraDbContext> options)
            : base(options) { }

        public DbSet<Chamado> Chamados => Set<Chamado>();
        public DbSet<ApontamentoHoras> Apontamentos => Set<ApontamentoHoras>();

        protected override void OnModelCreating(ModelBuilder mb)
        {
            mb.Entity<Chamado>(e =>
            {
                e.ToTable("Chamado", "dbo");
                e.HasKey(c => c.Id);
                e.Property(c => c.Protocolo).HasMaxLength(20).IsRequired();
                e.Property(c => c.Titulo).HasMaxLength(120).IsRequired();
                e.Property(c => c.Descricao).HasMaxLength(4000);
                e.Property(c => c.Versao).IsRowVersion();          // concorrencia otimista

                e.HasIndex(c => c.Protocolo).IsUnique();
                e.HasIndex(c => new { c.ClienteId, c.Status })
                 .HasDatabaseName("IX_Chamado_Cliente_Status");

                e.HasMany(c => c.Apontamentos)
                 .WithOne()
                 .HasForeignKey(a => a.ChamadoId)
                 .OnDelete(DeleteBehavior.Cascade);

                e.HasQueryFilter(c => c.Ativo);                     // exclusao logica
            });

            base.OnModelCreating(mb);
        }
    }
}
