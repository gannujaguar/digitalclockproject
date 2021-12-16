#creating digital clock using python with Gui

#libraries used in this project
from tkinter import *
import datetime

#creating a fuction for time
def date_time():
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    mi = time.strftime('%M')
    sec = time.strftime('%S')
    am = time.strftime('%p')
    date = time.strftime('%d')
    mon = time.strftime('%m')
    year = time.strftime('%y')
    day= time.strftime('%a')

#configuring the variables

    lab_hr.config(text = hr)
    lab_min.config(text=mi)
    lab_sec.config(text=sec)
    lab_am.config(text=am)
    lab_date.config(text=date)
    lab_mon.config(text=mon)
    lab_yr.config(text=year)
    lab_day.config(text=day)


    lab_hr.after(200,date_time)


#setting the clock graphics

clock = Tk()
clock.title('   ***Digital clock*** ')
clock.geometry("800x400")
clock.config(bg='lightblue')

#labling the parameters

lab_title = Label(clock,text = "Digital Clock",font = ("bold",25),bg ="black", fg = 'white')
lab_title.place(x = 300, y = 10, height = 30, width = 200)

#setting  time

lab_hr = Label(clock,text="00",font =('Time New Roman',50,"bold"),
              bg ='black',fg='white')
lab_hr.place(x=40,y=65,height= 80,width=80)

lab_hr_txt = Label(clock,text="Hour",font =('Time New Roman',25,"bold"),
              bg ='black',fg='white')
lab_hr_txt.place(x=40,y=155,height=40,width=80)


lab_min = Label(clock,text="00",font =('Time New Roman',50,"bold"),
               bg ='black',fg='white')
lab_min.place(x=240,y=65,height= 80,width=80)

lab_min_txt = Label(clock,text="Min.",font =('Time New Roman',25,"bold"),
              bg ='black',fg='white')
lab_min_txt.place(x=240,y=155,height= 40,width=80)
lab_sec = Label(clock,text="00",font =('Time New Roman',50,"bold",),
               bg ='black',fg='white')
lab_sec.place(x=460,y=65,height= 80,width=80)

lab_sec_txt = Label(clock,text="Sec.",font =('Time New Roman',25,"bold"),
              bg ='black',fg='white')
lab_sec_txt.place(x=460,y=155,height= 40,width=80)

lab_am = Label(clock,text="00",font =('Time New Roman',35,"bold"),
               bg ='black',fg='white')
lab_am.place(x=680,y=65,height= 80,width=80)

lab_am_txt = Label(clock,text="AM/PM.",font =('Time New Roman',15,"bold"),
              bg ='black',fg='white')
lab_am_txt.place(x=680,y=155,height= 40,width=80)

#setting date

lab_date = Label(clock,text="00",font =('Time New Roman',50,"bold"),
              bg ='black',fg='white')
lab_date.place(x=40,y=225,height= 80,width=80)

lab_date_txt = Label(clock,text="Date",font =('Time New Roman',25,"bold"),
              bg ='black',fg='white')
lab_date_txt.place(x=40,y=325,height=40,width=80)

lab_mon = Label(clock,text="00",font =('Time New Roman',50,"bold"),
               bg ='black',fg='white')
lab_mon.place(x=240,y=225,height= 80,width=80)

lab_mon_txt = Label(clock,text="Month",font =('Time New Roman',18,"bold"),
              bg ='black',fg='white')
lab_mon_txt.place(x=240,y=325,height= 40,width=80)

lab_yr = Label(clock,text="00",font =('Time New Roman',50,"bold"),
               bg ='black',fg='white')
lab_yr.place(x=460,y=225,height= 80,width=80)

lab_yr_txt = Label(clock,text="Year",font =('Time New Roman',22,"bold"),
              bg ='black',fg='white')
lab_yr_txt.place(x=460,y=325,height= 40,width=80)

lab_day = Label(clock,text="00",font =('Time New Roman',33,"bold"),
               bg ='black',fg='white')
lab_day.place(x=680,y=225,height= 80,width=80)

lab_day_txt = Label(clock,text="Day.",font =('Time New Roman',25,"bold"),
              bg ='black',fg='white')
lab_day_txt.place(x=680,y=325,height= 40,width=80)

date_time()



clock.mainloop()
