#  User Enum Yandexmail

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import extract_html_diff

print("The usernames present in Yandex Mail are:")

# Place all the Email IDs to test in the for loop as shown below.
# You can remove all the Email IDs below
for i in ["superman", "BegForMercy", "BraiasjdnkjnAxe", "CrazyMind", "DeathWaasdaish", "DisasterMaster", "ElNaaaino", "EndlessFacepalms", "FreakingOblin", "GhostlyPresence", "GridlockAndKey", "HoofHearted666", "KungFuMonk", "NineTees", "PlzJustDie", "SeekNDestroy", "SinisterChill", "BegqwForMercy", "BasxasdxrainAxe", "Crazy1Mind", "DeatasdasdhWish", "Dis1asterMaster", "EaslNino", "EndlessFaaacepalms", "FrrreakingOblin", "GhossdtlyPreseasnce", "GrisadlockAndKey", "HoofaHearted666", "KsungFuMonk", "NinessTees", "sPlzJustDie", "sSeeksNDestroy", "SssinisddterChill"]:

    user = i

    # Using edge browser
    driver = webdriver.Edge(executable_path='msedgedriver')

    # Using Firefox browser
    # driver = webdriver.FirefoxProfile()
    # driver = webdriver.Firefox(driver)

    driver.get("https://passport.yandex.com/registration/mail")
    sleep(3)
    p1=driver.page_source
    #elem=driver.find_element_by_xpath('//input[@type="text"]') #type = 'text'/'email'
    elem=driver.find_element_by_id("login")
    elem.send_keys(user)
    elem.send_keys(Keys.RETURN)
    sleep(2)
    p2 = driver.page_source
    p3 = extract_html_diff.as_string(p2, p1)
    if "Sorry" in p3:
    #if "This username isn't allowed. Try again." in p1:
       print(i)
    driver.close()




