import pandas as pd


def filter_data(data_set):
    # Open csv and delete the duplicates lines and/or blank fields.
    start_data = pd.read_csv(data_set, delimiter=',')
    start_data.dropna(inplace=True)
    start_data.drop_duplicates(inplace=True)
    """
    # Converts the data_set to the format specified in the architecture:
    # key_value = [
    #     {
    #     "field 1": "value 1",
    #     "...": "...",
    #     "field n": "value n"
    #     },
    # ]
    """
    final_data = []
    for line in range(len(start_data)):
        final_data.append({})
        for col in list(start_data.columns):
            final_data[line][col] = str(start_data.iloc[line][col])

    return final_data
