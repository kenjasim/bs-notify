#!/bin/bash

########################################################
# Shell script to run a notification on apple computers
# which remind you to test your blood sugar
########################################################


# Function to create the blood glucose notification on mac
function create_notification(){
    osascript -e 'display notification "Test your blood sugar" with title "Blood Sugar Alert"'
}

# Run the notification
create_notification