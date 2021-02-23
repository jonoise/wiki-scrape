from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DRIVER_PATH = "" # insert here your chromedriver path 

driver = webdriver.Chrome(DRIVER_PATH)
driver.get("https://wikipedia.org")

try:
    searchbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'searchInput'))
    )
    searchbox.clear()
    searchbox.send_keys('samurai', Keys.ENTER)
    content =  WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, 'p'))
    )
    count = 1
    with open('Samurais.txt', 'w', encoding="utf8") as file:
        count += 1
        file.write("\n".join([p.text for p in content]))


finally:
    driver.close()
