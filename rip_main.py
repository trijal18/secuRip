#sending fake/random entries
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 
import time
import pandas as pd
import random

driver_path=r"path to driver" #driver path
site=r"https://securit.club/join" #address of securit form

students=pd.read_csv(r"D:\projects\secuRIP\fake_students2.csv") #reading csv

def send_entry(df):
    driver = webdriver.Chrome(service=Service(driver_path)) 
    driver.get(site) 
    time.sleep(1)

    name=driver.find_element(By.XPATH,"/html/body/div[3]/div/div[1]/div/div/div/form/div[1]/input")
    name.send_keys(str(df["Name"]))

    time.sleep(1)

    usn=driver.find_element(By.XPATH,"/html/body/div[3]/div/div[1]/div/div/div/form/div[2]/input")
    usn.send_keys(str(df["Usn"]))

    time.sleep(1)

    mail=driver.find_element(By.XPATH,"/html/body/div[3]/div/div[1]/div/div/div/form/div[3]/input")
    mail.send_keys(str(df["mail"]))
    
    time.sleep(1)

    phone=driver.find_element(By.XPATH,"/html/body/div[3]/div/div[1]/div/div/div/form/div[4]/input")
    phone.send_keys(str(df["mobile"]))

    time.sleep(1)

    terms=driver.find_element(By.XPATH,"/html/body/div[3]/div/div[1]/div/div/div/form/div[5]/label")
    terms.click()

    time.sleep(1)

    submit=driver.find_element(By.XPATH,"//html/body/div[3]/div/div[1]/div/div/div/form/div[6]/input")
    submit.click()

    time.sleep(5)
 """
 #sending entry
try:
    send_entry(students.iloc[21])
except:
    print("sndj")"""

#sending multiple entries
for i in range(300):
    t=random.randint(15,90) #for random time delay
    print(f"Next entry in {t} mins")
    time.sleep(t*60)
    try:
        send_entry(students.iloc[i])
        print("entry successful")

    except:
        print("entry failed")

    finally:
        print(f"{i}/300")
