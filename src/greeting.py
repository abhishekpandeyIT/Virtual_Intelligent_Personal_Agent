from time_module import get_hours, get_date
from output_module import output
from database import update_last_seen, get_last_seen
from datetime import date

def greet():

    # Fetch Previous Date
    previous_date= get_last_seen()


    # Fetch Today's date and store it to database
    todays_date=get_date()
    update_last_seen(todays_date)

    
    
    if previous_date ==todays_date:
        output("Welcome Back, buddy!")
    
    else:
        hour=int(get_hours())

        if hour >=0 and hour <12:
            output("Hey, Good Morning!")
        
        elif hour >=12 and hour <16:
            output("Hey, Good After Noon!")
        
        else:
            output("Hey, Good Evening!")