from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

service = ChromeService(executable_path=ChromeDriverManager().install())

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors-spki-list')

driver = webdriver.Chrome(service=service, options=options)
#driver.implicitly_wait(30)

driver.get('https://www.youtube.com')

searchbox = driver.find_element(By.XPATH, '//input[@id="search"]')
sleep(1)

searchbox.send_keys('natalia qa')
sleep(1)

searchButton = driver.find_element(By.XPATH, '//*[@id="search-icon-legacy"]')
searchButton.click()
sleep(10)

driver.quit()