#!/usr/bin/env python3
from db_api import DatabaseLayer
# quotes need to removed to make searching from FE compatible

accession_code = 'AB001517'
chromosomal_loc = '"21q22.3"'
gene_id = '"TMEM1"'
protein_product = '"TMEM1 protein"'

db = DatabaseLayer()


gene_entry = db.get_protein_product(protein_product)
print(gene_entry)
gene_entry2 = db.get_accession_code(accession_code)
print(gene_entry2)
gene_entry3 = db.get_gene_id(gene_id)
print(gene_entry3)
gene_entry4 = db.get_chromosomal_loc(chromosomal_loc)
print(gene_entry4)












    
