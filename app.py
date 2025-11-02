import streamlit as st
import google.generativeai as genai
import PyPDF2
import os
from fpdf import FPDF

# ---------------------------
# 0) API Configuration
# ---------------------------
API_KEY = st.secrets.get("GEMINI_API_KEY", os.getenv("GEMINI_API_KEY", ""))
genai.configure(api_key=API_KEY)
st.sidebar.text(f"API Key Loaded: {bool(API_KEY)}")

# ---------------------------
# 1) Page Config + Header
# ---------------------------
st.set_page_config(page_title="EY Techathon 6.0 – Agentic AI for Healthcare", layout="wide")
st.title("🏥 Agentic AI for Provider Data Validation and Directory Management")

st.markdown("""
Welcome to **EY Techathon 6.0 – Challenge VI (Firstsource)** 💡  

This AI tool automates **Provider Data Validation and Directory Management** using the **Google Gemini API**.

Key Capabilities:
- 📄 Validate provider credentials (license, contact info, affiliations)
- 🧠 Auto-fill missing details via AI Enrichment
- 🌐 Translate directories (English ↔ Hindi/Tamil/Marathi)
- ❓ Ask questions from uploaded provider datasets
- 📊 Summarize reports or directory insights

Powered by **Streamlit + Gemini 2.5 Flash Lite**
""")
st.divider()

# ---------------------------
# 2) Sidebar
# ---------------------------
mode = st.sidebar.selectbox(
    "Select Mode",
    [
        "Provider Data Validation",
        "Data Enrichment Agent",
        "Summarize Mode",
        "Translate Mode",
        "Chat Mode"
    ]
)

lang = st.sidebar.selectbox("Output Language", ["English", "Hindi", "Marathi", "Tamil"])
tone_note = f"Answer in simple {lang}."

uploaded_file = st.sidebar.file_uploader("📂 Upload Provider Data (PDF/TXT)", type=["pdf", "txt"])

# ---------------------------
# 3) Session State
# ---------------------------
if "doc_text" not in st.session_state:
    st.session_state.doc_text = ""
if "last_output" not in st.session_state:
    st.session_state.last_output = ""
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------------
# 4) Helper Functions
# ---------------------------
def extract_text_from_upload(file) -> str:
    if not file:
        return ""
    try:
        if file.type == "text/plain":
            return file.read().decode("utf-8", errors="ignore")
        elif file.type == "application/pdf":
            reader = PyPDF2.PdfReader(file)
            text = []
            for i, page in enumerate(reader.pages):
                try:
                    text.append(page.extract_text() or "")
                except Exception:
                    text.append(f"[⚠️ Could not extract text from page {i+1}]")
            return "\n".join(text)
        else:
            return "⚠️ Unsupported file format."
    except Exception as e:
        return f"⚠️ Error reading file: {e}"

def gemini_text(prompt: str) -> str:
    try:
        model = genai.GenerativeModel("gemini-2.5-flash-lite")
        resp = model.generate_content(prompt)
        return resp.text.strip() if resp.text else "⚠️ No response from Gemini."
    except Exception as e:
        return f"⚠️ Gemini error: {e}"

def make_pdf_bytes(title: str, content: str) -> bytes:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 8, title)
    pdf.ln(4)
    pdf.multi_cell(0, 6, content)
    return pdf.output(dest="S").encode("latin-1")

def split_text_into_chunks(text, chunk_size=1200, overlap=200):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

# ---------------------------
# 5) Provider Data Validation
# ---------------------------
if mode == "Provider Data Validation":
    st.subheader("✅ Provider Data Validation")

    if uploaded_file:
        st.session_state.doc_text = extract_text_from_upload(uploaded_file)

    if st.session_state.doc_text:
        with st.expander("📜 Preview Extracted Text", expanded=False):
            st.text_area("Extracted Data", st.session_state.doc_text[:8000], height=200)

        if st.button("🔍 Validate Records"):
            with st.spinner("Validating provider data…"):
                prompt = f"""
You are an AI data validator for healthcare provider directories.
Validate the following records:
- Identify missing or outdated fields (phone, address, license)
- Highlight inconsistencies and expired data
- Suggest corrections concisely
{tone_note}

Data:
{st.session_state.doc_text}
"""
                st.session_state.last_output = gemini_text(prompt)

        if st.session_state.last_output:
            st.subheader("📊 Validation Report")
            st.write(st.session_state.last_output)

            txt_bytes = st.session_state.last_output.encode("utf-8")
            st.download_button("⬇️ Download (TXT)", data=txt_bytes, file_name="validation_report.txt")
            pdf_bytes = make_pdf_bytes("Provider Validation Report", st.session_state.last_output)
            st.download_button("⬇️ Download (PDF)", data=pdf_bytes, file_name="validation_report.pdf")

        q = st.text_input("❓ Ask about the data (e.g. 'Which providers need re-verification?')")
        if st.button("🔎 Get Answer"):
            if q.strip():
                with st.spinner("Analyzing..."):
                    qa_prompt = f"Based on this provider data, answer: {q}. {tone_note}\n\n{st.session_state.doc_text}"
                    st.write(gemini_text(qa_prompt))
            else:
                st.warning("Enter a question first.")
    else:
        st.info("⬅️ Upload a provider data file to start.")

# ---------------------------
# 6) Data Enrichment Agent
# ---------------------------
elif mode == "Data Enrichment Agent":
    st.subheader("🧠 Provider Data Enrichment")

    if uploaded_file:
        st.session_state.doc_text = extract_text_from_upload(uploaded_file)

    if st.session_state.doc_text:
        if st.button("✨ Enrich Data"):
            with st.spinner("Filling missing details…"):
                prompt = f"""
You are an AI data enrichment agent for healthcare directories.
For the following provider data:
- Identify missing specializations, licenses, affiliations.
- Suggest realistic values if possible.
- Maintain structured, clear output.
{tone_note}

Data:
{st.session_state.doc_text}
"""
                st.session_state.last_output = gemini_text(prompt)
        if st.session_state.last_output:
            st.subheader("📈 Enriched Provider Data")
            st.write(st.session_state.last_output)
    else:
        st.info("⬅️ Upload provider file to enrich data.")

# ---------------------------
# 7) Summarize Mode
# ---------------------------
elif mode == "Summarize Mode":
    st.subheader("🧾 Summarize Provider Dataset")
    uploaded_file = st.file_uploader("Upload provider report", type=["pdf", "txt"])
    if uploaded_file:
        text = extract_text_from_upload(uploaded_file)
        if st.button("🧠 Summarize"):
            with st.spinner("Summarizing report…"):
                st.session_state.last_output = gemini_text(f"Summarize this provider directory in {lang}. {tone_note}\n\n{text}")
        if st.session_state.last_output:
            st.write(st.session_state.last_output)
    else:
        st.info("⬅️ Upload provider directory or report to summarize.")

# ---------------------------
# 8) Translate Mode (Multi-language)
# ---------------------------
elif mode == "Translate Mode":
    st.subheader("🌐 Multi-Language Translation")
    user_input = st.text_area("Enter text to translate:")
    target_lang = st.selectbox("Target Language", ["English", "Hindi", "Marathi", "Tamil"])
    if st.button("🌍 Translate"):
        with st.spinner("Translating..."):
            prompt = f"Translate this healthcare text into {target_lang}:\n\n{user_input}"
            st.write(gemini_text(prompt))

# ---------------------------
# 9) Chat Mode
# ---------------------------
else:
    st.subheader("💬 Healthcare Chatbot")
    user_input = st.text_input("Ask me anything about healthcare data management:")
    if st.button("Send") and user_input:
        st.session_state.messages.append(("user", user_input))
        bot_response = gemini_text(f"{user_input}\n\n{tone_note}")
        st.session_state.messages.append(("bot", bot_response))

    for sender, msg in st.session_state.messages:
        if sender == "user":
            st.chat_message("user").write(msg)
        else:
            st.chat_message("assistant").write(msg)
