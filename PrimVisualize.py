import networkx as nx
import matplotlib.pyplot as plt

def display_gene_to_graph(genetics):
    Graph = nx.DiGraph()

    # Adding nodes - positional
    for gene in genetics:
        # Adding internal node
        if gene['sink_type'] == 0: # internal
            Graph.add_node(str(gene['sink_id']) + " (internal)", pos=(2, gene['sink_id']))
        else: # gene['source_type'] == 0
            Graph.add_node(str(gene['source_id']) + " (internal)", pos=(2, gene['source_id']))
        
        # Adding Input node
        if gene['source_type'] == 1: #input
            Graph.add_node(str(gene['source_id']) + " (Input)", pos=(1, gene['source_id']))
        
        # Adding Output node
        if gene['sink_type'] == 1: #output
            Graph.add_node(str(gene['sink_id']) + " (Output)", pos=(3, gene['sink_id']))

    # Adding node edges (directed)
    for gene in genetics:
        #debug
        print("gene:", gene)

        if gene['source_type'] == 0 and gene['sink_type'] == 0: #internal to internal
            Graph.add_edge(str(gene['source_id']) + " (internal)", str(gene['sink_id']) + " (internal)")
        elif gene['source_type'] == 1 and gene['sink_type'] == 0: #input to internal
            Graph.add_edge(str(gene['source_id']) + " (Input)", str(gene['sink_id']) + " (internal)")
        elif gene['source_type'] == 0 and gene['sink_type'] == 1: #internal to output
            Graph.add_edge(str(gene['source_id']) + " (internal)", str(gene['sink_id']) + " (Output)")
        else: #directly input to output
            Graph.add_edge(str(gene['source_id']) + " (Input)", str(gene['sink_id']) + " (Output)")

    pos=nx.get_node_attributes(Graph, 'pos')
    nx.draw(Graph, pos=pos, with_labels=True)

    plt.show()

def test_pos_poc():
    Graph = nx.DiGraph()

    Graph.add_node("1", pos=(1,1))
    Graph.add_node("2", pos=(2,1))
    
    nx.draw(Graph,with_labels=True)

#! Test POC only - kept only for reference
def test_poc():
    Graph = nx.DiGraph()

    Graph.add_node("alpha")
    Graph.add_node("alpha")
    Graph.add_node("bravo")

    Graph.add_edge("alpha", "bravo")

    nx.draw(Graph, with_labels=True)

    plt.show()

#! Testing only
if __name__ == "__main__":
    pass