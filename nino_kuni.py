import pyautogui as gui
import os, time, threading

from file import getPassword

class batchThread(threading.Thread):
    def run(self):
        os.system("start " + os.environ["PUBLIC"] + "\\Desktop\\\"Netmarble Launcher\".lnk")
        pass


password = getPassword()

thread = batchThread()
thread.daemon = True
thread.start()

while(True):
    if os.system("TASKLIST | FINDSTR /I \"Netmarble Launcher.exe\"") == 0:
        break
    
time.sleep(1)
gui.moveTo(1579,929)
gui.leftClick()
while(True):
    if os.system("TASKLIST | FINDSTR /I \"UnrealCEFSubProcess.exe\"") == 0:
        break
time.sleep(5)
gui.leftClick()
gui.moveTo(951,512)
gui.leftClick()


gui.write(password, interval=0.05)
gui.moveTo(1055, 812)
gui.leftClick()
gui.moveTo(1055, 612)
time.sleep(3)
gui.leftClick()


while(True):
    if os.system("TASKLIST | FINDSTR /I \"CrossWorlds.exe\"") != 0:
        print("EXIT")
        exit()

        
