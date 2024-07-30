import PyPDF2
import streamlit as st
import anthropic

anthropicSecretKey = "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"
client = anthropic.Anthropic(api_key=anthropicSecretKey)

def ask_claude(prompt, model="claude-3-opus-20240229"):
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        temperature=0,
        system="You are a helpful AI assistant.",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return message.content[0].text  # Example; adjust according to the actual response structure

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def analyze_pdf(file):
    text_content = extract_text_from_pdf(file)
    prompt = (f"Please provide a concise summary of the following PDF content."
              f" Focus on extracting only the most important information, key points, and notable details."
              f" Avoid including unnecessary details.\n\n{text_content}\n\nSummary:")

    return ask_claude(prompt)

st.set_page_config(page_title="PDF File Analyser", layout="wide")
st.markdown("""
<style>
    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
        background-color: #fafafa;
    }
    .main {
        max-width: 1200px;
        margin: 40px auto;
        padding: 20px;

        border-radius: 10px;

    }
    .uploader {
        margin-top: 20px;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 10px;
        background-color: #fff;
    }
    .analysis {
        margin-top: 20px;
        padding: 20px;
        background-color: #fff;
        border: 1px solid #ddd;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    .analysis h2 {
        font-weight: bold;
        margin-top: 0;
    }
    .analysis p {
        font-size: 16px;
        line-height: 24px;
        color: #333;
    }
</style>
""", unsafe_allow_html=True)
st.title("PDF File Analyser")
uploaded_file = st.file_uploader("Choose a PDF file.", type=["pdf"], key="uploader")

if uploaded_file is not None:
    with st.spinner("Analysing..."):
        analysis = analyze_pdf(uploaded_file)
        st.markdown(f"""
        <div class="analysis">
            <h2>Analysis Results:</h2>
            <p>{analysis}</p>
        </div>
        """, unsafe_allow_html=True)
