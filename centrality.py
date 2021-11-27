from igraph import *
import numpy as np

g = Graph.Read_GraphML('teimourpour_tags_without_zero_degrees.graphml')

centralities = {
    'Degree': g.degree(),
    'Closeness': g.closeness(),
    'Betweenness': g.betweenness(),
    'EigenVector': g.eigenvector_centrality(),
}
centality_names = list(centralities.keys())
for centrality in centality_names:
    i_index = centality_names.index(centrality)
    for j in range(i_index + 1, len(centality_names)):
        other_centrality = centality_names[j]
        x = centralities[centrality]
        y = centralities[other_centrality]
        x_set = np.asanyarray(x).reshape(-1, 1)
        y_set = np.asanyarray(y)
        print(f"{centrality}_{other_centrality}")
        # Pearson correlation
        r = np.corrcoef(x, y)
        print('Pearson Correlation')
        print(r[0, 1])