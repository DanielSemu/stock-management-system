from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'stock/home.html')

def add_stock(request):
    return render(request,'stock/addStock.html')