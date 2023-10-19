from tkinter import *
import datetime
import time
from pygame import mixer
from tkinter import messagebox

root = Tk()
root.title("Alarm Clock")
root.geometry("360x520")
root.configure(bg='lightyellow')
Alarmtime = StringVar()

head = Label(root, text="Alarm Clock", font=('comic sans', 20,),fg='blue', bg='Yellow')
head.grid(row=0, columnspan=3,pady=10,padx=50)

mixer.init()

def Alm():
    A = Alarmtime.get()
    AlarmT = A
    CurrentTime = time.strftime("%H:%M:%S")

    while AlarmT != CurrentTime:  
        CurrentTime = time.strftime("%H:%M:%S")
    if AlarmT == CurrentTime:
        mixer.music.load("C:\\Users\\vsanj\\OneDrive\\Download\\Program\\Python\\Gui Clock\\music.mp3")
        mixer.music.play()
        msg = messagebox.showinfo('Remainder', f'{MsgInput.get()}')  
        if msg == 'ok':
            mixer.music.stop()

ClockImg = PhotoImage(file="C:\\Users\\vsanj\\OneDrive\\Download\\Program\\Python\\Gui Clock\\c.png")
Img = Label(root, image=ClockImg)
Img.grid(row=2, columnspan=4,pady=5,padx=50)

Inputtime = Label(root, text="Set Time", font=('comic sans', 18),fg='blue', bg='yellow')
Inputtime.grid(row=3, column=1,pady=5,padx=50)

Almtime = Entry(root, textvariable=Alarmtime, font=('comic sans', 18))
Almtime.grid(row=4, column=1,pady=5,padx=50)

Msg = Label(root, text= "Message", font=('comic sans', 18),fg='blue', bg='yellow')
Msg.grid(row=5, column=1, columnspan=2,pady=5,padx=50)

MsgInput = Entry(root, textvariable="Msg", font=('comic sans', 18))  
MsgInput.grid(row=6, column=1, columnspan=2,pady=5,padx=50)

Submit = Button(root, text="Set", font=('comic sans', 20),fg='blue', bg='yellow', command=Alm)  
Submit.grid(row=7, column=1, columnspan=2,pady=5,padx=50)

root.mainloop()
