from app.domain.mutant_logic import is_mutant

def test_is_mutant_sequence():
    # Secuencia mutante horizontal
    assert is_mutant(["AAAA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]) == True

    # Secuencia mutante vertical
    assert is_mutant(["ATGCGA", "AAGTGC", "ATTGTG", "AGAAGG", "ACCCTA", "TCACTG"]) == True

    # Secuencia mutante en diagonal descendente (hacia abajo-derecha)
    assert is_mutant(["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCATA", "TCACTG"]) == True

    # Secuencia mutante en diagonal ascendente (hacia arriba-derecha)
    assert is_mutant(["ATGCGA", "CAGTGC", "TTATGT", "AGAACG", "TCCGTG", "TCAAAA"]) == True

    # Caso sin secuencias mutantes (falso negativo)
    assert is_mutant(["ATGCGA", "CAGTGC", "TTCTGT", "AGAACG", "TCCGTG", "TCACTG"]) == False

    # Caso sin secuencias mutantes (falso negativo) con estructura diferente
    assert is_mutant(["AGTCGA", "CAGTGC", "TTCAGT", "AGACCG", "TCCGTG", "TCACAG"]) == False

    # Caso completamente diferente para asegurar que recorre toda la matriz y retorna False
    assert is_mutant(["GTGCGA", "CACGTC", "TACGTA", "CGTACG", "ACGTCA", "GTACGT"]) == False
