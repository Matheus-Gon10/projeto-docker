"""Testes de integração: rodam contra a aplicação já em execução no contêiner."""
import os

import requests

BASE_URL = os.getenv("APP_URL", "http://localhost:5000")


def test_rota_raiz_responde():
    r = requests.get(f"{BASE_URL}/", timeout=5)
    assert r.status_code == 200
    assert r.json() == {"mensagem": "Olá, Docker!"}


def test_health():
    r = requests.get(f"{BASE_URL}/health", timeout=5)
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_soma_valida():
    r = requests.get(f"{BASE_URL}/soma", params={"a": 2, "b": 3}, timeout=5)
    assert r.status_code == 200
    assert r.json()["resultado"] == 5


def test_soma_sem_parametros_retorna_400():
    r = requests.get(f"{BASE_URL}/soma", timeout=5)
    assert r.status_code == 400
