import sqlite3
def create_connection():
    connection= sqlite3.connect('Database/memory.db')
    return connection

def get_questions_and_answers():
    con = create_connection()
    cur = con.cursor()

    cur.execute('SELECT * FROM inputResponses')
    for row in cur.fetchall():
        print(row)

get_questions_and_answers()