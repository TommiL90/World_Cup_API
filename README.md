# Projeto: 🏁 Kopa do Mundo

## Introdução
API básica, desenvolvida para organizar um campeonato de futebol, onde cada time representará uma seleção nacional. Para manter o mínimo de organização, se implementam algumas validações.

O desenvolvimento do projeto será realizado com Python, Django, Rest-Framework

## Rotas
A seguir, estão listadas as rotas disponíveis na API:

### Cadastrar Seleção
- **Endpoint**: api/teams/
- **Verbo HTTP**: POST
- **Objetivo**: Cadastrar uma nova seleção nacional.

### Listar Seleções
- **Endpoint**: api/teams/
- **Verbo HTTP**: GET
- **Objetivo**: Listar todas as seleções nacionais disponíveis.

### Filtragem de Seleção
- **Endpoint**: api/teams/<team_id>/
- **Verbo HTTP**: GET
- **Objetivo**: Obter detalhes de uma seleção nacional específica com base em seu ID.

### Atualização de Seleção
- **Endpoint**: api/teams/<team_id>/
- **Verbo HTTP**: PATCH
- **Objetivo**: Atualizar informações de uma seleção nacional específica com base em seu ID.

### Deleção de Seleção
- **Endpoint**: api/teams/<team_id>/
- **Verbo HTTP**: DELETE
- **Objetivo**: Excluir uma seleção nacional específica com base em seu ID.

## Como rodar os testes localmente
 - Verifique se os pacotes pytest e/ou pytest-testdox estão instalados globalmente em seu sistema:
```shell
pip list
```
- Caso seja listado o pytest e/ou pytest-testdox e/ou pytest-django em seu ambiente global, utilize os seguintes comando para desinstalá-los globalmente:

```shell
pip uninstall pytest pytest-testdox -y
```
---

## Próximos passos:

## 1 Clone e instale o projeto

### 2 Crie seu ambiente virtual:
```shell
python -m venv venv
```

### 3 Ative seu venv:

```shell
# linux:
source venv/bin/activate

# windows:
.\venv\Scripts\activate
```

### 4 Instalar o pacote <strong>pytest-testdox</strong>:

```shell
pip install pytest-testdox pytest-django
```


### 5 Rodar os testes referentes a cada tarefa isoladamente:

Exemplo:

- Tarefa 0

```shell
pytest --testdox -vvs tests/tarefas/tarefa_0/
```

---

## Observações
O projeto basico, foi desenvolvido para fines academicos y de aprendizagem.


