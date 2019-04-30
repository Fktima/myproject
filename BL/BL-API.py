#!/usr/bin/python3

"""
------------------------------------------------------------------------------------------------------------------------
This is the business logic API
Author: Miruna Serian
------------------------------------------------------------------------------------------------------------------------
"""
import re
import dummy as DB #using the dumy code instead of the DB api

class Search:
    """ Class that retrieves the query given by the user
    either as an AccessionCode, protein product name, Chromosomal location
    or GenBank identifier
    """

    def by_accession_code(accession_code):
        return DB.get_gene_entry()

    def by_protein_product(protein_name):
        return DB.get_gene_entry()

    def by_chromosomal_loc(chromosomal_loc):
        return DB.get_gene_entry()

    def by_genbank_identifier(genBank_id):
        return DB.get_gene_entry()
"""
------------------------------------------------------------------------------------------------------------------------
This is used by the front end to display information about the gene 
------------------------------------------------------------------------------------------------------------------------
"""
class SummaryList:
    """
    Class containing functions to display the summary list of all gene identifiers,
    protein product names, Genbank accession, chromosomal location. The front end
    should diplay the lists and one could click to see the details the particular gene
    """
    def get_gene_identifiers_list():
        gene_identifiers = DB.get_gene_list() #this ins not the actual name of the funcion from the DB API
        return gene_identifiers
    def get_protein_product_list():
        protein_product_names=DB.get_protein_product_names() #this ins not the actual name of the funcion from the DB API
        return protein_product_names
    def get_genbank_accession_liest():
        genbank_accession_list = DB.get_accessions() #this ins not the actual name of the funcion from the DB API
        return genbank_accession_list
    def get_chromosomal_loc_list():
        chromosomal_locations = DB.get_chromosomal_locations() #this ins not the actual name of the funcion from the DB API
        return chromosomal_locations

class Entry:
    """
    Class that displays information for a particular entry
    """
    def get_dna_seq(query):
        """ displays DNA seq associated with the query"""
        return DB.get_gene_entry(query)['DNA_seq']

    def get_aminoacid_seq(query):
        """ displays the amino acid sequence
         parameters: query, type string
        returns the amino acid sequence"""
        return DB.get_gene_entry(query)['aminoacid_sequence']

    def get_coding_seq(query):
        """
        displays the coding region
        Parameters: query, type string
        Ouput: CDS
        """
        coord =DB.get_gene_entry(query)['CDS']
        coding_seq = get_dna_seq(query)[coord[0]-1:coord[1]]
        return coding_seq

    def get_codon_usage(query):
        """
        displays the codon Usage
        parameters: query, type string
        output: frequencies, type dictionary
        """
        return codon_frequency(query)



"""
------------------------------------------------------------------------------------------------------------------------
Restriction enzymes
------------------------------------------------------------------------------------------------------------------------
"""

"""recognition_sites_5prime={
    "EcorI": "GAATTC",
    "BamHI": "GGATCC",
    "BsuMI": "CTCGAG"
}
"""
def find_restr_sites(query):
    cutting_sites= {}
def find_restriction_sites(query):
    """ this function determines the cutting sites for the enzymes. To be used by front end.
    Output: a dictionary of arrays of where the enzymes cut.
    """
    re_ecorI = re.compile(r'GAATTC')
    re_BamHI = re.compile(r'GGATCC')
    re_BsuMI = re.compile(r'CTCGAG')
    cutting_position_ecorI =[]
    cutting_position_BamHI =[]
    cutting_position_BsuMI =[]
    dna_seq = Entry.get_dna_seq(query)
    for a_match in  re_ecorI.finditer(dna_seq):
        cutting_position_ecorI.append(a_match.start()+1) #used +1 as enzyme cuts after first base in the recognition pattern
    for a_match in  re_BamHI.finditer(dna_seq):
        cutting_position_BamHI.append(a_match.start()+1)
    for a_match in  re_BsuMI.finditer(dna_seq):
        cutting_position_BsuMI.append(a_match.start()+1)
    cutting_positions_dict = {
        "ecorI": cutting_position_ecorI,
        "BamHI": cutting_position_BamHI,
        "BsuMI": cutting_position_BsuMI
    }
    return cutting_positions_dict


def check_which_enzyme_cuts(query):
    check_ecorI = False
    check_BamHI = False
    check_BsuMI = False
    if len(find_restriction_sites(query)['ecorI'])>0 :
        check_ecorI = True
    if len(find_restriction_sites(query)['BamHI'])>0:
        check_BamHI = True
    if len(find_restriction_sites(query)['BsuMI'])>0:
        check_BsuMI = True
    check_which_enzyme_dict ={
        "ecorI": check_ecorI,
        "BamHI": check_BamHI,
        "BsuMI": check_BsuMI
    }
    return check_which_enzyme_dict


"""
------------------------------------------------------------------------------------------------------------------------
Coding sequence and DNA to protein
------------------------------------------------------------------------------------------------------------------------
"""



table = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', '':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
}

def get_codons(query):
    dna_seq = Entry.get_dna_seq(query)
    codons = [dna_seq[i:i + 3] for i in range(0, len(dna_seq), 3)]
    for i in range(0, len(codons)):
        if len(codons[i])%3!=0:
            del codons[i]
    return(codons)

def DNA_to_protein(query):
    """
    converts DNA sequence obtained from GenBank to amino acid  sequence.
    :param query:
    :return: protein_seq, type strings
    """
    protein_seq= " "
    codons=get_codons(query)
    for codon in codons:
        protein_seq += table[codon]
    return(protein_seq)



def codon_frequency(query):
    """
    displays codon frequency as percentages rounded to 2 decimals
    :param query:
    :return: codon frequency
    """
    the_codons = get_codons(query)
    codon_freq={}
    for codon in the_codons:
        codon_freq[codon]=round(the_codons.count(codon)/len(the_codons)*100, 2)
    return(codon_freq)


a_try1=DNA_to_protein('678')
a_try2=codon_frequency('678')
a_try3=get_codons('678')

print(a_try1)
print(a_try2)
print(a_try3)
