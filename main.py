# Libraries imported
import pyautogui 
from datetime import datetime
import subprocess
import time

#Edit this file as Required
def zoomClass(meetingID,meetingPassword,meetingTime):

    #Getting Current Cursor Position
    a,b=pyautogui.position()

    # Edit Here
    # enter your path to Zoom.exe
    pathToZoom=r'C:\Users\Sanjay\AppData\Roaming\Zoom\bin\Zoom.exe'
    subprocess.Popen(pathToZoom)

    # Adjust sleep time if your PC is slow
    time.sleep(5)

    #Getting Joining Button Position
    x,y = pyautogui.locateCenterOnScreen('./joinButton.png')
    pyautogui.click(x,y)

    # Adjust Sleep time if Your Network speed is slow
    pyautogui.press('enter',interval=5)
    pyautogui.write(meetingID)
    pyautogui.press('enter',interval=5)
    pyautogui.write(meetingPassword)
    pyautogui.press('enter',interval = 5)

    print("Meeting started for %s minutes"%int(meetingTime/60))

    #Total time of zoom session
    time.sleep(meetingTime) 

    # closing Zoom
    subprocess.Popen("TASKKILL /F /IM Zoom.exe")
    time.sleep(5) 

    #Putting Cursor Back to Previous Position
    pyautogui.moveTo(a,b)
    return

def period_timing():
    #Checking Current subject and remaining time
    FMT = '%H:%M'
    now=datetime.now().strftime(FMT)
    current_time=datetime.strptime(now,FMT)

    # Edit Here
    # Set Your Timing According to Time Table in HH:MM format(24 Hr)
    class_not_started=["00:00","9:58"]

    P1=["10:00","10:50"]
    P2=["11:00","11:50"]
    P3=["12:00","12:50"]
    P4=["14:00","14:50"]
    P5=["15:00","15:50"]

    class_ended=["15:00","23:58"]

    if(current_time> datetime.strptime(class_not_started[0], FMT) and current_time < datetime.strptime(class_not_started[1], FMT)):
        remaining_time=(datetime.strptime(class_not_started[1], FMT)-current_time).total_seconds()
        print("Class Not Started for Today")
        time.sleep(remaining_time)
        return 7,0

    elif(current_time> datetime.strptime(P1[0], FMT) and current_time < datetime.strptime(P1[1], FMT)):
        remaining_time=(datetime.strptime(P1[1], FMT)-current_time).total_seconds()
        return 0,remaining_time

    elif(current_time> datetime.strptime(P2[0], FMT) and current_time < datetime.strptime(P2[1], FMT)):
        remaining_time=(datetime.strptime(P2[1], FMT)-current_time).total_seconds()
        return 1,remaining_time

    elif(current_time> datetime.strptime(P3[0], FMT) and current_time < datetime.strptime(P3[1], FMT)):
        remaining_time=(datetime.strptime(P3[1], FMT)-current_time).total_seconds()
        return 2,remaining_time

    elif(current_time> datetime.strptime(P4[0], FMT) and current_time < datetime.strptime(P4[1], FMT)):
        remaining_time=(datetime.strptime(P4[1], FMT)-current_time).total_seconds()
        return 3,remaining_time

    elif(current_time> datetime.strptime(P5[0], FMT) and current_time < datetime.strptime(P5[1], FMT)):
        remaining_time=(datetime.strptime(P5[1], FMT)-current_time).total_seconds()
        return 4,remaining_time

    elif(current_time> datetime.strptime(class_ended[0], FMT) and current_time < datetime.strptime(class_ended[1], FMT)):
        remaining_time=(datetime.strptime(class_ended[1], FMT)-current_time).total_seconds()
        print("Class Ended for Today")
        time.sleep(remaining_time)
        return 7,0
    
    else: 
        return 7,0

def getID(sub):
    # Edit Here 
    #Sub=[Meeting ID,Password]
    Subs={"DS":["987654321","123456"],
    "CO":["987654321","123456"],
    "NMPS":["987654321","123456"],
    "OS":["987654321","123456"],
    "DMS":["987654321","123456"],
    "CG": ["987654321","123456"],
    "DT":["987654321","123456"],
    "WCS":["987654321","123456"]}    
    return Subs.get(sub,"none")

def getTimeTable(day):
    # Edit Here
    # Day(Mon=0) Subject and time
    D0=['DS','CO','NMPS','OS','DS']
    D1=['OS','DMS','DS','CG','NMPS']
    D2=['DMS','CG','DS','CO','DT']
    D3=['CG','NMPS','CO','DMS','DS']
    D4=['NMPS','OS','DT','OS','WCS']
    Days=[D0,D1,D2,D3,D4]
    return Days[day]   

def getDayOfWeek():
    now = datetime.now()
    return now.weekday()

def getCurrentTime():
    now=datetime.now()
    return now.strftime("%H:%M")
    
def joinMe():
    today=getDayOfWeek()
    todayTimeTable=getTimeTable(today)

    [subIndex,meetingTime]=period_timing()
    if(subIndex==7):
        return 
    currentSubject=todayTimeTable[subIndex]
        
    #Print Day and Subject
    now=datetime.now()
    print("\n"+now.strftime("%A %H:%M - ") + currentSubject)

    [meetingID,meetingPassword]= getID(currentSubject)

    zoomClass(meetingID,meetingPassword,meetingTime)
    return 


print('Hold (Ctrl+c) to exit the program ')
while True:
    today=getDayOfWeek()
    if(today==5 or today==6):
        print("No Class for Today")
        # Sleep for six hour if day is Saturday or Sunday
        time.sleep(3600*6) 
    else:
        joinMe()
        time.sleep(10)

#Author - SANJAY SINGH     
