from django.shortcuts import render, redirect

import sqlite3

from .models import Message

# Create your views here.


def get_homepage(request):
    context = {}

    return render(request, "base/index.html", context)


def get_data_page(request):

    if not request.user.is_authenticated:
        return redirect("homepage")

    messages = Message.objects.all()

    context = {"messages": messages}
    return render(request, "base/data.html", context)