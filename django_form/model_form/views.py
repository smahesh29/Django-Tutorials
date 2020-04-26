from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AuthorForm, AuthorForm_1, AuthorForm_2, AuthorForm_3, AuthorForm_4, AuthorForm_5, BookForm

# Create your views here.
def author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your author has been created!')
            return redirect('author')
    else:
        form = AuthorForm()
    return render(request, 'model_form/author.html', {'form': form})

def author_1(request):
    if request.method == 'POST':
        form = AuthorForm_1(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your author has been created!')
            return redirect('author_1')
    else:
        form = AuthorForm_1()
    return render(request, 'model_form/author.html', {'form': form})

def author_2(request):
    if request.method == 'POST':
        form = AuthorForm_2(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your author has been created!')
            return redirect('author_2')
    else:
        form = AuthorForm_2()
    return render(request, 'model_form/author.html', {'form': form})


def author_3(request):
    if request.method == 'POST':
        form = AuthorForm_3(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your author has been created!')
            return redirect('author_3')
    else:
        form = AuthorForm_3()
    return render(request, 'model_form/author.html', {'form': form})


def author_4(request):
    if request.method == 'POST':
        form = AuthorForm_4(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your author has been created!')
            return redirect('author_4')
    else:
        form = AuthorForm_4()
    return render(request, 'model_form/author.html', {'form': form})


def author_5(request):
    if request.method == 'POST':
        form = AuthorForm_5(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your author has been created!')
            return redirect('author_5')
    else:
        form = AuthorForm_5()
    return render(request, 'model_form/author.html', {'form': form})


def book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your book has been Added!')
            return redirect('book')
    else:
        form = BookForm()
    return render(request, 'model_form/book.html', {'form': form})