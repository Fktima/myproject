#!usr/bin/env python3
import re
from re import match, split, IGNORECASE

class genbank_parser:
    def __init__(self, filename):
        self.openfile = open(filename, 'r')

    def parse_origin(self):
        sequence = ''
        file = self.openfile.readline()
        for line in file:
            if 'ORIGIN' in line:
                while match('^\d+.*'):
                    splitted = split('\s+', line)
                    del splitted[0]
                    sequence += ''.join(splitted).upper()
                    break
                    
        return sequence


    def parse_accession(self):
        accession = []
        pattern = re.compile('ACCESSION')
        file = self.openfile.readline()
        for line in file:
            if pattern.match(line):
                accession += line.strip

        return accession


        
        

