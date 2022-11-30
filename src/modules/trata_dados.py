import pandas as pd

def filter_data(dataSet):
    #Abre o csv e deleta as linhas duplicadas e/ou com campos vazios
    startData = pd.read_csv(dataSet, delimiter=',')
    startData.dropna(inplace=True)
    startData.drop_duplicates(inplace=True)
    
    #Converte o dataSet para o formato especificado na arquitetura:
    # chave_valor = [
    #     {
    #     "campo 1": "valor 1",
    #     "...": "...",
    #     "campo n": "valor n"
    #     },
    # ]
    finalData = []
    for line in range(len(startData)):
        finalData.append({})
        for col in list(startData.columns):
            finalData[line][col] = str(startData.iloc[line][col])
    
    return finalData