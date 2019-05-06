DROP TABLE IF EXISTS seq;
DROP TABLE IF EXISTS attribute;

CREATE TABLE attribute
(accession_code		VARCHAR(30)	NOT NULL,
 gene_id		VARCHAR(50) 	NOT NULL,
 protein_product	VARCHAR(100) 	NOT NULL,
 protein_seq		LONGTEXT	NOT NULL,
 cds			VARCHAR(500) 	NOT NULL,
 chromosomal_loc	VARCHAR(30) 	NOT NULL,

 PRIMARY KEY (accession_code)
 )ENGINE=InnoDB;

CREATE TABLE seq
(dna_seq		LONGTEXT 	NOT NULL,
 accession_code		VARCHAR(30) 	NOT NULL,
 
 PRIMARY KEY (accession_code)
)ENGINE=InnoDB;
