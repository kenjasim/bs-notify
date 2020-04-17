#!/usr/bin/env python
import os

#function to run the apple script needed to make a notification
def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

#Run the alert
notify("Blood Sugar Alert", "Test Your Blood Sugar")
