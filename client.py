import requests
import streamlit as st
import json


st.title("Translator")
#st.snow()


language={
    "Hindi": "en",
    "Urdu": "en",
    "Tamil": "en",
    "French": "en",
    "English":"en"

}
default_index = list(language.keys()).index("Hindi")
option = st.selectbox(
    "Select Language",
    language,
    index=default_index,
    placeholder="Select"
)

 
def get_groq_response(input_text):
    json_body={
  "input": {
    "language": f"{option}",
    "text": f"{input_text}"
  },
  "config": {},
  "kwargs": {}
}

    response=requests.post("http://127.0.0.0:8000/chain/invoke",json=json_body)
    response_json = response.json()
    output = response_json["output"]
    return output

input_text=st.text_input("Enter the text you want to convert to "f"{option}")

if input_text:
    st.write(get_groq_response(input_text))
