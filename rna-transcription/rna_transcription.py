def to_rna(dna_strand):
    dna_bases = ["G", "C", "T", "A"]
    if not set(dna_strand).issubset(dna_bases) or dna_strand == "":
        raise ValueError(dna_strand, "is not correct DNA strand.")
    bases_num = len(dna_strand)
    positions = range(bases_num)
    rna_dictionary = {"G":"C", "C":"G", "T":"A", "A":"U"}
    rna_strand = ""
    for base in positions:
        rna_strand += rna_dictionary[dna_strand[base]]
    return rna_strand
