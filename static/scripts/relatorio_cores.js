function getCSRFToken() {
    const cookieValue = document.cookie.match('(^|;)\\s*' + 'csrftoken' + '\\s*=\\s*([^;]+)')?.pop() || '';
    return cookieValue;
}

function list_channels_by_company_id(company_id){
    const cameraSelect = document.getElementById("camera");

    cameraSelect.innerHTML = '<option value="" disabled selected>Selecione a câmera</option>';

    fetch('/api/list/channels/' + company_id)
        .then(response => response.json())
        .then(data => {
            if(data){
                for (let x = 1; x <= data.max_channel; x++){
                    const option = document.createElement("option");
                    option.value = x;
                    option.textContent = "Câmera "+ x;
                    cameraSelect.appendChild(option);
                };
            }
        })
        .catch(error => console.error('Erro ao carregar empresas:', error));
}

document.addEventListener("DOMContentLoaded", function() {
    const dataInicio = document.getElementById("data-inicio");
    const dataFim = document.getElementById("data-fim");

    // Define a data atual para data-inicio
    const today = new Date();
    const tenDaysAgo = new Date();
    tenDaysAgo.setDate(today.getDate() - 10);

    // Formata as datas no formato yyyy-mm-dd
    dataInicio.value = today.toISOString().split("T")[0];
    dataFim.value = tenDaysAgo.toISOString().split("T")[0];

    // Define o limite máximo para as datas (a data atual)
    dataInicio.max = today.toISOString().split("T")[0];
    dataFim.max = today.toISOString().split("T")[0];

    // Atualiza o limite mínimo de data de fim com base na data de início
    dataInicio.addEventListener("change", function() {
        dataFim.min = dataInicio.value;
    });

    // Valida que a data de fim não é menor que a data de início nem maior que a data atual
    dataFim.addEventListener("change", function() {
        if (dataFim.value < dataInicio.value || dataFim.value > today) {
            alert("A data de fim deve estar entre a data de início e a data atual.");
            dataFim.value = ""; // Limpa o valor de dataFim se for inválido
        }
    });
});


async function obterRelatorioCores() {
    const dataInicio = document.getElementById("data-inicio").value;
    const dataFim = document.getElementById("data-fim").value;
    const camera = document.getElementById("camera").value;
    const empresa = document.getElementById("empresa").value;

    const requestData = {
        empresa_id: parseInt(empresa),
        channel: parseInt(camera),
        data_inicio: dataInicio,
        data_fim: dataFim
    };

    try {
        const response = await fetch("/api/list/relatorio_cores_info", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                'X-CSRFToken': getCSRFToken()
            },
            body: JSON.stringify(requestData)
        });
        
        if (!response.ok) {
            throw new Error(`Erro na requisição: ${response.statusText}`);
        }

        const data = await response.json();
        return data; // Retorna os dados recebidos da API
    } catch (error) {
        console.error("Erro:", error);
        throw error;
    }
}

async function exibirRelatorio() {
    try {
        const dadosRelatorio = await obterRelatorioCores();
        const tabela = document.getElementById("relatorioCoresTabela");
        tabela.innerHTML = ""; // Limpa o conteúdo atual da tabela

        // Extrai todas as datas únicas do relatório
        const todasDatas = new Set();
        dadosRelatorio.data.forEach(item => {
            item.dates.forEach(dateInfo => {
                todasDatas.add(dateInfo.date);
            });
        });
        const datasOrdenadas = Array.from(todasDatas).sort((a, b) => new Date(b) - new Date(a)); // Ordena da mais nova para a mais velha

        // Cria a primeira linha da tabela (cabeçalhos)
        const headerRow = tabela.insertRow();
        headerRow.insertCell(0).textContent = "Carro";
        headerRow.insertCell(1).textContent = "Modelo";
        datasOrdenadas.forEach(date => {
            const cell = headerRow.insertCell();
            cell.textContent = date;
        });

        // Cria as linhas para cada carro no relatório
        dadosRelatorio.data.forEach(item => {
            const { car, model, dates } = item;

            // Cria um dicionário para as contagens de arquivos por data
            const arquivosPorData = {};
            dates.forEach(dateInfo => {
                arquivosPorData[dateInfo.date] = dateInfo.files;
            });

            // Adiciona a linha do carro, modelo e arquivos
            const carRow = tabela.insertRow();
            carRow.insertCell(0).textContent = car;
            carRow.insertCell(1).textContent = model;

            datasOrdenadas.forEach(date => {
                const filesCell = carRow.insertCell();

                const count = arquivosPorData[date] || 0; // Exibe 0 se não houver arquivos para a data
                
                // Aplica a classe red-cell ou green-cell baseado no valor de count
                if (count < 200) {
                    filesCell.classList.add("red-cell");
                    filesCell.textContent = "x";  // Se o número for menor que 200, exibe 'x'
                } else {
                    filesCell.classList.add("green-cell");
                    filesCell.textContent = count; // Caso contrário, exibe o número de arquivos
                }
            });
        });

        console.log("Dados do relatório exibidos com sucesso.");
    } catch (error) {
        console.error("Erro ao obter o relatório:", error);
    }
}

document.querySelector(".btn.btn-primary").addEventListener("click", exibirRelatorio);



// document.querySelector(".btn.btn-primary").addEventListener("click", function() {
    
    
//     const dataInicio = document.getElementById("data-inicio").value;
//     const dataFim = document.getElementById("data-fim").value;
//     const camera = document.getElementById("camera").value;
//     const empresa = document.getElementById("empresa").value;

//     const requestData = {
//         empresa_id: parseInt(empresa),
//         channel: parseInt(camera),
//         data_inicio: dataInicio,
//         data_fim: dataFim
//     };

//     fetch("/api/list/relatorio_cores_info", {
//         method: "POST",
//         headers: {
//             "Content-Type": "application/json",
//             'X-CSRFToken': getCSRFToken()
//         },
//         body: JSON.stringify(requestData)
//     })
//     .then(response => response.json())
//     .then(data => {
//         console.log(data);
//         return data;
//         // Aqui você pode manipular a resposta recebida
//     })
//     .catch(error => console.error("Erro:", error));
// });