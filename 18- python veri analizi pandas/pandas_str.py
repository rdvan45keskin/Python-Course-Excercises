import pandas as pd
data = pd.read_csv("imdb1.csv")

# print(data.columns)

# data["Title"] = data["Title"].str.upper()
# data["Title"] = data["Title"].str.lower()
# data["index"] = data["Title"].str.find("a")
# data = data[data["Title"].str.contains("God")]
# data = data["Title"].str.replace(" ","-")

data[["column1","column2"]] = data["Title"].loc[data["Title"].str.split().str.len()==2].str.split(expand=True)

# titleyi boşlıktan bölüp 2 yeni sütüna atama işlemi



print(data.head(10))