from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

option = webdriver.ChromeOptions()
option.add_argument("user-data-dir=/Users/snehanshnchowdhury/Library/Application Support/Google/Chrome/")
option.add_argument("profile-directory=Profile 2")

# Initialize WebDrivers
driver = webdriver.Chrome(options=option)

#def load_cookies():
#    driver.get("https://libcal.rutgers.edu/space/129745")  # Navigate to the site first
#   time.sleep(3)  # Wait for the site to load

    # Load cookies from the exported JSON file
#    with open("cookies.json", "r") as cookies_file:
#        cookies = json.load(cookies_file)
#        for cookie in cookies:
#            driver.add_cookie(cookie)
    
def open_booking_page():
    # Step 1: Open the bookisng page
    driver.get('https://libcal.rutgers.edu/space/129745')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="eq-time-grid"]/div[1]/div[1]/div/button[2]')))

def navigate_to_date():
    # Step 2: Click the next day button 14 times to navigate to the date two weeks from today
    next_day_xpath = '//*[@id="eq-time-grid"]/div[1]/div[1]/div/button[2]'
    for _ in range(14):
        next_day_button = driver.find_element(By.XPATH, next_day_xpath)
        next_day_button.click()
        time.sleep(1)  # Allow the page to load

def book_time_slot():
    # Step 3: Click on the time slot from 5 pm 
    time_slot_xpath = '//*[@id="eq-time-grid"]/div[2]/div/table/tbody/tr/td[3]/div/div/div/table/tbody/tr/td/div/div[2]/div[37]/a/div/div/div'
    time_slot_xpath2 = '//*[@id="eq-time-grid"]/div[2]/div/table/tbody/tr/td[3]/div/div/div/table/tbody/tr/td/div/div[2]/div[17]/a/div/div/div'
    time_slot = driver.find_element(By.XPATH, time_slot_xpath)
    time_slot2 = driver.find_element(By.XPATH, time_slot_xpath2)
    #if time_slot.get_attribute('class') == 'timeslot timeslot-available':
    #    time_slot.click()
    #if time_slot2.get_attribute('class') == 'timeslot timeslot-available':
    #    time_slot2.click()
    
    time_slot2.click()
    time_slot.click()
    

    # Step 4: Click the submit times button
    submit_times_xpath = '//*[@id="submit_times"]' 
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, submit_times_xpath)))
    submit_button = driver.find_element(By.XPATH, submit_times_xpath)
    submit_button.click()

def confirm_booking():
    # Step 5: Click the continue button on the next page
    continue_button_xpath = '//*[@id="terms_accept"]'
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, continue_button_xpath)))
    continue_button = driver.find_element(By.XPATH, continue_button_xpath)
    continue_button.click()

def automate_booking():
    open_booking_page()
    navigate_to_date()
    book_time_slot()
    confirm_booking()
    print("Booking attempt completed.")

# Execute the booking process
automate_booking()

# Close the WebDriver
driver.quit()