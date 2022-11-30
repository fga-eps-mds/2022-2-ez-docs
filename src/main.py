from modules.gera_documento import gera_documento
from modules.utils import *
from modules.trata_dados import filter_data

# chave_valor = [
#     {
#     "NOME": "Rafael",
#     "DISCIPLINA": "Sistema de bancos de dados 1",
#     "DATA": "23 de Novembro de 2022",
#     "CPF": "074.167.341-00",
#     "MATRICULA": "200026488",
#     },
#     {
#         "NOME": "Mateus",
#         "DISCIPLINA": "Métodos de desenvolvimento de software",
#         "DATA": "23 de Novembro de 2022",
#         "CPF": "666.888.999-88",
#         "MATRICULA": "200026588"
#     },
#     {
#         "NOME": "Bruno",
#         "DISCIPLINA": "Métodos de desenvolvimento de software",
#         "DATA": "24 de Novembro de 2022",
#         "CPF": "666.888.999-88",
#         "MATRICULA": "2565865865"
#     },
# ]

chave_valor = filter_data("../random_data.csv")

flag = 0

verify_pasta_output()
for aluno in chave_valor:
    gera_documento("../template.md", aluno, "NOME_MATRICULA", 0)

if flag == 1:
    clean_dir_md()
