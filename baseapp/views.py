from django.shortcuts import render, redirect

from .dbfunctions import *

import sqlite3


# Create your views here.


def get_homepage(request):
    context = {}
    return render(request, "base/index.html", context)


def get_data_page(request):

    if not request.user.is_authenticated:
        return redirect("homepage")

    connection = sqlite3.connect("chat.db")
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM tbl_chat")
    data = {req:res for (req, res) in cursor.fetchall()}
    
    connection.close()

    context = {"chat_data": data}
    return render(request, "base/data.html", context)