from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
    
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user) # session ID oluşturma
            messages.add_message(request,messages.SUCCESS,"Giriş Başarılı")
            return redirect("index")
        else:
            messages.add_message(request,messages.ERROR,"Kullanıcı Adı veya Parola Yanlış")
            return redirect("login")
    else:
        return render(request, "user/login.html")

def register(request):
    if request.method == "POST":
        # formdan bilgileri alma
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password == repassword:
            # username daha önceden alınmış mı
            if User.objects.filter(username = username).exists():
                messages.add_message(request,messages.WARNING,"Bu kullanıcı Adı Daha Önceden Alınmış")
                return redirect("register")
            else: 
                # email daha önceden alınmış mı
                if User.objects.filter(email = email).exists():
                    messages.add_message(request,messages.WARNING,"bu email daha önce alınmış")
                    return redirect("register")
                else:
                    # her şey güzel
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    messages.add_message(request,messages.SUCCESS,"kullanıcı oluşturuldu")
                    return redirect("login")
        else:
            messages.add_message(request,messages.WARNING,"parolalar eşleşmiyor")
            return redirect("register")
        
        # user kayıt
    else:
        return render(request, "user/register.html")

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.add_message(request, messages.SUCCESS,"Oturum Sonlandırıldı")
    return redirect("index")

