#!usr/bin/env python3
import re
from re import match, split, IGNORECASE

class genbank_parser:
    def __init__(self, filename):
        self.openfile = open(filename, 'r')

    def get_keyword(self, keyword):
        line = ''
        while not line.startswith(keyword):
            line = self.openfile.readline().strip()
        line = line[len(keyword):].strip()
        return line

    def parse_accession(self):
        accession = self.get_keyword('ACCESSION')
                               
        return accession

    def parse_features(self):
        line = self.get_keyword('FEATURES')
        features = []

        return None
    

    def parse_origin(self):
        sequence = ''
        sequences = []
        line = self.get_keyword('ORIGIN')
        line = self.openfile.readline().strip()

        while match('^\d+.*', line):
            splitted = split('\s+', line)
            del splitted[0]
            sequence += ''.join(splitted).upper()
            line = self.openfile.readline().strip()

        sequences.append(sequence)
            
        return sequences

    def file_position(self):
        current_position = self.openfile.tell()
        return current_position

    def location_parser(self, location_string):

        return None
        

    def close(self):
        self.openfile.close()
        
        
        

