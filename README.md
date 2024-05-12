## Project : Building a WhatsApp bot with Python

<p>
  <img src="pictures/whatsapp-bot-image.png" />
</p>

### Table of contents :

1. Description
2. Compatible configurations
3. Installing packages
4. Running the bot

## 1. Description :

This project consists of the implementation of a WhatsApp bot. The idea is to programatically
perform a Google search containing the message/question received on WhatsApp and make the bot
respond automatically by sending a few related URLs.

## 2. Compatible configurations :

* Python 3
* Windows 10
* MacOS
* Linux

## 3. Installing packages :
This program uses the following Python libraries :

```
aiohttp 3.9.1
aiohttp-retry 2.8.3
aiosignal 1.3.1
async-timeout 4.0.3
attrs 23.2.0
beautifulsoup4 4.12.2
blinker 1.7.0
cachetools 5.3.2
certifi 2023.11.17
charset-normalizer 3.3.2
click 8.1.7
Flask 3.0.0
frozenlist 1.4.1
google 3.0.0
google-api-core 2.15.0
google-auth 2.26.1
google-auth-httplib2 0.2.0
googleapis-common-protos 1.62.0
httplib2 0.22.0
idna 3.6
itsdangerous 2.1.2
Jinja2 3.1.2
MarkupSafe 2.1.3
multidict 6.0.4
protobuf 4.25.1
pyasn1 0.5.1
pyasn1-modules 0.3.0
PyJWT 2.8.0
pyparsing 3.1.1
requests 2.31.0
rsa 4.9
soupsieve 2.5
twilio 8.11.0
uritemplate 4.1.1
urllib3 2.1.0
Werkzeug 3.0.1
yarl 1.9.4

```

## 4. Running the bot :

  * Open a terminal (ex: Cygwin for Windows, the terminal for MacOS) or in an IDE (ex: PyCharm)
  * Clone the repository in a local directory :
    > $<b> git clone repository path</b> 
  * Go to this folder using the terminal
  * Create a virtual environment with :
    > $<b> python -m venv <name of the environment></b> 
  * Activate the virtual environment by running :
    > $ <b>source env/bin/activate</b>  (on MacOS and Linux)
  
    > $ <b>env\Scripts\activate.bat</b> (on Windows)
  * Install the packages present in the requirements.txt file
(this file is located in the project folder) 
    > $ <b>pip install -r requirements.txt</b> 
  * Finally, run the development server :
    > $ python main.py
  * Set up a Twilio and Ngrok accounts then follow the instructions of the respective
sites to connect WhatsApp, Twilio, Ngrok and the local server together :\
    **https://www.twilio.com/en-us** \
    **https://ngrok.com/**
---