from app.services.mutant_service import check_mutant

def test_check_mutant():
    dna_mutant = ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
    assert check_mutant(dna_mutant) is True  # Debería ser mutante

    dna_non_mutant = ["ATGCGA", "CAGTGC", "TTCTGT", "AGAACG", "TCCGTG", "TCACTG"]
    assert check_mutant(dna_non_mutant) is False  # No debería ser mutante
