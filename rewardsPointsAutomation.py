# import time
# import os
# import platform
# import random
# from traceback import print_tb
# from selenium import webdriver
# from selenium.webdriver import Edge
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.edge.options import Options
# from selenium.webdriver.edge.service import Service
# import tkinter as tk
# from tkinter import *
# from PIL import ImageTk, Image
# from functools import partial
# from urllib3 import ProxyManager


# root = tk.Tk()  
# root.title('Microsoft Rewards Bot')
# # icon = PhotoImage(file = 'mslogo.png')
# # root.iconphoto(True, icon)
# root.geometry("370x180")
# root.config(bg='#1156a5')


# def submit(name, passw): 
#     print(name.get(), passw.get())
#     if(len(name.get()) == 0 ):
#         name.set('username')
#     if(len(passw.get()) == 0):
#         passw.set('')
#     print(name.get())
#     print(passw.get())
#     root.destroy()
    
     

# name_label = tk.Label(root, text = 'Email', font=('calibre',10, 'bold'))
# name = StringVar()
# name_entry = tk.Entry(root, textvariable = name, font=('calibre',10,'normal'), width=30)

# passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'bold'))
# passw = StringVar()
# passw_entry = tk.Entry(root, textvariable = passw, font = ('calibre',10,'normal'), show = '*', width=30)

# default = tk.Button(root, text = "Click this if you want to use the test account instead", command = defEmail)

# submit = partial(submit, name, passw)

# sub_btn = tk.Button(root, text = 'Start Bot', command = submit)
# root.bind('<Return>', lambda event=None: sub_btn.invoke())

# name_label.config(bg='#1156a5')
# passw_label.config(bg='#1156a5')
# sub_btn.config(bg='black', fg='white')
# default.config(bg='black', fg='white')

# name_label.grid(row=0,column=0)
# name_entry.grid(row=0,column=1)
# passw_label.grid(row=1,column=0)
# passw_entry.grid(row=1,column=1)
# sub_btn.grid(row=2,column=1)
# default.grid(row=4,column=1)

# root.mainloop()

# askq = input ("If you would like to use your own email, press enter. If you would like to use the default email account, type 'default'.\n")
# if(askq == 'default'):
#     user_email = 'csistestingacc2@outlook.com'
#     user_pw = 'compsci123'
# else:
#     user_email = input("Enter email: ")
#     user_pw = input("Enter password: ")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import random
import os
from dotenv import load_dotenv

load_dotenv('selenium_folder\\credentials.env')
email = os.getenv('USER')
password = os.getenv('PASS')

driver = webdriver.Edge()
driver.get('https://rewards.bing.com/?refd=www.microsoft.com&redref=amc')

email_entry = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='email']")))
email_entry.send_keys(email, Keys.RETURN)

password_entry = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='password']")))
password_entry.send_keys(password)

submit_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='submit']")))
submit_button.click()

forget_signin_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='idBtn_Back']")))
forget_signin_button.click()

# search method
def searchForX(x):
    string = ""
    for i in range(x):
        i = random.randrange(97, 122)
        string+=str(chr(i))
    sb = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.ID, "sb_form_q")))
    sb.clear()
    try:
        signin_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Sign in')]")))
        signin_button.click()
    except Exception as e:
        # print(e)
        print('no need to click sign in')
    for j in range(1, x+1):
        try:
            sb=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, "//textarea[@name='q']")))
        except:
            sb=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, "//input[@name='q']")))
        sb.send_keys(string[j-1:j])
        sb.send_keys(Keys.RETURN)

driver.get('https://bing.com')
searchForX(35)


def various_quests(driver):
    # this or that
    if 'This or That?' in driver.page_source:
        startPlaying = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'rqStartQuiz')))
        startPlaying.click()
        for option in range(10):
            answer = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'rqAnswerOption0')))
            answer.click()
    
    # bing news quiz (10 questions)
    if 'Bing news quiz' in driver.page_source:
        for option in range(10):
            answer = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, f'questionOptionChoice{option}0')))
            answer.click()
            try:
                sleep(0.5)
                nextq = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, f'nextQuestionbtn{option}')))
                nextq.click()
            except:
                print('exception')
                nextq = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f"//input[@name='submit']")))
                nextq.click()
                
    # bing homepage quiz (3 questions)
    if 'Bing homepage quiz' in driver.page_source:
        for option in range(3):
            answer = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, f'questionOptionChoice{option}0')))
            answer.click()
            try:
                sleep(0.5)
                nextq = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, f'nextQuestionbtn{option}')))
                nextq.click()
            except:
                print('exception')
                nextq = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f"//input[@name='submit']")))
                nextq.click()
                
    # warpspeed or supersonic quiz
    if 'Welcome to your Microsoft Rewards quiz' in driver.page_source:
        startPlaying = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'rqStartQuiz')))
        startPlaying.click()
        
        firstOption = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'rqAnswerOption0')))
        
        try:
            for question in range(5):
                if firstOption == WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'rqAnswerOption0'))):
                    for option in range(8):
                        try:
                            answer = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, f'rqAnswerOption{option}')))
                            answer.click()
                        except:
                            continue
                else:
                    firstOption = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'rqAnswerOption0')))
        except:
            print('quiz over')    
    
driver.get('https://rewards.microsoft.com/')
# learn how to use driver.find_elements() to get all the links that contain the word 'points >'
# get the elements using PARTIAL_LINK_TEXT, like in the example below
points_links = driver.find_elements(By.PARTIAL_LINK_TEXT, 'points >') 

index = 0
for i in points_links:
    driver.switch_to.window(driver.window_handles[0])
    i.click()
    driver.switch_to.window(driver.window_handles[index+1])
    
    try:
        signin_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Sign in')]")))
        signin_button.click()
    except Exception as e:
        # print(e)
        print('no need to click sign in')
    
    if index == 0:
        print('waiting')
        sleep(5)
        
    elif index == 2:
        pollOption = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "btoption0")))
        pollOption.click() 
        driver.implicitly_wait(5)
    
    else:
        driver.implicitly_wait(5)
        various_quests(driver)
        driver.implicitly_wait(5)
    
    index += 1
    
print('loop over')
    

input()