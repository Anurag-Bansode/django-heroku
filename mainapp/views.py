from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    return render(request,'mainapp/base.html',{})

def putStock(request):
    url ="https://finnhub.io/api/v1/quote?symbol=AAPL&token=ccmkt6qad3i2veb1f5f0ccmkt6qad3i2veb1f5fg"
    r=requests.get(url)
    print(r.json())
    return render(request,'mainapp/stockQuote.html',{'data':r.json()})