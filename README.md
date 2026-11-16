# Aplicação Flask com Docker e GitHub Actions

API simples em Python e Flask, empacotada em uma imagem Docker. A integração contínua constrói a imagem, inicia o contêiner e executa testes de integração contra a aplicação em execução.

## Aplicação

| Rota | Descrição | Exemplo |
|---|---|---|
| `GET /` | Mensagem de boas-vindas | `{"mensagem":"Olá, Docker!"}` |
| `GET /health` | Verificação de saúde | `{"status":"ok"}` |
| `GET /soma?a=2&b=3` | Soma dois números | `{"resultado":5.0}` |

A rota `/soma` responde com HTTP 400 se os parâmetros estiverem ausentes ou não forem numéricos.

## Arquivos principais

- `app.py`: aplicação Flask e rotas da API.
- `Dockerfile`: imagem baseada em Python 3.12, com Gunicorn como servidor.
- `tests/test_app.py`: testes HTTP da aplicação.
- `.github/workflows/ci.yml`: workflow acionado em pushes para `main` e em Pull Requests.

## Construir e executar

Na pasta que contém o Dockerfile:

```bash
docker build -t projeto-docker .
docker run -d --name projeto-docker-app -p 5000:5000 projeto-docker
```

Confira as respostas em outro terminal:

```bash
curl http://localhost:5000/
curl http://localhost:5000/health
curl "http://localhost:5000/soma?a=2&b=3"
```

Para encerrar e remover o contêiner:

```bash
docker rm -f projeto-docker-app
```

## Testes automatizados

Com o contêiner em execução, instale as dependências de desenvolvimento e rode os testes:

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -v
```

Os testes verificam que `/` e `/health` respondem corretamente, que `/soma` calcula 2 + 3 e que uma chamada a `/soma` sem parâmetros retorna HTTP 400. Uma falha em qualquer asserção faz o passo de testes do workflow falhar.

## Evidência da aplicação funcionando

![Aplicação funcionando no Docker](docs/evidencia.png)

## Experimento de falha na CI

- **Execução com erro:** [ver execução que falhou](https://github.com/Matheus-Gon10/projeto-docker/actions/runs/43782713652/job/133023320804?pr=1)

- **Execução após a correção:** [ver execução aprovada](https://github.com/Matheus-Gon10/projeto-docker/actions/runs/43783215884/job/133024940907?pr=1)


