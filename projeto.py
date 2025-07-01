import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("🔌 Simulador de Circuito RLC com Runge-Kutta 4ª Ordem")

# Entrada dos parâmetros
st.sidebar.header("Parâmetros do Circuito")
R = st.sidebar.number_input("Resistência R (Ohms)", value=10.0)
L = st.sidebar.number_input("Indutância L (Henries)", value=0.01)
C = st.sidebar.number_input("Capacitância C (Farads)", value=0.001)

tipo_fonte = st.sidebar.radio("Tipo de Fonte", ["Corrente Contínua (CC)", "Corrente Alternada (CA)"])

# Define a fonte de tensão
if tipo_fonte == "Corrente Contínua (CC)":
    V0 = st.sidebar.number_input("Tensão da fonte CC (V)", value=5.0)
    def V(t): return V0
else:
    A = st.sidebar.number_input("Amplitude da fonte CA (V)", value=5.0)
    f = st.sidebar.number_input("Frequência da fonte CA (Hz)", value=60.0)
    def V(t): return A * np.sin(2 * np.pi * f * t)

# Parâmetros de simulação
st.sidebar.header("Simulação")
t0 = 0.0
tf = st.sidebar.number_input("Tempo final de simulação (s)", value=0.1)
h = st.sidebar.number_input("Passo de tempo (s)", value=1e-5, format="%.1e")
n = int((tf - t0) / h)

# Condições iniciais
x = np.zeros((n, 2))
x[0, 0] = 0  # Corrente inicial I(0)
x[0, 1] = 0  # Derivada da corrente dI/dt(0)

tempo = np.linspace(t0, tf, n)

# Derivadas do sistema
def derivadas(t, x):
    I = x[0]
    dIdt = x[1]
    d2Idt2 = (1 / L) * (V(t) - R * dIdt - (1 / C) * I)
    return np.array([dIdt, d2Idt2])

# Método de Runge-Kutta 4ª ordem
for i in range(n - 1):
    t = tempo[i]
    k1 = h * derivadas(t, x[i])
    k2 = h * derivadas(t + h / 2, x[i] + k1 / 2)
    k3 = h * derivadas(t + h / 2, x[i] + k2 / 2)
    k4 = h * derivadas(t + h, x[i] + k3)
    x[i + 1] = x[i] + (k1 + 2*k2 + 2*k3 + k4) / 6

# Gráfico
st.subheader("📈 Corrente no circuito RLC")
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(tempo, x[:, 0], label="I(t)", color='tab:blue')
ax.set_xlabel("Tempo (s)")
ax.set_ylabel("Corrente (A)")
ax.grid(True)
ax.legend()
st.pyplot(fig)
