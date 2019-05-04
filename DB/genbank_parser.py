#!usr/bin/env python3
import re
from re import match, split

class genbank_parser:
    
    def __init__(self, filename):
        self.openfile = open(filename, 'r')

    def find_keyword(self, keyword):
        line = ''
        while not line.startswith(keyword):
            line = self.read_line()

        line = line[len(keyword):].strip()

        return line

    def read_line(self):
        line = self.openfile.readline().strip()

        return line

    def parse_accession(self):
        
        accession = []
        line = self.find_keyword('ACCESSION')
        if len(line) > 8:
            line = split('s+', line)
            accession.append(line[0])
        else:
            accession.append(line)      
                               
        return accession

    def parse_features(self):
        
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
        features.append(chrom[0])

        return features

    def parse_attributes(self, line):
        
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
            dictlist.append(value)

        return dictlist
        

    def parse_origin(self):
        
        sequence = ''
        sequences = []
        line = self.find_keyword('ORIGIN')
        line = self.read_line()
        
        while match('^\d+.*', line):
            seq = split('\s+', line)
            del seq[0]
            sequence += ''.join(seq).upper()
            line = self.openfile.readline().strip()
            
        sequences.append(sequence)
            
        return sequences

    def parse_location(self, location_string):
        
        terms = match('\w*', location_string)
        terms = terms.group(0)
        location_string = location_string.strip(terms)

        return location_string

    def close(self):
        self.openfile.close()
