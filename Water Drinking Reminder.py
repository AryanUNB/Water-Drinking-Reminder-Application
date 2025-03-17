import time
#need to pip install plyer for the line to work in the cmd prompt
from plyer import notification

#to do it specific number of times include a for loop using in range
while True:
    notification.notify(
        title="Please Drink Water",
        message="Drinking water aids digestion, transports nutrients, flushes waste, regulates body temperature, and lubricates joints.",
        app_icon=r"C:\Users\aryan\Desktop\Python files\WaterIcon.ico",
        #the time for which the message will appear in seconds
        timeout=30
    )
    # 60 seconds x 60 minutes = 1 hour
    time.sleep(60*60)

# to kill this following program go in task manager and close the python file