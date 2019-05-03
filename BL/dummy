
def get_gene_entry(query):

    if (query in query_search):
        for entry in  gene_entry:
            return entry

gene_entry=[]

entry1 ={
    "accession_code":  '1234',
    "protein_name": 'protein1',
    "DNA_seq": 'TGAATTCATATGGAATTCTGCAATTATATTCA',
    "aminoacid_sequence":'IHMEFCNYI',
    "CDS": [1, 6],
    "codon_usage": ' this is a codon sequenc',
    "chromosomal_loc": '18iq',
    "genBank_id": '678'
}
gene_entry.append(entry1)

entry2 ={
    "accession_code":  '4321',
    "protein_name": 'protein2',
    "DNA_seq": 'TAATGCGCTCGATGAARTCTCGACGTA',
    "aminoacid_sequence":'IHMEFCNYITBGSHS',
    "CDS": [2, 15],
    "chromosomal_loc": '18iq',
    "genBank_id": '876'
}
gene_entry.append(entry2)

query_search=[]
for entry in gene_entry:
    query_search.append(entry.get("protein_name", ""))
    query_search.append(entry.get("accession_code", ""))
    query_search.append(entry.get("genBank_id2",""))

try1= get_gene_entry('678')
print(try1)
