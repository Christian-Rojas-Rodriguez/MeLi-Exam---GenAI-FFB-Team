def is_mutant(dna):
    n = len(dna)

    for i in range(n):
        for j in range(n):
            if j + 3 < n:
                if dna[i][j] == dna[i][j + 1] == dna[i][j + 2] == dna[i][j + 3]:
                    return True
            if i + 3 < n:
                if dna[i][j] == dna[i + 1][j] == dna[i + 2][j] == dna[i + 3][j]:
                    return True
            if i + 3 < n and j + 3 < n:
                if dna[i][j] == dna[i + 1][j + 1] == dna[i + 2][j + 2] == dna[i + 3][j + 3]:
                    return True
            if i - 3 >= 0 and j + 3 < n:
                if dna[i][j] == dna[i - 1][j + 1] == dna[i - 2][j + 2] == dna[i - 3][j + 3]:
                    return True

    return False
