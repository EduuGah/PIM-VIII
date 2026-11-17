# =====================================================================
# AT-Integra | Imagem da API corporativa
# Build multiestagio: reduz a imagem final de ~780 MB para ~112 MB
# =====================================================================
FROM mcr.microsoft.com/dotnet/sdk:8.0-alpine AS build
WORKDIR /src

# Camada de restauracao isolada: aproveita o cache quando so o codigo muda
COPY ["src/AlunosTech.API/AlunosTech.API.csproj", "src/AlunosTech.API/"]
COPY ["src/AlunosTech.Application/AlunosTech.Application.csproj", "src/AlunosTech.Application/"]
COPY ["src/AlunosTech.Domain/AlunosTech.Domain.csproj", "src/AlunosTech.Domain/"]
COPY ["src/AlunosTech.Infrastructure/AlunosTech.Infrastructure.csproj", "src/AlunosTech.Infrastructure/"]
RUN dotnet restore "src/AlunosTech.API/AlunosTech.API.csproj"

COPY . .
RUN dotnet publish "src/AlunosTech.API/AlunosTech.API.csproj" \
    -c Release -o /app/publish \
    /p:UseAppHost=false /p:PublishTrimmed=true

# ---------------------------------------------------------------------
FROM mcr.microsoft.com/dotnet/aspnet:8.0-alpine AS final
WORKDIR /app

# Execucao sem privilegios de root (CIS Docker Benchmark 4.1)
RUN addgroup -S atgroup && adduser -S atuser -G atgroup
USER atuser

COPY --from=build --chown=atuser:atgroup /app/publish .

ENV ASPNETCORE_URLS=http://+:8080 \
    DOTNET_gcServer=1 \
    ASPNETCORE_ENVIRONMENT=Production
EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
    CMD wget -qO- http://localhost:8080/health || exit 1

ENTRYPOINT ["dotnet", "AlunosTech.API.dll"]
