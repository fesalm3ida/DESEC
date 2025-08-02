# RDAP (Registration Data Access Protocol)

## 📌 O que é RDAP?
RDAP é o sucessor moderno do protocolo WHOIS, oferecendo:

- **Dados estruturados** (formato JSON)
- **Padronização internacional** (RFC 7480-7484)
- **Suporte a caracteres internacionais**
- **Controle de acesso e limites de taxa**
- **Redirecionamento hierárquico**

## 🐍 Como usar RDAP em Python

### Consulta básica via HTTP
```python
import requests

dominio = "exemplo.com.br"
url = f"https://rdap.registro.br/domain/{dominio}"
response = requests.get(url, headers={"Accept": "application/rdap+json"})

if response.status_code == 200:
    print(response.json())
else:
    print("Erro:", response.status_code)