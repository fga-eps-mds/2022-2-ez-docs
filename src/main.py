from modules.doc_generation import doc_generator
from modules.usable import *
from modules.data_cleaning import filter_data

filter_doc = filter_data("./random.csv")
flag = 1

verify_folder_output()
for name in filter_doc:
    doc_generator("./template.md", name, "NAME_ID", flag)

if flag == 1:
    clean_dir_md()
