from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import UserRegistrationForm, PostForm, CommentForm
from django.contrib.auth import login


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('registration')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})




