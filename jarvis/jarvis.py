import time
import datetime
import subprocess

def execute_command(str):
	subprocess.Popen(['C:\Program Files (x86)\eSpeak\command_line\espeak.exe', str])

execute_command("Welcome back  Mr. Singh")

time.sleep(2)

day = datetime.date.today().strftime("%A")
month_date = datetime.date.today().strftime("%d")
month = datetime.date.today().strftime("%B")
year = datetime.date.today().strftime("%Y")

str = "Today is "+month_date+" of "+month+" "+year+". Hava a wonderfull "+day 

execute_command(str)

time.sleep(6)

hour = datetime.datetime.now().strftime("%H")
minutes = datetime.datetime.now().strftime("%M")

str = "and its   "+hour+" hours    "+minutes+" minutes at the moment. Hope you are doing great!"

execute_command(str)