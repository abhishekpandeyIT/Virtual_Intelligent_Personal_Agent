from output_module import output
from time_module import get_time
from database import get_answers_from_memory

def process(query):
    answer = get_answers_from_memory(query)

    if answer == "get time details":
        return ("Current Time is "+ get_time())
    else:
        return "Nothing to Return"
    