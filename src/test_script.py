from selenium import webdriver

# Set up the Chrome WebDriver
driver = webdriver.Chrome()

# Open a website
driver.get("https://www.google.com")

# Wait for a few seconds
import time
time.sleep(5)  # Just for demo purposes, to see the page

# Close the browser
driver.quit()
