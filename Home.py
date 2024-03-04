import streamlit as st
from streamlit import errors
from Jarvis_API import model, train
import base64
from gtts import gTTS
from PIL import Image
from alarm import AlarmClock
import streamlit_authenticator as stauth
from google.api_core import exceptions
import Data as db


try:
    logo = Image.open('ironman_logo.jpg')
    st.set_page_config(page_title='JARVIS- Your AI assistant', page_icon=logo)
except errors.StreamlitAPIException:
    pass

# NOTE: To update any changes to code, run following commands in cmd, in the folder, 1. git add . | 2. git commit -m 'Changed ----' | 3. git push -u origin main
names = ['Joshua Sharma', 'Caleb Sharma', 'Pramila Sharma', 'Lakshya Sharma', 'Rachel']
usernames = ['admin', 'potty', 'susu', 'lulu', 'rach']
passwords = ['admin', 'potty', 'susu', 'lulu', 'rach@jarvis']
credentials = {"usernames":{}}

for un, name, pw in zip(usernames, names, passwords):
    user_dict = {"name":name,"password":pw}
    credentials["usernames"].update({un:user_dict})

if 'authentication_status' not in st.session_state:
    st.session_state['authentication_status'] = None
def get_session_value(key, default=None):
    return st.session_state.get(key, default)

authenticator = stauth.Authenticate(credentials,  'Jarvis_AI', 'starkTech', cookie_expiry_days=15)
name, authentication_status, username = authenticator.login()
st.session_state['authentication_status'] = authentication_status
auth_status = get_session_value('authentication_status')

def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio controls autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(md, unsafe_allow_html=True)

def tts(text):
    speech = gTTS(text, lang='en', tld='co.uk', slow=False)
    speech_file = "audio.mp3"
    speech.save(speech_file)
    autoplay_audio(speech_file)

if auth_status == False:
    st.error("Invalid Username or Password!")
if auth_status == None:
    st.warning("Please enter your Username and Password!")
if auth_status:
    #------INITIALIZE JARVIS
    chat = db.get_logs('admin')
    history = train + chat
    print(history)
    convo = model.start_chat(history=train)
    def response(prompt):
        if prompt is not None:
            convo.send_message(prompt)
            output = convo.last.text # type: ignore
            return output
    #------MAIN BODY------
    st.title("JARVIS - AI Assistant")
    st.header("Alpha Version 2.4.1")
    st.markdown("---")

    #-------SIDE BAR--------
    authenticator.logout('Logout', 'sidebar')
    st.sidebar.title(f"Hello, {name}!")
    st.sidebar.markdown('---')
    try:
        sound = st.sidebar.checkbox("Would you like JARVIS to speak?", value=True, key="sound_preference")
        if sound:
            st.sidebar.markdown("sound on! (**slower**)")
            talk = True
        if not sound:
            st.sidebar.markdown("sound off! (**faster**)")
            talk = False
    except errors.DuplicateWidgetID:
        pass

    if "convo" not in st.session_state:
        st.session_state.convo = []

    for message in st.session_state.convo:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Enter a Prompt")

    if prompt:
        with st.chat_message("user"):
            st.markdown(prompt)
        db.add_log(username, 'user', prompt)
        st.session_state.convo.append({"role": "user", "content": prompt})

    if 'alarm' in str(prompt) or 'remind' in str(prompt):
        systemPrompt = AlarmClock(prompt)
        if systemPrompt:
            response = 'Sir, your alarm has rung! Please be notified. Is there anything else i can help you with today?'
            with st.chat_message('assistant'):
                st.markdown(response)
            db.add_log(username, 'model', response)
            if talk:
                tts(response)
    elif prompt != None:
        c_prompt = str(prompt) + " Jarvis"
        try:
            response = response(c_prompt)
        except exceptions.RetryError:
            response = 'Sorry Sir, but you seem to be offline! Please get back online, for a seamless connection!'
        with st.chat_message("assistant"):
            st.markdown(response)
        db.add_log(username, 'model', response)
        if talk:
            tts(response)

        st.session_state.convo.append({"role": "assistant", "content" : response})