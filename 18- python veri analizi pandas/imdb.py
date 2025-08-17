import pandas as pd
df = pd.read_csv("imdb1.csv")


# 1-  Dosya hakkındai bilgiler
result = df.columns

# 2-  ilk 5 kaydı gösterin
result = df.head()

# 3-  ilk 10 kaydı gösterin
result = df.head(10)

# 4-  son 5 kaydı gösterin
result = df.tail()

# 5-  son 10 kaydı gösterin
result = df.tail(10)

# 6-  sadece Title kolonunu alın
result = df["Title"]

# 7-  sadece Title kolonunu içeren ilk 5 kaydı alın
result = df["Title"].head()

# 8-  sadece Title ve Rating kolonunu içeren ilk 5 kaydı alın
result = df[["Title","imdbRating"]].head()

# 9-  sadece Title ve Rating kolonunu içeren son 7 kaydı alın
result = df[["Title","imdbRating"]].tail(7)

# 10- sadece Title ve Rating kolonunu içeren ikinci 5 kaydı alın
result = df[5:][["Title","imdbRating"]].head()
# 11- sadece Title ve Rating kolonunu içeren ve imdb puanı 8.0
#     ve üstünde olan kayıtlardan ilk 50 tanesini alın
result = df[df["imdbRating"]>8][["Title","imdbRating"]].head(50)

# 12- yayın tarihi 2014 ve 2015 arasında olan filmlerin listesini alın
result = df[(df["Year"]>=2014) & (df["Year"]<=2015)][["Title"]]

# 13- değerlendirme sayısı (num_reviews) 100.000 den büyük ya da imdb puanı
#     8 ile 9 arasında olan filmleri listeleyin
import numpy as np

# imdbVotes sütununu sayıya dönüştür, hatalı verileri NaN olarak işaretle
df["imdbVotes"] = pd.to_numeric(df["imdbVotes"], errors='coerce')

# imdbRating sütununu sayıya dönüştür, hatalı verileri NaN olarak işaretle
df["imdbRating"] = pd.to_numeric(df["imdbRating"], errors='coerce')
result = df[(df["imdbVotes"] >= 100000) | ((df["imdbRating"] >= 8) & (df["imdbRating"] <= 9))][["Title"]]



print(result)