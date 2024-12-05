let map;

class GpsMap {

    constructor() {
        this.empresaSelect = document.getElementById("empresa");
        this.carroSelect = document.getElementById("carro");
        this.data = document.getElementById("data");
        this.btnExibirRota = document.getElementById("btn");
        
        // Eventos
        this.addEventListeners();
    }

    addEventListeners() {
        document.addEventListener("DOMContentLoaded", () => this.initMap());
        this.empresaSelect.addEventListener("change", () => this.listCarsByCompanyId());
        this.btnExibirRota.addEventListener("click", () => this.exibirRota());
    }

    async initMap() {
        map = new google.maps.Map(document.getElementById("map"), {
            center: { lat: -22.9095109, lng: -43.2175685 },
            zoom: 15,
        });
    }

    listCarsByCompanyId(){
        const companyId = this.empresaSelect.value;
        if(!companyId){
            console.error('Empresa não selecionada');
            return;
        }
    
        // Limpa a lista de carros
        this.carroSelect.innerHTML ='<option value="" disabled selected>Selecione um carro</option>';

        // Realiza a requisição
        fetch(`/api/list_cars/${companyId}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Erro ao buscar os carros');
                }
                return response.json();
            })
            .then(data => {
                // Valida se a data é uma lista
                if(Array.isArray(data)){
                    data.forEach(carro =>{
                        const option = document.createElement("option");
                        option.value = carro.id;
                        option.textContent = carro.nome;
                        this.carroSelect.appendChild(option);    
                    });
                } else {
                        console.error('Formato de dados inesperado: ', data);
                    }
                })
                .catch(error => {
                    console.error('Erro na requisição:', erro);
                });
    }

    exibirRota() {
        const companyId = document.getElementById("empresa").value;
        const carroId = document.getElementById("carro").value;
        const data = document.getElementById("data").value;

        if (!carroId || !data || !companyId) {
            alert("Por favor, selecione empresa, carro e uma data.");
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

    desenharRota(rotaData) {
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
}
// Inicializa o mapa quando a página carrega
const gpsMap = new GpsMap()
