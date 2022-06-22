import sqlite3
import random



def create_table():
    connection = sqlite3.connect("chat.db")
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE tbl_chat (request text,response text)")

    connection.commit()
    connection.close()


def handle_request(request_text):

    expect = False
    #Preventing SQL injection by limiting the characters.
    request_text = "".join([char for char in request_text if char.isalnum() or char in " !+%&/()=;:.<>"]).strip()
    connection = sqlite3.connect("chat.db")
    cursor = connection.cursor()

    if (not request_text) or (len(request_text) < 2):
        cursor.execute(f"SELECT request FROM tbl_chat WHERE response = '' ")
        response_text = random.choice(cursor.fetchall())[0]
        expect = True
        return {"response_text":response_text, "expect":expect}

    cursor.execute("SELECT request FROM tbl_chat")
    all_requests = [req[0] for req in cursor.fetchall()]

    if request_text in all_requests:
        cursor.execute(f"SELECT response FROM tbl_chat WHERE request = '{request_text}' ")
        temp_response_text = cursor.fetchone()[0]

        if temp_response_text: # not equals to ''
            response_text = random.choice(temp_response_text.strip().split(",")[:-1]).strip()
        else:
            cursor.execute(f"SELECT request FROM tbl_chat WHERE response = '' ")
            response_text = random.choice(cursor.fetchall())[0]
            expect = True

    else:
        cursor.execute(f"INSERT INTO tbl_chat VALUES ('{request_text}', '')")
        connection.commit()
        
        cursor.execute(f"SELECT request FROM tbl_chat WHERE response = '' ")
        response_text = random.choice(cursor.fetchall()[0])
        expect = True
    
    


    #To make the chat to be continious and more realistic, I'm adding
    #the bot's response as a request, and going to record the user's answer
    #as the response of our bot's response whether if it is related or not.

    cursor.execute("SELECT request FROM tbl_chat")
    all_requests = [req[0] for req in cursor.fetchall()]

    if not (response_text in all_requests):
        cursor.execute(f"INSERT INTO tbl_chat VALUES ('{response_text}', '')")
        connection.commit()

    connection.close()

    return {"response_text":response_text, "expect":expect}



def handle_response(request_text, response_text):
    response_text = "".join([char for char in request_text if char.isalnum() or char in " !+%&/()=;:.<>"]).strip()
    connection = sqlite3.connect("chat.db")
    cursor = connection.cursor()

    cursor.execute(f"SELECT response FROM tbl_chat WHERE request = '{request_text}' ")
    current_responses = cursor.fetchone()[0]
    cursor.execute(f"UPDATE tbl_chat SET response = '{current_responses}{response_text}, ' WHERE request = '{request_text}' ")

    connection.commit()
    connection.close()