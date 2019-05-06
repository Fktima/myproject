#!usr/bin/env python3
import re
from re import match, split

class genbank_parser:
    ''' Use this class to parse the genbank file.

    Parsing the genbank file follows the order of:
        1) Accession - 6-8 character string containing the
        accession code
        2) Features - series of strings following the Features
        header within the genbank file. Those of importance
        are the "source" and "CDS".
        3) Origin - string of letters which refer to the DNA
        sequence.

    Iteration of the entire file is only possible by looping
    each of these in this same order.

    '''
        
    
    def __init__(self, filename):
        ''' Creates a new file parser

        Parameters:
            filename - string
            name of the file pointing to the file to be parsed

        Returns:
            file object
        '''
        self.openfile = open(filename, 'r')

    def find_keyword(self, keyword):
        ''' Places file pointer towards the header of interest
        given the order of headers is the same throughout the file.

        Parameters:
            keyword - string that a line should start with
            to be considered a header.
        Returns:
            line - return the read sting stripped of trailing
            whitespace.
        '''
        line = ''
        while not line.startswith(keyword):
            line = self.read_line()

        line = line[len(keyword):].strip()

        return line

    def read_line(self):
        ''' Reads a single line removing trailing whitespace
        This is neccessary for simplifying the searching of
        keyword string.
        '''
        
        line = self.openfile.readline().strip()

        return line

    def check_eof(self):
        ''' Identifies when the end of file has been reached
        Return:
            True - if the next line read after '//' is
            the string added to the end of the file
            aptly called 'eof'.
            False - if next line read does not start with 'eof'
        '''
        line = self.read_line()
        if line.startswith ('//'):
            line = self.read_line()
            if line.startswith('eof'):
                return True
            else:
                return False

    def parse_accession(self):
        # string or list?
        ''' Parses the ACCESSION code

        Returns
            accession (string):
            returns accession code as a string and if two
            accession codes are given, returns the first
        '''
        
        accession = ''
        line = self.find_keyword('ACCESSION')
        if len(line) > 8:
            line = split('s+', line)
            accession = line[0]
        else:
            accession = line
                               
        return accession

    def parse_features(self):
        ''' Parses FEATURES described in the docsting of this class.

        Return:
        features (list):
        list containing the gene ID, protein product,
        protein sequence, coding sequence, and chromosome
        location.

        '''
        
        line = self.find_keyword('FEATURES')
        
        while not line.startswith('/'):
            line = self.read_line()
        chrom = self.parse_attributes(line)
        line = self.find_keyword('CDS')
        location = line.strip()
        line = self.read_line()
        
        while not line.startswith('/'):
            location += line
            line = self.read_line()
            
        location = self.parse_location(location)
        features = self.parse_attributes(line)
        features.append(location)
        features.extend(chrom)

        return features

    def parse_attributes(self, line):
        ''' Parses values of features described in the docstring
        of this class.

        Return:
        dictlist (list):
        list containing the gene ID, protein product,
        protein sequence, coding sequence, and chromosome
        location.

        '''
        
        attributes = {}
        dictlist = []
        
        while line.startswith('/'):
            if match('^/gene|^/prod|^/trans|^/map', line):
                key = ''
                for char in line:
                    if char == '=':
                        break
                    key += char
                value = line[len(key) + 1:]

                if value[0:1] == '"':
                    remaining = value[1:]
                    while remaining[-1] != '"':
                        remaining += self.openfile.readline().strip()
                        value = remaining[:-1]
                    
                attributes[key] = value
                line = self.openfile.readline().strip()
            else:
                line = self.openfile.readline().strip()
                
        for key, value in dict.items(attributes):
            dictlist.append(value.strip('"'))

        return dictlist
        

    def parse_origin(self):
        ''' Parses ORIGIN described in the docstring of this class.

        Return:
        sequence (string):
        string containing sequence.

        '''
        
        sequence = ''
        line = self.find_keyword('ORIGIN')
        line = self.read_line()
        
        while match('^\d+.*', line):
            seq = split('\s+', line)
            del seq[0]
            sequence += ''.join(seq).upper()
            last_position = self.openfile.tell()
            line = self.openfile.readline().strip()
        self.openfile.seek(last_position)    
        return sequence

    def parse_location(self, location_string):
        ''' Formats location strings in the format:

        x..y - representative of a joined location

        Return:
        location_string (string):
        string representing the location of respective feature
        '''
        
        terms = match('\w*', location_string)
        terms = terms.group(0)
        location_string = location_string.strip(terms)
        for char in location_string:
            if char == '(':
                location_string = location_string.strip(char)
            elif char == ')':
                location_string = location_string.strip(char)
            elif char == '<':
                location_string = location_string.strip(char)
            elif char == '>':
                location_string = location_string.strip(char)                

        return location_string
    
    def close(self):
        ''' closes the file object '''
        self.openfile.close()



