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
        self.cur = self.cxn.cursor()

    def get_accession_code(self, query):
        ''' Retrieves all rows that match the given accession code


        Parameters:
        query (str): GenBank accession code


        Returns:
        gene_entry: Returning dictionary of results


        '''

        gene_entry = self.cur.execute("SELECT * from genbank WHERE accession_code = '%s' " %(query))
        gene_entry = self.cur.fetchall()
        return gene_entry

    def get_chromosomal_loc(self, query):
        ''' Retrieves all rows that match the given chromosomal location


        Parameters:
        query (str): Chromosmal location


        Returns:
        gene_entry: Returning dictionary of results


        '''

        gene_entry = self.cur.execute("SELECT * from genbank WHERE chromosomal_loc = '%s' " %(query))
        gene_entry = self.cur.fetchall()
        return gene_entry

    def get_gene_id(self, query):
        ''' Retrieves all rows that match the given gene identifier


        Parameters:
        query (str): Gene identifier


        Returns:
        gene_entry: Returning dictionary of results


        '''

        gene_entry = self.cur.execute("SELECT * from genbank WHERE genBank_id = '%s' " %(query))
        gene_entry = self.cur.fetchall()
        return gene_entry

    def get_protein_product(self, query):
        ''' Retrieves all rows that match the given protein product


        Parameters:
        query (str): protein product


        Returns:
        gene_entry: Returning dictionary of results


        '''

        gene_entry = self.cur.execute("SELECT * from genbank WHERE protein_product = '%s' " %(query))
        gene_entry = self.cur.fetchall()
        return gene_entry
    
    def __del__(self):
        self.cxn.close()
