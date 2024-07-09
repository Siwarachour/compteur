# This is a Handwriting Analyzer Python script.
import base64
import time
import anthropic
import streamlit as st
from PIL import Image
from io import BytesIO

anthropicSecretKey = "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"

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=anthropicSecretKey,
)


def analyze_handwriting(image_param):
    buffered = BytesIO()
    image_param.save(buffered, format="JPEG")
    image_data = base64.b64encode(buffered.getvalue()).decode()
    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1000,
        temperature=0,
        messages=[
            {
                "role": "user",

                "content": [
                    {
                        "type": "text",
                        "text": "Hi"
                    }
                ]
            }
        ]
    )
    return message.content[0].text


st.set_page_config(page_title="Analyser l'écriture manuscrite")
st.title("Analyser l'écriture manuscrite")
uploaded_file = st.file_uploader("Choisissez une image d'écriture manuscrite ou de signature.",
                                 type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Image téléchargée", use_column_width=True)
    # st.title("Analyser l'écriture manuscrite")

    if st.button("Analyser l'écriture manuscrite"):
        with st.spinner("Analyse en cours..."):

            analysis = analyze_handwriting(image)
            st.subheader("Résultats de l'analyse:")
            st.write(analysis)

