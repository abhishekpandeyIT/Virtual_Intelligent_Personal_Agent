import sqlite3
def create_connection():
    connection= sqlite3.connect('Database/memory.db')
    return connection

def get_questions_and_answers():
    con = create_connection()
    cur = con.cursor()

    cur.execute('SELECT * FROM inputResponses')
    return cur.fetchall()

def get_answers_from_memory(question):
    rows=get_questions_and_answers()
    answer= ""

    for row in rows:
        if row[0].lower() in question.lower():
            answer = row[1]
            break
    return answer

print(get_answers_from_memory("What is Time"))

get_questions_and_answers()