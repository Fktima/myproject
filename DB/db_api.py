#!/usr/bin/env python3
import sys
sys.path.insert(0, "../")

import mysql.connector
import config

class DBAccessLayer(object):
    ''' Use this module to retrieve results from the database layer '''

    def __init__(self):
        ''' Establishes connection with MySQL Database

        Return: Connection object and cursor object

        '''
        self.cxn = mysql.connector.connect(host=config.MyDB['host'],
                                     user=config.MyDB['user'],
                                     password=config.MyDB['password'],
                                     db=config.MyDB['dbname'])
        self.cur = self.cxn.cursor(dictionary=True)

    def getAllEntries(self):
        ''' Retrieves the accession codes and gene names for all entries in the database '''
        
        entries = self.cur.execute("SELECT accession_code from attribute")
        entries = self.cur.fetchall()

        return entries
        

    def get_accession_code(self, query, return_cds=True, return_dna=False, return_protein=False):

        ''' Retrieves all rows that match the given accession code


        Parameters:
            query (str): Accession Code

            return_cds (boolean): Default: True
            When set to "True" returns string showing the coding sequence loation

            return_dna (boolean): Default: False
            When set to "True" returns string showing the DNA sequence

            return_protein (boolean): Default: False
            When set to "True" returns a list giving a protein sequence for a given entry
        
        Return:
        gene_entry: list containing information related to the query based on which
        boolean parameters are set to true.

        '''
        gene_entry = []
        
        if return_protein:
            attribute = self.cur.execute("SELECT protein_seq from attribute WHERE accession_code = '%s' " %(query))
            attribute = self.cur.fetchall()
            gene_entry.extend(attribute)
        if return_cds:
            cds = self.cur.execute("SELECT cds from attribute WHERE accession_code = '%s' " %(query))
            cds = self.cur.fetchall()
            gene_entry.extend(cds)
        if return_dna:
            seq = self.cur.execute("SELECT dna_seq from seq WHERE accession_code = '%s' " %(query))
            seq = self.cur.fetchall()
            gene_entry.extend(seq)

        return gene_entry
        
    def get_chromosomal_loc(self, query, return_cds=True, return_dna=False, return_protein=False):

        ''' Retrieves all rows that match the given chromosomal location


        Parameters:
            query (str): Chromosomal Location

            return_cds (boolean): Default: True
            When set to "True" returns string showing the coding sequence loation

            return_dna (boolean): Default: False
            When set to "True" returns string showing the DNA sequence

            return_protein (boolean): Default: False
            When set to "True" returns a list giving a protein sequence for a given entry
        
        Return:
        gene_entry: list containing information related to the query based on which
        boolean parameters are set to true.

        '''
        gene_entry = []
        
        if return_protein:
            attribute = self.cur.execute("SELECT protein_seq from attribute WHERE chromosomal_loc = '%s' " %(query))
            attribute = self.cur.fetchall()
            gene_entry.extend(attribute)
        if return_cds:
            cds = self.cur.execute("SELECT cds from attribute WHERE chromosomal_loc = '%s' " %(query))
            cds = self.cur.fetchall()
            gene_entry.extend(cds)
        if return_dna:
            seq = self.cur.execute("SELECT dna_seq from seq s, attribute a WHERE s.accession_code = a.accession_code AND chromosomal_loc = '%s' " %(query))
            seq = self.cur.fetchall()
            gene_entry.extend(seq)

        return gene_entry

    def get_gene_id(self, query, return_cds=True, return_dna=False, return_protein=False):
        ''' Retrieves all rows that match the given gene identifier


        Parameters:
            query (str): Gene Identifier

            return_cds (boolean): Default: True
            When set to "True" returns string showing the coding sequence loation

            return_dna (boolean): Default: False
            When set to "True" returns string showing the DNA sequence

            return_protein (boolean): Default: False
            When set to "True" returns a list giving a protein sequence for a given entry
        
        Return:
        gene_entry: list containing information related to the query based on which
        boolean parameters are set to true.


        '''
        gene_entry = []
        
        if return_protein:
            attribute = self.cur.execute("SELECT protein_seq from attribute WHERE gene_id = '%s' " %(query))
            attribute = self.cur.fetchall()
            gene_entry.extend(attribute)
        if return_cds:
            cds = self.cur.execute("SELECT cds from seq s, attribute a WHERE s.accession_code = a.accession_code AND gene_id = '%s' " %(query))
            cds = self.cur.fetchall()
            gene_entry.extend(cds)
        if return_dna:
            seq = self.cur.execute("SELECT dna_seq from seq s, attribute a WHERE s.accession_code = a.accession_code AND gene_id = '%s' " %(query))
            seq = self.cur.fetchall()
            gene_entry.extend(seq)

        return gene_entry

    def get_protein_product(self, query, return_cds=True, return_dna=False, return_protein=False):
        ''' Retrieves all rows that match the given protein product


        Parameters:
            query (str): Protein product

            return_cds (boolean): Default: True
            When set to "True" returns string showing the coding sequence loation

            return_dna (boolean): Default: False
            When set to "True" returns string showing the DNA sequence

            return_protein (boolean): Default: False
            When set to "True" returns a list giving a protein sequence for a given entry
        
        Return:
        gene_entry: list containing information related to the query based on which
        boolean parameters are set to true.


        '''
        gene_entry = []
        
        if return_protein:
            attribute = self.cur.execute("SELECT protein_seq from attribute WHERE protein_product = '%s' " %(query))
            attribute = self.cur.fetchall()
            gene_entry.extend(attribute)
        if return_cds:
            cds = self.cur.execute("SELECT cds from attribute WHERE protein_product = '%s' " %(query))
            cds = self.cur.fetchall()
            gene_entry.extend(cds)
        if return_dna:
            seq = self.cur.execute("SELECT dna_seq from seq s, attribute a WHERE s.accession_code = a.accession_code AND protein_product = '%s' " %(query))
            seq = self.cur.fetchall()
            gene_entry.extend(seq)

        return gene_entry
    
    def __del__(self):
        self.cxn.close()
