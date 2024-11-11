# MeLi Exam-GenAI FFB Team

Magneto wants to recruit as many mutants as possible to fight against the X-Men. To help with this, he has hired you to develop a project that detects if a human is a mutant based on their DNA sequence.

The objective is to create a program with a function called `isMutant` that determines whether a given DNA sequence belongs to a mutant. A human DNA sequence will be represented by an NxN matrix, where each row in the matrix is a string containing one of four nitrogenous bases (A, T, C, G).

## Conditions for Mutation
You will know if a human is a mutant if you find **more than one sequence of four identical letters (A, T, C, G)** in any of the following directions:
- Horizontally
- Vertically
- Diagonally (from top-left to bottom-right or from bottom-left to top-right)

## Example
Given the following DNA matrix:

### Non-Mutant Example:

| A | T | G | C | G | A |
|---|---|---|---|---|---|
| C | A | G | T | G | C |
| T | T | A | T | T | T |
| A | G | A | A | G | G |
| C | C | C | C | T | A |
| T | C | A | C | T | G |

### Mutant Example:

| **A** | T | G | C | **G** | A |
|---|---|---|---|---|---|
| C | **A** | G | T | **G** | G |
| T | T | **A** | T | **G** | T |
| A | G | A | **A** | **G** | G |
| **C** | **C** | **C** | **C** | T | A |
| T | C | A | C | T | G |

In the mutant example, there are multiple sequences of four identical letters in a row: horizontally and vertically, confirming a mutation.

## Solution Requirements

1. **Level 1:** Create a program that detects if a DNA sequence is mutant according to the conditions given.
2. **Level 2:** Implement the program as a REST API. Host this API on a cloud service (e.g., Render, Google App Engine, AWS) and create an endpoint `/mutant` that accepts a JSON object with a DNA sequence array in the following format:
   ``` JSON
   {
    "dna": ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
   }
- The endpoint should return HTTP 200 if the DNA is mutant, and HTTP 403 if it is not.
3. **Level 3:** Add a database to store all verified DNA sequences, with only one record per sequence. Create an additional `/stats` endpoint that returns the total number of human and mutant DNA sequences, as well as the ratio of mutants to humans. Example response:
   ``` JSON
   {
    "count_mutant_dna": 40,
    "count_human_dna": 100,
    "ratio": 0.4
   }
## Additional Requirements
- Automated tests with code coverage over 80%.
- Include setup instructions and API usage in the README.



# Mutant Detection API
This is a Flask-based API to detect if a given DNA sequence belongs to a mutant. The project is designed for local development and testing, and it's deployed on Render for production.

## Prerequisites
- Python 3.12
- Virtualenv or similar environment manager
- Docker Client (optional, for database setup)
- Render account for deployment (or you can use another service)

## Setup

### Clone the repository:
    git clone https://github.com/Christian-Rojas-Rodriguez/MeLi-Exam---GenAI-FFB-Team.git
    cd <repository-folder>
### Set up a virtual environment:
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
### Install dependencies:
    pip install -r requirements.txt
### Set up a virtual environment:
- Create a .env file in the root of the project with the following content:
  
      DATABASE_URL=sqlite://database.db
  
### Initialize the database:
    python -c "from app.data.database import init_db; init_db()"
## Running the Application Locally
To start the application locally:
    
    python main.py
The application will be available at `http://127.0.0.1:5000`

## Testing the API
### 1.Using curl:
- Check for mutants:
  
      curl -X POST http://127.0.0.1:5000/mutant -H "Content-Type: application/json" -d "{\"dna\": [\"ATGCGA\", \"CAGTGC\", \"TTATGT\", \"AGAAGG\", \"CCCCTA\", \"TCACTG\"]}"
- Get stats:

      curl -X GET http://127.0.0.1:5000/stats
### 2.Using Postman or similar tools:
- Make a POST request to `http://127.0.0.1:5000/mutant` with a JSON body to check if the DNA is mutant.
- Make a GET request to `http://127.0.0.1:5000/stats` to retrieve stats.
    
## Deployment on Render
This API is deployed on Render. Follow these steps for deployment:
1. **Create a new Web Service** on Render and connect your GitHub repository.
2. **Build Command:** `pip install -r requirements.txt`
3. **Start Command:** `gunicorn main:app`
4. Render will automatically provide a URL for your API.
