# santander-ciencia-de-dados-etl
# Pipeline ETL: Santander Ciência de Dados com Python 📊

Este projeto simula um fluxo de dados bancários (ETL) utilizando Python e IA Generativa.

## 📝 Descrição do Problema
O objetivo é engajar clientes de forma personalizada, transformando dados brutos em mensagens de marketing focadas em investimentos através da API do GPT-4.

## 🛠️ Tecnologias Utilizadas
- **Python** (Pandas, Requests)
- **OpenAI API** (IA Generativa para textos)
- **JSON/CSV** (Armazenamento de dados)

## 🔄 O Ciclo ETL
1. **Extract (Extração):** Leitura de IDs de clientes a partir de um arquivo CSV.
2. **Transform (Transformação):** Processamento de dados via IA para gerar dicas personalizadas.
3. **Load (Carga):** Exportação dos dados enriquecidos para um arquivo JSON final.

> **Nota:** Como o endpoint da API original da Santander Dev Week 2023 está offline, o projeto utiliza uma simulação de dados (Mock) para garantir a execução do fluxo lógico.
