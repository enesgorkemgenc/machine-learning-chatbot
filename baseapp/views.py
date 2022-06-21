from django.shortcuts import render

from .dbfunctions import *

import sqlite3


# Create your views here.


def get_homepage(request):
    
    return render(request, "base/index.html")




def get_data_page(request):

    connection = sqlite3.connect("chat.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM tbl_chat")
    data = {req:res for (req, res) in cursor.fetchall()}
    
    connection.close()

    context = {"chat_data": data}
    return render(request, "base/data.html", context)