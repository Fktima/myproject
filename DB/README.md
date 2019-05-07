# Database Layer API Documentation
**This code was written by Dwayne Thomas**
## Prequisites and installation

* Configuration file `config.py` detailing parameters to connect to MySQL database store on the departmental server "**_hope_**".

## Functionality

### Retreive stored information on chromosome 21
Class `DBAccessLayer` establishes connection with the database and has the following functions within:

-`get_accession_code()`: executes the database query for the stored equivalent of the accession_code.

-`get_chromosomal_loc()`: executes the database query for the stored equivalent of the chromosomal location.

-`get_gene_id()`: executes the database query for the stored equivalent of the gene identifier/name.

-`get_protein_product()`: executes the database query for the stored equivalent of the protein product/name.

Each of these functions are dependent on the following boolean type parameters which should be specified in calling the function:

-`return_dna`: returns DNA sequence for given query.
-`return_cds`: retrieves coding sequence for given query.
-`return_protein`: retreives protein sequence for given query.
-`return_attributes`: retieves accession code and protein name for given query.

The default of each is set to `False`
