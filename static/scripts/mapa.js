let map;

function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: -22.9095109, lng: -43.2175685 },
        zoom: 15,
    });
}

function exibirRota() {
    const carroId = document.getElementById("carros").value;
    const data = document.getElementById("data").value;

    if (!carroId || !data) {
        alert("Por favor, selecione um carro e uma data.");
        return;
    }

    // Aqui você faria uma chamada AJAX para obter os dados da rota
    fetch(`/api/rota/${carroId}/${data}/`)
        .then(response => response.json())
        .then(data => {
            desenharRota(data);
        })
        .catch(error => console.error('Erro ao carregar rota:', error));
}

function desenharRota(rotaData) {
    // Limpa rotas anteriores
    map.clearOverlays();

    const path = rotaData.map(ponto => new google.maps.LatLng(ponto.lat, ponto.lng));
    
    const rota = new google.maps.Polyline({
        path: path,
        geodesic: true,
        strokeColor: "#FF0000",
        strokeOpacity: 1.0,
        strokeWeight: 2,
    });

    rota.setMap(map);

    // Ajusta o zoom e centro do mapa para mostrar toda a rota
    const bounds = new google.maps.LatLngBounds();
    path.forEach(ponto => bounds.extend(ponto));
    map.fitBounds(bounds);
}

// Inicializa o mapa quando a página carrega
window.onload = initMap;