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
                              {
   "Analysez l'écriture manuscrite visible dans cette image en français.
    Décrivez les caractéristiques observées et ce qu'elles pourraient indiquer sur l'auteur, en incluant des aspects comme la pression, l'inclinaison, la taille, l'espacement et tout autre élément notable.
    Présentez votre analyse sous forme de liste numérotée, en commençant directement par le premier point sans introduction ni titre.
    Ajoutez une conclusion à la fin de l'analyse.
    Présentez le résultat en JSON."
}


                        """

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

