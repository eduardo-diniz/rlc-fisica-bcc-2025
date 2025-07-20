import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Simulador RLC", layout="centered")

# Estilo global com fundo moderno
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #e0f2f1, #ffffff);
    }

    .stApp {
        background-color: #ADD8E6;
    }

    .stSidebar {
        background-color: #e3f2fd !important;
    }

    h1 {
        text-align: center;
        color: #007acc;
        text-shadow: 1px 1px 1px #ccc;
    }

    .stNumberInput > div > div > input {
        border-radius: 8px;
        border: 1px solid #ccc;
    }

    .stRadio > div {
        background-color: #f0f4f8;
        padding: 10px;
        border-radius: 8px;
    }


    .block-container {
        padding: 2rem;
        background-color: #ffffff;
        border: 2px solid #007acc;
        border-radius: 15px;
        box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
        margin-top: 6rem;
    }
    </style>
""", unsafe_allow_html=True)

# Créditos
st.markdown("""
<div class="creditos">
    <h4>Autores do Projeto</h4>
    <ul>
        <li><strong>Eduardo Gomes</strong></li>
        <li><strong>Fabio Barros</strong></li>
        <li><strong>Marco Antonio</strong></li>
        <li><strong>Rodrigo Tibiriça</strong></li>
    </ul>
    <h4>Orientador</h4>
    <p><strong>Prof. Dr. Marcos George Moreno</strong></p>
    <p><em>Projeto acadêmico para a disciplina de Física Aplicada à Computação (2025.1)</em></p>
    <p>🔗 <a href="https://github.com/eduardo-diniz/rlc-fisica-bcc-2025.git" target="_blank">Repositório no GitHub</a></p>
</div>
""", unsafe_allow_html=True)

# Título
st.title("Simulador de Circuito RLC com Runge-Kutta 4ª Ordem")
st.markdown("Explore o comportamento de um circuito **RLC** série sob uma fonte de tensão CC ou CA, utilizando o método numérico de **Runge-Kutta de 4ª ordem**.")

col1, col2 = st.columns(2)

# Entradas do circuito
with col1:
    st.header("Parâmetros do Circuito")
    R = st.number_input(
        "Resistência R (Ω)",
        value=10.0,
        step=1.0,
        help="Valor da resistência elétrica (R), que limita o fluxo de corrente no circuito."
    )
    L = st.number_input(
        "Indutância L (H)",
        value=0.01,
        step=0.001,
        format="%.4f",
        help="Valor da indutância (L), que se opõe à variação da corrente elétrica."
    )
    C = st.number_input(
        "Capacitância C (F)",
        value=0.001,
        step=0.0001,
        format="%.4f",
        help="Valor da capacitância (C), que armazena energia na forma de campo elétrico."
    )

# Fonte
with col2:
    st.header("Fonte de Tensão")
    tipo_fonte = st.radio(
        "Tipo de Fonte",
        ["Corrente Contínua (CC)", "Corrente Alternada (CA)"],
        help="Escolha entre uma fonte de tensão constante (CC) ou senoidal (CA)."
    )
    if tipo_fonte == "Corrente Contínua (CC)":
        V0 = st.number_input(
            "Tensão da fonte CC (V)",
            value=5.0,
            help="Valor constante da tensão fornecida pela fonte de corrente contínua."
        )
        def V(t): return V0
    else:
        A = st.number_input(
            "Amplitude (V)",
            value=5.0,
            help="Valor máximo (positivo ou negativo) da tensão senoidal da fonte CA."
        )
        f = st.number_input(
            "Frequência (Hz)",
            value=60.0,
            help="Número de ciclos por segundo (Hz) da fonte senoidal."
        )
        def V(t): return A * np.sin(2 * np.pi * f * t)

# Simulação
st.markdown("---")
st.header("Configurações da Simulação")
col3, col4, col5 = st.columns(3)
with col3:
    tf = st.number_input(
        "Tempo final (s)",
        value=0.1,
        step=0.01,
        help="Tempo total da simulação (duração em segundos)."
    )
with col4:
    h = st.number_input(
        "Passo de tempo (s)",
        value=1e-5,
        format="%.1e",
        help="Tamanho do intervalo entre os pontos simulados (quanto menor, mais preciso)."
    )
with col5:
    t0 = 0.0
    n = int((tf - t0) / h)

# Inicialização
x = np.zeros((n, 2))  # [I, dI/dt]
x[0, 0] = 0
x[0, 1] = 0
tempo = np.linspace(t0, tf, n)

# Equações diferenciais
def derivadas(t, x):
    I = x[0]
    dIdt = x[1]
    d2Idt2 = (1 / L) * (V(t) - R * dIdt - (1 / C) * I)
    return np.array([dIdt, d2Idt2])

# Runge-Kutta
for i in range(n - 1):
    t = tempo[i]
    k1 = h * derivadas(t, x[i])
    k2 = h * derivadas(t + h / 2, x[i] + k1 / 2)
    k3 = h * derivadas(t + h / 2, x[i] + k2 / 2)
    k4 = h * derivadas(t + h, x[i] + k3)
    x[i + 1] = x[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6

# Gráfico
st.markdown("---")
st.subheader("Corrente no circuito RLC")

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(tempo, x[:, 0], label="I(t)", color='#007acc', linewidth=2)
ax.set_xlabel("Tempo (s)")
ax.set_ylabel("Corrente (A)")
ax.set_title("Resposta do Circuito", fontsize=14)
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend()
st.pyplot(fig)

st.caption("💡 Dica: ajuste os valores de R, L e C para visualizar diferentes regimes de amortecimento.")
