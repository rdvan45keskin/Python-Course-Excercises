import pandas as pd
import numpy as np

data = {
    "Column1": [1,2,3,4,5],
    "Column2": [10,12,20,25,20],
    "Column3": ["abd","bcad","ade","cb","dea"]
}

df = pd.DataFrame(data)

def kareal(x):
    return x*x
kareal2 = lambda x: x*x

result = df
result = df["Column2"].unique()                         # dizide tekrarlayan elemanları 1 kere gösterme
result = df["Column2"].nunique()                        # dizide sqldeki distict methodu içindenki miktar
result = df["Column2"].value_counts()                   # dizide hangi elemanın kaç kere tekrar ettiğini gösterir
result = df["Column1"] * 2
result = df["Column1"].apply(kareal)                    # fonksiyon gönderme
result = df["Column1"].apply(kareal2) 
result = df["Column1"].apply(lambda x: x*x) 
df["Column4"] = df["Column3"].apply(len)                # bulunan değeri yeni sütun olarak ekleme
result = df.columns
result = len(df.columns)
result = df.index
result = len(df.index)
result = df.info

result = df.sort_values("Column2")                      # küçükten büyüğe sıralama
result = df.sort_values("Column3", ascending=False)     # büyükten küçüğe sıralama

data2 = {
    "Column1": np.tile([1,2,3,4,5],4),  # 20 eleman oluşturmak için 5 elemanı 4 kez tekrarladık
    "Column2": np.random.randint(1,100,20),
    "Column3": np.random.choice(["abd", "bcad", "ade", "cb", "dea"], 20) # 20 eleman oluşturmak için rastgele seçim yaptık
}

df = pd.DataFrame(data2)

print(df.pivot_table(index="Column1",columns="Column3",values="Column2"))

# print(result)

