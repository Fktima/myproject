from re import match, split, IGNORECASE
from genbank_parser_temp import genbank_parser
import mysql.connector
import config


file = genbank_parser('chrom_CDS_21')
accession = file.parse_accession()
features = file.parse_features()
features.append(accession[0])
features = tuple(features)
print(features)
sequence = file.parse_origin()
file.close()
zipped = zip(sequence, accession)
seq_data = list(zipped)
connection = mysql.connector.connect(host=config.MyDB['host'],
                                   user=config.MyDB['user'],
                                   password=config.MyDB['password'],
                                   db=config.MyDB['dbname'])
sql = ("INSERT INTO seq(dna_seq, accession_code) VALUES (%s, %s)")
data = seq_data
sql2 = ("INSERT INTO attribute(gene_id, protein_product, protein_seq, cds, chromosomal_loc, accession_code) VALUES (%s, %s, %s, %s, %s, %s)")
data2 = []
data2.append(features)
cursor = connection.cursor()
# sql commited
cursor.executemany(sql2, data2)
connection.commit()
cursor.close()
connection.close()
