from output_module import output
from time_module import get_time

def process(query):
    if "what is time" in query:
        return ("Current Time is "+ get_time())
    else:
        return "Nothing to Return"
    