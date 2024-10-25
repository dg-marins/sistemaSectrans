function selecionarEmpresa() {
    var dropdown = document.getElementById("empresas");
    var empresaSelecionada = dropdown.options[dropdown.selectedIndex].text;
    console.log("Empresa selecionada:", empresaSelecionada);
}

function atualizarSelect(selectId, listItens){
    var selectItem = document.getElementById(selectId);

    // Limpar opções existentes
    selectItem.innerHTML = '';
    
    listItens.forEach(function(item)
    {
        var option = document.createElement("option");
        option.value = item.id;
        option.text = item.text;

        selectItem.appendChild(option);
    });
}

function listarCarros(empresaId) {
    if (empresaId) {
        fetch(`/empresas/${empresaId}/carros/`)
            .then(response => response.json())
            .then(data => {
                // Atualize o select de carros com os dados recebidos
                atualizarSelect("carros", data.carros);
            })
            .catch(error => console.error('Erro ao listar carros:', error));
    }
}

function modifyDisplay(ids, exibition){
    for (var i = 0; i < ids.length; i++) {
        var element = document.getElementById(ids[i]);
        if (element) {
            element.style.display = exibition; // Modifica o estilo para exibição
        }
    }
}

function atualizarParametrosGravacao(modeloEquipamento){
    var IdDisplayDvr = ["dvr_label", "dvr_select"];
    var IdDisplayCameras = ["cameras_label", "cameras_select"];

    // Verificar se o modelo de equipamento é "RaspDvr"
    if (modeloEquipamento === "RaspDvr") {
        modifyDisplay(IdDisplayDvr, "block")
        modifyDisplay(IdDisplayCameras, "block")
    } else {
        modifyDisplay(IdDisplayDvr, "none")
        modifyDisplay(IdDisplayCameras, "none")
    }
}

// Executar a função listarEmpresas() quando o DOM estiver pronto
document.addEventListener("DOMContentLoaded", function() {
        // Obtendo o nome do arquivo HTML atual
        var currentPage = window.location.pathname.split("/").pop();

        // Verificando se a página atual é gravacao.html
        if (currentPage === "gravacao.html") {
            listarEmpresas();
        }
});

function solicitarGravacao() {
    // Obter os valores dos selects
    var empresa = document.getElementById("empresas").value;
    var carro = document.getElementById("carros").value;
    var modeloEquipamento = document.getElementById("modelo_equipamento").value;
    var dvr = document.getElementById("dvr_select").value;
    var cameras = document.getElementById("cameras_select").value;

    // Aqui você pode enviar os valores para onde quiser, como uma API ou fazer alguma operação com eles
    // Por exemplo, você pode exibir os valores em um alerta
    alert("Empresa: " + empresa + "\nCarro: " + carro + "\nModelo de Equipamento: " + modeloEquipamento + "\nDVR: " + dvr + "\nCâmeras: " + cameras);
}