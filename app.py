import pandas as pd
import streamlit as st
import pickle
import numpy as np
# import sklearn as sns
import datetime
from datetime import date, timedelta
from streamlit_lottie import st_lottie
from PIL import Image
# import base64

import requests

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


from datetime import datetime


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


def assistUser():
    # check = 1

    st.image('Employee-Productivity-Statistics.png')

    st.title("EfficiencyBoost: Empowering Work Productivity with AI")

    st.title("Unlock Your Peak Potential: Streamline, Optimize, Excel!")

    userName = st.text_input("Let's get acquainted! Start by entering your name")

    gender = st.selectbox("To improve our services, please let us know your gender", ['Male', 'Female'])

    age = st.number_input("To customize our recommendations, we need to know your age (in years)", value=18, step=1)

    agree = st.checkbox('I understand and agree to the T&C of the EfficiencyBoost.')

    check = 1
    if age < 10:
        st.title("You're not eligible to use this website. You should be above 10 years of age.")
        people = st.image('bottomPeople.png')
        check = 0

    if agree and check:

        st.write('Great to Go!')

        # st_lottie(url_json)

        st_lottie(url_json,
                  height=100,
                  width=100,
                  speed=0.79,
                  loop=False,
                  quality='high',
                  key='Tick'
                  )

        taskslist = st.number_input("Select the Number of Tasks", value=2, step=1)

        st.title("Rate Your Energy Levels Throughout the Day")

        col1, col2, col3 = st.columns(3)

        with col1:
            morning = st.selectbox("Energy level for Morning", ['High', 'Medium', 'Low'])
        with col2:
            afternoon = st.selectbox("Energy level for Afternoon", ['Medium', 'High', 'Low'])
        with col3:
            evening = st.selectbox("Energy level for Evening", ['High', 'Medium', 'Low'])
        l1 = [morning, afternoon, evening]

        dict1 = {}

        l2 = ['Morning', 'Afternoon', 'Evening']
        pos = 0

        for i in l1:
            if i == "High":
                # i = 0
                dict1[l2[pos]] = 0
            elif i == 'Medium':
                dict1[l2[pos]] = 1
            else:
                dict1[l2[pos]] = 2
            pos += 1

        highEff, medEff, LowEff = [], [], []

        for i in dict1:
            if dict1[i] == 0:
                highEff.append(i)

        for i in dict1:
            if dict1[i] == 1:
                medEff.append(i)

        for i in dict1:
            if dict1[i] == 2:
                LowEff.append(i)

        # just for test purpose
        # for i in dict1:
        #     st.text(i + "->" + str(dict1[i]))

        st.text("ELABORATE THE TASKS AND DEADLINES")

        lastDate = ""  # to store the last date for our benefit in future

        listValues = []
        tasks, deadlines, delayedTasks = [], [], []

        today = str(date.today())

        for i in range(taskslist):

            cl1, cl2, cl3 = st.columns(3)
            currList = []

            with cl1:
                name = st.text_input("Task{} Name".format(i + 1))
            with cl2:
                catg = st.selectbox("Category of Task{}".format(i + 1),
                                    ['Academics', 'Professional', 'Personal', 'Projects', 'Meetings'])
            with cl3:
                priority = st.selectbox("Priority of Task{}".format(i + 1), ['High', 'Medium', 'Low'])

            compData = st.number_input("How much percentage of Task{} is completed".format(i + 1))

            if i == 0:
                deadline = st.date_input(
                    "When\'s the deadline for {}st Task {}".format(i + 1, name))

            elif i == 1:
                deadline = st.date_input(
                    "When\'s the deadline for {}nd Task {}".format(i + 1, name))

            elif i == 2:
                deadline = st.date_input(
                    "When\'s the deadline for {}rd Task {}".format(i + 1, name))

            else:
                deadline = st.date_input(
                    "When\'s the deadline for {}th Task {}".format(i + 1, name))

            deadline = str(deadline)

            if compData != 100:

                checker = 0

                DLD = str(datetime.strptime(deadline, "%Y-%m-%d"))

                if lastDate != "" and maxDate(lastDate, DLD) == DLD:
                    lastDate = maxDate(deadline, lastDate)
                    checker = 1

                if lastDate == "" and maxDate(today, DLD) == DLD:
                    lastDate = deadline
                    checker = 1

                if checker == 1:
                    DL = getDeadline(deadline)

                    st.write('Days Left for {} is:'.format(name), DL + 1)

                    currList.extend([priority, catg, DL, compData])
                    deadlines.append(DL)
                    tasks.append(name.upper())
                    listValues.append(currList)

                else:
                    delayedTasks.append(name.upper())

        for i in listValues:

            for j in range(3):

                if i[j] == 'High' or i[j] == 'Academics':
                    i[j] = 0
                elif i[j] == 'Low' or i[j] == 'Meetings':
                    i[j] = 1
                elif i[j] == 'Medium' or i[j] == 'Personal':
                    i[j] = 2
                elif i[j] == 'Professional':
                    i[j] = 3
                else:
                    i[j] = 4

        if st.button('Click to get Work Efficiency'):

            efficiencies = []

            # for i in listValues:
            #     st.text(i)

            for i in listValues:

                query = []

                for j in i:
                    query.append(j)

                query = np.array(query)
                query = query.reshape(1, -1)
                query1 = scaler.transform(query)

                eff = pipe.predict(query1)[0]
                efficiencies.append(eff)

            indices = []

            pos = 0

            # for i in efficiencies:
            #     st.text(i)

            for i in efficiencies:

                if i != 100:
                    indices.append(pos)

                pos += 1

            font_size = 28
            st.markdown(
                f"<h1 style='font-size: {font_size}px;'>Prioritise the above Tasks for Better Work Efficiency:-</h1>",
                unsafe_allow_html=True)

            arrSorted = []
            for i in range(len(indices)):
                elem = (indices[i], efficiencies[indices[i]])
                arrSorted.append(elem)

            arrSorted = Sort_Tuple(arrSorted)

            for i in range(len(indices)):
                st.title(str(i + 1) + "." + tasks[arrSorted[i][0]])

            if len(delayedTasks) != 0:
                st.write(
                    "<div style='color:#2368fb; text-align:left; font-weight:bold; "
                    "font-size:33px;'>List of Tasks which can't be completed 😔</div>",
                    unsafe_allow_html=True)

                for i in range(len(delayedTasks)):
                    st.title("{}. {}".format(i + 1, delayedTasks[i]))

            else:

                st.markdown(
                    f"<h1 style='font-size: {font_size}px;'>All the tasks can be finished successfully! 😎</h1>",
                    unsafe_allow_html=True)

            st.title(
                "Hi {}!, I am Jarvis, an AI Customised Tool Developed by Rashid Siddiqui, PoweredBy AIStorm.".format(
                    userName))

            st.markdown(
                f"<h1 style='font-size: {font_size}px;'>Here's a Personalised Schedule for you which will make sure "
                f"that all Tasks are completed on Time! 😊</h1>",
                unsafe_allow_html=True)

            # Create a schedule dataframe for user
            schedule = pd.DataFrame()

            currDay = 0
            lastDeadline = 0

            for i in deadlines:
                lastDeadline = max(lastDeadline, i)

            dates, tasksForDF, time = [], [], []

            # for i in arrSorted:
            #     st.text("{}-{}".format(i[0],i[1]))

            # st.title("Last DDL:{}".format(lastDeadline))

            # st.title("deadline:{}".format(deadlines[arrSorted[1][0]]))

            while currDay <= lastDeadline:

                posi = 0

                chk1, chk2, chk3, chk4 = 0, 0, 0, 0

                for j in range(len(indices)):

                    # if posi >= len(indices):
                    #     break

                    if deadlines[arrSorted[posi][0]] < currDay:
                        continue

                        # posi += 1
                        # while posi < len(indices):
                        #
                        #     if deadlines[arrSorted[posi][0]] < currDay:
                        #         posi += 1

                    if j == 0:

                        dates.append(datetime.now().date() + timedelta(days=currDay))
                        tasksForDF.append(tasks[arrSorted[posi][0]])
                        try:
                            time.append(highEff[0])
                        except:
                            try:
                                time.append(medEff[0])
                                chk1 = 1
                            except:
                                time.append(LowEff[0])
                                chk2 = 1

                    elif j == 1:
                        dates.append(datetime.now().date() + timedelta(days=currDay))
                        tasksForDF.append(tasks[arrSorted[posi][0]])
                        try:
                            time.append(highEff[1])
                            chk4 = 1
                        except:
                            if chk1 == 0:
                                try:
                                    time.append(medEff[0])

                                except:
                                    time.append(LowEff[0])

                            else:
                                try:
                                    time.append(medEff[1])
                                    chk3 = 1

                                except:
                                    time.append(LowEff[0])

                    else:

                        dates.append(datetime.now().date() + timedelta(days=currDay))
                        tasksForDF.append(tasks[arrSorted[posi][0]])

                        try:
                            time.append(highEff[2])

                        except:

                            if chk3 == 0 and chk4 == 1:
                                try:
                                    time.append(medEff[0])

                                except:
                                    time.append(LowEff[0])

                            elif chk3 == 0 and chk4 == 0:
                                try:
                                    time.append(medEff[1])

                                except:
                                    time.append(LowEff[0])

                            else:
                                try:
                                    time.append(medEff[2])
                                except:
                                    time.append(LowEff[0])

                    posi += 1

                currDay += 1

            schedule['DAY NO.'] = dates
            schedule['Tasks'] = tasksForDF
            schedule['TIME'] = time

            # adding styles to the schedule dataframe
            css = """
                    <style>
                    .dataframe {
                        color: grey;
                        background-color: #8b0000;
                        te
                        font-style: sans-serif;
                    }
                    </style>
                """
            st.markdown(css, unsafe_allow_html=True)

            styles = [
                dict(selector="th", props=[("color", "red")]),  # Header font color
                dict(selector="td", props=[("color", "white")]),  # Cell font color
            ]
            styled_table = schedule.style.set_table_styles(styles)

            # Displaying the personalised schedule to user.
            st.write(styled_table)

            image = Image.open("bottomPeople.png")

            # Display the image at the bottom
            st.image(image, use_column_width=True, caption="Footer Image")

            image = open('bottomPeople.png')

            if image is not None:
                # Save the uploaded image to a local file
                # with open("bottomPeople.png", "wb") as f:
                #     f.write(image.getbuffer())

                st.markdown(
                    """
                    <style>
                    .footer {
                        position: relative;
                        left: 0;
                        bottom: 0;
                        width: 100%;
                        text-align: center;
                        background-color: #7f1acb;
                        padding: 5px;
                    }

                    .footer h5 {
                        width: 100%;
                        max-height: 30px;
                        object-fit: contain;
                    }
                    </style>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    """
                    <div class="footer">
                        <h5>© 2023 EffiMax by AIStorm. All Right Reserved.</h5>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
