from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth import login
from .forms import RegisterForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data.get("role")
            if role:
                group, _ = Group.objects.get_or_create(name=role)
                user.groups.add(group)
            login(request, user)
            messages.success(request, "Registration successful")
            return redirect("jobs:home")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})

# Create your views here.
