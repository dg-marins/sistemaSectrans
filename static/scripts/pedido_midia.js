function listarModelos(){
    const modelosSelect = document.getElementById("modelo_equipamento");

    modelosSelect.innerHTML = '<option value="" disabled selected>Selecione modelo</option>';
    modelosSelect.disabled = true;  

    fetch('/listar_modelos/')
        .then(response => response.json())
        .then(data => {
            console.log(data); // Para verificar os dados no console
            if(data.length > 0){
                modelosSelect.disabled = false;
                data.forEach(modelo =>{
                    const option = document.createElement("option");
                    option.value = modelo.id;
                    option.textContent = modelo.modelo;
                    modelosSelect.appendChild(option);
                });
            }
        })
        .catch(error => console.error('Erro ao carregar modelos:', error));
}

function listarCarros(empresaId) {
    const carrosSelect = document.getElementById("carros");

    // Limpa as opções anteriores
    carrosSelect.innerHTML = '<option value="" disabled selected>Selecione carro</option>';
    carrosSelect.disabled = true;

    if (empresaId) {
        fetch(`/listar_carros/${empresaId}/`)
            .then(response => response.json())
            .then(data => {
                if (data.length > 0) {
                    carrosSelect.disabled = false;
                    data.forEach(carro => {
                        const option = document.createElement("option");
                        option.value = carro.id;
                        option.textContent = carro.nome;
                        carrosSelect.appendChild(option);
                    });
                }
            })
            .catch(error => console.error("Erro ao carregar carros:", error));
    }
}

function solicitarGravacao(){
    
}