from output_module import output
from time_module import get_time
from input_module import take_input
from database import get_answers_from_memory, insert_ques_ans

def process(query):
    answer = get_answers_from_memory(query)

    if answer == "get time details":
        return ("Current Time is "+ get_time())
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
    