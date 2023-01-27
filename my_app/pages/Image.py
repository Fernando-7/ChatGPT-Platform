import streamlit as st
import openai
from PIL import Image
import json
from openapi_schema_to_json_schema import to_json_schema
openai.api_key = st.secrets["api_secret"]

st.markdown("# Buscador de Imagens 🖼️")
st.sidebar.markdown("Buscador de Imagens 🖼️")

def chatbot_response_image(prompt):
    image_resp = openai.Image.create(
        prompt=prompt, 
        n=4, 
        size="512x512")
    return image_resp

with st.form(key = 'my_form', clear_on_submit = True):
    user_input = st.text_input("Descreva o que você quer ver")
    submit_button = st.form_submit_button(label = 'Buscar')

if user_input:
    value = chatbot_response_image(user_input)
    options = {"supportPatternProperties": True}
    converted = to_json_schema(value, options)
    st.image(converted['data'][0]['url'])
