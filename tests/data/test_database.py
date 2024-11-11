import pytest
import sqlite3
from app.data.database import save_dna_record

@pytest.fixture
def setup_database():
    # Configura una base de datos en memoria para pruebas
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE dna_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sequence TEXT NOT NULL,
            is_mutant BOOLEAN NOT NULL
        )
    ''')
    conn.commit()
    yield conn  # Proporciona la conexión para las pruebas
    conn.close()  # Cierra la conexión después de las pruebas

def test_init_db(setup_database):
    # No debería fallar al crear la base de datos
    assert setup_database is not None

def test_save_dna_record(setup_database):
    conn = setup_database
    dna_sequence = ["ATGCGA", "CAGTGC", "TTCTGT", "AGAACG", "TCCGTG", "TCACTG"]
    save_dna_record(dna_sequence, True, conn)  # Pasa la conexión de prueba

    # Verifica que el registro fue guardado en la conexión de prueba
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM dna_records')
    records = cursor.fetchall()
    assert len(records) == 1
    assert records[0][1] == ",".join(dna_sequence)
    assert records[0][2] == True

