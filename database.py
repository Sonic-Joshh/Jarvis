import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json')

file = gspread.authorize(creds)
workbook = file.open("user_data_jarvis_ai")
sheet = workbook.sheet1

# Establishing a Google Sheets connection
conn = st.connection("gsheets", type=GSheetsConnection)

# Fetch existing vendors data
def add_log(username, role, parts):
    index = len(sheet.col_values(2)) + 1
    sheet.update(range_name=f'A{index}:C{index}', values=[[username, role, parts]])

#Get Vendor
def get_log(user):
    matrix = []
    rng = len(sheet.col_values(2))
    for i in range(rng):
        if sheet.row_values(i+1)[0] == user:
            matrix.append([sheet.row_values(i+1)[1],sheet.row_values(i+1)[2]])
    chat = []
    for log in matrix:
        if len(matrix) % 2 == 0:
            chat.append({'role': log[0], "parts": [log[1]]})
    return chat

# Delete Vendor
def delete_user(user):
    existing_data = conn.read(worksheet="Sheet1", usecols=[0, 1, 2], ttl=1)
    existing_data = existing_data.dropna(how="all")
    existing_data.drop(
        existing_data[existing_data["user"] == user].index,
        inplace=True,
    )
    conn.update(worksheet="Sheet1", data=existing_data)


