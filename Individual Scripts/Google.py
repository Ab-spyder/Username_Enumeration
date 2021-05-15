#  User Enum Google
# Please use Usernames instead of email IDs - ex: Use superman instead of superman@gmail.com
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

print("The usernames present in google are:")

# Place all the Usernames to test in the for loop as shown below.
# You can remove all the usernames below
for i in ["BegForMercy", "BdkndcmsjdnkjnAxe", "CrazyMind", "DeathWaasdaish", "DisasterMaster", "ElNaaaino", "EndlessFacepalms" ]:
    # Using edge browser
    driver = webdriver.Edge(executable_path='msedgedriver')

    # Using Firefox browser
    # driver = webdriver.FirefoxProfile()
    # driver = webdriver.Firefox(driver)

    user = i

    driver.get("https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ltmpl=default&dsh=S1963587235%3A1615230351442196&gmb=exp&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp")

    elem=driver.find_element_by_xpath('//input[@type="email"]') #type = 'text'/'email'
    elem.send_keys(user)
    elem.send_keys(Keys.TAB)
    sleep(2)
    p1 = driver.page_source
    if "That username is taken" in p1:
    #if "This username isn't allowed. Try again." in p1:
       print(i)
    driver.close()




