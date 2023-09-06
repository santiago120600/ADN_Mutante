from src.main import mutante

def test_mutante():
    assert mutante([ 
        "ATGCGA", 
        "AAGTAA",
        "ATAAGA",
        "AGAAGA",
        "CCCCTA",
        "AAAATG" 
            ]) == True
    assert mutante([ 
        "ATGCGA", 
        "CAGTGC",
        "TTATGT",
        "AGAAGG",
        "CCCCTA",
        "TCACTG" 
            ]) == True
    
def test_no_mutante():
    assert mutante([
        "ATGCGA", 
        "CAGTGC", 
        "TTATGT", 
        "AGAAGG", 
        "CCCCTA", 
        "TCACTW" 
        ]) == False
    assert mutante([
        "ATGCGA", 
        "CAGTGC",
        "TTATTT",
        "AGACGG",
        "GCGTCA",
        "TCACTG" 
    ]) == False