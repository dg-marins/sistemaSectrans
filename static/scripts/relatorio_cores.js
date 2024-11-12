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

    // Define a data atual para limitar os campos
    const today = new Date().toISOString().split("T")[0];
    dataInicio.max = today;
    dataFim.max = today;

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

document.querySelector(".btn.btn-primary").addEventListener("click", function() {
    
    
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

    fetch("/api/list/relatorio_cores_info", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            'X-CSRFToken': getCSRFToken()
        },
        body: JSON.stringify(requestData)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        return data;
        // Aqui você pode manipular a resposta recebida
    })
    .catch(error => console.error("Erro:", error));
});