import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data, columns=["Column1","Column2","Column3","Column4","Column5"])

result = df
result = df.columns
result = df.head()                              # ilk 5 satırı gösterme
result = df.head(10)                            # ilk 10 satırı gösterme
result = df.tail()                              # son 5 satırı gösterme
result = df.tail(10)                            # son 10 satırı gösterme
result = df["Column1"].head()                   # column1 in ilk  5 satırını gösterme
result = df.Column1.head()                      # alternatif
result = df[["Column1","Column2"]].head()
result = df[["Column1","Column2"]].tail()
result = df[5:15][["Column1","Column2"]].head() # 5ten sonraki ilk 5 kaydı alma
result = df[5:15][["Column1","Column2"]].tail()

# filtreleme işlemi içindeki verilerle

result = df[df > 50]
result = df[df %2 == 0]
result = df[df["Column1"] > 50][["Column1"]]    # 50den büyük column1 deki sayıları getir
result = df[(df["Column1"] > 50) & (df["Column2"] <= 70)][["Column1","Column2"]]    # and operatorü
result = df[(df["Column1"] > 50) | (df["Column2"] <= 70)][["Column1","Column2"]]    # or operatörü
# ------
result = df.query("Column1 >= 50 & Column1 %2 == 0")[["Column1","Column2"]]    # filtreleme yapma methodu
# ------















print(result)
print(df)