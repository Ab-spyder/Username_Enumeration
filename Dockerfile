FROM ubuntu:20.10
RUN apt update -y

# Installing text editors
RUN apt install vim emacs nano less -y
# RUN apt install emacs -y
# RUN apt install nano -y
# RUN apt install less -y

#Installing networking tools
RUN apt install curl net-tools netcat firefox tor -y
# RUN apt install net-tools -y
# RUN apt install netcat -y
# RUN apt install firefox -y


#Installing Python3
RUN apt install python3 python3-pip -y
#Installing Pip3
# RUN apt install python3-pip -y
# RUN python3 -y
RUN pip3 install selenium bs4 requests regex stem pysocks webdriver-manager
# RUN pip3 install bs4
# RUN pip3 install requests
# RUN pip3 install regex
#Installing Firefox Geckodriver
RUN apt-get install firefox-geckodriver
RUN /bin/bash -c 'torpass=$(tor --hash-password "HkB3IDWD#143") \
printf "HashedControlPassword $torpass\nControlPort 9051\n" | tee -a /etc/tor/torrc'
#RUN systemctl restart tor
RUN tor&

WORKDIR /UserEnum
ADD ./TorCheck.py check.py
ADD ./msg2.txt msg2.txt
ADD ./newlinks.txt newlinks.txt
ADD ./emailID.txt emailID.txt
ADD ./usernames.txt usernames.txt
ADD ./enumerator.py enumerator.py
ADD ./error_msgs.txt error_msgs.txt









CMD ["/bin/bash"]
