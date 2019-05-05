import dummy as dummy
import BL_API as bl_api
import pytest


def test_dna_seq():
    assert bl_api.Entry.get_dna_seq('678') =='TGAATTCATATGGAATTCTGCAATTATATTCA'

def test_aa_seq():
    assert bl_api.Entry.get_aminoacid_seq('678') == 'IHMEFCNYI'

def test_cds_coord():
    assert bl_api.Entry.get_CDS_coord('678') == [5, 16]

def test_coding_sequence():
    assert bl_api.Entry.get_coding_seq('678') == 'TTCATATGGAAT'

def test_codon_frequency():
    assert bl_api.Entry.get_codon_frequency('678')== {'TGA': 10.0, 'ATT': 20.0, 'CAT': 10.0, 'ATG': 10.0, 'GAA': 10.0, 'TTC': 10.0, 'TGC': 10.0, 'AAT': 10.0, 'TAT': 10.0}

def test_dna_to_protein():
    assert bl_api.DNA_to_protein('678')== 'IHMEFCNYI'

def test_check_alignment():
    assert bl_api.check_alignment('678') == True

def test_non_coding_dna():
    assert bl_api.non_coding_dna_seq('678') == "TGAA TTCTGCAATTATATTC"

def test_find_restriction_sites():
    assert bl_api.find_restriction_sites('678') == {'ecorI': [], 'BamHI': [], 'BsuMI': []}

def test_which_enzyme_cuts():
    assert bl_api.check_which_enzyme_cuts('678') == {'ecorI': False, 'BamHI': False, 'BsuMI': False}
