# Username_Enumeration
Automated Tool and scripts to perform Username Enumeration on 50+ sites. 

Why this tool, when there are other similar tools that perform username enumeration ?

The current tools available, perform enumeration by appending the username to the site and checking if the link exists or not. For eg: User "zuck" is considered a valid user on Facebook if the link https://www.facebook.com/zuck is valid. This is helpful to find whether the username is taken or not. These usernames cannot be used for other purposes.
The tool we proposed, identifies the user by Email IDs which are typically used to login to a particular user account. This is a serious vulnerabiliity as the Usernames/Email IDs gathered could be used for Credential Stuffing, Password Spraying or other Social Engineering Attacks. 
The only downside of the tool is it's relatively slow when compared to other tools.

## Instructions:

The following files exist inside the docker: check.py, enumerator.py, emailID.txt, usernames.txt, newlinks.txt, error_msgs.txt, msg2.txt
* check.py       – A simple script to check if TOR is working, i.e. if IP addresses are changing. 
* enumerator.py  – The main Username Enumeration tool. 
* emailID.txt    – Enter the Email IDs to be tested in this file.
* usernames.txt  – Enter the Usernames to be tested in this file.
* newlinks.txt   – Enter the Website links to be tested in this file.
* error_msgs.txt – Enter the error messages related to the runProgram function (-P option).
* msg2.txt       – Enter the error messages related to the accountNotPresent function (-NP option).

The complete websites list and other details to be entered in the above files are listed in the vulnerable_database excel file.

    1. Choose a website to perform the enumeration from the excel file.
    2. Copy the corresponding link from the excel file to newlinks.txt file
    3. Enter the email ids or usernames to be tested in emailID.txt or usernames.txt files, respectively.
    4. Copy the Error Messages from the excel file to error_msgs.txt or msg2.txt files, respectively
    5. Run the tool

Some sites do not work properly with TOR. Refer to Excel file to see which sites do not work with TOR. Most of the sites work with -P flag and error_msgs.txt. The -NP flag and msg2.txt files are rarely used. This tool will be updated continuously, and new sites will be added. Multiple sites could be Enumerated by including them in the newlinks.txt file.

## Installation:
```
Clone the UsernameEnumeration Repository:
$ git clone https://github.com/ningala-a/Username_Enumeration.git

Go to the UsernameEnumeration directory.
$ cd Username_Enumeration

Run the script.sh file to build the docker image and run this as a container
$ chmod +x script.sh
$ ./script.sh

Start TOR by using the following command.
$ tor &
Press the ENTER key when it says “Bootstrapped 100% (done)”.

Run the enumerator tool.
$ python3 enumerator.py -P -email tor

NOTE: If you get an Error Message stating: 'geckodriver' executable needs to be in PATH, Run this command:
$ apt-get install firefox-geckodriver
```
## Usage:
```
$ python3 enumerator.py -P -[email]/[username] [tor]/[notor]

P or NP : P denotes to check if the error message indicates the username/email to exist - Use error_msgs.txt.
          NP denotes to check if the error message indicates the current username doesn’t exist - Use msg2.txt (rarely used).

email or username : email means website takes email id as input; username means website takes usernames as input

tor : to run the tool with tor – changes IP addresses [This parameter is optional]

Examples:

python3 enumerator.py -P -email tor

python3 enumerator.py -P -username notor

python3 enumerator.py -NP -email tor
```
## Note:
Alternatively, it is better to run Individual scripts for the sites of your choice. These scripts are faster and are usefull for enumerating small list of usernames/email IDs. Offcourse, to use the TOR functionality, you'll need to run the main tool.  

The Individual scripts are made to be pretty straightforward and self-explanatory.

Pycharm 2021.1 IDE was used for testing purposes. You can use any IDE of your choice. 

Selenium WebDriver can not communicate with a browser directly. We need an intimidatory executable agent between Selenium WebDriver and the actual browser. These intimidatory are provided by third parties. For edge, we need a msedgedriver as an interface between Selenium WebDriver and a real edge browser[Source]. For firefox, we need geckodriver. Download the drivers for browser of your choice and place them in your system path. 

https://github.com/mozilla/geckodriver/releases

https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

At the time of testing, all the sites listed in vulnerable_database.xlsx were working!
