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

> Pendente: salvar uma captura de tela das respostas da aplicação executada em contêiner e adicioná-la ao repositório (por exemplo, em `docs/evidencia.png`). A captura deve mostrar as chamadas e respostas de `/`, `/health` e `/soma`.

## Experimento de falha na CI

Para registrar o experimento exigido:

1. Em uma branch de trabalho, altere temporariamente a soma em `app.py` de `a + b` para `a - b`.
2. Abra um Pull Request com essa alteração e aguarde a execução da CI. O teste de `test_soma_valida` deve falhar, pois recebe `-1` em vez de `5`.
3. Registre o link dessa execução com erro abaixo.
4. Corrija a operação para `a + b`, sem remover ou enfraquecer os testes, e envie a correção ao mesmo Pull Request.
5. Registre o link da execução aprovada abaixo.

- **Erro introduzido:** a rota `/soma` subtrai os valores (`a - b`) em vez de somá-los.
- **Causa da falha:** `test_soma_valida` espera `5` para os parâmetros `a=2` e `b=3`, mas recebe `-1`.
- **Execução com erro:** pendente — inserir o link da execução na aba Actions.
- **Correção:** restaurar `a + b`; manter os testes existentes.
- **Execução após a correção:** pendente — inserir o link da execução aprovada na aba Actions.

## Publicação

> Pendente: publicar este projeto em um repositório GitHub e substituir os campos pendentes acima pelos links e pela evidência reais.
