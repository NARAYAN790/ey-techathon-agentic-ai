🏥 Agentic AI for Provider Data Validation & Directory Management

An EY Techathon 6.0 Project
Built with Google Gemini API + Streamlit

🚨 Problem Statement

Healthcare payers maintain millions of provider records — names, addresses, contact info, and licenses — yet 40–80% of this data is inaccurate.
Manual validation is slow, error-prone, and costly, leading to member frustration, compliance risks, and inefficiency.

💡 Our Solution

We developed an Agentic AI-powered system that autonomously validates and enriches healthcare provider data using AI-driven document understanding and public APIs.

Users can:

📂 Upload provider credential PDFs or CSV data

🔍 View verified and enriched profiles with confidence scores

📊 See discrepancies and recommended actions

⬇️ Export updated records and summary reports

This reduces manual effort, ensures data accuracy, and keeps directories compliant and up to date.

✨ Core Features

🩺 Provider Validation Agent → Cross-verifies contact info via NPI Registry, Google Maps, and public APIs

🧠 Information Enrichment Agent → Fills missing fields (specializations, affiliations, certifications)

📄 Document Parser → Extracts structured data from scanned PDFs

📊 Quality Assurance Agent → Generates confidence scores and flags inconsistencies

🌐 Multi-Language Support → Auto-translation between English and Hindi

⬇️ Report Generator → Exports validated records (PDF/TXT)

🛠️ Tech Stack

⚡ Streamlit – Interactive UI framework

🤖 Google Gemini API – AI backend for validation & reasoning

📄 PyPDF2 / FPDF – Text extraction & PDF export

🌍 BeautifulSoup + Requests – Web scraping for public data

🐍 Python 3.10+

🚀 Run Locally

# 1️⃣ Clone the repository
git clone https://github.com/NARAYAN790/ey-techathon-agentic-ai.git
cd ey-techathon-agentic-ai

# 2️⃣ Create & activate virtual environment
python -m venv venv
venv\Scripts\activate   # on Windows
# source venv/bin/activate  # on Mac/Linux

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Add your Gemini API key
# Edit .streamlit/secrets.toml
GEMINI_API_KEY = "your-api-key-here"

# 5️⃣ Run the app
streamlit run app.py


🧭 Judge Walkthrough


Upload a sample provider dataset (CSV or scanned PDF)


The AI validates each provider record and highlights errors


View a summary report with confidence scores


Export updated directory as PDF/TXT


(Optional) Ask: “Which providers have missing licenses?”



💡 Future Extensions


☁️ Vertex AI Integration – Enterprise-scale data pipelines


📱 Gemma Deployment – On-device privacy version


🔗 API Expansion – Integration with state medical boards & insurance registries



👨‍💻 Author
Narayan Gupta
🎓 B.Tech (Electronics & Communication) – Dr. A.I.T.D Kanpur
💡 Interests: AI, NLP, Data Science, Generative AI
🌐 LinkedIn | GitHub | Project Repo

🏆 Acknowledgements
Developed for EY Techathon 6.0 – Challenge VI (Firstsource)
Powered by Google Gemini API + Streamlit


