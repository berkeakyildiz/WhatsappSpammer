import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome('C:\\Users\\berke\\chromedriver_89\\chromedriver')

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 6000)

print("Enter recipient: ")
target = input()
target = "'" + target + "'"

print("Enter message: ")
message = input()

x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(expected_conditions.presence_of_element_located((By.XPATH, x_arg)))
group_title.click()
inp_xpath = '//div[@class="_2_1wd copyable-text selectable-text"][@contenteditable="true"][@data-tab="6"]'
input_box = wait.until(expected_conditions.presence_of_element_located((By.XPATH, inp_xpath)))
for i in range(1):
    input_box.send_keys(message + Keys.ENTER)
    time.sleep(1)
