from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from blog.models import Book, Comment


def index(request):
    return render(request, "home.html")


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registration.html', {'form': form})


def books(request):
    context = {'books': Book.objects.order_by('title').all()}
    return render(request, 'bookblog.html', context)


def comments(request):
    if request.method == 'POST':
        posted_comment = Comment()
        posted_comment.date = timezone.now()
        posted_comment.text = request.POST.get("comment")
        posted_comment.book_id = request.POST.get("bookId")
        posted_comment.user_id = request.user.id

        posted_comment.save()
        return redirect("bookblog")

    else:
        return redirect("bookblog")
