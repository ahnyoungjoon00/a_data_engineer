from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm

import pandas as pd
# Create your views here.
def index(request) :
    return render(request,'book_app/index.html')

# def book_list(request):
#     books = Book.objects.all()
#     print(books)
#     print(Book.objects.values())
#     return render(request, "book_app/book_list.html", {"books" : books})

def book_list(request):
    books = Book.objects.all()

    bk_list = []
    for book in books.values():
        bk_list.append(book)
    df = pd.DataFrame.from_dict(bk_list)
    df["bookno"] = df["bookno"].astype(int)
    df = df.sort_values("bookno")
    bk_dict = df.to_dict("records")
    print(bk_dict)
    return render(request, "book_app/book_list.html", {"books" : bk_dict})

def book_detail(request, bookno) :
    book = get_object_or_404(Book, pk = bookno)
    return render(request, "book_app/book_detail.html", {"book":book})


def book_insert(request) :
    form = BookForm()
    if request.method == "POST" :
        form = BookForm(request.POST)
        if form.is_valid() :
            book = form.save(commit=False)
            book.save()
            return redirect("book_list")
    return render(request, "book_app/book_form.html", {"form":form})
