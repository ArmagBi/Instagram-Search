from tkinter import *
from tkinter import filedialog
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, urllib.request
import requests
from tkinter import *
from tkinter import ttk
import time

driver = webdriver.Firefox()

def StartProgress():
    driver.get("https://www.instagram.com/")

    #login
    time.sleep(5)
    username = driver.find_element_by_css_selector("input[name='username']")
    password = driver.find_element_by_css_selector("input[name='password']")
    username.clear()
    password.clear()
    username.send_keys("armagbi")
    password.send_keys("Shiy123456")
    login = driver.find_element_by_css_selector("button[type='submit']").click()

    #save your login info?
    time.sleep(10)
    notnow = driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
    #turn on notif
    time.sleep(5)
    notnow2 = driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

    #searchbox
    time.sleep(2)
    for i in range(0,200):
            progress_var['value'] += 0.5
            stringvar.set(progress_var['value'])
            # get the value
            label.config(text=stringvar.get()+' %')
            # update value
            ws.update_idletasks()
            X = 0
            X += i
            time.sleep(1)
            searchbox = driver.find_element_by_css_selector("input[placeholder='Search']")
            searchbox.clear()
            searchbox.send_keys('e')
            time.sleep(5)
            searchbox.send_keys(Keys.ENTER)
            searchbox.send_keys(X * (Keys.DOWN))
            time.sleep(0.5)
            searchbox.send_keys(Keys.ENTER)
            with open('F:\PycharmProjects\Test\Result.txt', 'a+') as f:
                    print(driver.current_url.replace('https://www.instagram.com/'+'/', ''), file=f)
        
def StopProgress():
    # stop progress
    progress_var.stop()
    driver.close()
    # set zero percent
    stringvar.set('00.0 %')
    label.config(text=stringvar.get())
    ws.destroy()      
  

def saveFile():
    tf = filedialog.asksaveasfile(
        mode='w',

        title ="Save file",
        defaultextension=".txt"
        )
    tf.config(mode='w')

    path.insert(END, tf)
    data = str(txtarea.get(1.0, END))
    tf.write(data)
   
    tf.close()

ws = Tk()
ws.title("Instagram Search")
ws.geometry("400x500")
ws['bg']='#2a636e'

# adding frame
frame = Frame(ws)
frame.pack(pady=20)

# adding scrollbars 
ver_sb = Scrollbar(frame, orient=VERTICAL )
ver_sb.pack(side=RIGHT, fill=BOTH)

hor_sb = Scrollbar(frame, orient=HORIZONTAL)
hor_sb.pack(side=BOTTOM, fill=BOTH)

# adding writing space
txtarea = Text(frame, width=40, height=20)
txtarea.pack(side=LEFT)


# binding scrollbar with text area
txtarea.config(yscrollcommand=ver_sb.set)
ver_sb.config(command=txtarea.yview)

txtarea.config(xscrollcommand=hor_sb.set)
hor_sb.config(command=txtarea.xview)

# adding path progress bar

progress_var=ttk.Progressbar(ws,orient=HORIZONTAL,length=400,mode='determinate')
progress_var.pack(side=BOTTOM, expand=True, fill=X, padx=20)
stringvar=StringVar()
stringvar.set('00.0 %')
label=Label(ws,text=stringvar.get(),font=('',12))

# adding buttons 
Button(
    ws, 
    text="Search", 
    command=StartProgress
    ).pack(side=LEFT, expand=True, fill=X, padx=20)

Button(
    ws, 
    text="Save File", 
    command=saveFile
    ).pack(side=LEFT, expand=True, fill=X, padx=20)

Button(
    ws, 
    text="Exit", 
    command=StopProgress
    ).pack(side=LEFT, expand=True, fill=X, padx=20, pady=20)

ws.mainloop()
