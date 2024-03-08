# Teste Prático para BackEnd Developer

Este é um projeto desenvolvido como parte do teste prático para a vaga de BackEnd Developer na Amicci.

## Descrição

A aplicação consiste em uma API para consulta de briefings, onde um Briefing é um documento que descreve um projeto a ser desenvolvido por um Fornecedor, a partir do levantamento realizado com o Cliente.

## Tecnologias Utilizadas

- Django/Python
- Django Rest Framework

## Pré-requisitos

- Python 3.x
- Ambiente virtual (venv)

## Configuração

1. Clone o repositório e crie o ambiente virtual:

```bash
git clone https://github.com/gradaschi/amicci-backend-test
cd amicci-backend-test

python3 -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate  # Para Windows
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute as migrações:

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Execute o container:

```bash
docker-compose up
```

## Endpoints da API

### 1. Listar Briefings

- **Método**: GET
- **Endpoint**: `/api/briefings/`
- **Descrição**: Retorna a lista de briefings.

### 2. Criar Novo Briefing

- **Método**: POST
- **Endpoint**: `/api/briefings/`
- **Descrição**: Cria um novo briefing.
- **JSON exemplo**:

```JSON
{
  "name": "Exemplo de Briefing",
  "retailer": "Exemplo Retailer",
  "responsible": "Exemplo Responsável",
  "category": "Exemplo Categoria",
  "release_date": "2024-03-07",
  "available": 10
}
```

### 3. Detalhes do Briefing por ID

- **Método**: GET
- **Endpoint**: `/api/briefings/{id}/`
- **Descrição**: Retorna detalhes de um briefing específico.

### 4. Atualizar Briefing por ID

- **Método**: PUT
- **Endpoint**: `/api/briefings/{id}/`
- **Descrição**: Atualiza um briefing específico.
- **JSON exemplo**:

```JSON
{
  "name": "Exemplo atualizado de Briefing",
  "retailer": "Exemplo atualizado de Retailer",
  "responsible": "Exemplo atualizado de Responsável",
  "category": "Exemplo atualizado de Categoria",
  "release_date": "2024-03-08",
  "available": 11
}
```

### 5. Excluir Briefing por ID

- **Método**: DELETE
- **Endpoint**: `/api/briefings/{id}/`
- **Descrição**: Exclui um briefing específico.

#

### 1. Listar Retailers

- **Método**: GET
- **Endpoint**: `/api/retailers/`
- **Descrição**: Retorna a lista de retailers.

### 2. Criar Novo Retailers

- **Método**: POST
- **Endpoint**: `/api/retailers/`
- **Descrição**: Cria um novo retailers.
- **JSON exemplo**:

```JSON
{
  "name": "Exemplo de Retailers",
  "vendors": [1,3]
}
```

### 3. Detalhes do Retailers por ID

- **Método**: GET
- **Endpoint**: `/api/retailers/{id}/`
- **Descrição**: Retorna detalhes de um retailers específico.

### 4. Atualizar Retailers por ID

- **Método**: PUT
- **Endpoint**: `/api/retailers/{id}/`
- **Descrição**: Atualiza um retailers específico.
- **JSON exemplo**:

```JSON
{
  "name": "Exemplo atualizado de Retailers",
  "vendors": [2,4]
}
```

### 5. Excluir Retailers por ID

- **Método**: DELETE
- **Endpoint**: `/api/retailers/{id}/`
- **Descrição**: Exclui um retailers específico.

#

### 1. Listar Categorias

- **Método**: GET
- **Endpoint**: `/api/categories/`
- **Descrição**: Retorna a lista de categorias.

### 2. Criar Nova Categoria

- **Método**: POST
- **Endpoint**: `/api/categories/`
- **Descrição**: Cria uma nova categoria.
- **JSON exemplo**:

```JSON
{
  "name": "Exemplo de Categoria",
  "description": "Descrição da categoria de exemplo"
}
```

### 3. Detalhes da Categoria por ID

- **Método**: GET
- **Endpoint**: `/api/categories/{id}/`
- **Descrição**: Retorna detalhes de uma categoria específica.

### 4. Atualizar Categoria por ID

- **Método**: PUT
- **Endpoint**: `/api/categories/{id}/`
- **Descrição**: Atualiza uma categoria específica.
- **JSON exemplo**:

```JSON
{
  "name": "Categoria Atualizada",
  "description": "Nova descrição da categoria"
}
```

### 5. Excluir Categoria por ID

- **Método**: DELETE
- **Endpoint**: `/api/categories/{id}/`
- **Descrição**: Exclui uma categoria específica.

#

### 1. Listar Vendors

- **Método**: GET
- **Endpoint**: `/api/vendors/`
- **Descrição**: Retorna a lista de fornecedores.

### 2. Criar Novo Vendor

- **Método**: POST
- **Endpoint**: `/api/vendors/`
- **Descrição**: Cria um novo fornecedor.
- **JSON exemplo**:

```JSON
{
  "name": "Exemplo de Fornecedor"
}
```

### 3. Detalhes do Vendor por ID

- **Método**: GET
- **Endpoint**: `/api/vendors/{id}/`
- **Descrição**: Retorna detalhes de um fornecedor específico.

### 4. Atualizar Vendor por ID

- **Método**: PUT
- **Endpoint**: `/api/vendors/{id}/`
- **Descrição**: Atualiza um fornecedor específico.
- **JSON exemplo**:

```JSON
{
  "name": "Fornecedor Atualizado"
}
```

### 5. Excluir Vendor por ID

- **Método**: DELETE
- **Endpoint**: `/api/vendors/{id}/`
- **Descrição**: Exclui um fornecedor específico.

## Testes

O projeto inclui testes unitários para garantir a estabilidade e confiabilidade.

```bash
python manage.py test
```
