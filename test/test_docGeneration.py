from ez_docs.modules.doc_generation import loc_sub

def test_loc_sub():
    assert loc_sub("Ola <<Chave>>", "Chave", "Mundo")  == "Ola Mundo"
