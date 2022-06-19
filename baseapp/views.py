from django.shortcuts import render

from .dbfunctions import *

import sqlite3


# Create your views here.


def get_homepage(request):
    connection = sqlite3.connect("chat.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM tbl_chat")
    table_data = {req:res for (req, res) in cursor.fetchall()}
    
    connection.close()
    context = {"data": table_data}
    return render(request, "temporary.html", context)
