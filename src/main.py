from modules.gera_documento import gera_documento, identifica_nome_arquivo
from modules.utils import *

chave_valor = [
    {
    "NOME": "Rafael",
    "DISCIPLINA": "Sistema de bancos de dados 1",
    "DATA": "23 de Novembro de 2022",
    "CPF": "074.167.341-00",
    "MATRICULA": "200026488",
    },
    {
        "NOME": "Mateus",
        "DISCIPLINA": "Métodos de desenvolvimento de software",
        "DATA": "23 de Novembro de 2022",
        "CPF": "666.888.999-88",
        "MATRICULA": "200026588"
    },
    {
        "NOME": "Bruno",
        "DISCIPLINA": "Métodos de desenvolvimento de software",
        "DATA": "24 de Novembro de 2022",
        "CPF": "666.888.999-88",
        "MATRICULA": "2565865865"
    },
]

verify_pasta_output()
for aluno in chave_valor:
    gera_documento("../template.docx", aluno, "NOME_MATRICULA", 1)
clean_dir_docx()
