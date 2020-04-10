from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://instagram.com')

time.sleep(2)

username_field = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
username_field.send_keys('# Your username')

password_field = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
password_field.send_keys('# your password')

time.sleep(1)

login_btn = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button')
login_btn.click()
