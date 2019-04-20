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
        return line

    def parse_accession(self):
        accession = self.get_keyword('ACCESSION')
                               
        return accession

    def parse_features(self):
        line = self.get_keyword('FEATURES')
            
        features = []
        line = self.openfile.readline()
        while not 'CDS' in line:
            line = self.openfile.readline()
        else:
            name, location = split('\s+', line.strip())
            features.append(name)

        return features

    def parse_origin(self):
        sequence = ''
        line = self.get_keyword('ORIGIN')
        line = self.openfile.readline().strip()

        while match('^\d+.*', line):
            splitted = split('\s+', line)
            del splitted[0]
            sequence += ''.join(splitted).upper()
            line = self.openfile.readline().strip()
                        
        return sequence

    
    def close(self):
        self.openfile.close()
        
        
        

