from app.domain.mutant_logic import is_mutant

def test_is_mutant_with_horizontal_sequence():
    dna_sequence = ["AAAA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
    assert is_mutant(dna_sequence) == True

def test_is_mutant_with_vertical_sequence():
    dna_sequence = ["ATGCGA", "AAGTGC", "ATTGTG", "AGAAGG", "ACCCTA", "TCACTG"]
    assert is_mutant(dna_sequence) == True

def test_is_mutant_with_diagonal_descending_sequence():
    dna_sequence = ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCATA", "TCACTG"]
    assert is_mutant(dna_sequence) == True

def test_is_mutant_with_diagonal_ascending_sequence():
    dna_sequence = ["ATGCGA", "CAGTGC", "TTATGT", "AGAACG", "TCCGTG", "TCAAAA"]
    assert is_mutant(dna_sequence) == True

def test_is_not_mutant_with_no_matching_sequences_1():
    dna_sequence = ["ATGCGA", "CAGTGC", "TTCTGT", "AGAACG", "TCCGTG", "TCACTG"]
    assert is_mutant(dna_sequence) == False

def test_is_not_mutant_with_no_matching_sequences_2():
    dna_sequence = ["AGTCGA", "CAGTGC", "TTCAGT", "AGACCG", "TCCGTG", "TCACAG"]
    assert is_mutant(dna_sequence) == False

def test_is_not_mutant_with_no_matching_sequences_3():
    dna_sequence = ["GTGCGA", "CACGTC", "TACGTA", "CGTACG", "ACGTCA", "GTACGT"]
    assert is_mutant(dna_sequence) == False

