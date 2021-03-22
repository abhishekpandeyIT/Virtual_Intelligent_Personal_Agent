import socket
import wikipedia

def check_internet_connection():
    return socket.gethostbyname(socket.gethostname())
    
# print(check_internet_connection())

def check_on_wikipedia(query):
    query= query.lower()
    query = query.replace("who is","")
    query = query.replace("what is","")
    query = query.replace("do you know","")
    query = query.replace("tell me","")
    query =query.strip()

    try:
        data=wikipedia.summary(query,sentences=2)
        return data

    except Exception:
        return ""


