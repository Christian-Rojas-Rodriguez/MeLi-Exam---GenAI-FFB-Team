import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dna_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sequence TEXT NOT NULL,
            is_mutant BOOLEAN NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


def save_dna_record(dna_sequence, is_mutant, conn=None):
    if conn is None:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO dna_records (sequence, is_mutant) VALUES (?, ?)',
                       (','.join(dna_sequence), is_mutant))
        conn.commit()
        conn.close()
    else:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO dna_records (sequence, is_mutant) VALUES (?, ?)',
                       (','.join(dna_sequence), is_mutant))
        conn.commit()


def get_statistics(conn=None):
    if conn is None:
        conn = get_db_connection()
    cursor = conn.cursor()
    total_count = cursor.execute('SELECT COUNT(*) FROM dna_records').fetchone()[0]
    mutant_count = cursor.execute('SELECT COUNT(*) FROM dna_records WHERE is_mutant = 1').fetchone()[0]

    if conn != get_db_connection():
        conn.close()

    return {
        "count_mutant_dna": mutant_count,
        "count_human_dna": total_count - mutant_count,
        "ratio": mutant_count / total_count if total_count > 0 else 0
    }
