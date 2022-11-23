# Importando bibliotecas
import docx
from docx.text.paragraph import Paragraph

from docx2pdf import convert

import re
import unicodedata


def loc_e_substitui(chave: str, valor:str, paragrafo: Paragraph):
    regex = re.compile(f"<<{chave}>>")
    is_match = False
    while True:
        text = paragrafo.text
        match = regex.search(text)
        if not match:
            break
        is_match=True
        runs = iter(paragrafo.runs)
        start, end = match.start(), match.end()

        for run in runs:
            run_len = len(run.text)
            if start < run_len:
                break
            start, end = start - run_len, end - run_len

        run_text = run.text
        run_len = len(run_text)
        run.text = "%s%s%s" % (run_text[:start], valor, run_text[end:])
        end -= run_len

        for run in runs:
            if end <= 0:
                break
            run_text = run.text
            run_len = len(run_text)
            run.text = run_text[end:]
            end -= run_len

    return is_match

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

    doc = docx.Document(diretorio_template)
    for chave in chave_valor.keys():
        for paragraph in doc.paragraphs:
            loc_e_substitui(chave, chave_valor[chave], paragraph)
    filename = identifica_nome_arquivo(chave_valor, chave_nome_arquivo)
    doc.save(f"output/{filename}.docx")
    if(flag == 1):
        convert(f"output/{filename}.docx", f"output/{filename}.pdf")
