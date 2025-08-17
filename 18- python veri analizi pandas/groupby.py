import pandas as pd
import numpy as np

personeller = {
    "Çalışan":["Ahmet Yılmaz","Can Ertürk","Hasan Korkmaz","Cenk Saymaz","Ali Turan","Rıza Ertürk","Mustafa Can"],
    "Departman":["İnsan Kaynakları","Bilgi İşlem","Muhasebe","İnsan Kaynakları","Bilgi İşlem","Muhasebe","Bilgi İşlem"],
    "Yas":[30,25,45,50,23,34,42],
    "Semt":["Kadıköy","Tuzla","Maltepe","Tuzla","Kadıköy","Tuzla","Maltepe"],
    "Maas":[5000,3000,4000,3500,2750,6500,4500]
}

df = pd.DataFrame(personeller)

result = df
result = df["Maas"].sum()
result = df.groupby("Departman").groups
result = df.groupby(["Departman","Semt"]).groups

# # semte göre gruplama
# for name,group in df.groupby("Semt"):
#     print(name)
#     print(group)

# # departmana göre gruplama
# for name,group in df.groupby("Departman"):
#     print(name)
#     print(group)

# result = df.groupby("Semt").get_group("Kadıköy")
# result = df.groupby("Departman").get_group("Muhasebe")


# result = df.groupby("Departman").sum()
result = df.groupby("Departman")["Maas"].mean()             # her departmandaki maaş ortalaması
result = df.groupby("Semt")["Yas"].mean()                   # her semtteki yaş ortalaması
result = df.groupby("Semt")["Maas"].mean()                  # her semtteki maaş ortalaması
result = df.groupby("Semt")["Çalışan"].count()              # her semtteki çalışan sayısı
result = df.groupby("Departman")["Yas"].max()               # her departmandaki maximum yaş
result = df.groupby("Departman")["Yas"].min()               # her departmandaki minimum yaş
result = df.groupby("Departman")["Maas"].max()["Muhasebe"]  # muhasebe departmanındaki maximum maaş
result = df.groupby("Departman")["Maas"].agg(np.mean)       # her departmandaki maaş ortalaması
result = df.groupby("Departman")["Maas"].agg([np.sum,np.mean,np.min,np.max]).loc["Muhasebe"]
print(result)