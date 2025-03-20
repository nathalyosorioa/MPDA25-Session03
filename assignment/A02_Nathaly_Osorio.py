#r: networkx
#r: matplotlib

import networkx as nx #type: ignore
import matplotlib.pyplot as plt #type: ignore

#create a Graph
G = nx.Graph()

#add nodes
G.add_node('Colombia')
G.add_node('Ecuador')
G.add_node('Peru')
G.add_node('Bolivia')
G.add_node('Venezuela')
G.add_node('Guyana')
G.add_node('Suriname')
G.add_node('French_Guyana')
G.add_node('Brasil')
G.add_node('Paraguay')
G.add_node('Uruguay')
G.add_node('Argentina')
G.add_node('Chile')

#add edges
G.add_edge('Colombia', 'Ecuador')
G.add_edge('Colombia', 'Venezuela')
G.add_edge('Colombia', 'Brasil')
G.add_edge('Colombia', 'Peru')
G.add_edge('Venezuela', 'Brasil')
G.add_edge('Venezuela', 'Guyana')
G.add_edge('Guyana', 'Brasil')
G.add_edge('Guyana', 'Suriname')
G.add_edge('Suriname', 'French_Guyana')
G.add_edge('Brasil', 'Suriname')
G.add_edge('French_Guyana', 'Brasil')
G.add_edge('Brasil', 'Ecuador')
G.add_edge('Brasil', 'Peru')
G.add_edge('Brasil', 'Bolivia')
G.add_edge('Brasil', 'Paraguay')
G.add_edge('Brasil', 'Argentina')
G.add_edge('Brasil', 'Uruguay')
G.add_edge('Ecuador', 'Peru')
G.add_edge('Bolivia', 'Peru')
G.add_edge('Chile', 'Peru')
G.add_edge('Bolivia', 'Paraguay')
G.add_edge('Bolivia', 'Argentina')
G.add_edge('Bolivia', 'Chile')
G.add_edge('Paraguay', 'Argentina')
G.add_edge('Chile', 'Argentina')
G.add_edge('Uruguay', 'Argentina')


#add position to display
pos = nx.spring_layout(G)

#draw serttings
fig = plt.figure(figsize=(10,10))
ax = plt.subplot()
ax.set_title('South America Neighboring Countries', fontsize=12)
nx.draw(G, pos, node_size=1500, with_labels=True, node_color='pink', font_size=9, font_color='black')

#draw the graph
plt.tight_layout()


#plot
path= r"C:\Users\57301\Desktop\Maestría\AT PY\session02-20250319T131422Z-001\session02\images\MPDA_plot1.png"
plt.savefig(path, format="PNG")