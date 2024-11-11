import pytest
import sqlite3
from app.data.database import init_db, save_dna_record, get_statistics

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

def test_init_db():
    # Verifica que init_db crea la tabla correctamente en la base de datos persistente
    init_db()
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='dna_records'")
    table = cursor.fetchone()
    conn.close()
    assert table is not None  # Verifica que la tabla fue creada

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

def test_get_statistics_empty(setup_database):
    # Verifica que get_statistics maneja correctamente el caso sin datos
    conn = setup_database
    stats = get_statistics(conn)
    assert stats == {
        "count_mutant_dna": 0,
        "count_human_dna": 0,
        "ratio": 0
    }

def test_get_statistics_with_data(setup_database):
    conn = setup_database

    # Agrega algunos registros de prueba
    save_dna_record(["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"], True, conn)
    save_dna_record(["ATGCGA", "CAGTGC", "TTCTGT", "AGAACG", "TCCGTG", "TCACTG"], False, conn)
    save_dna_record(["ATGCGA", "AAGTGC", "ATTGTG", "AGAAGG", "ACCCTA", "TCACTG"], True, conn)

    # Verifica que get_statistics calcula correctamente las estadísticas
    stats = get_statistics(conn)
    assert stats["count_mutant_dna"] == 2
    assert stats["count_human_dna"] == 1
    assert stats["ratio"] == 2 / 3  # 2 mutantes de un total de 3
