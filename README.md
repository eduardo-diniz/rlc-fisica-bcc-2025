
# 🔌 Simulador de Circuito RLC com Runge-Kutta 4ª Ordem

Este projeto implementa um simulador interativo de circuitos RLC série utilizando o método de **Runge-Kutta de 4ª ordem (RK4)** para resolver numericamente a equação diferencial da corrente.

A interface gráfica é feita com [Streamlit](https://streamlit.io), permitindo simulações via navegador.

---

## 🚀 Funcionalidades

- Escolha entre fonte de tensão **contínua (CC)** ou **senoidal (CA)**
- Definição de:
  - Resistência (R)
  - Indutância (L)
  - Capacitância (C)
  - Tensão (CC) ou Amplitude e Frequência (CA)
- Gráfico da corrente \( I(t) \)
- Simulação com o método **Runge-Kutta de 4ª ordem**

---

## ⚙️ Como executar o projeto

Você pode executar o projeto localmente com os seguintes passos:

### 1. Clone este repositório

```bash
git clone https://github.com/seu-usuario/simulador-rlc.git
cd simulador-rlc
```

### 2. Crie um ambiente virtual (recomendado)

```bash
python -m venv venv
```

### 3. Ative o ambiente virtual

- **Windows:**
  ```bash
  .\venv\Scripts\activate
  ```

- **Linux/macOS:**
  ```bash
  source venv/bin/activate
  ```

### 4. Instale as dependências

Se você tiver o `requirements.txt`:

```bash
pip install -r requirements.txt
```

Ou instale manualmente:

```bash
pip install streamlit matplotlib numpy
```

### 5. Execute a aplicação

```bash
streamlit run projeto.py
```

> Caso o comando `streamlit` não funcione, use:
```bash
python -m streamlit run projeto.py
```

---

## 📚 Equação usada

A equação diferencial do circuito RLC série é:

\[
L \frac{d^2I}{dt^2} + R \frac{dI}{dt} + \frac{1}{C} I = V(t)
\]

O método de Runge-Kutta de 4ª ordem é usado para resolver numericamente o sistema equivalente.

---

## 📁 Estrutura do projeto

```
simulador-rlc/
│
├── projeto.py              # Código principal com Streamlit
├── README.md               # Este arquivo
├── requirements.txt        # Lista de dependências
└── exemplo.gif             # (Opcional) Animação ou imagem do app
```

---

## Autores

- Eduardo Gomes  - Fabio Barros - Marco Antonio - Rodrigo Tibiriça
- Projeto acadêmico para disciplina de Fisica Aplicada à Computação (2025.1)

---

## 📝 Licença

Este projeto está disponível para uso pessoal e educacional. Sinta-se livre para modificar.
