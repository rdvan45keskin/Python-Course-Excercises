# import datetime
from datetime import datetime
from datetime import timedelta

# print(dir(datetime))  date içerikleri

simdi = datetime.now()                        #**güncel zamanı verir**
result = datetime.now().year                  #**zamanın sadece yılını verir ve bu her zaman için geçerli gün ay vb**
result = datetime.today()                     #**güncel zamanı verir**
result = datetime.ctime(simdi)                #**daha açık bir şekilde yazar**

result = datetime.strftime(simdi,"%Y ")       #=> Yılı verir
result = datetime.strftime(simdi,"%X ")       #=> Saati verir
result = datetime.strftime(simdi,"%d ")       #=> Günü  verir
result = datetime.strftime(simdi,"%A ")       #=> string olarak günü verir
result = datetime.strftime(simdi,"%B ")       #=> string olarak ayı verir
result = datetime.strftime(simdi,"%Y %B %A ") #=> Yılı verir

t = "19 June 2024 10:35:30"
dt = datetime.strptime(t, "%d %B %Y %H:%M:%S")
dt = dt.year
print(dt)

birthday = (datetime(2003,6,19))

result = datetime.timestamp(birthday)         # savniye olarak gösterir
result = datetime.fromtimestamp(result)       # normal tarih formatına geri çevirir
result = datetime.fromtimestamp(0)            # bilgisayarların miladı olan tarih

result = simdi - birthday                     # timedelta

# result = result.days
# result = result.seconds
# result = result.microseconds
print(simdi)
# result = simdi + timedelta(days=730)        # tarih ekleme
# result = simdi - timedelta(days=110)        #tarih çıkarma

print(result)