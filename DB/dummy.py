#!/usr/bin/env python3
from db_api import DatabaseLayer

accession_code = 'AB001517'
chromosomal_loc = '21q22.3'
genBank_id = 'TMEM1'
protein_name = 'BAA21136.1'

db = DatabaseLayer()
gene_entry = db.get_accession_code(accession_code)

gene_entry2 = db.get_chromosomal_loc(chromosomal_loc)

gene_entry3 = db.get_gene_id(genBank_id)

gene_entry4 = db.get_protein_product(protein_name)

print(gene_entry, gene_entry2, gene_entry3, gene_entry4)











    
