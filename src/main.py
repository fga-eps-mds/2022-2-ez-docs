from modules.gera_documento import gera_documento
from modules.utils import *
from modules.trata_dados import filter_data

chave_valor = filter_data("./random.csv")

flag = 1

verify_pasta_output()
for aluno in chave_valor:
    gera_documento("./template.md", aluno, "NOME_MATRICULA", flag)

if flag == 1:
    clean_dir_md()
