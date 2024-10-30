# Sistema Sectrans

Este projeto está sendo desenvolvido com o intuito de gerenciar pedidos de mídias, equipamentos, empresas e geração de relatórios.

## Funcionalidades Base

### Sistema de Autenticação
- [x] Página de login implementada
- [x] Autenticação de usuários
- [x] Redirecionamento após login
- [x] Sistema de mensagens para feedback de login

### Interface do Usuário
- [x] Layout base responsivo
- [x] Header com logo e menu de navegação
- [x] Footer com informações de copyright
- [x] Tema consistente com cores personalizadas:
  - Cor principal: #f34d25
  - Cor secundária: #c5c5c5
  - Cor terciária: #e9e9e9

### Modelos de Dados

1. **Empresa**
   - Nome
   - Razão Social
   - VPN
   - Data de cadastro
   - Status (ativa/inativa)

2. **Rede**
   - Nome (único)
   - Chave
   - Status (ativa/inativa)
   - Vínculo com Empresa
   - Tipo de criptografia (WPA/WEP)
   - IP do servidor

3. **Carro**
   - Nome
   - Vínculo com Empresa
   - Vínculo com Rede
   - Modelo de equipamento
   - Número serial
   - IP (único por rede)

4. **Modelo_Equipamento**
   - Modelo

### Funcionalidades Administrativas
- [x] Interface administrativa personalizada
- [x] Listagem de empresas com filtros
- [x] Gestão de redes com busca
- [x] Administração de carros com atribuição automática de IP
- [x] Validações automáticas para:
  - IPs únicos por rede
  - Carros únicos por empresa
  - Formato válido de IP

### API e Endpoints
- [x] Listagem de empresas
- [x] Listagem de carros por empresa
- [x] Listagem de modelos de equipamento

### Pedido de Mídia
- [x] Interface para solicitação de gravação
- [x] Seleção dinâmica de:
  - Empresas
  - Carros
  - Modelos de equipamento
- [x] Atualização dinâmica dos campos dependentes

## Pendências/TODO
1. Implementação completa do sistema de gravação
2. Geração de relatórios
3. Gestão de equipamentos
4. Sistema de notificações
5. Dashboard com métricas
6. Histórico de pedidos
7. Gestão de usuários e permissões

## Notas de Implementação
- Sistema desenvolvido com Django
- Frontend com HTML/CSS puro
- JavaScript para interações dinâmicas
- Banco de dados PostgreSQL
- Estrutura modular e extensível

## Requisitos Técnicos
- Python 3.11+
- PostgreSQL 13+
- Django Framework

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
