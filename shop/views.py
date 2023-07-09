from django.shortcuts import render

def home(request):
    return render(request,"shops/index.html ");

def register(request):
    return render(request,"shops/register.html ");

def collections(request):
    catagory=Catagory.objects.filter(status=0)
    return render(request,"shops/collections.html ",{"catagory":catagory})