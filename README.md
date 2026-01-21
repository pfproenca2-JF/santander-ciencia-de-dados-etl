📊 Pipeline ETL com IA Generativa: Personalização de CRM Bancário
Este projeto foi desenvolvido como o desafio final do curso Santander Ciência de Dados com Python. O objetivo é demonstrar um fluxo completo de ETL (Extract, Transform, Load), integrando Python com a API da OpenAI para criar uma experiência de marketing personalizada para clientes bancários.
🚀 Contexto do Projeto
No cenário atual, a personalização é a chave para o engajamento. Este pipeline automatiza a criação de mensagens de incentivo a investimentos, transformando dados brutos de clientes em comunicações estratégicas geradas por Inteligência Artificial.
🛠️ Tecnologias e Ferramentas
Linguagem: Python
Bibliotecas: Pandas (Manipulação de dados), OpenAI SDK (IA Generativa), JSON/CSV (Formatos de dados).
Infraestrutura Mobile: Termux e Editor GNU nano (para gestão de arquivos e segurança de credenciais via terminal).
🔄 O Fluxo ETL
1. Extract (Extração)
O pipeline inicia lendo uma lista de IDs de usuários a partir de um arquivo SDW2023.csv. Como a API original do desafio estava instável, implementei uma camada de Mock Data para garantir que o fluxo lógico de extração permanecesse funcional e resiliente.
2. Transform (Transformação)
Utilizei o modelo GPT-4o-mini da OpenAI para processar o nome de cada cliente e gerar uma dica de investimento exclusiva.
Engenharia de Prompt: O sistema atua como um especialista em marketing bancário, gerando textos curtos e persuasivos.
3. Load (Carga)
Os dados transformados, agora contendo as novas mensagens de marketing, são exportados para um arquivo SDW2023_final.json. Este arquivo simula a carga final em um banco de dados de produção ou sistema de CRM.
🔐 Segurança e Boas Práticas
Gestão de Segredos: Implementei a sanitização de chaves de API antes da publicação no GitHub, garantindo que credenciais sensíveis nunca sejam expostas no histórico de commits.
Versionamento: Uso estratégico de mensagens de commit para documentar a evolução do desenvolvimento.
