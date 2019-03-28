USE test
DROP TABLE IF EXISTS genbank;
CREATE TABLE genbank
(accession_code 	VARCHAR(8)	NOT NULL,
 chromosomal_loc	VARCHAR(10)	NOT NULL,
 genBank_id			VARCHAR(10)	NOT NULL,
 protein_product	VARCHAR(15)	NOT NULL,
 cds				VARCHAR(30)	NOT NULL,
 dna_seq			MEDIUMTEXT	NOT NULL,
 protein_seq		MEDIUMTEXT	NOT NULL,
 
 PRIMARY KEY (accession_code)
)ENGINE=InnoDB;

INSERT INTO genbank VALUES
	('AB001517', '21q22.3', 'TMEM1', 'BAA21136.1', '1823..2017,2338..2576', 'ATCG', 'MEVGE');