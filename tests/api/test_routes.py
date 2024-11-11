import json
import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    return app.test_client()

def test_mutant_check_mutant(client):
    response = client.post('/mutant', data=json.dumps({
        "dna": ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
    }), content_type='application/json')

    assert response.status_code == 200
    assert response.get_json() == {"message": "Mutant detected"}

def test_mutant_check_non_mutant(client):
    response = client.post('/mutant', data=json.dumps({
        "dna": ["ATGCGA", "CAGTGC", "TTCTGT", "AGAACG", "TCCGTG", "TCACTG"]

    }), content_type='application/json')

    # Debería devolver 403 si no es mutante
    assert response.status_code == 403
    assert response.get_json() == {"message": "Not a mutant"}

def test_stats(client):
    response = client.get('/stats')
    assert response.status_code == 200
    data = response.get_json()

    assert "count_mutant_dna" in data
    assert "count_human_dna" in data
    assert "ratio" in data
