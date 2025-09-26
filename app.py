import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations

# --- Lógica do Algoritmo de Backtracking (COMPLETA) ---
def is_valid(v, G, path, pos):
    """
    Verifica se o vértice 'v' pode ser adicionado ao caminho na posição 'pos'.
    """
    # Verifica se a aresta entre o último vértice no caminho e 'v' existe
    if v not in G.neighbors(path[pos - 1]):
        return False

    # Verifica se o vértice 'v' já foi incluído no caminho
    if v in path:
        return False
        
    return True

def hamiltonian_circuit_util(G, path, pos):
    """
    Função recursiva para encontrar o circuito hamiltoniano.
    """
    # Caso base: Se todos os vértices forem incluídos no caminho
    if pos == len(G.nodes()):
        # Verifica se há uma aresta do último vértice para o primeiro
        if path[pos - 1] in G.neighbors(path[0]):
            return True
        else:
            return False

    # Tenta um vértice de cada vez
    for v in G.nodes():
        if is_valid(v, G, path, pos):
            path[pos] = v
            
            if hamiltonian_circuit_util(G, path, pos + 1):
                return True
            
            # Se a tentativa falhar, remove o vértice e faz 'backtracking'
            path[pos] = -1
    
    return False

def get_solution(graph_nodes, graph_edges):
    """
    Função principal que inicializa o algoritmo de backtracking.
    """
    G = nx.Graph()
    G.add_nodes_from(graph_nodes)
    G.add_edges_from(graph_edges)
    
    path = [-1] * len(G.nodes())
    path[0] = list(G.nodes())[0]  # Começa com o primeiro nó

    if not hamiltonian_circuit_util(G, path, 1):
        return None
    
    # Se uma solução for encontrada, adicione o primeiro nó ao final para fechar o ciclo
    path.append(path[0])
    return path

def justificar_falha(G):
    """
    Verifica condições simples que impedem a existência de um circuito Hamiltoniano
    e retorna uma string com a justificativa.
    """
    # 1. Verifica se algum vértice tem grau < 2
    for node, degree in G.degree():
        if degree < 2:
            return f"**Justificativa:** O vértice **{node}** tem grau {degree}, que é menor que 2. Para um circuito existir, todos os vértices devem ter grau de pelo menos 2 (uma aresta para entrar e uma para sair)."

    # 2. Verifica se o grafo é conectado
    if not nx.is_connected(G):
        num_components = nx.number_connected_components(G)
        return f"**Justificativa:** O grafo não é conectado. Ele possui **{num_components}** componentes separados, tornando impossível visitar todos os vértices em um único circuito."

    # 3. Verifica se existem pontos de articulação (cut vertices)
    articulation_points = list(nx.articulation_points(G))
    if articulation_points:
        return f"**Justificativa:** O grafo possui pontos de articulação (vértices críticos): **{', '.join(map(str, articulation_points))}**. A remoção de qualquer um desses vértices desconectaria o grafo, o que impede a formação de um circuito Hamiltoniano."

    return "O algoritmo de backtracking explorou todas as possibilidades e confirmou que não existe um caminho que visite cada vértice exatamente uma vez antes de retornar ao início."

# --- Interface Gráfica com Streamlit ---

st.set_page_config(page_title="Circuito Hamiltoniano", layout="wide")

st.title("🔎 Visualizador de Circuito Hamiltoniano")
st.write("Esta ferramenta utiliza um algoritmo de backtracking para encontrar um circuito Hamiltoniano em um grafo não direcionado.")

with st.expander("💡 O que é um Circuito Hamiltoniano e onde é usado?"):
    st.markdown("""
    Um **Circuito Hamiltoniano** é um caminho em um grafo que visita cada vértice (ou "nó") exatamente uma vez e retorna ao vértice inicial, formando um ciclo fechado.
    
    **Exemplo de Aplicação:** Imagine um robô que precisa perfurar vários buracos em uma placa de circuito. Para otimizar o tempo, ele deve seguir um caminho que passe por cada ponto de perfuração exatamente uma vez e volte ao início, minimizando a distância total. Encontrar esse caminho é um problema clássico relacionado ao Circuito Hamiltoniano.
    """)

# --- Barra Lateral para Entradas ---
st.sidebar.header("⚙️ Configurações do Grafo")

num_nodes = st.sidebar.slider("Número de Vértices", 3, 10, 5, key="num_nodes")

# Gera todas as arestas possíveis para o número de vértices selecionado
possible_edges_tuples = list(combinations(range(1, num_nodes + 1), 2))
possible_edges_str = [f"{u}-{v}" for u, v in possible_edges_tuples]

# Gera um ciclo padrão para ser pré-selecionado
default_edges = []
if num_nodes > 0:
    # Adiciona arestas como 1-2, 2-3, ...
    for i in range(1, num_nodes):
        default_edges.append(f"{i}-{i+1}")
    # Fecha o ciclo com a aresta n-1
    default_edges.append(f"1-{num_nodes}")

selected_edges = st.sidebar.multiselect(
    "Selecione as Arestas",
    options=possible_edges_str,
    default=default_edges,
    help="Escolha as arestas que formarão o seu grafo."
)

if st.sidebar.button("Encontrar Circuito", use_container_width=True):
    try:
        with st.spinner("Calculando... O algoritmo pode levar um tempo."):
            nodes = list(range(1, num_nodes + 1))
            edges = [tuple(map(int, edge.split('-'))) for edge in selected_edges]
            
            # Chama a função de resolução
            solution = get_solution(nodes, edges)
            
            # Layout em duas colunas para o resultado
            col1, col2 = st.columns([1, 2])

            with col1:
                st.subheader("📊 Resultado")
                if solution:
                    st.success("Circuito Hamiltoniano Encontrado!")
                    st.write("Caminho:")
                    st.code(" -> ".join(map(str, solution)))
                else:
                    # Cria o grafo para análise da falha
                    G_fail = nx.Graph()
                    G_fail.add_nodes_from(nodes)
                    G_fail.add_edges_from(edges)
                    justificativa = justificar_falha(G_fail)
                    st.error("Nenhum circuito hamiltoniano foi encontrado para o grafo fornecido.")
                    st.warning(justificativa)

            with col2:
                G = nx.Graph()
                G.add_nodes_from(nodes)
                G.add_edges_from(edges)
                
                pos = nx.spring_layout(G, seed=42)
                fig, ax = plt.subplots(figsize=(8, 6))
                nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, edge_color='gray', font_size=12, ax=ax)
                if solution:
                    path_edges = list(zip(solution, solution[1:]))
                    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2.5, ax=ax)
                st.pyplot(fig)

    except ValueError:
        st.error("Formato de entrada de arestas inválido. Por favor, use '1-2, 2-3, ...'")