from boltiot import Bolt
import requests
import tkinter
import time

HEIGHT = 500
WIDTH = 600
key = "hjkl67890-4567829o3rtv" # REPLACE WITH CORRECT KEY
id = "BOLTXXXX" #REPLACE WITH CORRECT ID

def webhook_trigger():
   URL = "https://hook.integromat.com/" # REPLACE WITH CORRECT URL
   response = requests.request("GET", URL)
   print (response.text)

def ledON():
   r = mybolt.digitalWrite('0', 'HIGH')
   webhook_trigger()
def ledOFF():
   r = mybolt.digitalWrite('0', 'LOW')
   res = mybolt.digitalWrite('1', 'HIGH')
   time.sleep(2)
   res = mybolt.digitalWrite('1','LOW')

mybolt = Bolt(key,id)
root = tkinter.Tk()

canvas = tkinter.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_img = tkinter.PhotoImage(file='head.png')
background_label = tkinter.Label(root, image=background_img)
background_label.place(relwidth=1, relheight=1)

frame = tkinter.Frame(root, bg="#524d42",bd=5)
frame.place(relwidth=0.75, relheight=0.1, relx=0.5, rely=0.6, anchor="n")

button = tkinter.Button(frame, text="YES", bg="#a73562", font=('Courier', 13), command=lambda: ledON())
button.place(relx=0, rely=0, relwidth= 0.3, relheight=1)

button2 = tkinter.Button(frame, text="NO", bg="#a73562", font=('Courier', 13), command=lambda: ledOFF())

button2.place(relx=0.7, rely=0, relwidth= 0.3, relheight=1)

upper_frame = tkinter.Frame(root, bg="#524d42",bd=10)
upper_frame.place(relwidth=0.75, relheight=0.4, relx=0.5, rely=0.1, anchor="n")

label = tkinter.Label(upper_frame,text="HABIT LIGHT\n\nDid you remember to do it?\nYour goal is to keep the light\nlit!!", font=('Courier', 18), anchor='nw',justify="left",bd=4)
label.place(relx=0, rely=0,relwidth=1, relheight=1)

root.mainloop()
