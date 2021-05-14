# User Enum Chaturbate
# Need usernames instead of email IDs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import extract_html_diff


print("The usernames present in Chaturbate.com are:")

# Place all the Usernames to test in the for loop as shown below.
# You can remove all the Usernames below
for i in ["superman", "batman", "asdjhbasbdajd"]:

    user = i
    # Using edge browser
    driver = webdriver.Edge(executable_path='msedgedriver')
    # Using Firefox browser
    # driver = webdriver.FirefoxProfile()
    # driver = webdriver.Firefox(driver)
    driver.get("https://chaturbate.com/accounts/register/?src=header&auipsrc=navbar")
    sleep(2)
    p1 = driver.page_source
    elem=driver.find_element_by_xpath("//input[@type='text']") #type = 'text'/'email'
    elem.send_keys(user)
    elem.send_keys(Keys.RETURN)
    sleep(2)
    p2 = driver.page_source
    p3 = extract_html_diff.as_string(p2,p1)
    if "Username is already taken" in p3:
        print(i)
    sleep(3)
    driver.close()