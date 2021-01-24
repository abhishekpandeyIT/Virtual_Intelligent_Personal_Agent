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

insert_ques_ans('Check internet connection','Internet Status')