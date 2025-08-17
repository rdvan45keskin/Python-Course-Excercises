from django.shortcuts import render
from django.http import HttpResponse # yanıt yollama
# Create your views here.
# http://127.0.0.1:8000/
# buraya gönderilmek istenen http bilgileri giriliyo
def index(request):
    # return HttpResponse("<h1>Hello from pages app</h1>")
    return render(request, "pages/index.html")

def about(request):
    return render(request, "pages/about.html")
