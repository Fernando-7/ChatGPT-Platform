import streamlit as st
from streamlit_chat import message
import openai
from PIL import Image
import json
from openapi_schema_to_json_schema import to_json_schema
openai.api_key = st.secrets["api_secret"]

st.markdown("# Converse Comigo 💬")
st.sidebar.markdown("Converse Comigo 💬")


def chatbot_response(prompt):
     completion = openai.Completion.create(
          engine = 'text-davinci-003',
          prompt = prompt,
          max_tokens = 2048,
          stop = None,
          temperature = 0.7
     )

     return (completion.choices[0].text)

def get_text():
    input_text = st.text_input("Diga alguma coisa", key="conversation")
    return input_text 

with st.form(key = 'my_form', clear_on_submit = True):
    user_input = st.text_input("Diga alguma coisa")
    submit_button = st.form_submit_button(label = 'Enviar')
#user_input = get_text()

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

if submit_button:
    bot_output = chatbot_response(user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(bot_output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')