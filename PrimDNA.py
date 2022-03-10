'''
Author      : Jeremy Soh @breaktoprotect
Date        : 20 Feb 2022
Description : A gene class in encoded in hexadecimal to be generated or translated to work on artificial neural networks
'''
import secrets
from bitstring import BitArray

# Encoding structure is heavily influenced by David R. Miller's works - https://github.com/davidrmiller/biosim4
class PrimDNA:
    def __init__(self, num_connections):
        self.genetics_size = num_connections # Each connection is a size of 8 characters in hexadecimal representation
        self.genetic_code = [] 

        # Initialize genetics
        char_set = "0123456789abcdef" # Hexadecimal
        for i in range(0, num_connections):
            #* Generate a gene
            gene = ""
            for i in range(0, 8):
                gene += secrets.choice(char_set)

            self.genetic_code.append(gene)

    def get_genetic_code(self):
        return self.genetic_code

    def to_string(self,pretty=True): #pretty=True spaces out every 4 bytes
        genetic_code_text = ""
        for i in self.genetic_code:
            if pretty:
                genetic_code_text = genetic_code_text + i + " "
            else:
                genetic_code_text = genetic_code_text + i
        return genetic_code_text

#*** Helper methods ***
#* Gene decoder
#  Converts hexadecimal encoding into artificial neural network information
#? For reference: Encoding structure
'''
Left to right orientation
Bit 0       : Source neuron type. 0 is input sensory neuron; 1 is internal neuron
Bit 1 - 7   : Source neuron ID (either input sensory neuron or internal neuron); Unsigned
Bit 8       : Sink neuron type. 0 is output action neuron, 1 is internal neuron
Bit 9 - 15  : Sink neuron ID (either output action neuron or internal neuron); Unsigned
Bit 16 - 23 : Signed 8-bit integer value of weight
Bit 24 - 31 : Signed 8-bit integer value of bias (only applies to internal node; all others ignored)
For example -> [0][1110101][0][1011101][01101010][10010011]
'''
def _decode_gene(hex_gene, num_inputs, num_internals, num_outputs):
    # 1. Convert hexadecimal to binary (str)
    # Solution from: https://stackoverflow.com/questions/1425493/convert-hex-to-binary
    rep = 16 # hexadecimal
    bits = 32 # Expecting 32-bit
    bin_gene_str = bin(int(hex_gene, rep))[2:].zfill(bits)

    # 2. Neural network dict
    conn_dict = {
        'source_type': int(bin_gene_str[0]),
        'source_id': int(bin_gene_str[1:8], 2) % (num_inputs + num_internals),
        'sink_type': int(bin_gene_str[8], 2),
        'sink_id': int(bin_gene_str[9:16], 2) % (num_outputs + num_internals),
        'weight': BitArray(bin=bin_gene_str[16:24]).int / 127,  # normalized to range between -1.0 to 1.0
        'bias': BitArray(bin=bin_gene_str[24:32]).int / 127  # normalized to range between -1.0 to 1.0
    }

    return conn_dict

def decode_genetics(genetic_code, num_inputs, num_internals, num_outputs):
    decoded_dict_list = []
    for i in genetic_code:
        decoded_dict_list.append(_decode_gene(i, num_inputs, num_internals, num_outputs))

    return decoded_dict_list

#! Test only
if __name__ == "__main__":
    prim = PrimDNA(1)
    print("[DEBUG] DNA to string:",prim.to_string(pretty=True))
    print("[DEBUG] Gene decoded:", decode_genetics(prim.get_genetic_code(), 6, 3, 2))