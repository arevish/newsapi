# Listen & Read News API ![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)

This is a News listening API project that aims to help the user easy access, sort and read news information gotten from the News Website of times of india . 
The program automaticly finds the top latest news around the globe and reads the headlines to you 
and extract the link to that article so that the user can click on view article to read the articles in detail or you can just listen to the voice for some news update.

### Module used
python modules
```
import requests
import json
from win32com.client import Dispatch
```

## Instructions

* This script is intended to be used as a Simple News reader software by using api from https://newsapi.org/
* It required internet connection to run the speech commands and to extract the information from web.

## PRE-REQUISITES
Your laptop with 3.6.x (onwards) installed.

**NOTE:** Those with Linux and MacOSX would have Python installed by default, no action required.

Windows: Download the version for your laptop via https://www.python.org/downloads/

**NOTES**
In your preferred editor, make sure indentation is set to "4 spaces".

* Make sure you have **pywin32** installed in python otherwise code may fail, to install it in your machine > open python in your terminal then type `pip install pywin32` or `pip install pypiwin32.`  to install. :warning:
---

## Run using Python3.8+
1. Clone or download repositiory: https://github.com/arevish/newsapi.git
2. In source folder, run `python3 'akhbaar.py'` to start program, optionally, run with `--help` argument to see other runtime options.

### ThankYou!