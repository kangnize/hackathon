from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Set up the WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Optional: Run in headless mode
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # 1. Navigate to the Facebook login page
    driver.get("https://www.facebook.com")

    # 2. Enter the email and password, then click 'Log In'
    email_field = driver.find_element(By.ID, "email")
    password_field = driver.find_element(By.ID, "pass")
    email_field.send_keys("kazunguvictor12@gmail.com")  # add  your email
    password_field.send_keys("Kazungu12")  # add  your password
    
    # Wait for the login button to be clickable and then click it
    wait = WebDriverWait(driver, 20)
    login_button = wait.until(EC.element_to_be_clickable((By.NAME, "login")))
    login_button.click()

    # 3. Wait for the homepage to load and verify login
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Account']")))

    # If the script reaches this point, the login is likely successful
    print("Login successful.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
