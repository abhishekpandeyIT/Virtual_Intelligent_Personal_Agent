from output_module import output
from time_module import get_time, get_date
from input_module import take_input
from database import *
from internet_module import check_internet_connection, check_on_wikipedia
import assistantResume
from web import *
import os

def process(query):
    answer = get_answers_from_memory(query)

    
        
    if answer == "get time details":
        return ("Current Time is "+ get_time())

    elif answer == "Internet Status":
        if check_internet_connection:
            return "Internet is connected"
        else:
            return "Internet is not connected"
    
    elif answer == "tell_date":
        return "Today's Date is: " + get_date()

    elif answer == "on speak":
        return turn_on_speech()
    
    elif answer == "off speak":
        return turn_off_speech()

    elif answer == "open facebook":
        open_facebook()
        return "Opening Facebook"

    elif answer == "open instagram":
        open_instagram()
        return "Opening Instagram"

    elif answer == "open google":
        open_google()
        return "Opening Google"

    elif answer == "open browser":
        open_browser()
        return "Opening Browser"

    elif answer == "open youtube":
        open_youtube()
        return "Opening Browser"


    
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