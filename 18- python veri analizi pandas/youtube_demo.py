import pandas as pd

df = pd.read_csv("youtube-ing.csv")

# 1- ilk 10 kaydı getirin
result = df.head(10)

# 2- ikinci 5 kaydı getirin
result = df[5:].head()

# 3- dataset de bulunnan kolon isimleri ver sayısını bulun
result = df.columns
result = len(df.columns)

# 4- aşağıda bulunan bazı kolonları silin ve kalan kolonları listeleyin
#     ("thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description")
df.drop(["thumbnail_link", "comments_disabled", "ratings_disabled", "video_error_or_removed", "description"], axis=1, inplace=True)

# 5- beyenme ve beğenmeme ortalamalarını yazdır
result = df["likes"].mean()
result = df["dislikes"].mean()

# 6- ilk 50 videonun like ve dislike kolonlarını göster
result = df.head(50)[["title","likes","dislikes"]]

# 7- en çok görüntülenen video hangisidir
result = df["views"].max()
result = df[(df["views"].max()) == df["views"]][["title","views"]].iloc[0]

# 8- en düşük görüntülenen video hangisidir
result = df["views"].min()
result = df[(df["views"].min()) == df["views"]][["title","views"]].iloc[0]

# 9- en fazla görüntülenen ilk 10 video hangisidir
result = df.sort_values("views",ascending=False)[["title","views"]].head(10)

# 10- kategoriye göre beğeni ortalamalarını sıralaı şekilde getirin 
# çalışmıyo saçmalık
# result = df.groupby("category_id").mean().sort_values("likes")["likes"]

# 11- kategoriye göre yorum sayılarını yukarıdan aşağıya sıralayın
# çalışmıyo saçmalık
# result = df.groupby("category_id").sum().sort_values("comment_count", ascending=False)["comment_count"]

# 12- her kategoride kaç video vardır
result = df["category_id"].value_counts()

# 13- her videonun title uzunluğu bilgisini yeni bir kolonda gösterin
df["title_len"] = df["title"].apply(len)
result = df
# 14- her video için kullanılan tag sayısını yeni kolonda gösterin
# 1-
# df["tag_count"] = df["tags"].apply(lambda x: len(x.split("|")))
# 2-
def tagCount(tag):
    return len(tag.split("|"))
df["tag_count"] = df["tags"].apply(tagCount)

# 15- en popüler videoları listeleyin (like/dislike oranına göre)

def oranHesap(dataset):
    likesList = list(dataset["likes"])
    dislikesList = list(dataset["dislikes"])

    liste = list(zip(likesList,dislikesList))         # birleştirme likelist[0] ile dislikelist[0] birleştirme gibi

    oranListe = []

    for like,dislike in liste:
        if (like + dislike == 0):
            oranListe.append(0)
        else:
            oran = like/(like+dislike)
            oranListe.append(oran)
        
    return oranListe

df["begeni_orani"] = oranHesap(df)

print(df.sort_values("begeni_orani",ascending=False)[["title","likes","dislikes","begeni_orani"]])


