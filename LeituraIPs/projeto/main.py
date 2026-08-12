from fastapi import FastAPI
from pydantic import BaseModel

from extractor import extrair_ips
from storage import (
    inserir_registro,
    carregar_dados
)

app = FastAPI(
    title="API Consulta IP",
    version="1.0"
)


class Entrada(BaseModel):
    texto: str


@app.post("/extrair")
def extrair(dados: Entrada):

    resultado = extrair_ips(
        dados.texto
    )

    inserir_registro(resultado)

    return resultado


@app.get("/historico")
def historico():

    return carregar_dados()


@app.get("/")
def home():

    return {
        "mensagem": "API Consulta IP Online",
        "swagger": "/docs"
    }

@app.post("/extrair")
def extrair(dados: Entrada):

    resultado = extrair_ips(
        dados.texto
    )

    inserir_registro(resultado)

    return resultado

@app.get("/historico")
def historico():

    return carregar_dados()