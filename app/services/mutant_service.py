from app.domain.mutant_logic import is_mutant
from app.data.database import save_dna_record, get_statistics

def check_mutant(dna):
    result = is_mutant(dna)
    save_dna_record(dna, result)
    return result

def get_stats():
    return get_statistics()
