import socket

def check_internet_connection():
    return socket.gethostbyname(socket.gethostname())
    
# print(check_internet_connection())