from output_module import output
from time_module import get_time, get_date
from input_module import take_input
from database import get_answers_from_memory, insert_ques_ans, update_name
from internet_module import check_internet_connection, check_on_wikipedia
import assistantResume

def internet_accessbility():
    IP_address = check_internet_connection()

    if IP_address =='127.0.0.1':
        return False
    else:
        return True

def process(query):
    answer = get_answers_from_memory(query)

    
        
    if answer == "get time details":
        return ("Current Time is "+ get_time())

    elif answer == "Internet Status":
        if internet_accessbility():
            return "Internet is connected"
        else:
            return "Internet is not connected"
    
    elif answer == "tell_date":
        return "Today's Date is: " + get_date()
    
    elif answer == 'change name':
        output("Okay! What do you want to call me")
        temp = take_input()
        if temp == assistantResume.name:
            return "Can't Change. Its my current Name!!!"
        else:
            update_name(temp)
            assistantResume.name=temp
            return "Congrats! Now you can call me"


    else:
        output("Don't know this one, should I search on Internet")
        ans=take_input()
        if "yes" in ans:
            answer=check_on_wikipedia(query)
            if answer !="":
                return answer
        else:
            output("Please tell me what it means?")
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