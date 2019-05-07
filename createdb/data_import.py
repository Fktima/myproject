import sys
sys.path.insert(0, "../")

import pymysql.cursors
import config

from re import search
from genbank_parser import genbank_parser

def populate(data):
    ''' Populates the database with given data list.

    Parameters
        data(list):
        list of tuples containing the data to be inserted.

    '''
    try:
        connection = pymysql.connect(host=config.MyDB['host'],
                                     user=config.MyDB['user'],
                                     password=config.MyDB['password'],
                                     db=config.MyDB['dbname'])
        cursor = connection.cursor()

        sql = ("INSERT INTO seq(dna_seq, accession_code) VALUES (%s, %s)")
        sql2 = ("INSERT INTO attribute(accession_code, gene_id, protein_product, protein_seq, cds, chromosomal_loc) VALUES (%s, %s, %s, %s, %s, %s)")

        if len(data[0]) == 2:
            cursor.executemany(sql, data)
            print("Data to be inserted to table seq")
        else:
            cursor.executemany(sql2, data)
            print("Data to be inserted to table attribute")
        connection.commit()
        print("Records inserted successfully into database")
    except pymysql.Error as error:
        connection.rollback()
        print("Failed to insert into MySQL table {}".format(error))
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("MySQL connection closed")


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

zipped = zip(sequence, accession)
seq_data = list(zipped)

populate(seq_data)
populate(features)
