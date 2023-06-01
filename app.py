
import pandas as pd
import streamlit as st
import pickle
import numpy as np
import sklearn as sns
import datetime
from datetime import date, timedelta
from streamlit_lottie import st_lottie
import re
from PIL import Image
import base64

import requests
from datetime import datetime

pipe = pickle.load(open("TaskSchedulerMModel.pkl", 'rb'))
scaler = pickle.load(open("dataScaler.pkl", 'rb'))

# getting animations in our webapp

url = requests.get(
    "https://assets10.lottiefiles.com/packages/lf20_FGeQJWRr14.json")

url2 = requests.get("https://assets10.lottiefiles.com/packages/lf20_lZZX75saS2.json")
# Creating a blank dictionary to store JSON file,
# as their structure is similar to Python Dictionary
url_json = dict()
url_json2 = dict()

if url.status_code == 200:
    url_json = url.json()
else:
    print("Error in the URL")

if url2.status_code == 200:
    url_json2 = url2.json()
else:
    print("Error in the URL")


# UtilApps
# Function to sort the list by second item of tuple
def Sort_Tuple(tup):
    tup.sort(key=lambda x: x[1])
    return tup



def getDeadline(dld):
    # Get today's date
    today = datetime.now().date()

    target_date = datetime.strptime(dld, "%Y-%m-%d").date()

    # Calculate the number of days between today and the target date
    days_gap = (target_date - today).days

    return days_gap


def maxDate(dld, ld):
    deadline = dld.split('-')
    lastDate = ld.split('-')

    if deadline[0] != lastDate[0]:

        if deadline[0] >= lastDate[0]:
            return dld
        else:
            return ld

    elif deadline[1] != lastDate[1]:
        if deadline[1] >= lastDate[1]:
            return dld
        else:
            return ld
    else:
        if deadline[2] >= lastDate[2]:
            return dld
        else:
            return ld

