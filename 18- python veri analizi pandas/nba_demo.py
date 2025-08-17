import pandas as pd
df = pd.read_csv("Players.csv")

# 1- ilk 10 kaydı getirin
result = df.head(10)

# 2- toplam kaç kayıt var
result = len(df.index)
# 3- tüm oyuncuların toplam boy ortalaması nedir
result = df["height"].mean()

# 4- en uzun boy ne kadardır
result = df["height"].max()

# 5- en uzun boy kime aittir
result = df[df["height"]==df["height"].max()]["Player"].iloc[0]

# 6- boyu 200-225 arasında olan oyuncuların ismi ve collage isimleri ve boya göre azalan şekilde sırala
result = df[(df["height"]>=200) & (df["height"]<=205)][["Player","collage","height"]].sort_values("height",ascending=False)

# 7- "Tierre Brown" isimli oyuncunun doğum tarihi
result = df[(df["Player"]=="Tierre Brown")]["born"].iloc[0]

# 8- collagelere göre oyuncuların ortalama doğum yılı nedir
result = df.groupby("collage")["born"].mean()

# 9- kaç farklı collage var
result = len(df.groupby("collage"))
result = df["collage"].nunique()

# 10- her collagede kaç kisi vars
result = df["collage"].value_counts()

# 11- ismi içinde "and" geçen kayıtları bulun
df = df.dropna()
result = df[df["Player"].str.contains("and")]

print(result)