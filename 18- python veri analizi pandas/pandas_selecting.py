import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(3,3), index=["a","b","c"],columns=["column1","column2","column3"])

result = df
result = df["column1"]
result = df[["column1","column2"]]      # sütunları seçmek için kullanılır


#loc["row","column"] => loc["row"] => loc[:,"column"]

# seçme işlemleri
result = df.loc["a"]                    
result = df.iloc[2]                     # indexler deişse bile bu meethod varsayılan indeksle işlem yapar
result = df.loc[["a","b"]]              # satırları seçmek için kullanılır
result = df.loc[:,"column1"]
result = df.loc[:,["column1","column2"]]
result = df.loc[:,"column1":"column3"]  # column 1 ve 3 arasında tüm satırları getirir
result = df.loc[:,:"column3"]           # bastan column3 e kadar tüm satırları alma
result = df.loc["a":"b",:"column3"]
result = df.loc[:"b",:"column3"]
result = df.loc["a","column2"]
result = df.loc["c","column1"]
result = df.loc[["a","b"],["column1","column2"]]

# kolon ekleme
df["column4"] = pd.Series(np.random.randn(3),["a","b","c"])
df["column5"] = df["column1"] + df["column3"]

# kolon silme
result = (df.drop("column5", axis = 1))     # inplace = True değeri eklenirse datada değişikliği yapar

print(result)
print(df)
