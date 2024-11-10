import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def save_dna_record(dna, is_mutant):
    conn = get_db_connection()
    conn.execute('INSERT INTO dna_records (sequence, is_mutant) VALUES (?, ?)',
                 (",".join(dna), int(is_mutant)))
    conn.commit()
    conn.close()

def get_statistics():
    conn = get_db_connection()
    cursor = conn.cursor()
    total_count = cursor.execute('SELECT COUNT(*) FROM dna_records').fetchone()[0]
    mutant_count = cursor.execute('SELECT COUNT(*) FROM dna_records WHERE is_mutant = 1').fetchone()[0]
    conn.close()
    return {
        "count_mutant_dna": mutant_count,
        "count_human_dna": total_count - mutant_count,
        "ratio": mutant_count / total_count if total_count > 0 else 0
    }