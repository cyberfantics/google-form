import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize the WebDriver
driver = webdriver.Chrome()
driver.maximize_window()  # Maximize the browser window
wait = WebDriverWait(driver, 15)  # WebDriver wait to handle dynamic elements
actions = ActionChains(driver)  # ActionChains for scrolling and interactions

# Load the CSV file
data = pd.read_csv('info.csv')

# Iterate over each row in the CSV file
for index, row in data.iterrows():
    print(row)
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdKd5MpvP_emWHNccV2az_NGWcW9Gc4twvZoE-ciyu2DHJOJA/viewform?usp=sf_link')

    try:
        # Fill in the Full Name field
        name_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="text" and @aria-labelledby="i1"]')))
        name_input.send_keys(row['Full Name'])
        
        # Scroll down after entering the name
        actions.move_to_element(name_input).perform()

        # Select Preferred Method of Communication (Radio Button)
        communication_method = row['Preferred Method of Communication']
        communication_option = wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[@aria-label="{communication_method}"]')))
        communication_option.click()

        # Scroll down after selecting the radio button
        actions.move_to_element(communication_option).perform()

        # Select Skills (Checkboxes) - Skills are separated by '|'
        skills = row['Skills'].split('|')
        for skill in skills:
            skill_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[@aria-label="{skill}"]')))
            if not skill_checkbox.is_selected():
                skill_checkbox.click()

        # Scroll down after selecting checkboxes
        actions.move_to_element(skill_checkbox).perform()

        # Select Employment Status (Dropdown)
        employment_status_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]')))
        employment_status_dropdown.click()

        # Wait for the dropdown options to appear and select the correct status
        employment_status = row['Employment Status']
        employment_option = wait.until(EC.element_to_be_clickable((By.XPATH, f'//div[@role="option" and @data-value="{employment_status}"]')))
        employment_option.click()

        # Scroll to the date input field
        date_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')))
        actions.move_to_element(date_input).perform()

        # Set the Meeting Date
        date_input.send_keys(row['Meeting Date'])

        # Scroll to the Submit button and submit the form
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')))
        actions.move_to_element(submit_button).perform()
        submit_button.click()

        # Wait for the form submission to complete
        time.sleep(15)  # Adjust the waiting time based on the submission process

    except Exception as e:
        print(f"An error occurred while processing row {index}: {e}")

# Quit the browser once the loop is completed
driver.quit()
