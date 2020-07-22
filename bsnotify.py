#!/usr/bin/env python
import os
from datetime import datetime, timedelta
import time

class BSNotify():

    def __init__(self):
        """
        Class constructor which runs the run function
        """

        #Run the Program
        self.run()
        

    def run(self):
        """
        Runs the command then waits two hours to run the next command
        """

        while True:

            #Run the alert
            self.notify("Blood Sugar Alert", "Test Your Blood Sugar")

            # Format the time
            dt = datetime.now() + timedelta(hours=2)
            dt = dt.replace(minute =0, second=0, microsecond=0)

            # Wait until the time has passed
            while datetime.now() < dt:
                time.sleep(1)


    def notify(self,title, text):
        """
        Function to run the apple script needed to make a notification

        Keyword Arguments
            title - title of the notification
            text - text of the notification
        """
        # Parse the command into the command line
        os.system("""
                osascript -e 'display notification "{}" with title "{}"'
                """.format(text, title))

b = BSNotify()
