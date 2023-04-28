import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

    # Prompt the user to enter the number of nodes and the starting node
n = int(input("Enter the number of nodes: "))
start = int(input("Enter the starting node: "))

    # Display an example of an adjacency matrix for the user
print("Each cell in the matrix represents an edge between two nodes. If there is an edge between node i and node j, then the cell in the ith row and jth column will have a value of 1. If there is no edge between the two nodes, the value will be 0")
print("For example, if you have a graph with 4 nodes and edges (1,2), (1,3), (2,4), and (3,4), the adjacency matrix would be")
matrix = [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]
print("  ", end="")
for i in range(len(matrix)):
    print(i+1, end=" ")
print()
for i in range(len(matrix)):
    print(i+1, "|", end=" ")
    for j in range(len(matrix[i])):
        print(matrix[i][j], end="  ")
    print()

    # Prompt the user to enter the adjacency matrix values
matrix = []
for i in range(n):
    row = list(map(int, input(f"Enter the values for row {i+1}, separated by spaces: ").split()))
    matrix.append(row)
while True:

    # Prompt the user to choose the algorithm to visualize the graph
    print("\nChoose an algorithm to visualize the graph:")
    print("1. Depth-first search (DFS)")
    print("2. Breadth-first search (BFS)")
    print("3. Dijkstra's algorithm")
    print("4. A* algorithm")
    choice = int(input("Enter your choice (1-4): "))

    # Create a graph from the adjacency matrix
    G = nx.from_numpy_array(np.array(matrix))

    # Visualize the graph using the chosen algorithm
    if choice == 1:
        # Depth-first search
        pos = nx.spring_layout(G)
        visited = set()

        def dfs(v):
            visited.add(v)
            nx.draw_networkx_nodes(G, pos, nodelist=[v], node_color='r')
            for w in G.neighbors(v):
                if w not in visited:
                    nx.draw_networkx_edges(G, pos, edgelist=[(v,w)], edge_color='b')
                    dfs(w)

        for v in G.nodes:
            if v not in visited:
                dfs(v)
        nx.draw_networkx_labels(G, pos)

    elif choice == 2:
        # Breadth-first search
        pos = nx.spring_layout(G)
        visited = set()

        def bfs(v):
            queue = [v]
            visited.add(v)
            while queue:
                v = queue.pop(0)
                nx.draw_networkx_nodes(G, pos, nodelist=[v], node_color='r')
                for w in G.neighbors(v):
                    if w not in visited:
                        visited.add(w)
                        nx.draw_networkx_edges(G, pos, edgelist=[(v,w)], edge_color='b')
                        nx.draw_networkx_nodes(G, pos, nodelist=[w], node_color='y')
                        nx.draw_networkx_labels(G, pos)
                        queue.append(w)

        for v in G.nodes:
            if v not in visited:
                bfs(v)

    if choice == 3:
    # Dijkstra's algorithm
      pos = nx.spring_layout(G)
      path = nx.dijkstra_path(G, 0, n-1)
      nx.draw_networkx_nodes(G, pos)
      nx.draw_networkx_edges(G, pos)
      nx.draw_networkx_labels(G, pos)
      nx.draw_networkx_edges(G, pos, edgelist=list(zip(path,path[1:])), edge_color='r', width=2)
    elif choice == 4:
    # A* algorithm
      pos = nx.spring_layout(G)
      path = nx.astar_path(G, 0, n-1)
      nx.draw_networkx_nodes(G, pos)
      nx.draw_networkx_edges(G, pos)
      nx.draw_networkx_labels(G, pos)
      nx.draw_networkx_edges(G, pos, edgelist=list(zip(path,path[1:])), edge_color='r', width=2) 
    # Show the graph
    plt.show()