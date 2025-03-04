import pandas as pd 
file = pd.read_csv ("Akash.csv")
training =file [['Time','RMS']]
print(file.to_string)