# Database Construction
**This code was written by Dwayne Thomas**
## Prequisites and installation

* Genbank file for chromosome 21 `chrom_CDS_21`.
* Configuration file `config.py` detailing parameters to connect to MySQL database store on the departmental server "**_hope_**".
* Access to MySQL from terminal.

## Functionality

### Genbank Parser
Run `create_tables.sql` to populate database.

Use `data_import.py` to parse the file and populate the database.

File `genbank_parser` class `genbank_parser` opens file object for given file. Each of the following functions within that class are to be used in the implementation in the following order:

1. `parse_accession()`: parses the next accession following the file position.

2. `parse_features()`: parses five features of the first coding sequence.

3. `parse_origin()`: parses the DNA sequence following the previous coding sequence.