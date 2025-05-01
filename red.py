import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo dirigido
G = nx.DiGraph()

# Agregar nodos (conceptos)
conceptos = ["Inteligencia Artificial", "Aprendizaje Automático", "Redes Neuronales", "Algoritmos", "Datos"]
G.add_nodes_from(conceptos)

# Agregar relaciones (aristas)
relaciones = [
    ("Inteligencia Artificial", "Aprendizaje Automático"),
    ("Aprendizaje Automático", "Redes Neuronales"),
    ("Redes Neuronales", "Algoritmos"),
    ("Algoritmos", "Datos"),
    ("Datos", "Aprendizaje Automático")  # Círculo de dependencia
]
G.add_edges_from(relaciones)

# Dibujar la red semántica
plt.figure(figsize=(8,6))
pos = nx.spring_layout(G)  # Disposición del grafo
nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=3000, font_size=10)
plt.title("Red Semántica Simple")
plt.show()
