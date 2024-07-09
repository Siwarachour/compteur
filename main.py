import streamlit as st
import base64
#from PIL import Image
#import io

uploaded_files = st.file_uploader("Choose a  file", accept_multiple_files=True)
for uploaded_file in uploaded_files:

    if uploaded_file is not None:
        bytes_data = uploaded_file.read()

        base64_bytes = base64.b64encode(bytes_data)

        base64_string = base64_bytes.decode('utf-8')

        # print(base64_string)
        st.image(uploaded_file)
        st.write(base64_string)
    else:
        st.write('Please upload a correct image ')


