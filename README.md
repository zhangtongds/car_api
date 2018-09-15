# Smartcar Backend Coding Challenge - Tong Zhang
## Summary
This app is built with Python on Flask.
This is the document that explains how to initialize and run the app.   
The server.py implements all the smartcar APIs using GM APIs.   
The functions in server.py return vehicle information, security status and fuel/battery level and change the engine status.  
demo.py calls the Smartcar APIs and shows the returned results.
tests.py file runs all tests for each function in server.py. The test coverage is 96%.  
Please see attached demo video that comes from this folder.  

## About the Developer
This task was created by Tong Zhang for Smartcar take-home assignment, she is a software engineer in Mountain View, CA. Learn more about the developer on [LinkedIn](https://www.linkedin.com/in/tong--zhang/).
## Tech Stack
Python, Flask

## Setup/Installation

Please follow the below steps to have this app running on your computer:

Download the folder:
```
/Smartcar_Tong_Zhang
```

Create a virtual environment:

```
$ virtualenv env
```

Activate the virtual environment:

```
$ source env/bin/activate
```

Install dependencies:

```
$ pip install -r requirements.txt
```

Run the app from the command line:

```
$ python server.py
```



