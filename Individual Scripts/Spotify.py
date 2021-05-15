#  User Enum Spotify

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import extract_html_diff

print("The usernames present in spotify are:")

# Place all the Email IDs to test in the for loop as shown below.
# You can remove all the Email IDs below
for i in ["ccohen@gmail.com", "superman@gmail.com", "keijser@yahoo.com", "mredjeansjane@gmail.com", "ajohnson@yahoo.com", "rnewman@gmail.com", "sfoskett@yahoo.com", "seurat@yahoo.com", "richard@gmail.com", "punkyis@gmail.com"]:

    user = i

    # Using edge browser
    driver = webdriver.Edge(executable_path='msedgedriver')

    # Using Firefox browser
    # driver = webdriver.FirefoxProfile()
    # driver = webdriver.Firefox(driver)

    p1 = driver.page_source
    #elem=driver.find_element_by_name("Mobile Number or Email")
    elem=driver.find_element_by_xpath("//input[@type='email']") #type = 'text'/'email'
    elem.send_keys(user)
    elem.send_keys(Keys.TAB)
    sleep(2)
    p2 = driver.page_source
    p3 = extract_html_diff.as_string(p2,p1)

    if "This email is already connected to an account" in p3:
        print(i)
    driver.close()