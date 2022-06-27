from sys import implementation
import time
import os
import platform
import random
from traceback import print_tb
from selenium import webdriver
from selenium.webdriver import Edge
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from functools import partial
from urllib3 import ProxyManager
 
cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))
 
# search method
def searchForX(string, x, slp):
    sb = driver.find_element(By.ID, "sb_form_q")
    sb.clear()
    for j in range(1, x+1):
        sb=driver.find_element(By.XPATH, "//input[@name='q']")
        sb.send_keys(string[j-1:j])
        sb.send_keys(Keys.RETURN)
        time.sleep(slp)
 
def defEmail():
    name.set('defaultemail@outlook.com')
    passw.set('default password')
    root.destroy()
 
root = tk.Tk()  
root.title('Microsoft Rewards Bot')
icon = PhotoImage(file = 'mslogo.png')
# root.iconphoto(True, icon)
root.geometry("370x180")
root.config(bg='#1156a5')
 
def submit(name, passw):
    if(len(name.get()) == 0 ):
        name.set('your original microsoft email here')
    if(len(passw.get()) == 0):
        passw.set('password')
    print(name.get())
    print(passw.get())
    root.destroy()
     
name_label = tk.Label(root, text = 'Email', font=('calibre',10, 'bold'))
name = StringVar()
name_entry = tk.Entry(root,textvariable = name, font=('calibre',10,'normal'), width=30)
 
passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'bold'))
passw = StringVar()
passw_entry = tk.Entry(root, textvariable = passw, font = ('calibre',10,'normal'), show = '*', width=30)
 
default = tk.Button(root, text = "Click this if you want to use the test account instead", command = defEmail)
 
submit = partial(submit, name, passw)
 
sub_btn = tk.Button(root, text = 'Start Bot', command = submit)
root.bind('<Return>', lambda event=None: sub_btn.invoke())
 
name_label.config(bg='#1156a5')
passw_label.config(bg='#1156a5')
sub_btn.config(bg='black', fg='white')
default.config(bg='black', fg='white')
 
name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
passw_label.grid(row=1,column=0)
passw_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)
default.grid(row=4,column=1)
 
root.mainloop()
time.sleep(2)

for i in range(2):
    driver = webdriver.Edge()
    driver.get("https://bing.com")
    time.sleep(5)
    
     # you could do more than 2 in theory but you could possibly get ip banned
    if i != 0:
        name.set("secondary email to get more points (optional)")
        passw.set("password 2")
    
    # log out if personal account is logged in
    try:
        # signout = driver.find_element(By.LINK_TEXT, "Yasir").click()
        signout = driver.find_element(By.XPATH, ("//img[@id='id_p']")).click()
        time.sleep(3)
        signout = driver.find_element(By.XPATH, "//span[text()=\"Sign out\"]").click()
        time.sleep(3)
        print("signed out")
    except:
        try:
            time.sleep(5)
            print('no need to log out')
            driver.find_element(By.ID, "id_a").click()
        except:
            print('not necessary to click log out')
    
    # login
    driver.implicitly_wait(2)
    signin = driver.find_element(By.ID, "id_a").click()
    driver.implicitly_wait(2)
    email=driver.find_element(By.XPATH, "//input[@name='loginfmt']")
    email.send_keys(name.get())
    email.send_keys(Keys.RETURN)
    time.sleep(5)
    pw=driver.find_element(By.XPATH, "//input[@name='passwd']")
    pw.send_keys(passw.get())
    time.sleep(1)
    signin=driver.find_element(By.XPATH, "//*[@id='idSIButton9']").click()
    time.sleep(2)
    try:
        signin=driver.find_element(By.XPATH, "//*[@id='idSIButton9']").click()
    except:
        time.sleep(1)
    
    time.sleep(5)
    sbb = driver.find_element(By.XPATH, "//input[@name='q']")
    sbb.send_keys("first search to click sign in")
    sbb.send_keys(Keys.RETURN)
    time.sleep(4)
    string = ''
    for i in range(50):
        i = random.randrange(97, 122)
        string+=str(chr(i))
    try:
        signin=driver.find_element(By.XPATH, "//input[@id='id_a']").click()
        time.sleep(6)
    except:
        print("no need to click sign in")
    
    time.sleep(4)
    
    # do the 50 searches for 250 points
    searchForX(string, 50, 1)

    # open the tabs for the 3 daily tasks
    driver.get("https://rewards.microsoft.com/")
    time.sleep(1)
    try:
        driver.find_element(By.PARTIAL_LINK_TEXT,"SIGN IN").click()
    except:
        print("no need to click sign in")
    tasks = driver.find_elements(By.PARTIAL_LINK_TEXT, "points")
    numTabs = 0
    for task in tasks:
        task.click()
        time.sleep(2)
        numTabs+=1
        if(numTabs==3):
            break
    
    time.sleep(2)
    
    # task 1 is always completed by simply clicking on the link so no extra code is necessary
    driver.switch_to.window(driver.window_handles[3])
    time.sleep(10)

    # task 2
    driver.switch_to.window(driver.window_handles[2])
    theTask = driver.find_element(By.ID, 'sb_form_q').get_attribute("value")
    if "quiz" in theTask:
        try:
            for questionNumber in range(0,10):
                # it doesn't matter if the answer is wrong, amount of points awarded is always the same
                driver.find_element(By.ID,"ChoiceText_"+str(questionNumber)+"_1").click()
                time.sleep(3)
                if(questionNumber != 9):
                    driver.find_element(By.XPATH, "//input[@value='Next question']").click()
                    time.sleep(1)
                else:
                    driver.find_element(By.XPATH, "//input[@value='Get your score']").click()
        except:
            print("this quiz has already been completed")
    time.sleep(2)
    try:
        driver.find_element(By.ID, "rqStartQuiz").click()
        time.sleep(1)
        driver.find_element(By.ID, "rqAnswerOption0").click()
        time.sleep(3)
        if driver.find_element(By.ID, "rqAnswerOption0").get_attribute("tabindex") == "-1":
            try:
                for quizQuestion in range(0,5):
                    try:
                        driver.find_element(By.ID, "rqAnswerOption0").click()
                        driver.find_element(By.ID, "rqAnswerOption0").click()
                        time.sleep(3)
                    except:
                        print("broken")
                        break
                    for quizQuestionAnswer in range(1,10):
                        time.sleep(4)
                        try:
                            driver.find_element(By.ID, "rqAnswerOption"+str(quizQuestionAnswer)).click()
                        except:
                            break
                    print("next question")    
                    time.sleep(2)          
            except:
                print("no quiz")
    except:
        try:
            for k in range(3):
                for j in range(5):
                    firstTime = True
                    # if(firstTime == False):
                    #     driver.find_element(By.ID, "rqAnswerOption"+str(i)).click()
                    if(firstTime == True):
                        driver.find_element(By.ID, "rqAnswerOption0").click()
                        firstTime = False
                    for i in range(1, 8):
                        print("rqAnswerOption"+str(i))
                        driver.find_element(By.ID, "rqAnswerOption"+str(i)).click()
                        time.sleep(4)
                        firstTime = False
                        time.sleep(2)
        except:
            print("end of supersonic")
        print("quiz is over/not there")
    try:
        for i in range(10):
            driver.find_element(By.ID, "rqAnswerOption0").click()
            time.sleep(6)
    except:
        print('no this or that quiz found')
        
    # task 3
    driver.switch_to.window(driver.window_handles[1])
    # theTask = driver.find_element(By.ID, 'sb_form_q').get_attribute("value")
    time.sleep(3)
    
    try:
        driver.find_element(By.ID, "rqStartQuiz").click()
        print("invalid poll option/there is no poll")
        try:
            time.sleep(1.5)
            driver.find_element(By.ID, "rqAnswerOption1").click()
            time.sleep(1.5)
            if driver.find_element(By.ID, "rqAnswerOption1").get_attribute("tabindex") == "-1":
                driver.find_element(By.ID, "rqAnswerOption0").click()
        except:
            print('no guessing game')
    except:
        try:
            driver.find_element(By.ID, "btoption0").click()
        except:
            print('tab 3 done')
    
    time.sleep(5)
    driver.quit()