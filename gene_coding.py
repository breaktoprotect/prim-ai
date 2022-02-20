'''
Author      : Jeremy Soh @breaktoprotect
Date        : 20 Feb 2022
Description : A gene class in encoded in hexadecimal to be generated or translated to work on artificial neural networks
'''
import secrets

# Structure is based on David R. Miller's works - https://github.com/davidrmiller/biosim4
class PrimDNA:
    def _generate_genetics(size):
        #TODO size cannot be 0

        genetic_code = []

            
        return genetic_code
    def __init__(self, genetics_size):
        self.genetics_size = genetics_size # Each gene size is 8 characters in hexadecimal representation
        self.genetic_code = [] 
        # Initialize genetics
        char_set = "0123456789abcdef" # Hexadecimal
        for i in range(0,genetics_size):
            #* Generate a gene
            gene = ""
            for i in range(0, 8):
                gene += secrets.choice(char_set)

            self.genetic_code.append(gene)

    def to_string(self):
        genetic_code_text = ""
        for i in self.genetic_code:
            genetic_code_text = genetic_code_text + i + " "
        return genetic_code_text

    def decode(self):
        pass

#! Test only
if __name__ == "__main__":
    dna = PrimDNA(4)
    print(dna.to_string())