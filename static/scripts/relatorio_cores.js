class RelatorioCores {
    constructor() {
        this.cameraSelect = document.getElementById("camera");
        this.dataInicio = document.getElementById("data-inicio");
        this.dataFim = document.getElementById("data-fim");
        this.empresaSelect = document.getElementById("empresa")
        this.tabela = document.getElementById("relatorioCoresTabela");
        this.btnExibirRelatorio = document.querySelector(".btn.btn-primary");

        // Eventos
        this.addEventListeners();
    }

    // Método para adicionar event listeners
    addEventListeners() {
        document.addEventListener("DOMContentLoaded", () => this.configurarDatas());
        this.btnExibirRelatorio.addEventListener("click", () => this.exibirRelatorio());
        this.dataInicio.addEventListener("change", () => this.dataFim.min = this.dataInicio.value);
        this.dataFim.addEventListener("change", () => this.validarDataFim());
        this.empresaSelect.addEventListener("change",() => this.listChannelsByCompanyId())
    }

    // Método para configurar as datas iniciais e limites
    configurarDatas() {
        const today = new Date();
        const tenDaysAgo = new Date();
        tenDaysAgo.setDate(today.getDate() - 10);

        this.dataInicio.value = today.toISOString().split("T")[0];
        this.dataFim.value = tenDaysAgo.toISOString().split("T")[0];

        this.dataInicio.max = today.toISOString().split("T")[0];
        this.dataFim.max = today.toISOString().split("T")[0];
    }

    // Validação para a data de fim
    validarDataFim() {
        const today = new Date();
        if (this.dataFim.value < this.dataInicio.value || this.dataFim.value > today) {
            alert("A data de fim deve estar entre a data de início e a data atual.");
            this.dataFim.value = ""; // Limpa o valor de dataFim se for inválido
            this.dataFim.classList.add("invalid"); // Adiciona uma classe para destacar o erro
        } else {
            this.dataFim.classList.remove("invalid"); // Remove a classe de erro se válido
        }
    }
    

    // Função para pegar o token CSRF
    getCSRFToken() {
        const cookieValue = document.cookie.match('(^|;)\\s*' + 'csrftoken' + '\\s*=\\s*([^;]+)')?.pop() || '';
        return cookieValue;
    }

    // Método para listar câmeras baseado no ID da empresa
    listChannelsByCompanyId() {
        const companyId = this.empresaSelect.value; // Obter o ID da empresa
        if (!companyId) {
            console.error('Empresa não selecionada');
            return;
        }
    
        this.cameraSelect.innerHTML = '<option value="" disabled selected>Selecione a câmera</option>';
    
        fetch(`/api/list/channels/${companyId}`)
            .then(response => response.json())
            .then(data => {
                if (data) {
                    for (let x = 1; x <= data.max_channel; x++) {
                        const option = document.createElement("option");
                        option.value = x;
                        option.textContent = "Câmera " + x;
                        this.cameraSelect.appendChild(option);
                    }
                }
            })
            .catch(error => console.error('Erro ao carregar câmeras:', error));
    }
    

    // Método para obter o relatório de cores
    async obterRelatorioCores() {
        const dataInicio = this.dataInicio.value;
        const dataFim = this.dataFim.value;
        const camera = this.cameraSelect.value;
        const empresa = document.getElementById("empresa").value;
    
        const requestData = {
            empresa_id: parseInt(empresa),
            channel: parseInt(camera),
            data_inicio: dataInicio,
            data_fim: dataFim
        };
    
        try {
            // Mostra uma mensagem de carregamento
            this.tabela.innerHTML = "<tr><td colspan='5'>Carregando...</td></tr>";
            
            const response = await fetch("/api/list/relatorio_cores_info", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    'X-CSRFToken': this.getCSRFToken()
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
    // Método para exibir o relatório
    async exibirRelatorio() {
        try {
            const dadosRelatorio = await this.obterRelatorioCores();
            this.tabela.innerHTML = ""; // Limpa o conteúdo atual da tabela
    
            if (!dadosRelatorio.data || dadosRelatorio.data.length === 0) {
                this.tabela.innerHTML = "<tr><td colspan='5'>Nenhum dado encontrado.</td></tr>";
                return;
            }
    
            const todasDatas = new Set();
            dadosRelatorio.data.forEach(item => {
                item.dates.forEach(dateInfo => {
                    todasDatas.add(dateInfo.date);
                });
            });
    
            const datasOrdenadas = Array.from(todasDatas).sort((a, b) => new Date(b) - new Date(a));
    
            const headerRow = this.tabela.insertRow();
            headerRow.insertCell(0).textContent = "Carro";
            headerRow.insertCell(1).textContent = "Modelo";
            datasOrdenadas.forEach(date => {
                const cell = headerRow.insertCell();
                cell.textContent = date;
            });
    
            dadosRelatorio.data.forEach(item => {
                const { car, model, dates } = item;
                const arquivosPorData = {};
                dates.forEach(dateInfo => {
                    arquivosPorData[dateInfo.date] = dateInfo.files;
                });
    
                const carRow = this.tabela.insertRow();
                carRow.insertCell(0).textContent = car;
                carRow.insertCell(1).textContent = model;
    
                datasOrdenadas.forEach(date => {
                    const filesCell = carRow.insertCell();
                    const count = arquivosPorData[date] || 0;
    
                    if (count <= 0) {
                        filesCell.classList.add("red-cell");
                        filesCell.innerHTML = '<i class="fa fa-exclamation-triangle" aria-hidden="true"></i>';
                    } 
                    else if(count <= 350){
                        filesCell.classList.add("yellow-cell");
                        filesCell.textContent = count;
                    }
                    else {
                        filesCell.classList.add("green-cell");
                        filesCell.textContent = count;
                    }
                });
            });
    
            console.log("Dados do relatório exibidos com sucesso.");
        } catch (error) {
            console.error("Erro ao obter o relatório:", error);
        }
    }
    
}

// Instanciando e inicializando a classe
const relatorioCores = new RelatorioCores();
