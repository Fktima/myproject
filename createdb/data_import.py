import sys
sys.path.insert(0, "../")

import pymysql.cursors
import config

from re import search
from genbank_parser import genbank_parser

file = genbank_parser('chrom_CDS_21')
continue_parsing = True
accession = []
features = []
sequence = []
while continue_parsing:
    accession.append(file.parse_accession())
    features.append(file.parse_features())
    features[-1].insert(0, accession[-1])
    features[-1] = tuple(features[-1])
    sequence.append(file.parse_origin())
    if len(features[-1]) < 6 or search('[A-Z]',((features[-1][-2]))):
        del accession[-1]
        del features[-1]
        del sequence[-1]
    end_of_file = file.check_eof()

    if end_of_file:
        continue_parsing = False
    elif not end_of_file:
        continue

file.close()
print(len(features))
print(len(sequence))
print(len(accession))

zipped = zip(sequence, accession)
seq_data = list(zipped)

connection = pymysql.connect(host=config.MyDB['host'],
                                   user=config.MyDB['user'],
                                   password=config.MyDB['password'],
                                   db=config.MyDB['dbname'])
sql = ("INSERT INTO seq(dna_seq, accession_code) VALUES (%s, %s)")
data = seq_data
sql2 = ("INSERT INTO attribute(accession_code, gene_id, protein_product, protein_seq, cds, chromosomal_loc) VALUES (%s, %s, %s, %s, %s, %s)")
data2 = features
cursor = connection.cursor()
cursor.executemany(sql, data)
cursor.executemany(sql2, data2)
connection.commit()
cursor.close()
connection.close()
