import assistantResume
from speak_module import speak
from database import speak_is_on

def output(o):
    # For command line input
    if speak_is_on():
        speak(o)
    print(assistantResume.name +": "+o+"\n")