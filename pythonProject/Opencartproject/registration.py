import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.core import driver

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://demo.opencart.com/")
driver.find_element(By.LINK_TEXT,"My Account").click()
driver.find_element(By.LINK_TEXT,"Register").click()
time.sleep(5)
print(driver.title)

driver.find_element(By.ID,"input-firstname").send_keys("vaishu")
driver.find_element(By.ID,"input-lastname").send_keys("kumthekar")
driver.find_element(By.ID,"input-email").send_keys("vk@gmail.com")
driver.find_element(By.ID,"input-password").send_keys("vk")
driver.find_element(By.NAME,"agree").click()
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(5)



