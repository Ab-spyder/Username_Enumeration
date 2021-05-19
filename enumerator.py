# Automated tool to perform Username Enumeration with TOR functionality.
"""
Project Contributors:
* Abhishek Ningala
* Jugal Joshi
* Raaghavv Devgon
"""
from selenium.webdriver.common.keys import Keys
from time import sleep,time
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

from selenium import webdriver
import requests
import time
from stem import Signal
from stem.control import Controller
from bs4 import BeautifulSoup
import re
import sys

with open('error_msgs.txt') as f:
    msg_database = [line.rstrip() for line in f]

#Cleaning the msg_database and converting all the text into lower case.
msg_database = [re.sub('[^A-Za-z0-9]+', '', mystring.lower()) for mystring in msg_database]

with open('msg2.txt') as f:
    account_not_exist_msg = [line.rstrip() for line in f]

#Cleaning the msg_database and converting all the text into lower case.
account_not_exist_msg = [re.sub('[^A-Za-z0-9]+', '', mystring.lower()) for mystring in account_not_exist_msg]


def get_current_ip():
    session = requests.session()
    session.proxies = {'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'}
    try:
        r = session.get('https://httpbin.org/ip')
    except Exception as e:
        print(str(e))
    else:
        return r.text


def my_proxy(PROXY_HOST, PROXY_PORT):
    fp = webdriver.FirefoxProfile()
    # Direct = 0, Manual = 1, PAC = 2, AUTODETECT = 4, SYSTEM = 5
    fp.set_preference("network.proxy.type", 1)
    fp.set_preference("network.proxy.socks",PROXY_HOST)
    fp.set_preference("network.proxy.socks_port",int(PROXY_PORT))
    fp.update_preferences()
    options = Options()
    options.headless = True
    # return webdriver.Firefox(options=options, firefox_profile=fp,executable_path=GeckoDriverManager().install())
    return webdriver.Firefox(options=options, firefox_profile=fp)


def renew_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="HkB3IDWD#143")
        controller.signal(Signal.NEWNYM)

def accountNotPresentLogin(user,link):
    browser = my_proxy("127.0.0.1", 9050)
    browser.get(str(link))
    flag = False
    sleep(3)
    file1 = browser.page_source
    passwordV = 'A$wwr12#1c0{}@'
    try:
        elem = browser.find_element_by_name("username")
    except:
        # print("username doesnt exist")
        try:
            elem = browser.find_element_by_name("usernameOrEmail")
        except:
            # print("usernameOrEmail doesnt exist")
            try:
                elem = browser.find_element_by_name("email")
            except:
                # print("email doesnt exist")
                try:
                    elem = browser.find_element_by_name("ap_email")
                except:
                    # print("email doesnt exist")
                    try:
                        elem = browser.find_element_by_name("userid")
                    except:
                        # print("email doesnt exist")
                        try:
                            elem = browser.find_element_by_xpath("//*[@id='forgot-password-email']")
                        except:
                            # print("email doesnt exist")
                            try:
                                elem = browser.find_element_by_xpath("//*[@id='/html/body/div[2]/div/form/input[2]']")
                            except:
                                # print("email doesnt exist")
                                try:
                                    elem = browser.find_element_by_xpath("//input[@type='email']")
                                except:
                                    print("can't enumerate")
                                    exit(0)


    elem.send_keys(user)
    sleep(2)

    # try:
    #     pass_=browser.find_element_by_name("passwd")
    # except:
    #     try:
    #         pass_=browser.find_element_by_name("password")
    #
    #     except:
    #         print("email doesnt exist")
    #         flag_pass=True
    # if(flag_pass):
    #     print("no password field")
    # else:
    #     pass_.send_keys(passwordV)
    # print(pass_.is_displayed())

    # print(flag_pass)
    # if('box.com' in link):
    #     print("BOX")
    #
    #     elem.send_keys(Keys.TAB)
    #
    # else:

    elem.send_keys(Keys.RETURN)
    sleep(10)
    file2 = browser.page_source

    soup = BeautifulSoup(file2, "html.parser")
    for script in soup(["script", "style"]):
        script.decompose()

    content = list(soup.stripped_strings)

    #Cleaning the html text and converting the text in lower case.
    content = [re.sub('[^A-Za-z0-9]+', '', data.lower()) for data in content]

    for x in content:
        if x in account_not_exist_msg:
            flag = True

    if(flag):
        print("doesnt exist")
    else:
        accounts.append(i)
    browser.close()



def runProgram(user,link):
    browser = my_proxy("127.0.0.1", 9050)
    browser.get(str(link))
    sleep(3)
    file1 = browser.page_source
    try:
        elem = browser.find_element_by_xpath("//*[@id='user_email']")
    except:
        try:
            elem = browser.find_element_by_xpath("//input[@type='email']")
        except:
            # print("email doesnt exist")
            try:
                elem = browser.find_element_by_name("email")
            except:
                # print("text doesnt exist")
                try:
                    elem = browser.find_element_by_xpath("//input[@type='text']")
                except:
                    # print("text doesnt exist")
                    try:
                        elem = browser.find_element_by_name("yid")
                    except:
                        print("can't enumerate")
                        sys.exit(0)


    elem.send_keys(user)
    time.sleep(2)
    try:
        pass_ = browser.find_element_by_name("passwd")
    except:
        try:
            pass_ = browser.find_element_by_name("password")
        except:
            flag_pass = True
    if('box.com' in link ):
        # print("BOX")
        elem.send_keys(Keys.TAB)
    elif('engadget.com' in link):
        elem.send_keys(Keys.TAB)
    elif('fastmail.com' in link):
        elem.send_keys(Keys.TAB)
    elif('ibm.com' in link):
        elem.send_keys(Keys.TAB)
    elif('imgur .com' in link):
        elem.send_keys(Keys.TAB)
    elif('independent.co.uk' in link):
        elem.send_keys(Keys.TAB)
    elif('techcrunch.com' in link):
        elem.send_keys(Keys.TAB)
    elif('indeed.com' in link):
        # print('indeed')
        elem.send_keys(Keys.TAB)
    elif('zippyshare.com' in link):
        elem.send_keys(Keys.TAB)
    elif('samsung.com' in link):
        elem.send_keys(Keys.TAB)
    elif('wondershare.com' in link):
        elem.send_keys(Keys.TAB)
    elif('redtube.com' in link):
        elem.send_keys(Keys.TAB)

    else:

        elem.send_keys(Keys.RETURN)
    sleep(8)
    file2 = browser.page_source


    soup = BeautifulSoup(file2, "html.parser")
    for script in soup(["script", "style"]):
        script.decompose()

    content = list(soup.stripped_strings)

    #Cleaning the html text and converting the text in lower case.
    content=[re.sub('[^A-Za-z0-9]+', '', data.lower()) for data in content]

    for x in content:
        if x in msg_database:
            print("[+] ---------------------------> Match found: {}".format(user))
            accounts.append(i)
    browser.close()



if __name__ == "__main__":
    if(len(sys.argv)!=4):
        print("Please use the tool as for example -c 'python3 enumerator.py -P -[email]/[username] [tor]/[notor]'")
        sys.exit(0)

    if sys.argv[2] == '-username':
        with open('usernames.txt') as f:
            emailID = [line.rstrip() for line in f]
    elif sys.argv[2] == '-email':
        print("FETCHING EMAILS...")
        with open('emailID.txt') as f:
            emailID = [line.rstrip() for line in f]
    else:
        print("Please enter -username or -email as the second argument!")
        sys.exit(0)

    with open('newlinks.txt') as f:
        links = [line.rstrip() for line in f]

    f = 0
    for l in links:
        accounts = []

        for i in emailID:
            if sys.argv[3] == 'tor':
                print('tor is used')
                if(f%2==0):
                    renew_tor_ip()
            else:
                print("no tor")
            print(get_current_ip())

            if sys.argv[1] == '-P':
                runProgram(i, l)
                print("Checking if username exists..")
            elif sys.argv[1] == '-NP':
                print("Checking if username doesnt exists..")

                accountNotPresentLogin(i, l)
            else:
                print("enter valid argument.")
                sys.exit(0)
            f += 1
        print("The current Link crawled: ",l);
        print("FOUND accounts: ", set(accounts));


# Try and Catch more websites:
# Gather more website error messages
# Test this on more websites.
