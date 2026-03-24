import pandas as pd
import requests
import streamlit as st
from data.banco_dados import carregar_dados

# =========== CONFIGURAÇÕES DO OLLAMA ===========
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss:20b"

# =========== CARREGAR DADOS ===========
# Carregamos o DataFrame com as movimentações da escola de dança
df_transacoes = carregar_dados()

caixa_inicial = 5000.00
total_receitas = df_transacoes[df_transacoes['tipo'] == 'Receita']['valor'].sum()
total_despesas = df_transacoes[df_transacoes['tipo'] == 'Despesa']['valor'].sum()
saldo_atual = caixa_inicial + total_receitas + total_despesas 

# =========== MONTAR CONTEXTO ===========

contexto = f"""
RESUMO FINANCEIRO DA ESCOLA DE DANÇA:
- Caixa Inicial: R$ {caixa_inicial:.2f}
- Total de Receitas no período: R$ {total_receitas:.2f}
- Total de Despesas no período: R$ {total_despesas:.2f}
- Saldo atual estimado: R$ {saldo_atual:.2f}

HISTÓRICO DE TRANSAÇÕES (Últimos registros):
{df_transacoes.tail(10).to_string(index=False)}
"""

# =========== SYSTEM PROMPT ===========

SYSTEM_PROMPT = """Você é o Fin, um agente de prospecção financeiro consultivo e investigador.

OBJETIVO:
Você irá comparar o fluxo de entrada e saída de dinheiro do banco de dados do programa: seus descritivos, valores, datas, número de matrículas novas, número de cancelamento de matrículas, etc., e com base nessas métricas irá apresentar o histórico e estimar possíveis entradas/saídas e projetar um gráfico de déficit/superavit para os meses seguintes.

REGRAS:
1. Responder apenas com base nos dados internos fornecidos
2. Utilizar dados internos de no máximo 1 ano para evitar discrepâncias
3. Se não souber algo, admita e ofereça alternativas"""

# =========== CHAMAR OLLAMA ===========
def perguntar(msg):
    prompt_completo = f"""
    {SYSTEM_PROMPT}
    
    CONTEXTO DO CLIENTE:
    {contexto}
    
    Pergunta: {msg}"""
    
    payload = {
        "model": MODELO,
        "prompt": prompt_completo,
        "stream": False
    }
    
    r = requests.post(OLLAMA_URL, json=payload)
    return r.json()['response']

# =========== INTERFACE ===========
st.title("🩰 Fin, Seu Assistente Financeiro")

if pergunta := st.chat_input("Pergunte algo sobre o caixa, eventos ou projeções..."):
    
    st.chat_message("user").write(pergunta)
    
    with st.spinner("Analisando e gerando resposta..."):
        resposta = perguntar(pergunta)
        st.chat_message("assistant").write(resposta)