import time
import os
import platform
import random
from traceback import print_tb
from selenium import webdriver
from selenium.webdriver import Edge
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
import tkinter as tk
from tkinter import *
from tkinter import simpledialog, messagebox
from PIL import ImageTk, Image
from functools import partial

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))

# search method
def searchForX(string, x, slp):
    sb = driver.find_element_by_id("sb_form_q")
    sb.clear()
    for j in range(1, x+1):
        sb=driver.find_element_by_xpath("//input[@name='q']")
        sb.send_keys(string[j-1:j])
        # sb.send_keys("Ayseye asigim")
        sb.send_keys(Keys.RETURN)
        time.sleep(slp)

def defEmail():
    name.set('csistestingacc6@outlook.com')
    passw.set('compsci123')
    root.destroy()

root = tk.Tk()  
root.title('Microsoft Rewards Bot')
icon = PhotoImage(file = 'mslogo.png')
root.iconphoto(True, icon)
root.geometry("370x180")
root.config(bg='#1156a5')


def submit(name, passw): 
    if(len(name.get()) == 0 ):
        name.set('bonersalad69@outlook.com')
    if(len(passw.get()) == 0):
        passw.set('areyoumal1')
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
# time.sleep(2)

# csistestingacc@outlook.com
# compsci123

# askq = input ("If you would like to use your own email, press enter. If you would like to use the default email account, type 'default'.\n")
# if(askq == 'default'):
#     user_email = 'csistestingacc2@outlook.com'
#     user_pw = 'compsci123'
# else:
#     user_email = input("Enter email: ")
#     user_pw = input("Enter password: ")

driver=webdriver.Edge('msedgedriver.exe')
driver.maximize_window()
driver.get("https://bing.com")
time.sleep(5)

# log out if my personal account is logged in
try:
    signout = driver.find_element_by_link_text("Yasir").click()
    time.sleep(2)
    signout = driver.find_element_by_xpath("//span[text()=\"Sign out\"]").click()
    time.sleep(3)
except:
    print('no need to log out')
    driver.find_element_by_id("id_a").click()

# login
driver.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1610213540&rver=6.7.6631.0&wp=MBI_SSL&wreply=https%3a%2f%2fwww.bing.com%2fsecure%2fPassport.aspx%3frequrl%3dhttps%253a%252f%252fwww.bing.com%252f%253ftoWww%253d1%2526redig%253dE7D1934D54C441089EA720081A2C7EAB%2526wlsso%253d1%2526wlexpsignin%253d1%26sig%3d1EDFA8270D8760490948A79D0CEE61A2&lc=1033&id=264960&CSRFToken=25fb211b-ebd0-42e0-a0fc-cf081ffd526f&aadredir=1")
# user_email = 'bonersalad69@outlook.com'
# user_pw = 'areyoumal1'
email=driver.find_element_by_xpath("//input[@name='loginfmt']")
email.send_keys(name.get())
email.send_keys(Keys.RETURN)
time.sleep(1)
pw=driver.find_element_by_xpath("//input[@name='passwd']")
pw.send_keys(passw.get())
time.sleep(1)
signin=driver.find_element_by_xpath("//*[@id='idSIButton9']").click()
time.sleep(2)
try:
    signin=driver.find_element_by_xpath("//*[@id='idSIButton9']").click()
except:
    time.sleep(1)
    time.sleep(1)
# do the 52 searches for 260 points
sbb = driver.find_element_by_xpath("//input[@name='q']")
sbb.send_keys("first search to click sign in")
sbb.send_keys(Keys.RETURN)
time.sleep(4)
string = ''
for i in range(50):
    i = random.randrange(97, 122)
    string+=str(chr(i))
try:
    signin=driver.find_element_by_xpath("//input[@id='id_a']").click()
    time.sleep(6)
except:
    print("no need to click sign in")

# time.sleep(4)
searchForX(string, 50, 1) # edge

# open the tabs for the 3 daily tasks
driver.get("https://account.microsoft.com/rewards/?refd=www.microsoft.com")
time.sleep(1)
try:
    driver.find_element_by_partial_link_text("SIGN IN").click()
except:
    print("no need to click sign in")
tasks = driver.find_elements_by_partial_link_text("points")
numTabs = 0
for task in tasks:
    task.click()
    time.sleep(2)
    numTabs+=1
    if(numTabs==3):
        break

# task 1 is always completed by simply clicking on the link so no extra code is necessary

# task 2
driver.switch_to.window(driver.window_handles[2])
theTask = driver.find_element_by_id('sb_form_q').get_attribute("value")
if "quiz" in theTask:
    try:
        for questionNumber in range(0,10):
            # it doesn't matter if the answer is wrong, amount of points awarded is always the same
            driver.find_element_by_id("ChoiceText_"+str(questionNumber)+"_1").click()
            time.sleep(3)
            if(questionNumber != 9):
                driver.find_element_by_xpath("//input[@value='Next question']").click()
                time.sleep(1)
            else:
                driver.find_element_by_xpath("//input[@value='Get your score']").click()
    except:
        print("this quiz has already been completed")
time.sleep(2)
try:
    driver.find_element_by_id("rqStartQuiz").click()
    time.sleep(1)
    driver.find_element_by_id("rqAnswerOption0").click()
    time.sleep(3)
    if driver.find_element_by_id("rqAnswerOption0").get_attribute("tabindex") == "-1":
        try:
            for quizQuestion in range(0,5):
                try:
                    driver.find_element_by_id("rqAnswerOption0").click()
                except:
                    print("broken")
                    break
                for quizQuestionAnswer in range(1,10):
                    time.sleep(4)
                    try:
                        driver.find_element_by_id("rqAnswerOption"+str(quizQuestionAnswer)).click()
                    except:
                        break
                print("next question")     
                time.sleep(2)           
        except: 
            print("no quiz")
except:
    try:
        firstTime = True
        for j in range(5):
            if(firstTime == False):
                driver.find_element_by_id("rqAnswerOption"+str(i)).click()
            for i in range(1, 8):
                print("rqAnswerOption"+str(i))
                driver.find_element_by_id("rqAnswerOption"+str(i)).click()
                time.sleep(4)
                firstTime = False
    except:
        print("end of supersonic")
    print("quiz is over/not there")
try:
    for i in range(10):
        driver.find_element_by_id("rqAnswerOption0").click()
        time.sleep(6)
except:
    print('no this or that quiz found')
# task 3
driver.switch_to.window(driver.window_handles[1])
# theTask = driver.find_element_by_id('sb_form_q').get_attribute("value")
time.sleep(3)

try:
    driver.find_element_by_id("rqStartQuiz").click()
    print("invalid poll option/there is no poll")
    try:
        time.sleep(1.5)
        driver.find_element_by_id("rqAnswerOption1").click()
        time.sleep(1.5)
        if driver.find_element_by_id("rqAnswerOption1").get_attribute("tabindex") == "-1":
            driver.find_element_by_id("rqAnswerOption0").click()
    except:
        print('no guessing game')
except:
    try:
        driver.find_element_by_id("btoption0").click()
    except:
        print('tab 3 done')


time.sleep(5)
driver.quit()