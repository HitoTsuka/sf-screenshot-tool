from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import shutil
from datetime import datetime

def take_screenshot(url, identifier, output_filename):
    try:
        driver = webdriver.Edge()
        driver.get(url)  
        driver.maximize_window()

        time.sleep(1)

        # Salesforce login
        # Read username and password from file
        with open(r'filepath', 'r') as file:
            lines = file.readlines()
            sfusername = lines[0].strip()
            sfpw = lines[1].strip()

        username = driver.find_element(By.NAME, 'username')
        pw = driver.find_element(By.NAME, 'pw')

        username.clear()
        pw.clear()

        username.send_keys(sfusername)
        pw.send_keys(sfpw)

        username.submit()

        time.sleep(5)

        # Determine if the identifier is an ID or a class
        element = None
        if identifier.startswith('#'):
            element = driver.find_element(By.ID, identifier[1:])
            # Click the refresh button
            refresh = driver.find_element(By.NAME, 'refresh')
            refresh.click()
            time.sleep(120)
        elif identifier.startswith('.'):
            element = driver.find_element(By.CLASS_NAME, identifier[1:])
        else:
            raise ValueError("Identifier must start with '#' for ID or '.' for class")

        # Get the location and size of the element
        location = element.location 
        size = element.size 

        # Take a screenshot of the webpage
        driver.save_screenshot('full_page_screenshot.png') 

        # Crop the screenshot to the specified element
        left = location['x'] 
        top = location['y'] 
        right = location['x'] + size['width'] 
        bottom = location['y'] + size['height'] 

        from PIL import Image 
        # Open the full page screenshot
        image = Image.open('full_page_screenshot.png') 
        # Crop the screenshot to the specified element
        element_screenshot = image.crop((left, top, right, bottom)) 
        # Save the screenshot
        element_screenshot.save(output_filename) 
        # Delete the temporary file
        os.remove('full_page_screenshot.png')
        #driver.quit()

    finally:
        # Quit the WebDriver
        if driver:
            driver.quit()

def get_week_of_month(date):
    first_day = date.replace(day=1)
    # Adjust weekday index: Sunday=0, Monday=1, ..., Saturday=6
    offset = (first_day.weekday() + 1) % 7
    print(offset)
    
    # Number of days in the first week
    first_week_num_days = 7 - offset
    
    # Calculate the week number
    if date.day <= first_week_num_days:
        return 1
    else:
        remaining_days = date.day - first_week_num_days
        return 1 + remaining_days // 7 + (1 if remaining_days % 7 > 0 else 0)

def copy_images_with_date(source_folder, destination_folder, image_files):
   # Get the date
    today_date = datetime.now().strftime("%Y%m%d")
    
    # Create a folder for today's date
    folder_path = os.path.join(destination_folder, today_date)
    os.makedirs(folder_path, exist_ok=True)

    # Copy the images
    for image_path in image_files:
        image_name = os.path.basename(image_path)
        destination_path = os.path.join(folder_path, image_name)
        shutil.copyfile(image_path, destination_path)
