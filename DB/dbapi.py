#!/usr/bin/env python3
import sys
sys.path.insert(0, "../")

import pymysql.cursors
import config

class DBAccessLayer(object):
    ''' Use this Class to establish connection with the database and execute searching '''

    def __init__(self):
        
        self.cxn = pymysql.connect(host=config.MyDB['host'],
                                     user=config.MyDB['user'],
                                     password=config.MyDB['password'],
                                     db=config.MyDB['dbname'])
        self.cur = self.cxn.cursor()
        self.dictcur = self.cxn.cursor(pymysql.cursors.DictCursor)


    def getAllDNA(self):
        '''Retrieves all DNA sequences stored in the database '''

        dna = self.cur.execute("SELECT dna_seq from seq")
        dna = self.cur.fetchall()

        return dna
        

    def getAllaccession(self):
        ''' Retrieves the accession codes for all entries in the database '''
        
        accession = self.cur.execute("SELECT accession_code from attribute")
        accession = self.cur.fetchall()

        return accession
    

    def getAllprotein(self):
               
        ''' Retrieves all gene products stored in the database '''
        
        protein = self.cur.execute("SELECT protein_product from attribute")
        protein = self.cur.fetchall()

        return protein
    
    def getAllgene(self):
        ''' Retrieves all genes stored in the database '''

        gene = self.cur.execute("SELECT gene_id from attribute")
        gene = self.cur.fetchall()

        return gene
        

    def get_accession_code(self, query, return_cds=True, return_dna=True, return_protein=True,
                           return_attribute=True):

        ''' Retrieves all rows that match the given accession code


        Parameters:
            query (str): Accession Code

            return_cds (boolean): Default: True
            When set to "True" returns string showing the coding sequence loation.

            return_dna (boolean): Default: True
            When set to "True" returns string showing the DNA sequence.

            return_protein (boolean): Default: True
            When set to "True" returns a list giving a protein sequence for a given entry.

            return_attribute (boolean): Default: True
            When set to true return a list of accession codes and repective protein names.
        
        Return:
            gene_entry: list containing information related to the query based on which
            boolean parameters are set to "true". If boolean parameters are set to "false"
            returns an empty list.
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
        if return_attribute:
            attributes = self.cur.execute("SELECT accession_code, protein_product from attribute"
                                          "WHERE accession_code = '%s' " %(query))
            attributes = self.cur.fetchall()
            gene_entry.extend(attributes)

        return gene_entry
    
        
    def get_chromosomal_loc(self, query, return_cds=True, return_dna=True, return_protein=True,
                            return_attribute=True):

        ''' Retrieves all rows that match the given chromosomal location


        Parameters:
            query (str): Chromosomal Location

            return_cds (boolean): Default: True
            When set to "True" returns string showing the coding sequence loation.

            return_dna (boolean): Default: True
            When set to "True" returns string showing the DNA sequence.

            return_protein (boolean): Default: True
            When set to "True" returns a list giving a protein sequence for a given entry.

            return_attribute (boolean): Default: True
            When set to true return a list of accession codes and repective protein names.
        
        Return:
            gene_entry: list containing information related to the query based on which
            boolean parameters are set to "true". If boolean parameters are set to "false"
            returns an empty list.            
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
            seq = self.cur.execute("SELECT dna_seq from seq s, attribute a"
                                   "WHERE s.accession_code = a.accession_code AND chromosomal_loc = '%s' " %(query))
            seq = self.cur.fetchall()
            gene_entry.extend(seq)
        if return_attribute:
            attributes = self.cur.execute("SELECT accession_code, protein_product from attribute"
                                          "WHERE chromosomal_loc = '%s' " %(query))
            attributes = self.cur.fetchall()
            gene_entry.extend(attributes)

        return gene_entry
    

    def get_gene_id(self, query, return_cds=True, return_dna=True, return_protein=True,
                    return_attribute=True):
        ''' Retrieves all rows that match the given gene identifier


        Parameters:
            query (str): Gene Identifier

            return_cds (boolean): Default: True
            When set to "True" returns string showing the coding sequence loation.

            return_dna (boolean): Default: True
            When set to "True" returns string showing the DNA sequence.

            return_protein (boolean): Default: True
            When set to "True" returns a list giving a protein sequence for a given entry.

            return_attribute (boolean): Default: True
            When set to true return a list of accession codes and repective protein names.
        
        Return:
            gene_entry: list containing information related to the query based on which
            boolean parameters are set to "true". If boolean parameters are set to "false"
            returns an empty list.


        '''
        gene_entry = []
        
        if return_protein:
            attribute = self.cur.execute("SELECT protein_seq from attribute WHERE gene_id = '%s' " %(query))
            attribute = self.cur.fetchall()
            gene_entry.extend(attribute)
        if return_cds:
            cds = self.cur.execute("SELECT cds from seq s, attribute a"
                                   "WHERE s.accession_code = a.accession_code AND gene_id = '%s' " %(query))
            cds = self.cur.fetchall()
            gene_entry.extend(cds)
        if return_dna:
            seq = self.cur.execute("SELECT dna_seq from seq s, attribute a"
                                   "WHERE s.accession_code = a.accession_code AND gene_id = '%s' " %(query))
            seq = self.cur.fetchall()
            gene_entry.extend(seq)
        if return_attribute:
            attributes = self.cur.execute("SELECT accession_code, protein_product from attribute"
                                          "WHERE gene_id = '%s' " %(query))
            attributes = self.cur.fetchall()
            gene_entry.extend(attributes)

        return gene_entry
    

    def get_product(self, query, return_cds=True, return_dna=True, return_protein=True,
                            return_attribute=True):
        ''' Retrieves all rows that match the given protein product


        Parameters:
            query (str): Protein product.

            return_cds (boolean): Default: True
            When set to "True" returns string showing the coding sequence loation.

            return_dna (boolean): Default: True
            When set to "True" returns string showing the DNA sequence.

            return_protein (boolean): Default: True
            When set to "True" returns a list giving a protein sequence for a given entry.

            return_attribute (boolean): Default: True
            When set to true return a list of accession codes and repective protein names.
        
        Return:
            gene_entry: list containing information related to the query based on which
            boolean parameters are set to "true". If boolean parameters are set to "false"
            returns an empty list.
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
            seq = self.cur.execute("SELECT dna_seq from seq s, attribute a"
                                   "WHERE s.accession_code = a.accession_code AND protein_product = '%s' " %(query))
            seq = self.cur.fetchall()
            gene_entry.extend(seq)
        if return_attribute:
            attributes = self.cur.execute("SELECT accession_code, protein_product from attribute"
                                          "WHERE protein_product = '%s' " %(query))
            attributes = self.cur.fetchall()
            gene_entry.extend(attributes)

        return gene_entry

    def get_gene_entry(self, query):
        ''' Retrieves the gene information for a entry based on all search terms

        Parameters:
            query (str): Any of four types of identifiers used as search terms.

        Returns:
            gene_entry (list): Returns a dictionary with values for DNA sequence,
            protein sequence and coding sequence.

        '''
        sql = (" SELECT dna_seq as DNA_seq, protein_seq as amnio_acid_sequence, cds as CDS" 
              " from attribute a INNER JOIN seq ON a.accession_code = seq.accession_code "
              " WHERE a.accession_code LIKE '%s' OR protein_product LIKE '%s' OR gene_id LIKE '%s' " %(query, query, query))

        cds_list = []
        
        gene_entry = self.dictcur.execute(sql)
        gene_entry = self.dictcur.fetchall()
        
        cds = gene_entry[0]["CDS"]
        
        splitted = cds.split(',')
        for location in splitted:
            coord = location.split('..')
            coord[0] = int(coord[0])
            coord[1] = int(coord[1])
            cds_list.append(tuple(coord))
            
        gene_entry[0]["CDS"] = cds_list[0:]

        return gene_entry

    
    def __del__(self):
        self.cxn.close()


                     
