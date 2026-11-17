using System;
using System.Threading.Tasks;
using AlunosTech.Application.DTOs;
using AlunosTech.Application.Servicos;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace AlunosTech.API.Controllers
{
    [ApiController]
    [Route("api/v1/chamados")]
    [Authorize]
    [Produces("application/json")]
    public class ChamadosController : ControllerBase
    {
        private readonly IChamadoService _servico;

        public ChamadosController(IChamadoService servico) => _servico = servico;

        /// <summary>Abre um novo chamado e calcula o prazo de SLA do contrato.</summary>
        [HttpPost]
        [Authorize(Roles = "Cliente,Atendente")]
        [ProducesResponseType(typeof(ChamadoRespostaDto), StatusCodes.Status201Created)]
        [ProducesResponseType(StatusCodes.Status400BadRequest)]
        public async Task<IActionResult> Abrir([FromBody] AberturaChamadoDto dto)
        {
            if (!ModelState.IsValid) return ValidationProblem(ModelState);

            var resposta = await _servico.AbrirAsync(dto);
            return CreatedAtAction(nameof(Abrir), new { id = resposta.Id }, resposta);
        }

        /// <summary>Atribui o chamado a um tecnico do time de campo.</summary>
        [HttpPatch("{id:guid}/atribuicao")]
        [Authorize(Roles = "Supervisor")]
        [ProducesResponseType(StatusCodes.Status204NoContent)]
        public async Task<IActionResult> Atribuir(Guid id, [FromQuery] Guid tecnicoId)
        {
            await _servico.AtribuirAsync(id, tecnicoId);
            return NoContent();
        }
    }
}
