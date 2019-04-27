USE test
DROP TABLE IF EXISTS seq;
DROP TABLE IF EXISTS attribute;

CREATE TABLE attribute
(accession_code		VARCHAR(30)	NOT NULL,
 gene_id			VARCHAR(10) NULL,
 protein_product	VARCHAR(20) NULL,
 chromosomal_loc	VARCHAR(10) NULL,

 PRIMARY KEY(accession_code)
 FOREIGN KEY(accession_code)
)ENGINE=InnoDB;

CREATE TABLE seq
(dna_seq			MEDIUMTEXT 	NULL,
 protein_seq		MEDIUMTEXT	NULL,
 cds				VARCHAR(30)	NOT NULL,
 accession_code		VARCHAR(30) NOT NULL,
 
 PRIMARY KEY(accession_code)
)ENGINE=InnoDB