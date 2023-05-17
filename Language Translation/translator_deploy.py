import streamlit as st
import googletrans
from googletrans import Translator

# Set up the Google Translate API
translator = Translator(service_urls=['translate.google.com'])

# Define the Streamlit app
def app():
    # Set up the title and page layout
    st.set_page_config(page_title='Google Translate', layout='wide')
    st.title('Google Translate')

    # Define the text input and output areas
    input_text = st.text_area('Enter text to translate:', height=200)
    output_language = st.selectbox('Select output language:', options=googletrans.LANGUAGES.values())
    translate_button = st.button('Translate')

    def get_key(dict,val):
        for key, value in dict.items():
            if val == value:
                return key
    # Translate the input text when the button is clicked
    if translate_button:
        with st.spinner('Translating...'):
            output_text = translator.translate(input_text, dest=get_key(googletrans.LANGUAGES,output_language)).text
        st.write('Translation:', output_text)

# Run the app
if __name__ == '__main__':
    app()
