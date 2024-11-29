from django.shortcuts import render , HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
 
    return render(request , 'index.html' )
    # return HttpResponse("this is home page")

def about(request):
    # return HttpResponse("this is About page")
    return render(request , 'about.html' )

def shop(request):
    return render(request, 'shop.html')

def recipe(request):
    return render(request, 'recipe.html')

def login(request):
    return render(request, 'login.html')

def houseOfSky(request):
    return render(request, 'houseOfSky.html')

def cart(request):
    return render(request, 'cart.html')

def blog(request):
    return render(request, 'blog.html')

def bestSellingItem(request):
    return render(request, 'bestSellingItem.html')

def Anime(request):
    return render(request, 'Anime.html')

def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name , email=email , phone=phone , desc=desc , date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent !! 📬")

    return render(request , 'contact.html' )