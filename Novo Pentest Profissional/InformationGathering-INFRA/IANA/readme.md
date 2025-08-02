# 🌐 Resumo sobre IANA, RIRs, NIRs e ISPs

## 1️⃣ **IANA** (Internet Assigned Numbers Authority)
- **Função**: Autoridade máxima que coordena recursos críticos da Internet
- **Responsabilidades**:
  - Alocação global de blocos IPv4/IPv6
  - Gestão do sistema DNS raiz (.com, .org, etc.)
  - Registro de protocolos técnicos (portas, ASNs)
- **Site**: [iana.org](https://www.iana.org/)

## 2️⃣ **RIRs** (Regional Internet Registries)
- **Função**: Distribuem recursos IP regionalmente
- **Lista dos 5 RIRs**:

  | Região        | RIR       | Cobertura               | Site |
  |---------------|-----------|-------------------------|------|
  | América do N  | ARIN      | EUA/Canadá              | [arin.net](https://arin.net) |
  | América Latina| LACNIC    | América Latina/Caribe   | [lacnic.net](https://lacnic.net) |
  | Europa        | RIPE NCC  | Europa/Ásia Central     | [ripe.net](https://ripe.net) |
  | Ásia-Pacífico | APNIC     | Ásia/Oceania            | [apnic.net](https://apnic.net) |
  | África        | AFRINIC   | África                  | [afrinic.net](https://afrinic.net) |

## 3️⃣ **NIRs** (National Internet Registries)
- **Função**: Operam em nível nacional (sob RIRs)
- **Exemplos**:
  - Brasil: [NIC.br](https://nic.br)
  - Japão: [JPNIC](https://jpnic.net)
  - China: [CNNIC](https://cnnic.cn)
- **Atribuições**:
  - Gerencia recursos IP no país
  - Mantém registros locais WHOIS/RDAP

## 4️⃣ **ISPs** (Internet Service Providers)
- **Hierarquia**:
  ```mermaid
  graph LR
    IANA-->RIRs
    RIRs-->NIRs
    RIRs/NIRs-->ISPs_Tier1
    ISPs_Tier1-->ISPs_Tier2
    ISPs_Tier2-->ISPs_Tier3
    ISPs_Tier3-->Usuários