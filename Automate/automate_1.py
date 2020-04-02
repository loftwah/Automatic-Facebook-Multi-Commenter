import random
import string
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random

driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe') #add your chromedrive's path in: executable_path=r'your path'


def login(link, email, password):
    driver.get(link)
    sleep(2)
    email_in = driver.find_element_by_xpath('//*[@id="email"]')
    email_in.send_keys(email)
    pass_in = driver.find_element_by_xpath('//*[@id="pass"]')
    pass_in.send_keys(password)
    log_in = driver.find_element_by_xpath('//*[@id="loginbutton"]')
    log_in.click()
    sleep(2)


def comm(modLink):
    abc = driver.get(modLink)


def only_comment(abc):
    ins = driver.find_element_by_id('composerInput')
    sleep(8)
    ins.send_keys(abc)
    sleep(2)
    driver.find_element_by_name("submit").send_keys(Keys.RETURN)


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def niceWords():
    words = ["You are Beautiful", "You are so Cute", "You are Hot!", "You are Sexy", "You are Amazing", "You are Creative", "You are Dazzling", "You are Encouraging", "You are Enchanting", "You are fabulous", "You are Glamorous"
             , "You are Spiritual", "You are Simple and I love it", "You are Powerful", "You are Positive", "You are Motivating", "You have a damn Personality!"]
    num = random.randrange(0, len(words))
    return words[num]


count = 0
print("Please Enter The Post Link. To Find The Post Link Go To The Post > Click On The Post's Time Stamp > Copy the URL > Paste Here.....  ")
link = input("After Pasting Hit SPACEBAR and Than ENTER: ")
link = link.strip()
print("Please Remove any 2 way security authentications for this Program to Work: ")
email = input("Now Please Enter Your Facebook Email Address:  ")
email = email.strip()
password = input("Now Please Enter Your Facebook Password (Warning: Password Input Is Visible in Console):  ")
password = password.strip()
modLink = link[12:]
modLink = "https://m." + modLink
print("What Type of Comments You Want To Make?")
print("Press 1 and Enter For Sweet Comments!")
print("Press 2 and Enter For Random Character Word Comments!")
choice = input().strip()
print("How many Comments you want to Make?")
maxNo = int(input())
if choice == str(1):
    login(link, email, password)
    comm(modLink)
    for i in range (1, maxNo+1):
        only_comment(niceWords())
        count = i
    print("Done Commenting! Commented " + str(i) + " Times")

if choice == str(2):
    login(link, email, password)
    comm(modLink)
    for i in range(1, maxNo + 1):
        only_comment(randomString())
        count = i
    print("Done Commenting! Commented " + str(i) + " Times")

print("_____________________________________________________________________________________________________")
print()
print("Developed by Swakhar Poddar, UBC B.Sc, Computer Science")