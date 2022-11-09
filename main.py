#Training python pandas lib

#LOADING DATA
import pandas as pd

df_csv = pd.read_csv("pokemon_data.csv")
df_xlsx = pd.read_excel("pokemon_data.xlsx")
df_txt = pd.read_csv("pokemon_data.txt")

#.head(n) prints the first n elements from the beginning of the file
print(df_csv.head(8))

#.tail(n) prints the last n elements from the end of the file
print(df_xlsx.tail(3))

print(df_txt)
#We gonna use a delimiter to separate the elements from the text using the demiliter argument
df_txt = pd.read_csv("pokemon_data.txt", delimiter="\t")
print("Text:\n", df_txt)

###############
#READING DATA#

#Read headers
print(df_csv.columns)

#Read each column
print(df_csv['Name'][10:20])
#print(df_csv.Name);
print(df_csv[['Name', 'Type 1', 'HP']])

#Read each row
#iloc stands for integer location
print(df_csv.iloc[1])
#it will prints all about object at line 1
# for index, row in df_csv.iterrows():
#     print(index, row['Name']);


#.loc() is used to find a specific data into the data set based on a given information
print("Grass:");
print(df_csv.loc[df_csv["Type 1"] == "Grass"])


print(df_csv.iloc[2:7])

#Read a specific location (R,C)
print(df_csv.iloc[2,1])


