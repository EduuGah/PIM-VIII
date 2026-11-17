using System.Text;
using AlunosTech.Application.Servicos;
using AlunosTech.Domain.Interfaces;
using AlunosTech.Infrastructure.Data;
using AlunosTech.Infrastructure.Repositorios;
using Microsoft.AspNetCore.Authentication.JwtBearer;
using Microsoft.EntityFrameworkCore;
using Microsoft.IdentityModel.Tokens;

var builder = WebApplication.CreateBuilder(args);

// ---------- Persistencia ----------
builder.Services.AddDbContext<AtIntegraDbContext>(opt =>
    opt.UseSqlServer(builder.Configuration.GetConnectionString("AtIntegra"),
        sql => sql.EnableRetryOnFailure(maxRetryCount: 5)));

// ---------- Injecao de dependencia (Inversao de Controle) ----------
builder.Services.AddScoped<IUnitOfWork, UnitOfWork>();
builder.Services.AddScoped<IChamadoRepositorio, ChamadoRepositorio>();
builder.Services.AddScoped<IChamadoService, ChamadoService>();

// ---------- Seguranca: autenticacao JWT ----------
builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddJwtBearer(opt =>
    {
        opt.TokenValidationParameters = new TokenValidationParameters
        {
            ValidateIssuer = true,
            ValidateAudience = true,
            ValidateLifetime = true,
            ValidateIssuerSigningKey = true,
            ValidIssuer = builder.Configuration["Jwt:Issuer"],
            ValidAudience = builder.Configuration["Jwt:Audience"],
            IssuerSigningKey = new SymmetricSecurityKey(
                Encoding.UTF8.GetBytes(builder.Configuration["Jwt:Chave"]))
        };
    });

builder.Services.AddAuthorization();
builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

// ---------- Observabilidade e resiliencia ----------
builder.Services.AddHealthChecks()
       .AddDbContextCheck<AtIntegraDbContext>("banco-de-dados");
builder.Services.AddResponseCompression();

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();
app.UseResponseCompression();
app.UseAuthentication();
app.UseAuthorization();
app.MapControllers();
app.MapHealthChecks("/health");   // endpoint consumido pelo probe do Kubernetes

app.Run();
