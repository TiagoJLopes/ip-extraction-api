# API Consulta IP

## 📌 Sobre o Projeto

A **API Consulta IP** foi desenvolvida para automatizar a análise de bilhetes operacionais na área de redes e telecomunicações.

A solução processa textos não estruturados, identifica informações relevantes de rede e extrai automaticamente endereços IPv4 e seus respectivos prefixos (CIDR) associados aos ambientes:

- LAN
- WAN
- SBC
- SIPTG

Além da API REST, o projeto conta com uma interface web desenvolvida em **Streamlit**, permitindo que analistas coletem informações de um bilhete e obtenham os IPs extraídos em poucos segundos.

### Benefícios

- Redução da análise manual de chamados.
- Padronização da coleta de informações.
- Maior agilidade operacional.
- Diminuição de erros humanos.
- Facilidade para consultas futuras.

---

## 🚀 Funcionalidades

- Extração automática de endereços IPv4.
- Validação de IPv4.
- Identificação de prefixos CIDR (/0 até /32).
- Processamento de textos não estruturados.
- Extração dos campos LAN, WAN, SBC e SIPTG.
- Retorno estruturado em JSON.
- Persistência dos resultados em arquivo JSON.
- API REST com documentação Swagger/OpenAPI.
- Interface Web para usuários não técnicos.
- Testes compatíveis com Postman.

---

## 🏗️ Arquitetura

```text
Bilhete Operacional
        ↓
 Interface Web (Streamlit)
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
- Streamlit
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
├── app.py
├── main.py
├── extractor.py
├── storage.py
├── ips.json
├── requirements.txt
└── README.md
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

Extrai IPs e prefixos encontrados no texto informado.

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

Retorna todos os registros armazenados no arquivo JSON.

#### Exemplo de Resposta

```json
[
  {
    "tipo": "WAN",
    "ip": "200.200.250.200",
    "barramento": "/30"
  },
  {
    "tipo": "LAN",
    "ip": "10.10.10.10",
    "barramento": "/29"
  }
]
```

---

## 💻 Interface Web

A aplicação possui uma interface desenvolvida com Streamlit para facilitar a utilização por analistas operacionais.

### Fluxo de Uso

1. Abrir a aplicação no navegador.
2. Colar o texto completo do bilhete.
3. Clicar em **Analisar**.
4. Visualizar os IPs e prefixos identificados automaticamente.

---

## ⚙️ Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/SEU-USUARIO/consulta-ip.git
```

```bash
cd consulta-ip
```

### 2. Criar ambiente virtual

#### Windows

```bash
python -m venv .venv
```

```bash
.venv\Scripts\activate
```

#### Linux/macOS

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar a API

```bash
uvicorn main:app --reload
```

API disponível em:

```text
http://localhost:8000
```

Documentação Swagger:

```text
http://localhost:8000/docs
```

### 5. Executar a Interface Web

```bash
streamlit run app.py
```

Interface disponível em:

```text
http://localhost:8501
```

---

## 🎯 Caso de Uso

### Antes

```text
Analista lê o bilhete manualmente.
Localiza os IPs.
Anota os dados.
Valida as informações.
```

### Depois

```text
Analista cola o bilhete.
Sistema extrai automaticamente.
Resultado apresentado em segundos.
```

---

## 👨‍💻 Autor

**Tiago Junqueira Lopes**

Desenvolvido como projeto de automação voltado para operações de redes e telecomunicações, aplicando Python, FastAPI, Streamlit e Expressões Regulares para otimizar a análise de bilhetes operacionais.

---

## 📜 Licença

Este projeto está disponível para fins de estudo, aprendizado e demonstração de portfólio.
