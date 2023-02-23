from multiprocessing import context
from django.shortcuts import render, HttpResponseRedirect, redirect

from book_app.models import Book
from book_app.forms import BookForm
from django.urls import reverse, reverse_lazy

from django.contrib import messages
# Create your views here.

def book(request):
    form = BookForm()
    registered = False
    if request.method == "POST":
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True

            # return HttpResponseRedirect(reverse('book_app:book'))
    diction = {'form':form, 'registered':registered}
    return render(request,'book_app/book.html', context = diction)







