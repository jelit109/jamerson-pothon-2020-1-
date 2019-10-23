import time
import calendar
from tkinter import*
from tkinter import ttk
from tkinter import font 




def current_time():
    totalSeconds = calendar.timegm(time.gmtime())
    currentSecond = totalSeconds%60

    totalMinute = totalSeconds//60
    currentMinute = totalMinute%60

    totalHours = totalMinute//60
    currentHour = (totalHours%24)-6


    am_pm = " "
    if currentHour>=12:
      am_pm+"PM"
    if currentHour==0:
        curentHour=courentHour+12
    else:
        if currentHour==0:
            curentHour=courentHour+12
    

    timex= str(currentHour)+":"+str(currentMinute)+":"+str(currentSecond)+" "+am_pm
    return timex
def show_time():
    time = current_time()
    txt.set(time)
    root.after(100, show_time)
    

root = Tk()
# set window size
root.geometry("500x200")
root.configure(background='Green')

#set up font
root.after(1000,show_time)
fnt= font.Font(family='Helvetica',size=60, weight='bold')
txt = StringVar()
#display timeand set up
ibl=ttk.Label(root, textvariable=txt, font=fnt, foreground="Green",background='Black')
#place the time in the center of the screen
lbl.place(relx=0.5, rely=0.5, anchor= CENTER)

#start main loop
root.mainloop()
