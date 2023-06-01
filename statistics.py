import streamlit as st
import app

def stats():

    btn = st.button("Productivity Booster",help="This will help to boost your efficiency!")

    if btn:
        app.assistUser()

        return

    st.title('General Employee Productivity Statistics')

    # Create an unordered list
    # items = ["Item 1", "Item 2", "Item 3"]
    # st.write("Here is an unordered list:")
    # st.write(items)

    st.markdown(
        """
        <style>
        ul {
            list-style-type: square;
            margin-left: 20px;
            color: #0c3030;
        }
        </style>
        """
        "<ul>"
        "<li>A study by academics at the University of California, Irvine found that workers are interrupted every three minutes and five seconds on average. And they take 23 minutes plus 15 seconds while attempt to get back on track.</li>"
        "<li>The typical employee is only productive for 60% of the day across all professions. But for office workers, that proportion dramatically declines. According to Voucher Cloud’s research, the average office worker is barely productive for two hours and 23 minutes per day.</li>"
        "<li>A highly engaged team can experience 41% reduction in absenteeism, 59% less turnover and 28% less internal theft.</li>"
        "</ul>",

        unsafe_allow_html=True
    )

    st.image('Productivity.png')

    st.title('Statistics Showing Loss of Businesses Owing to Employee Productivity')

    st.markdown(
        """
        <style>
        ul {
            list-style-type: square;
            margin-left: 20px;
            color: #0c3030;
        }
        </style>
        """
        "<ul>"
        "<li>Employers Loses Over $150 Billion Per Year Owing to Employee Obesity and Other Chronic Health Issues.</li>"
        "<li>Employees spend most of their time on social media like Facebook which Costs Businesses $28 Billion Per Year.</li>"
        "<li>Employers lose approximately 24 billion hours annually due to unproductive meetings resulting in reduced productivity at the workplace.</li>"
        "</ul>",

        unsafe_allow_html=True
    )

    st.title("Credits for Statistics [Quixy](https://quixy.com/)")

    # st.title('Credits for Statistics : {}'.format('quixy.com'))




