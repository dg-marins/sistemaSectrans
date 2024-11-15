async function obterVersionTag() {
    fetch('/api/git-tag/')
        .then(response => response.json())
        .then(data => {
            // Define o conteúdo do elemento com a tag do Git
            document.getElementById('git-tag').textContent = data.git_tag;
        })
        .catch(error => {
            console.error('Erro ao buscar a tag do Git:', error);
            document.getElementById('git-tag').textContent = "Erro ao carregar a tag";
        });
}

document.addEventListener("DOMContentLoaded", function() {
    obterVersionTag(); // Carrega as empresas ao inicializar a página
});