from ez_docs.modules.data_cleaning import filter_data

final_data = [
    {'nome': 'Bruno'},
    {'nome': 'Miguel'},
    {'nome': 'Gobbi'},
    {'nome': 'Igor'},
]

final_data2 = [
    {'nome': 'Bruno'},
    {'nome': 'Miguel'},
    {'nome': 'Gobbi'},
    {'nome': 'Igor'},
    {'nome': 'Igor'},
]

def test_data_cleaning():
    assert filter_data("test/example.csv") == final_data

def test_data_cleaning_error():
    assert filter_data("test/example.csv") != final_data2