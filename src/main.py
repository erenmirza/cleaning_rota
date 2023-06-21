import streamlit as st
import pandas as pd
import datetime

my_date = datetime.date.today()
year, week_num, day_of_week = my_date.isocalendar()  # Using isocalendar() function

kieran_task_set = (week_num % 3) + 1
zoeb_task_set = (kieran_task_set % 3) + 1
eren_task_set = (zoeb_task_set % 3) + 1


df = pd.read_csv('src/task_sets.csv')
kieran_df = df[df['Task Set'] == kieran_task_set]
zoeb_df = df[df['Task Set'] == zoeb_task_set]
eren_df = df[df['Task Set'] == eren_task_set]

# Setup
st.set_page_config(layout="wide")
st.header('New Gaff Cleaning Rota')
st.subheader(f'Week Number: {week_num}')
col1, col2, col3 = st.columns(3)

# Column 1
col1.header("Kieran")
col1.subheader(f'Task Set: {kieran_task_set}')
col1.dataframe(kieran_df['Tasks'])

# Column 2
col2.header("Zoeb")
col2.subheader(f'Task Set: {zoeb_task_set}')
col2.dataframe(zoeb_df['Tasks'])

# Column 3
col3.header("Eren")
col3.subheader(f'Task Set: {eren_task_set}')
col3.dataframe(eren_df['Tasks'])
