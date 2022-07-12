import pyautogui as gui
import os, time, sys, threading
import bcrypt

salt = b'$2b$12$u0VZrJCZLV3fFwqywWOKVe'

if(not os.path.exists('password.txt')):
    f = open('password.txt', 'w')
    

    password = "".encode('utf-8')
    hashedPassword = bcrypt.hashpw(password, salt)

    f.write(hashedPassword.decode())
    

f = open('password.txt', 'r')
password = str.encode(f.readline())

check = "".encode('utf-8')

if bcrypt.checkpw(check, password):
    print("login success")
else:
    print("incorrect password")

class batchThread(threading.Thread):
    def run(self):
        os.system("start " + os.environ["PUBLIC"] + "\\Desktop\\\"Netmarble Launcher\".lnk")

        pass

if(open('password.txt', 'r+')):
    print('yes')
else:
    print('no')

thread = batchThread()
thread.daemon = True
thread.start()

time.sleep(5)
print(1)
gui.moveTo(1579,929)
time.sleep(5)
gui.leftClick()
time.sleep(13)
gui.leftClick()
gui.moveTo(951,517)
gui.leftClick()


gui.write("", interval=0.1)
gui.moveTo(1055, 812)
gui.leftClick()
gui.moveTo(1055, 712)
time.sleep(3)
gui.leftClick()

while(True):
    if os.system("TASKLIST | FINDSTR /I \"CrossWorlds.exe\"") != 0:
        print("EXIT")
        exit()
   
        
