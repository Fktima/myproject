USE test
DROP TABLE IF EXISTS location;
DROP TABLE IF EXISTS seq;
DROP TABLE IF EXISTS qualifiers;

CREATE TABLE qualifiers
(accession_code		VARCHAR(10)	NOT NULL,
 gene_id			VARCHAR(10) NOT NULL,
 protein_product	VARCHAR(20) NOT NULL,
 codon_start		INTEGER		NOT NULL,
 chromosomal_loc	VARCHAR(10) NOT NULL,

 PRIMARY KEY(accession_code)
)ENGINE=InnoDB;

CREATE TABLE seq
(dna_seq			MEDIUMTEXT 	NOT NULL,
 ptotein_seq		MEDIUMTEXT	NOT NULL,
 accession_code		VARCHAR(10) NOT NULL,
 
 PRIMARY KEY(accession_code)
)ENGINE=InnoDB;

CREATE TABLE location
(gene				VARCHAR(30) NOT NULL,
 cds				VARCHAR(30)	NOT NULL,
 chromosomoal_loc	VARCHAR(30) NOT NULL,
 
 PRIMARY KEY(cds)
)ENGINE=InnoDB;

INSERT INTO qualifiers VALUES
	('AB001517', 'TMEM1', 'TMEM1 protein', 3, '21q22.3'); 
INSERT INTO seq VALUES
	('ATCG', 'MEVGE', 'AB001517');
INSERT INTO location VALUES
	('<1823..5594', '<join 1823..2017, 2338..2576', '1..43051');
