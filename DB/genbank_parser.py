#!usr/bin/env python3
import re
from re import match, split, IGNORECASE

class genbank_parser:
    def __init__(self, filename):
        self.openfile = open(filename, 'r')

    def parse_accession(self):
        keyword = 'ACCESSION'
        accession = []
        for line in self.openfile:
            if line.startswith(keyword):
                line = line[len(keyword):].strip()
                accession.append(line)      
                               
        return accession

    def parse_features(self):
        keyword = 'FEATURES'
        features = []
        file_position = self.openfile.seek(0)       
        for line in self.openfile:
            if line.startswith(keyword):
                while not line.startswith('CDS'):
                    line = self.openfile.readline().strip()
                name, location = split('\s+', line.strip())
                line = self.openfile.readline().strip()
                while not line.startswith('/'):
                    location += line
                    line = self.openfile.readline().strip()
                location = self.parse_location(location)
                features.append(location)
                features.append(self.parse_attributes(line))

        return features

    def parse_attributes(self, line):
        attributes = {}
        while line.startswith('^/.*'):
            if re.search('t', line):
                key = ''
                for char in line:
                    if char == '=':
                        break
                    key += char
                value = line[len(key) + 1:]
                attributes[key] = value
                line = self.openfile.readline().strip()
            else:
                line = self.openfile.readline().strip()
            if not attributes:
                raise ValueError('no attributes found')
            
        return attributes
        

    def parse_origin(self):
        sequence = ''
        sequences = []
        keyword = 'ORIGIN'
        file_position = self.openfile.seek(0)
        for line in self.openfile:
            if line.startswith(keyword):
                line = self.openfile.readline().strip()
                while match('^\d+.*', line):
                    splitted = split('\s+', line)
                    del splitted[0]
                    sequence += ''.join(splitted).upper()
                    line = self.openfile.readline().strip()
                sequences.append(sequence)
            
        return sequences

    def parse_location(self, location_string):
        terms = re.match('\w*', location_string)
        terms = terms.group(0)
        location_string = location_string.strip(terms)

        return location_string
        

    def close(self):
        self.openfile.close()
