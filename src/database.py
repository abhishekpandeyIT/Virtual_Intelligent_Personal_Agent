import sqlite3
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