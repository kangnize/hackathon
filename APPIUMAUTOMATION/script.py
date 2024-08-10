from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import time

# Desired capabilities for Android
desired_caps = {
    'platformName': 'Android',
    'platformVersion': '11.0',  # Replace with your Android version
    'deviceName': 'emulator-5554',  # Replace with your device name or ID
    'appPackage': 'com.example.android',  # Replace with your app package
    'appActivity': '.MainActivity',  # Replace with your app activity
    'noReset': True
}

# Initialize the driver
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

try:
    # Wait for the app to load
    time.sleep(5)

    # Log in
    username_field = driver.find_element(MobileBy.ID, 'com.example.android:id/username')  # Replace with your element's ID
    password_field = driver.find_element(MobileBy.ID, 'com.example.android:id/password')  # Replace with your element's ID
    login_button = driver.find_element(MobileBy.ID, 'com.example.android:id/login_button')  # Replace with your element's ID
    
    username_field.send_keys('your_username')  # Replace with your predefined username
    password_field.send_keys('your_password')  # Replace with your predefined password
    login_button.click()

    # Wait for the login to complete
    time.sleep(5)

    # Navigate to the settings screen
    settings_button = driver.find_element(MobileBy.ID, 'com.example.android:id/settings_button')  # Replace with your element's ID
    settings_button.click()

    # Wait for the settings screen to load
    time.sleep(5)

    # Update profile information
    profile_name_field = driver.find_element(MobileBy.ID, 'com.example.android:id/profile_name')  # Replace with your element's ID
    profile_name_field.clear()
    profile_name_field.send_keys('New Profile Name')  # Replace with the new profile name

    save_button = driver.find_element(MobileBy.ID, 'com.example.android:id/save_button')  # Replace with your element's ID
    save_button.click()

    # Verify profile update
    updated_name = driver.find_element(MobileBy.ID, 'com.example.android:id/profile_name')  # Replace with your element's ID
    assert updated_name.text == 'New Profile Name'  # Verify the updated profile name

finally:
    # Close the driver
    driver.quit()
