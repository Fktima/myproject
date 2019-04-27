#!/usr/bin/env python3
import mysql.connector
import config
''' Use this module to retrieve results from the database layer '''
class DatabaseLayer(object):

    def __init__(self):
        self.cxn = mysql.connector.connect(host=config.MyDB['host'],
                                     user=config.MyDB['user'],
                                     password=config.MyDB['password'],
                                     db=config.MyDB['dbname'])
        self.cur = self.cxn.cursor(dictionary=True)

    def get_accession_code(self, query, return_cds=True, return_dna=True, return_attribute=True):

        ''' Retrieves all rows that match the given accession code


        Parameters:
            query (str): Accession Code

            return_cds (boolean): Default: True
            When set to "True" returns string showing the coding sequence loation

            return_dna (boolean): Default: True
            When set to "True" returns string showing the DNA sequence

            return_attributes (boolean): Default: True
            When set to "True" returns a list giving attributes for the a
            coding sequence
        
        Return:
        gene_entry: list containing information related to the query based on which
        boolean parameters are set to true.

        '''
        gene_entry = []
        
        if return_attribute:
            attribute = self.cur.execute("SELECT * from attributes WHERE accession_code = '%s' " %(query))
            attribute = self.cur.fetchall()
            gene_entry.append(attribute)
        if return_cds:
            cds = self.cur.execute("SELECT cds from seq WHERE accession_code = '%s' " %(query))
            cds = self.cur.fetchall()
            gene_entry.append(cds)
        if return_seq:
            seq = self.cur.execute("SELECT dna_seq from seq WHERE accession_code = '%s' " %(query))
            seq = self.cur.fetchall()
            gene_entry.append(seq)

        return gene_entry
        
    def get_chromosomal_loc(self, query, return_cds=True, return_dna=True, return_attribute=True):

        ''' Retrieves all rows that match the given chromosomal location


        Parameters:
            query (str): Chromosomal Location

            return_cds (boolean): Default: True
            When set to "True" returns string showing the coding sequence loation

            return_dna (boolean): Default: True
            When set to "True" returns string showing the DNA sequence

            return_attributes (boolean): Default: True
            When set to "True" returns a list giving attributes for the a
            coding sequence
        
        Return:
        gene_entry: list containing information related to the query based on which
        boolean parameters are set to true.

        '''
        gene_entry = []
        
        if return_attribute:
            attribute = self.cur.execute("SELECT * from attributes WHERE chromosomal_loc = '%s' " %(query))
            attribute = self.cur.fetchall()
            gene_entry.append(attribute)
        if return_cds:
            cds = self.cur.execute("SELECT cds from seq s, atribute a WHERE s.accession_code = a.accession_code AND chromosomal_loc = '%s' " %(query))
            cds = self.cur.fetchall()
            gene_entry.append(cds)
        if return_seq:
            seq = self.cur.execute("SELECT dna_seq from seq s, atribute a WHERE s.accession_code = a.accession_code AND chromosomal_loc = '%s' " %(query))
            seq = self.cur.fetchall()
            gene_entry.append(seq)

        return gene_entry

    def get_gene_id(self, query, return_cds=True, return_dna=True, return_attribute=True):
        ''' Retrieves all rows that match the given gene identifier


        Parameters:
            query (str): Gene Identifier

            return_cds (boolean): Default: True
            When set to "True" returns string showing the coding sequence loation

            return_dna (boolean): Default: True
            When set to "True" returns string showing the DNA sequence

            return_attributes (boolean): Default: True
            When set to "True" returns a list giving attributes for the a
            coding sequence
        
        Return:
        gene_entry: list containing information related to the query based on which
        boolean parameters are set to true.


        '''
        gene_entry = []
        
        if return_attribute:
            attribute = self.cur.execute("SELECT * from attributes WHERE gene_id = '%s' " %(query))
            attribute = self.cur.fetchall()
            gene_entry.append(attribute)
        if return_cds:
            cds = self.cur.execute("SELECT cds from seq s, atribute a WHERE s.accession_code = a.accession_code AND gene_id = '%s' " %(query))
            cds = self.cur.fetchall()
            gene_entry.append(cds)
        if return_seq:
            seq = self.cur.execute("SELECT dna_seq from seq s, atribute a WHERE s.accession_code = a.accession_code AND gene_id = '%s' " %(query))
            seq = self.cur.fetchall()
            gene_entry.append(seq)

        return gene_entry

    def get_protein_product(self, query, return_cds=True, return_dna=True, return_attribute=True):
        ''' Retrieves all rows that match the given protein product


        Parameters:
            query (str): Protein product

            return_cds (boolean): Default: True
            When set to "True" returns string showing the coding sequence loation

            return_dna (boolean): Default: True
            When set to "True" returns string showing the DNA sequence

            return_attributes (boolean): Default: True
            When set to "True" returns a list giving attributes for the a
            coding sequence
        
        Return:
        gene_entry: list containing information related to the query based on which
        boolean parameters are set to true.


        '''
        gene_entry = []
        
        if return_attribute:
            attribute = self.cur.execute("SELECT * from attributes WHERE protein_product = '%s' " %(query))
            attribute = self.cur.fetchall()
            gene_entry.append(attribute)
        if return_cds:
            cds = self.cur.execute("SELECT cds from seq s, atribute a WHERE s.accession_code = a.accession_code AND protein_product = '%s' " %(query))
            cds = self.cur.fetchall()
            gene_entry.append(cds)
        if return_seq:
            seq = self.cur.execute("SELECT dna_seq from seq s, atribute a WHERE s.accession_code = a.accession_code AND protein_product = '%s' " %(query))
            seq = self.cur.fetchall()
            gene_entry.append(seq)

        return gene_entry
    
    def __del__(self):
        self.cxn.close()
