from django.shortcuts import render, HttpResponse

from datetime import datetime

# Create your views here.
def index(request):
    daytime_str = datetime.today().strftime("%Y/%m/%d %H:%M:%S")
    
    return render(request, "index.html", {'today_str':daytime_str})
