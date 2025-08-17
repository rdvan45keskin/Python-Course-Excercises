# series + series = dataframe
import pandas as pd

list = [["ahmet",50],["ali",60],["yağmur",70],["çınar",80]]
dict = {"name":["ahmet","ali","yağmur","çınar"],"grade":[50,60,70,80]}
dict_list = [
    {"Name":"Ahmet","Grade":50},
    {"Name":"Ali","Grade":60},
    {"Name":"Yağmur","Grade":70},
    {"Name":"Cınar","Grade":80}
    ]

# df = pd.DataFrame()
# df = pd.DataFrame([1,2,3,4])
# df = pd.DataFrame(list, columns=["ad","puan"],index=[1,2,3,4])
# df = pd.DataFrame(list, [1,2,3,4], ["ad","puan"],)       # ilk verileri gönderme 2. index numaraları 3. sütun adları
# df = pd.DataFrame(dict)
# df = pd.DataFrame(dict, index=["212","232","252","272"])
# df = pd.DataFrame(dict_list)
df = pd.DataFrame(dict_list, index=["212","232","252","272"])


print(df)

# s1 = pd.Series([3,2,0,1])
# s2 = pd.Series([0,3,7,2])

# data = dict(apples = s1 , oranges = s2)

# df = pd.DataFrame(data)

# print(df)