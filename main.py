# Libraries imported
import pyautogui 
import datetime
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

    print("Meeting started for %s minutes"%meetingTime)

    #Total time of zoom session
    time.sleep(meetingTime*60) 

    # closing Zoom
    subprocess.Popen("TASKKILL /F /IM Zoom.exe")
    time.sleep(5) 

    #Putting Cursor Back to Previous Position
    pyautogui.moveTo(a,b)
    return



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
    now = datetime.datetime.now()
    return now.weekday()

def getCurrentTime():
    now=datetime.datetime.now()
    return now.strftime("%H:%M")
    
def joinMe():
    today=getDayOfWeek()
    todayTimeTable=getTimeTable(today)
    # Edit Here
    # Set Your Timing According to Time Table in HH:MM format(24 Hr)
    timing={"10:02":0,"11:02":1,"12:02":2,"14:02":3,"15:02":4}

    subIndex=timing.get(getCurrentTime(),7)
    if(subIndex==7):
        return 
    currentSubject=todayTimeTable[subIndex]
        
    #Print Day and Subject
    now=datetime.datetime.now()
    print("\n"+now.strftime("%A %H:%M - ") + currentSubject)

    [meetingID,meetingPassword]= getID(currentSubject)

    # Edit Here
    # default is 45 Min change total meeting time Accordinly
    meetingTime=45
    zoomClass(meetingID,meetingPassword,meetingTime)
    return 


print('Hold (Ctrl+c) to exit the program ')
while True:
    today=getDayOfWeek()
    if(today==5 or today==6):
        # Edit Here
        # Sleep for hour if day is Saturday or Sunday
        time.sleep(3600) 
    else:
        joinMe()
        time.sleep(10)

#Author - SANJAY SINGH     
