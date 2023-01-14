import networkx as nx

grid = nx.MultiGraph(nx.grid_2d_graph(4,4))
grid = nx.eulerize(grid)
print('->'.join(str(edge[0]) for edge in nx.eulerian_circuit(grid, (0, 0))))

drawing = nx.nx_agraph.to_agraph(grid)
drawing.layout()
drawing.draw('plow_truck.png')
