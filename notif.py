from plyer import notification
import time

notification_title="TAKE CARE OF YOURSELF"
notification_message="Please Drink water in every two hours"
while(True):

    notification.notify(
        title = notification_title,  
        message = notification_message,  
        app_icon = "D:/CODING/PYTHON/DAY_94/1.ico",  
        timeout = 8,  
        toast = False 
    )
    time.sleep(60*60*2)