import sqlite3
import random

def custom_command():
    connection = sqlite3.connect("chat.db")
    cursor = connection.cursor()

    cursor.execute("SELECT response FROM tbl_chat")

    for item in cursor.fetchall():
        data = item[0].replace(",",";")
        cursor.execute(f"UPDATE tbl_chat SET response = '{data}' WHERE response = '{item[0]}' ")
        connection.commit()
        
    connection.close()

def create_table():
    connection = sqlite3.connect("chat.db")
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE tbl_chat (request text,response text)")

    connection.commit()
    connection.close()


def handle_request(old_response, request_text):

    #Preventing SQL injection by limiting the characters.
    request_text = "".join([char for char in request_text if char.isalnum() or char in " ?!:(),."]).strip().lower()
    connection = sqlite3.connect("chat.db")
    cursor = connection.cursor()

    if (not request_text) or (len(request_text) < 2):
        cursor.execute(f"SELECT request FROM tbl_chat WHERE response = '' ")
        response_text = random.choice(cursor.fetchall())[0]
        return {"response_text":response_text}

    if old_response:
        cursor.execute(f"SELECT response FROM tbl_chat WHERE request = '{old_response}'")
        current_responses_for_old_response = cursor.fetchone()[0]

        cursor.execute(f"UPDATE tbl_chat SET response = '{current_responses_for_old_response}{request_text}; ' WHERE request = '{old_response}' ")
        connection.commit()


    cursor.execute("SELECT request FROM tbl_chat")
    all_requests = [req[0] for req in cursor.fetchall()]

    if request_text in all_requests:
        cursor.execute(f"SELECT response FROM tbl_chat WHERE request = '{request_text}' ")
        temp_response_text = cursor.fetchone()[0]

        if temp_response_text: # not equals to ''
            response_text = random.choice(temp_response_text.strip().split(";")[:-1]).strip()
        else:
            cursor.execute(f"SELECT request FROM tbl_chat WHERE response = '' ")
            response_text = random.choice(cursor.fetchall())[0]

    else:
        cursor.execute(f"INSERT INTO tbl_chat VALUES ('{request_text}', '')")
        connection.commit()
        
        cursor.execute(f"SELECT request FROM tbl_chat WHERE response = '' ")
        response_text = random.choice(cursor.fetchall()[0])
    

    #To make the chat to be continuous and more realistic, I'm adding
    #the bot's response as a request, and going to record the user's answer
    #as the response of our bot's response whether if it is related or not.

    cursor.execute("SELECT request FROM tbl_chat")
    all_requests = [req[0] for req in cursor.fetchall()]

    if not (response_text in all_requests):
        cursor.execute(f"INSERT INTO tbl_chat VALUES ('{response_text}', '')")
        connection.commit()

    connection.close()

    return {"response_text":response_text}
