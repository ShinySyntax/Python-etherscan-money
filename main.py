from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import re

def get_amount(driver, address):
    try:
        search = driver.find_element(by=By.NAME, value="q")
        search.send_keys(address)
        search.send_keys(Keys.ENTER)

        parent_amount = driver.find_element(by=By.ID, value="ContentPlaceHolder1_divSummary")
        second_child = parent_amount.find_elements(By.XPATH, "*[2]/*[1]/*[1]/*[1]/*[3]")
    
        money_amount = re.search(r"\$[\d,]+\.\d{2}", second_child[0].text)

        with open('output.txt', 'a') as file:
            file.write(money_amount.group() + "\n")

    except Exception as error:
        print(error)

if __name__ == "__main__":
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    url = 'https://etherscan.io'
    with open('input.txt', 'r') as file:
        addresses = file.readlines()
        for address in addresses:
            driver.get(url)
            get_amount(driver, address.replace('\n', ''))
        
        file.close()
