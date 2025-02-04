import streamlit as st

def analisar_credito(renda, pontuacao_credito, idade, historico_pagamento):
    """Analisa o crédito com base nos critérios definidos."""
    
    if idade > 60:
        return "🔴 Rejeitado (Idade acima de 60 anos)"

    if renda > 5000 and pontuacao_credito > 700 and historico_pagamento:
        return "🟢 Aprovado"

    if renda < 5000 and pontuacao_credito < 600:
        return "🔴 Rejeitado"

    return "🟡 Em análise manual"

# Interface Gráfica com Streamlit
st.title("💳 Análise de Crédito")

# Entrada do usuário
renda = st.number_input("💰 Renda Mensal (R$)", min_value=0, step=500)
pontuacao_credito = st.slider("📊 Pontuação de Crédito", 0, 1000, 500)
idade = st.number_input("🎂 Idade", min_value=18, max_value=100, step=1)
historico_pagamento = st.checkbox("✅ Bom Histórico de Pagamento?")

# Botão para análise
if st.button("🔍 Analisar Crédito"):
    resultado = analisar_credito(renda, pontuacao_credito, idade, historico_pagamento)
    st.subheader(f"Resultado: {resultado}")
