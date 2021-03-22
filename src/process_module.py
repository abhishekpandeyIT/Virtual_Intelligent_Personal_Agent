from output_module import output
from time_module import get_time
from input_module import take_input
from database import get_answers_from_memory, insert_ques_ans
from internet_module import check_internet_connection, check_on_wikipedia

def internet_accessbility():
    IP_address = check_internet_connection()

    if IP_address =='127.0.0.1':
        return False
    else:
        return True

def process(query):
    answer = get_answers_from_memory(query)

    if answer == "":
        answer=check_on_wikipedia(query)
        if answer !="":
            return answer

    if answer == "get time details":
        return ("Current Time is "+ get_time())

    elif answer == "Internet Status":
        if internet_accessbility():
            return "Internet is connected"
        else:
            return "Internet is not connected"


    else:
        output("I don't know this one, pls. tell me what it means?")
        ans= take_input()
        if "it means" in ans:
            ans = ans.replace("it means", "")
            ans= ans.strip()

            value=get_answers_from_memory(ans)
            if value== "":
                return "can't help with this one"
            else:
                insert_ques_ans(query, value)
                return "Thanks I will remember it for the next Time."
        else:
            return "can't help with this one"