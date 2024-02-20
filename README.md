# Keylogger

This is the final application-based project of my 6-week IBM Skillsbuild Cybersecurity internship with Edunet Foundation between June and July 2023.

## What is a keylogger?
A keylogger is an application that has the capability to capture all keystrokes made while it is run, along with the ability to save these keystrokes to a database or file.
The agenda for this project is to understand how a keylogger works fundamentally, what are the scopes of its application, and to really understand the consequences of its use, be it productive or malicious, from a cybersecurity perspective.

## Positive use cases for a keylogger
* Helps in the form of a backup in the event of a loss of information, since it stores
whatever that is entered.
* Parental/Employer monitoring of children/employee activity

## Negative use cases for a keylogger
* Sensitive information such as login credentials, financial information, personal data,
or sensitive corporate information may be stolen by cybercriminals by running such
software.
* Stalkers can misuse keyloggers to invade someone's privacy, monitor their online
activities, and/or harass them digitally.

## My project

Designed a keylogger that waits for keypress and records keystrokes and stores them in file(s). Here, I have stored these keystrokes in files of different formats (.json and .txt)
Further I have also designed a simple GUI with an activation button that starts the keylogger.

### GUI of the Keylogger

<img src="https://github.com/userlikescoffee/Keylogger/assets/130635108/7b888839-a000-4262-8c58-fe048cb0b95a" width="250">

### Working of the Keylogger

Entered text:    
![image](https://github.com/userlikescoffee/Keylogger/assets/130635108/5486d341-0ad9-4bc7-bee7-cbd4b7a70f9f)

keylogs.txt   
![image](https://github.com/userlikescoffee/Keylogger/assets/130635108/3349d598-6179-4606-8fd5-d54011427a5a)

keylogs.json  
![image](https://github.com/userlikescoffee/Keylogger/assets/130635108/422c1c66-940f-4939-a9d6-705bc76e2f91)

It can be observed that when the above output was typed on the keyboard, the keystrokes were captured and stored in different formats.

### Language(s) used
Python
  ### Libraries used
  1. pynput
     * keyboard - module containing keyboard classes and will be used to access the key related functions to listen and record the keystrokes
     * json - imported to be able to dump the keystrokes to a json file
  2. Tkinter - for creating the GUI

