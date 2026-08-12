import re

# ============================================================
# CONFIGURAÇÃO
# ============================================================

# Procura um IPv4

PADRAO_IP = r'(?<!\d)(?:\d{1,3}\.){3}\d{1,3}(?!\d)'

# Procura um prefixo de rede /0 até /32

PADRAO_PREFIXO = r'/\s*(3[0-2]|[12]?\d)\b'
CAMPOS = ["LAN", "WAN", "SBC", "SIPTG"]

# ============================================================
# VALIDAÇÃO DO IP
# ============================================================

def ip_valido(ip):

    """
    Verifica se o IP é um IPv4 válido.
    Exemplo válido:
        10.10.10.10
    Exemplo inválido:
        999.999.999.999
    """

    try:
        octetos = ip.split(".")
        if len(octetos) != 4:
            return False
        return all(
            0 <= int(octeto) <= 255
            for octeto in octetos
        )
    except ValueError:
        return False

# ============================================================
# EXTRAÇÃO DOS IPS E BARRAMENTOS
# ============================================================

def extrair_ips(texto):
    resultado = {
        "LAN": {
            "ip": None,
            "barramento": None
        },
        "WAN": {
            "ip": None,
            "barramento": None
        },
        "SBC": {
            "ip": None,
            "barramento": None
        },
        "SIPTG": {
            "ip": None,
            "barramento": None
        },
    }
    # Percorre o texto linha por linha
    for linha in texto.splitlines():
        # Procura LAN, WAN ou SBC
        for campo in CAMPOS:
            marcador = re.search(
                rf'\b{campo}\b',
                linha,
                re.IGNORECASE
            )
            # Não encontrou o campo nessa linha
            if not marcador:
                continue
            # Ignora tudo que está antes de LAN/WAN/SBC
            trecho = linha[marcador.end():]
            # Procura IP depois do marcador
            ips_encontrados = re.findall(
                PADRAO_IP,
                trecho
            )
            # Valida os IPs encontrados
            for ip in ips_encontrados:
                if not ip_valido(ip):
                    continue
                # Guarda somente o IP
                resultado[campo]["ip"] = ip
                # Procura o barramento/prefixo depois do IP
                posicao_ip = trecho.find(ip)
                trecho_depois_ip = trecho[
                    posicao_ip + len(ip):
                ]
                prefixo = re.search(
                    PADRAO_PREFIXO,
                    trecho_depois_ip
                )
                if prefixo:
                    resultado[campo]["barramento"] = (
                        "/" + prefixo.group(1)
                    )
                break
    return resultado