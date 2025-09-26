# 🔎 Visualizador de Circuito Hamiltoniano

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![NetworkX](https://img.shields.io/badge/NetworkX-2A628F?style=for-the-badge)

Uma aplicação web interativa construída com Streamlit para encontrar e visualizar **Circuitos Hamiltonianos** em grafos não direcionados. A ferramenta utiliza um algoritmo de backtracking para determinar se um circuito existe e, em caso afirmativo, o exibe visualmente.

---

## 🎯 O que é um Circuito Hamiltoniano?

Um **Circuito Hamiltoniano** é um caminho em um grafo que visita cada vértice (ou "nó") exatamente uma vez e retorna ao vértice inicial, formando um ciclo fechado.

Este é um problema clássico na teoria dos grafos, com aplicações práticas em logística, planejamento de rotas (como o Problema do Caixeiro Viajante), e design de circuitos.

---

## ✨ Funcionalidades

- **🎨 Interface Interativa**: Crie grafos facilmente selecionando o número de vértices e as arestas desejadas.
- **🧠 Algoritmo de Backtracking**: Utiliza uma abordagem de força bruta inteligente para explorar todas as possibilidades e encontrar um circuito.
- **📊 Visualização Clara**: Desenha o grafo e destaca o circuito Hamiltoniano encontrado em vermelho.
- **💡 Justificativas Inteligentes**: Se um circuito não for encontrado, a aplicação fornece uma explicação clara, como:
  - Vértices com grau insuficiente.
  - Grafos desconectados.
  - Presença de pontos de articulação (vértices críticos).

---

## 🚀 Como Executar

Siga os passos abaixo para rodar a aplicação em sua máquina local.

### 📋 Pré-requisitos

- 🐍 Python 3.8+

### ⚙️ Instalação

1.  **Clone o repositório (ou baixe os arquivos):**
    ```bash
    # Exemplo com git
    git clone <url-do-repositorio>
    cd <pasta-do-repositorio>
    ```

2.  **Crie um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

### ▶️ Rodando a Aplicação

1.  Abra o terminal na pasta do projeto.
2.  Execute o seguinte comando:
    ```bash
    streamlit run app.py
    ```
3.  A aplicação abrirá automaticamente no seu navegador!
