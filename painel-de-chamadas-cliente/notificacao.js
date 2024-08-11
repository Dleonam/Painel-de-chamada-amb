let ultimoId = null;

function tocarSom() {
    const audio = new Audio('ding.mp3');
    audio.play();
}

function verificarNovasChamadas() {
    fetch('chamadas.php')
        .then(response => response.json())
        .then(chamadas => {
            if (chamadas.length > 0) {
                const novoId = chamadas[0].id;

                if (ultimoId !== null && novoId > ultimoId) {
                    tocarSom();
                }

                ultimoId = novoId;

                const container = document.querySelector('.chamadas-container');
                container.innerHTML = '';

                chamadas.forEach(chamada => {
                    const card = document.createElement('div');
                    card.className = 'chamada-card';

                    const pacienteDiv = document.createElement('div');
                    pacienteDiv.className = 'paciente';
                    pacienteDiv.textContent = chamada.nome_paciente;

                    const unidadeDiv = document.createElement('div');
                    unidadeDiv.className = 'unidade';
                    unidadeDiv.textContent = chamada.nome_unidade;

                    card.appendChild(pacienteDiv);
                    card.appendChild(unidadeDiv);
                    container.appendChild(card);
                });
            }
        })
        .catch(error => console.error('Erro ao carregar chamadas:', error));
}

// Recarregar chamadas a cada 5 segundos
setInterval(verificarNovasChamadas, 5000);

// Carregar chamadas ao iniciar a página
window.onload = verificarNovasChamadas;
