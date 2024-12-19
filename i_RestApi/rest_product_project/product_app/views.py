from django.shortcuts import render
from .forms import ProductForm
# Create your views here.
def index(request):
    return render(request, "product_app/index.html")

def prd_insert(request):
    form = ProductForm()
    return render(request, "product_app/product_form.html", {"form":form})