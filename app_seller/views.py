from django.shortcuts import render

# Create your views here.
def seller_index(request):
    return render(request,"seller_index.html")