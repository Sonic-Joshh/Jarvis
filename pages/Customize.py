import streamlit as st
from PIL import Image

logo = Image.open('ironman_logo.jpg')
st.set_page_config(page_title='JARVIS- Your AI assistant', page_icon=logo)

st.title("You can let Jarvis know information about you so it can  assist you better!")
u_input =  st.text_input("Tell me something  about yourself", max_chars=200)
st.write("PS: to save changes please reload the home page!")

file_name = 'user_data.txt'

def save_value(input_data, filename):
    with open(filename, 'w') as f:
        f.write(input_data)

save_value(u_input, filename=file_name)