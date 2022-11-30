from modules.trata_dados import filter_data

chave_valor = filter_data("../random.csv")
for ch in chave_valor:
    print(ch, "\n")