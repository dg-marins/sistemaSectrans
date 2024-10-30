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