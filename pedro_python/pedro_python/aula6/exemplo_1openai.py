from openai import OpenAI
# inicializar o cliente
cliente = OpenAI(api_key="sk-proj-8YQ2pDneb2-mtrXnlGgVSpjF3d0RzulEPQ8mNO6bA6PUt5NBee5mlaucy")
# 
# OpenAI Dashboard -> Conta de vocês

# faz a chamada para o OpenAI
resposta = cliente.chat.completions.create(
    model='gpt-4o-mini', # gpt-4, gpt-5,gpt-4o
    messages=[
        {"role": "system", "content": "Você é um assistente que responde em português"},
        {"role": "user", "content": "Qual a diferença entre JavaScript e Java?"}
    ]
)

# exibe resposta do modelo
print(resposta.choices[0].message.content)