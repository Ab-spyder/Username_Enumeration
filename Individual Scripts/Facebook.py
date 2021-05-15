#  User-Enum Facebook
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


print("The Usernames present in Facebook are: ")

# Place all the Email IDs to test in the for loop as shown below.
# You can remove all the Email IDs below
for i in ["ccabsdjh2aohen@aol.com", "superman@gmail.com", "keijselkjhur@aol.com", "ajohnson@hotmail.com", "rnewman@aol.com",
          "sfoskett@hotmail.com", "seurat@aol.com", "richard@gmail.com", "punkis@gmail.com" ]:

    # Using edge browser
    driver = webdriver.Edge(executable_path='msedgedriver')

    # Using Firefox browser
    # driver = webdriver.FirefoxProfile()
    # driver = webdriver.Firefox(driver)

    user = i

    driver.get("https://www.facebook.com/login/identify/")
    elem = driver.find_element_by_xpath("//input[@type='text']")  # type = 'text'/'email'
    elem.send_keys(user)
    elem.send_keys(Keys.RETURN)
    sleep(3)
    p1 = driver.page_source

    if "How do you want to get the code to reset your password?" in p1:
        print(i)
    sleep(3)
    driver.close()