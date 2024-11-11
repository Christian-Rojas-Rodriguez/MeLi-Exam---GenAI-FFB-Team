from app.domain.mutant_logic import is_mutant

def test_is_mutant_sequence():
    # Prueba para secuencias mutantes y no mutantes
    assert is_mutant(["AAAA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]) == True
    assert is_mutant(["ATGCGA", "CAGTGC", "TTCTGT", "AGAACG", "TCCGTG", "TCACTG"]) == False
