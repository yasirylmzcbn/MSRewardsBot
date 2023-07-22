from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import random
import os
from dotenv import load_dotenv

load_dotenv('credentials.env')
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
def searchForX(x, slp):
    string = ""
    for i in range(50):
        i = random.randrange(97, 122)
        string+=str(chr(i))
    sb = driver.find_element(By.ID, "sb_form_q")
    sb.clear()
    for j in range(1, x+1):
        try:
            sb=driver.find_element(By.XPATH, "//textarea[@name='q']")
        except:
            sb=driver.find_element(By.XPATH, "//input[@name='q']")
        sb.send_keys(string[j-1:j])
        sb.send_keys(Keys.RETURN)
        sleep(slp)

driver.get('https://bing.com')
searchForX(50, 1)

def various_quests(driver):
    # this or that
    if 'This or That?' in driver.page_source:
        startPlaying = driver.find_element(By.ID, 'rqStartQuiz')
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