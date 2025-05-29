import os
import requests
import json

api_key = os.getenv("DEEPSEEK_API_KEY")
diff = os.getenv("DIFF", "")[:6000]  # limite de segurança

if not diff.strip():
    print("No diff to review.")
    with open("review_result.txt", "w") as f:
        f.write("Nenhuma alteração relevante encontrada no diff.")
    exit(0)

prompt = f"""
Você é um revisor de código experiente.

Analise o seguinte diff de código. Faça comentários objetivos apenas sobre mudanças que realmente impactam o comportamento do código, a clareza ou a manutenção. 

Não comente mudanças triviais como renomeações simples ou ajustes cosméticos, a menos que causem erro ou inconsistência. 

Evite explicações excessivamente longas. Seja direto, técnico e relevante.

### Diff:
{diff}
"""

response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
  },
  data=json.dumps({
    "model": "deepseek/deepseek-r1-0528-qwen3-8b:free",
     "messages": [
            {"role": "system", "content": "Você é um revisor de código."},
            {"role": "user", "content": prompt}
    ],
  })
)

result = response.json()
review = result["choices"][0]["message"]["content"]

print("\n--- Code Review Result ---\n")
print(review)

with open("review_result.txt", "w") as f:
    f.write(review)