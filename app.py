from selenium import webdriver
import time
import requests
import sys
from PIL import Image

# input of user details
reg_no = input("Enter your SLCM username:{}".format("  "))
passwd = input("Enter your SLCM Password:{}".format("  "))
print("\nfetching captcha please wait...")

# Fetching captcha
options = webdriver.ChromeOptions()
options.headless = True
# /home/aryaman/Downloads/chromedriver
browser = webdriver.Chrome( options=options)
browser.get('https://slcm.manipal.edu/')
captcha = browser.find_element_by_id('imgCaptcha')
captcha.screenshot('captcha.png')
time.sleep(2)
img = Image.open('captcha.png')
img.show()

# User inputs the capcha
captcha_txt = input('Enter text shown in image\n')
print("\n\nthis might take a few moments.")
img.close()

# automating filling of login form
try:
    browser.find_element_by_id('txtUserid').send_keys(reg_no)
    browser.find_element_by_id('txtpassword').send_keys(passwd)
    browser.find_element_by_id('txtCaptcha').send_keys(captcha_txt)
    browser.find_element_by_id('btnLogin').click()
 

    time.sleep(2)
    
    # getting attendance-info
    browser.get("https://slcm.manipal.edu/Academics.aspx")

    browser.find_element_by_xpath('/html/body/div[3]/form/div[5]/div/div/div/div[1]/div[2]/ul/li[4]/a').click()
    time.sleep(2)
    browser.find_element_by_xpath('/html/body/div[3]/form/div[5]/div/div/div/div[2]/div[3]/div/div/div[1]/div[2]/a').click()
    time.sleep(2)
    tables = browser.find_elements_by_css_selector('#tblAttendancePercentage tbody td')
except:
    print("\n \nError ocurred. This is probably due to invalid login details or incorrect captcha. Please restart app")
    sys.exit()

# printing attendance details 
c = -1
print("\n\nATTENDANCE:\n\n")

for x in tables:

    c = (c+1) % 8
    if(c == 2):
        print("SUB: ", x.text)
    if(c == 7):
        print(x.text, "%")
        print("____________________________________________________")
    else:
        if(c == 4):
            print("total: ", x.text)
        elif(c == 5):
            print("present: ", x.text)
        elif(c == 6):
            print("absent: ", x.text)
        else:
            pass


