# Sistema Sectrans

Este projeto está sendo desenvolvido com o intuito de gerenciar pedidos de mídias, equipamentos, empresas e geração de relatórios.

## Requisitos

Antes de instalar, certifique-se de que o seu ambiente possui os seguintes requisitos:

- **Python** 3.11 ou superior
- **PostgreSQL** 13 ou superior

## Instalação

### 1. Clone o Repositório

```bash
git clone https://github.com/dg-marins/sistemaSectrans.git

cd sistemaSectrans
```

### 2. Crie e Ative um Ambiente Virtual

```bash
python3 -m venv venv

# No Linux
source venv/bin/activate  

# No Windows
venv\Scripts\activate
```

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 4. Aplique as Migrações

```bash
python manage.py migrate
```

### 5. Crie um Superusuário

```bash
python manage.py createsuperuser
```

### 7. Execute o Servidor

```bash
python manage.py runserver
```