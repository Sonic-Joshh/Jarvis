import streamlit as st
from streamlit import errors
import Jarvis_API 
import base64
from gtts import gTTS
from pydub import AudioSegment
from pydub.effects import speedup
from PIL import Image

logo = Image.open('C:/Users/JC/OneDrive/Desktop/PYTHON BEGGINERS/A_Jarvis_WebApp/ironman_logo.jpg')
st.set_page_config(page_title='JARVIS- Your AI assistant', page_icon=logo)


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
    audio = AudioSegment.from_mp3("audio.mp3")
    sped_up_audio = speedup(audio, 1.3, 50)
    sped_up_audio.export("sped_audio.mp3", format="mp3")# Speeds up the play
    autoplay_audio(speech_file) # Switch to this for sped up responses but it will take longer: sped_audio.mp3

st.title("JARVIS - AI Assistant")
st.header("Beta Version 1.4")
st.markdown("---")

st.sidebar.title("Personalisation Options")
st.sidebar.markdown("---")
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
st.sidebar.markdown("---")

if "convo" not in st.session_state:
    st.session_state.convo = []

for message in st.session_state.convo:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Enter a Prompt")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
        

    st.session_state.convo.append({"role": "user", "content": prompt})


if prompt != None and prompt != "None":
    c_prompt = str(prompt) + " Jarvis"
    response = Jarvis_API.response(c_prompt)
    with st.chat_message("assistant"):
        st.markdown(response)

    if talk:
        tts(response)

    st.session_state.convo.append({"role": "assistant", "content" : response})
