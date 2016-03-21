#!/usr/local/bin/python

import sys
import time
import datetime
from datetime import date
import subprocess

def say(words):
    subprocess.Popen(args=["say " + words], shell=True)

def run(start_hour, increment):
    start_time = datetime.datetime(date.today().year, date.today().month, date.today().day, int(start_hour))
    time_delta = datetime.timedelta(minutes=int(increment))

    while (start_time < datetime.datetime.now()):
        start_time = start_time + time_delta

        minutes = start_time.strftime("%M")
        if minutes == "00":
            minutes = ""
        else:
            minutes = minutes +  " minutes"
        #say("Advancing " + increment + " minutes to " + start_time.strftime("%H") + "hundred hours" + minutes) 

    say("Alarm initiated")

    while (True):
        if (start_time < datetime.datetime.now()):
            minutes = start_time.strftime("%M")
            if minutes == "00":
                minutes = ""
            else:
                minutes = minutes +  " minutes"   
            say(start_time.strftime("%H") + "hundred hours" + minutes) 
            start_time = start_time + time_delta

        time.sleep(10) 



if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "Usage: work_alarm.py <start hour> <increment in minutes>"
        exit()
    run(sys.argv[1], sys.argv[2])



    


    
