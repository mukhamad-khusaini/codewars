def dna_to_rna(dna):
    return "".join([i if i!="T" else "U" for i in dna])

print(dna_to_rna("GCAAATT"))