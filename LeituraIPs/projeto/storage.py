import json
import os

ARQUIVO = "ips.json"


def carregar_dados():

    if not os.path.exists(ARQUIVO):
        return []

    with open(
        ARQUIVO,
        "r",
        encoding="utf-8"
    ) as arquivo:

        return json.load(arquivo)


def salvar_dados(dados):

    with open(
        ARQUIVO,
        "w",
        encoding="utf-8"
    ) as arquivo:

        json.dump(
            dados,
            arquivo,
            indent=4,
            ensure_ascii=False
        )


def inserir_registro(resultado):

    dados = carregar_dados()

    for tipo, info in resultado.items():

        if info["ip"]:

            dados.append({
                "tipo": tipo,
                "ip": info["ip"],
                "barramento": info["barramento"]
            })

    salvar_dados(dados)