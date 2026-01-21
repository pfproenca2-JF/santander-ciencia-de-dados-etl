import pandas as pd
import json
from openai import OpenAI

# CONFIGURAÇÃO - A chave fica vazia para segurança no GitHub
OPENAI_API_KEY = 'SUA_CHAVE_AQUI'
client = OpenAI(api_key=OPENAI_API_KEY)

print("Iniciando Pipeline ETL - Santander Ciência de Dados...")

# --- E: EXTRACT ---
# Simulação de dados (Mock) devido à indisponibilidade da API original
users_mock = [
    {"id": 1, "name": "Pyterson", "news": []},
    {"id": 2, "name": "Pip", "news": []},
    {"id": 3, "name": "Pep", "news": []}
]
print("Extração concluída.")

# --- T: TRANSFORM ---
def generate_ai_news(user):
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Você é um especialista em marketing bancário."},
                {"role": "user", "content": f"Crie uma mensagem para {user['name']} sobre investimentos (máx 100 caracteres)"}
            ]
        )
        return completion.choices[0].message.content.strip('\"')
    except Exception as e:
        return f"Dica: Invista no seu futuro!"

for user in users_mock:
    user['news'].append({
        "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
        "description": generate_ai_news(user)
    })

# --- L: LOAD ---
print("\n--- RESULTADO FINAL ---")
print(json.dumps(users_mock, indent=2, ensure_ascii=False))

with open('SDW2023_final.json', 'w', encoding='utf-8') as f:
    json.dump(users_mock, f, ensure_ascii=False, indent=2)

print("\nPipeline concluído com sucesso!")

