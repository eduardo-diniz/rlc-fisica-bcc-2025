# 🔄 Simulador RLC com Método de Runge-Kutta 4ª Ordem

Este é um simulador interativo de circuitos RLC em regime transiente, implementado com o método de Runge-Kutta de 4ª ordem e interface gráfica em [Streamlit](https://streamlit.io/). Ele permite simular a corrente de um circuito RLC série ao longo do tempo com parâmetros ajustáveis.

---



## 🧪 Funcionalidades

- Simulação numérica com método de Runge-Kutta de 4ª ordem.
- Ajuste de parâmetros: resistência (R), capacitância (C), indutância (L), tempo total (T) e passo (h).
- Visualização gráfica da corrente em função do tempo.
- Exportação dos dados simulados em CSV (com amostragem).

---

## ⚙️ Requisitos

- Python 3.8 ou superior
- Navegador web moderno (Chrome, Firefox, etc.)

---

## 📦 Instalação

### ✅ 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/simulador-rlc.git
cd simulador-rlc
```

✅ 2. (Opcional, mas recomendado) Crie um ambiente virtual
No macOS/Linux:
```bash

python3 -m venv venv
source venv/bin/activate
```
No Windows:
```bash

python -m venv venv
venv\Scripts\activate
```
✅ 3. Instale as dependências
```bash

pip install -r requirements.txt
```
Se preferir, instale manualmente:

```bash

pip install streamlit numpy matplotlib pandas
```
▶️ Executando o simulador
```bash

streamlit run simulador_rlc.py
```
📂 Estrutura do Projeto

simulador-rlc/
├── simulador_rlc.py
├── requirements.txt
├── README.md
└── .github/
 
💡 Notas
O CSV exportado possui amostragem para reduzir o tamanho do arquivo (configurável no código via fator_amostragem).

A simulação utiliza condições iniciais: corrente inicial = 0, carga inicial = 0.

## Autores

- Eduardo Gomes  - Fabio Barros - Marco Antonio - Rodrigo Tibiriça
- Projeto acadêmico para disciplina de Fisica Aplicada à Computação (2025.1)

---

## 📝 Licença

Este projeto está disponível para uso pessoal e educacional. Sinta-se livre para modificar.
](https://fisica-bcc-2025.streamlit.app/)](https://fisica-bcc-2025.streamlit.app/)
