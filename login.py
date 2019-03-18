from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By as b
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=AddSession")
email_ele = driver.find_element(b.ID,"identifierId")
email_ele.send_keys("ENTER YOUR MAIL_ID")
next_but1= driver.find_element(b.ID,"identifierNext")
next_but1.click()
time.sleep(2)
pass_ele = driver.find_element(b.NAME,"password")
pass_ele.send_keys("ENTER YOUR PASSWORD")
pass_next = driver.find_element(b.ID,"passwordNext")
pass_next.click()
