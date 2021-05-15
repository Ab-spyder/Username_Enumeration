#  User Enum theguardian
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import extract_html_diff

print("The usernames present in theguadian are:")

# Place all the Email IDs to test in the for loop as shown below.
# You can remove all the Email IDs below
for i in ["ccohen@aol.com", "superman@gmail.com", "batman@gmail.com"]:

    user = i
    # Using edge browser
    driver = webdriver.Edge(executable_path='msedgedriver')

    # Using Firefox browser
    # driver = webdriver.FirefoxProfile()
    # driver = webdriver.Firefox(driver)
    driver.get("https://profile.theguardian.com/signin?")
    p1 = driver.page_source
    elem=driver.find_element_by_xpath("//input[@type='email']") #type = 'text'/'email'
    elem.send_keys(user)
    elem.send_keys(Keys.RETURN)
    sleep(2)
    p2 = driver.page_source
    p3 = extract_html_diff.as_string(p2,p1)
    driver.close()
    if "This email account is registered with The Guardian." in p3:
        print(i)
    sleep(2)
    driver.close()