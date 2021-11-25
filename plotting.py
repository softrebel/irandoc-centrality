from igraph import *
g=Graph.Read_GraphML('teimourpour_tags_without_zero_degrees.graphml')
# layout = g.layout("kamada_kawai")
# layout = g.layout("fr")
plot(g,'kk.svg', layout=layout)