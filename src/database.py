import sqlite3
from internet_module import check_internet_connection



def create_connection():
    connection= sqlite3.connect('Database/memory.db')
    return connection

def get_questions_and_answers():
    con = create_connection()
    cur = con.cursor()

    cur.execute('SELECT * FROM inputResponses')
    return cur.fetchall()

def insert_ques_ans(question,answer):
    con= create_connection()
    cur=con.cursor()
    query = "INSERT INTO inputResponses values('"+question+"','"+answer+"')"
    cur.execute(query)
    con.commit()

def get_answers_from_memory(question):
    rows=get_questions_and_answers()
    answer= ""
    for row in rows:
        if row[0].lower() in question.lower():
            answer = row[1]
            break
    return answer

def get_name():
    con= create_connection()
    cur=con.cursor()
    query = "SELECT status FROM memoryStatus WHERE name='assitantName'"
    cur.execute(query)
    return cur.fetchall()[0][0]
    
def update_name(new_name):
    con= create_connection()
    cur=con.cursor()
    query = "UPDATE memoryStatus SET status='"+new_name+"' WHERE name='assitantName'"
    cur.execute(query)
    con.commit()

def update_last_seen(last_seen_date):
    con= create_connection()
    cur=con.cursor()
    query = "UPDATE memoryStatus SET status='"+str(last_seen_date)+"' WHERE name='last_seen'"
    cur.execute(query)
    con.commit()

def get_last_seen():
    con= create_connection()
    cur=con.cursor()
    query = "SELECT status FROM memoryStatus WHERE name='last_seen'"
    cur.execute(query)
    return str(cur.fetchall()[0][0])

def turn_on_speech():
    if(check_internet_connection()):
        con= create_connection()
        cur=con.cursor()
        query = "UPDATE memoryStatus SET status='on' WHERE name='speech'"
        cur.execute(query)
        con.commit()
        return "Auto-Speech is on"
    else:
        return "Hey, Please turn on Internet First!"


def turn_off_speech():
    con= create_connection()
    cur=con.cursor()
    query = "UPDATE memoryStatus SET status='off' WHERE name='speech'"
    cur.execute(query)
    con.commit()
    return "Auto-Speech is off"

def speak_is_on():
    con= create_connection()
    cur=con.cursor()
    query = "SELECT status FROM memoryStatus WHERE name='speech'"
    cur.execute(query)
    ans= str(cur.fetchall()[0][0])

    if ans=="on":
        return True
    else:
        return False