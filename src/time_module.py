from datetime import datetime

def get_time():
    now = datetime.now()

    current_time= now.strftime("%H Hours %M Minutes")
    return current_time