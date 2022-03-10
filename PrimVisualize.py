import networkx as nx
import matplotlib.pyplot as plt

def display_gene_to_graph(genetics):
    Graph = nx.DiGraph()

    for gene in genetics:
        #debug
        print("gene:", gene)

        if gene['source_type'] == 0 and gene['sink_type'] == 0: #internal to internal
            Graph.add_edge(str(gene['source_id']) + " (internal)", str(gene['source_id']) + " (internal)")
        elif gene['source_type'] == 1 and gene['sink_type'] == 0: #input to internal
            Graph.add_edge(str(gene['source_id']) + " (Input)", str(gene['source_id']) + " (internal)")
        elif gene['source_type'] == 0 and gene['sink_type'] == 1: #internal to output
            Graph.add_edge(str(gene['source_id']) + " (internal)", str(gene['source_id']) + " (Output)")
        else: #directly input to output
            Graph.add_edge(str(gene['source_id']) + " (Input)", str(gene['source_id']) + " (Output)")

    nx.draw(Graph, with_labels=True)

    plt.show()



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