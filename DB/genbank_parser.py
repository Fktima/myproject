#!usr/bin/env python3
from re import match, split, IGNORECASE

class genbank_parser:
    def __init__(self):
        self.openfile = open(filename, 'r') as file
        self.line = file.readline()

    def parse_origin(self, line):
        sequence = []
        pattern = re.compile('^\d+.*')
        while pattern.match(line)
        sequence += line.split('/s+')

        return sequence
        
        

