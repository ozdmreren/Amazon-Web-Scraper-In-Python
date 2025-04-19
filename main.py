import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By


def getDriver():
    driver = webdriver.Chrome(
        webdriver.ChromeOptions(),
        webdriver.ChromeService("C:\\Users\\CANAVAR\\Desktop\\chromedriver.exe"))
    
    return driver

URL = "https://www.amazon.com.tr"

driver = getDriver()

response = driver.get(URL)

driver.maximize_window()

time.sleep(1)

cookie_message_decline_xpath = '//*[@id="sp-cc-rejectall-link"]'
cookie_decline_button = driver.find_element(By.XPATH,cookie_message_decline_xpath)
cookie_decline_button.click()

time.sleep(1)

input_xpath = '//*[@id="twotabsearchtextbox"]'
inputbox = driver.find_element(By.XPATH,input_xpath)
inputbox.send_keys("Mekanik klavyeler")
inputbox.submit()

time.sleep(3)

keyboards_selector = '.sg-col-4-of-24.sg-col-4-of-12.s-result-item.s-asin.sg-col-4-of-16.AdHolder.sg-col.s-widget-spacing-small.sg-col-4-of-20'

scroll_height = driver.execute_script("return document.body.scrollHeight;")
scroll_down_size = scroll_height // 3
current_point = 0

time.sleep(0.5)

keyboards = list()

while current_point <= scroll_height:
    
    for keyboard in driver.find_elements(By.CSS_SELECTOR,keyboards_selector):
        title = keyboard.find_element(By.CSS_SELECTOR,".a-size-base-plus.a-spacing-none.a-color-base.a-text-normal")
        img = keyboard.find_element(By.TAG_NAME,"img").get_attribute("src")
        
        keyboards.append({
            "title":title.text,
            "img":img})
        
    driver.execute_script(f"window.scrollTo({current_point},{scroll_down_size + current_point});")
    time.sleep(3)
    current_point = current_point + scroll_down_size
        

print()
    
scraped_data_json = json.dumps(keyboards,ensure_ascii=False)


with open("scraped-data.json","w") as file:
    file.write(scraped_data_json)
    
print("JSON FILE CREATED !")
        

        
        