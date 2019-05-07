# Business Layer API Documentation

#### The middle layer code was writen by Miruna Serian


## Prerequisites and installation
- in order to access the database, use the config.py in the **Database Layer**

- the database is stored on **Hope server** and access to it is essential

## Functionality
###Display summary list


Class `Summary List` contains functions to generate a list of either:

- gene identifiers:  `get_gene_identifiers_list()` 
- protein product: `get_protein_product_list()`
- Genbank accession codes: `get_genbank_accession_list()`  
- chromosomal location: `get_chromosomal_loc_list()`
- all entries:`get_all_entries()`

These functions can be called to retrieve the lists from the database.
### Display information about specific entry  ###

All of the below functions take the input query as parameter:

- **DNA sequence**: type *string*

    `Entry.get_dna_seq()`

	Output example:
	`'TGAATTCATATGGAATTCTGCAATTATATTCA'`

	
	

- **Aminoacid sequence** : type *string*

    `Entry.get_aminoacid_seq()`

	Output example:
	`'IHMEFCNYI'`

- **CDS coordinates** : type *list of lists*
    
	`Entry.get_CDS_coord()`: Returns a lists of lists containing pairs of coordinates

	Output example:
	`[[12, 167], [180, 356]]`

- **Coding Sequence** : type *string*

    `Entry.get_coding_seq()`: returns the only the coding sequence of the DNA
- **Codon frequency** : type *dictionary*

     `Entry.get_codon_frequency()`: returns a dictionary of all codons found in the DNA coding sequence

	Output example:
	`{'TGA': 10.0, 'ATT': 20.0, 'CAT': 10.0, 'ATG': 10.0, 'GAA': 10.0, 'TTC': 10.0, 'TGC': 10.0, 'AAT': 10.0, 'TAT': 10.0}`
	
- **Find which restriction enzyme cuts**: type *dictionary*

    `Entry.get_which_enzyme_cuts()`: returns a dictionary of keys being the name of the restriction enzyme and values being True or False depending on whether they cut in the non coding sequence of the DNA or not

	Output Example:
	`{'ecorI': False, 'BamHI': False, 'BsuMI': True}`

- **Restriction enzyme cutting sites**: type*dictionary*

    `Entry.get_restriction_sites()`: returns a dictionary containing the restriction sites and their cutting positions stored in a list

	Output example:
	`{'ecorI': [167, 233], 'BamHI': [864], 'BsuMI': []}`
	
- **Codon frequency for all entries in the database**: type *dictionary*

    `Entry.get_frequency_all_data()`: returns a dictionary of all codons found in all DNA sequences in the database
