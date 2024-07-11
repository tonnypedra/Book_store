from django.shortcuts import render
from .models import Book
from .models import Product

# Create your views here.
def index(request):
    booklist = Book.objects.all()
    productlist = Product.objects.all()


    context= {
        'booklist':booklist,
        'productlist':productlist
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')

def contuct(request):
    return render(request, 'contuct.html')

def regisration(request):
    return render(request, 'registration.html')







