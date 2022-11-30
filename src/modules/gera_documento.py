# Importando bibliotecas
import re
import unicodedata
import os


def loc_sub(text, chave, valor):
    pattern = f"<<{chave}>>"
    text = re.sub(pattern, valor, text)
    return text

def slugify(value, allow_unicode=False):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')

def identifica_nome_arquivo(chave_valor: str, chave_nome_arquivo:str):
    nome_final = chave_nome_arquivo
    for chave in chave_valor.keys():
        pattern=rf'{chave}(?=[:\-_ .,\s]|$)'
        nome_final = re.sub(pattern, chave_valor[chave], nome_final)
    return slugify(nome_final)

def gera_documento(diretorio_template: str, chave_valor: dict, chave_nome_arquivo: str, flag: int=1):

    with open(diretorio_template, "r", encoding="utf-8") as input_file:
        text = input_file.read()
        input_file.close()
    filename = identifica_nome_arquivo(chave_valor, chave_nome_arquivo)
    with open(f"./output/{filename}.md", "w+", encoding="utf-8") as input_file:
        for chave in chave_valor.keys():
            text = loc_sub(text, chave, chave_valor[chave])
        input_file.write(text)
    if flag == 1:
        os.system(f"mdpdf -o ./output/{filename}.pdf ./output/{filename}.md")

