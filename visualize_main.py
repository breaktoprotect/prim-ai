import PrimDNA as PDNA
import PrimVisualize as PViz

def poc_visualize():
    prim = PDNA.PrimDNA(12)
    print("[DEBUG] DNA to string:",prim.to_string(pretty=True))

    # Convert genetic code to Graph for visualization
    PViz.display_gene_to_graph(PDNA.decode_genetics(prim.get_genetic_code(), 2, 3, 2))



if __name__ == "__main__":
    poc_visualize()