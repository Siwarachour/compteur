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
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg",
                            "data": image_data
                        }
    },
                    {
                        "type": "text",
                        "text": """
                                                    examine the provided image or text of the bank check and extract the
                                                    following information:
                                                     the account holder's full name, address (including street, city,
                                                     state, and ZIP code),
                                                    and phone number if available. Additionally, identify the bank's
                                                    name and address
                                                    (including street, city, state, and ZIP code), as well as the bank
                                                    routing number. Extract the check number,
                                                    date of issue, payee name, amount in numerical form, amount in
                                                    written form,
                                                     memo if present, and the signature of the account holder.
                                                    Lastly, capture the MICR line information, including the routing
                                                     number, account number, and check number. Ensure all details are
                                                     accurately captured and presented in a clear and structured format.
                                                    show the result in JSON format.
                                   """

                    },
                ]
            }

        ]

    )

    return message.content[0].text

st.set_page_config(page_title="analyseur de chèques des banques ")
st.title("analyseur de chèques des banques ")
uploaded_file = st.file_uploader("Choisissez une image d'un chéque .",
                                 type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Image téléchargée", use_column_width=True)
    # st.title("Analyser l'écriture manuscrite")

    if st.button("analyseur de chèques des banques"):
        with st.spinner("Analyse en cours..."):

            analysis = analyze_handwriting(image)
            st.subheader("Vérifier les informations:")
            st.write(analysis)


