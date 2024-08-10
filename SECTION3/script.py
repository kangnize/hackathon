from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Update this with the correct path to your chromedriver
chromedriver_path = '/Users/victorkazungu/path/to/chromedriver'

# Initialize the Chrome WebDriver
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

try:
    # Open Google
    driver.get('https://www.google.com')

    # Find the search box and enter the search term
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys('TEST AUTOMATION')
    search_box.send_keys(Keys.RETURN)

    # Wait for results to load
    time.sleep(3)

    # Verify that results are present
    results = driver.find_elements(By.CSS_SELECTOR, 'div.g')
    if len(results) > 0:
        print("Search results are present.")
    else:
        print("No search results found.")

finally:
    # Close the browser
    driver.quit()
