import argparse

from modules.gera_documento import gera_documento
from modules.utils import *
from modules.trata_dados import filter_data

def gerador_documentos(dict_args: dict):

    verify_pasta_output()
    for obj in filter_data(dict_args['diretorio_base']):
        gera_documento(
            dict_args['diretorio_template'],
            obj, dict_args['modelo_nome_arquivo'],
            dict_args['flag']
        )

    if dict_args['flag'] == 1:
        clean_dir_md()

def main():
    parser = argparse.ArgumentParser(description='Gere documentos automaticamente.')
    parser.add_argument('diretorio_template', help='Diretorio do template.')
    parser.add_argument('diretorio_base', help='Diretorio da base de dados')
    parser.add_argument('modelo_nome_arquivo', help='Modelo do nome do arquivo de saida.')
    parser.add_argument('--flag', help='Flag de extensao de saida. 0 para .md,  1 para .pdf', default=1)
    args = parser.parse_args()
    gerador_documentos(dict(args._get_kwargs()))

if __name__ == '__main__':
    main()
