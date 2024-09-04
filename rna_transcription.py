def to_rna(dna_strand):
    rna = ""
    for item in dna_strand:
        if item == "G":
            rna = rna + "C"
        if item == "C":
            rna = rna + "G"
        if item == "T":
            rna = rna + "A"
        if item == "A":
            rna = rna + "U"
    return rna
