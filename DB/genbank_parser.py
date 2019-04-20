#!usr/bin/env python3
import re
from re import match, split, IGNORECASE

class genbank_parser:
    def __init__(self, filename):
        self.openfile = open(filename, 'r')

    def parse_origin(self):
        line = ''
        line_origin = ''
        sequence = ''

        while not line.startswith('ORIGIN'):
            line = self.openfile.readline().strip()
    
        line_origin = self.openfile.readline().strip()
        while match('^\d+.*', line_origin):
            splitted = split('\s+', line_origin)
            del splitted[0]
            sequence += ''.join(splitted).upper()
            line_origin = self.openfile.readline().strip()
                        
        return sequence

    def parse_accession(self):
        line = ''
        while not line.startswith('ACCESSION'):
            line = self.openfile.readline().strip()
            
        return line

    


    def close(self):
        self.openfile.close()
        
        

