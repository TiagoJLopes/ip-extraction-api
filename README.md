# API Consulta IP

## 📌 Sobre o Projeto

A API Consulta IP foi desenvolvida para automatizar a análise de bilhetes operacionais.

O objetivo da solução é processar textos não estruturados, identificar informações relevantes de rede e extrair automaticamente endereços IPv4 associados aos ambientes:

- LAN
- WAN
- SBC

A aplicação reduz a necessidade de análise manual dos bilhetes, padronizando a coleta de informações e facilitando consultas futuras.

---

## 🚀 Funcionalidades

- Extração automática de endereços IPv4.
- Validação de IPv4 para garantir consistência dos dados.
- Identificação de prefixos de rede (CIDR).
- Processamento de textos não estruturados.
- Retorno dos resultados em formato JSON.
- Persistência dos dados em arquivo JSON.
- API REST documentada automaticamente com Swagger/OpenAPI.
- Testes compatíveis com Postman.

---

## 🏗️ Arquitetura

```text
Bilhete Operacional
        ↓
     FastAPI
        ↓
  Extração com Regex
        ↓
   Validação IPv4
        ↓
 Persistência JSON
        ↓
   Retorno JSON
```

---

## 🛠️ Tecnologias Utilizadas

- Python
- FastAPI
- Uvicorn
- Regex (Expressões Regulares)
- JSON
- Swagger/OpenAPI
- Postman
- Git
- GitHub

---

## 📂 Estrutura do Projeto

```text
projeto/
│
├── main.py
├── extractor.py
├── storage.py
├── ips.json
└── requirements.txt
```

---

## 🔍 Exemplo de Entrada

```json
{
  "texto": "WAN 200.200.250.200/30 LAN 10.10.10.10/29 SBC 172.16.110.5/28 SIPTG 100.100.100.100/24"
}
```

---

## ✅ Exemplo de Saída

```json
{
  "LAN": {
    "ip": "10.10.10.10",
    "barramento": "/29"
  },
  "WAN": {
    "ip": "200.200.250.200",
    "barramento": "/30"
  },
  "SBC": {
    "ip": "172.16.110.5",
    "barramento": "/28"
  },
  "SIPTG": {
    "ip": "100.100.100.100",
    "barramento": "/24"
  }
}
```

---

## 📡 Endpoints

### POST /extrair

Extrai os IPs encontrados no texto informado.

#### Exemplo

```http
POST /extrair
```

Body:

```json
{
  "texto": "WAN 200.200.250.200/30 LAN 10.10.10.10/29"
}
```

---

### GET /historico

Retorna
