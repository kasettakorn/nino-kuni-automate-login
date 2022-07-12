import os

import bcrypt, pyautogui as gui

salt = b'$2b$12$u0VZrJCZLV3fFwqywWOKVe'

if(not os.path.exists('password.txt')):
    f = open('password.txt', 'w')

    password = gui.password(title='Input password', mask="*")

    password = password.encode('utf-8')
    hashedPassword = bcrypt.hashpw(password, salt)

    f.write(hashedPassword.decode())
    

f = open('password.txt', 'r')
password = str.encode(f.readline())

check = "".encode('utf-8')

if bcrypt.checkpw(check, password):
    print("login success")
else:
    print("incorrect password")
