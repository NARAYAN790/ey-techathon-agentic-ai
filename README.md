
🏥 Agentic AI for Provider Data Validation and Directory Management

An EY Techathon 6.0 Project built with Google Gemini API + Streamlit

🚨 Problem Statement
Healthcare payers maintain millions of provider records (doctors, clinics, hospitals) with 40–80% inaccurate information—wrong phone numbers, outdated addresses, expired licenses, and missing credentials.
Manual validation is slow, inconsistent, and expensive, leading to patient frustration, compliance risks, and inefficient healthcare delivery.

💡 Our Solution
We built an Agentic AI system that autonomously validates, enriches, and manages healthcare provider data from scanned documents and public APIs.

Users can:
📂 Upload provider credential PDFs or CSV data
🔍 Get verified and enriched profiles with confidence scores
📊 View discrepancies and recommended actions
⬇️ Export updated records and summary reports

This enables healthcare organizations to maintain accurate, compliant, and up-to-date provider directories with minimal manual effort.

✨ Core Features
🩺 Provider Validation Agent → Verifies names, contact info, and license numbers using public APIs
🧠 Information Enrichment Agent → Fills missing fields (specializations, affiliations, certifications)
📄 Document Parser → Extracts key data from scanned or uploaded PDFs
📊 Quality Assurance Agent → Cross-checks and flags inconsistencies, generates confidence scores
⬇️ Report Generator → Exports validated records as PDF or TXT

🔮 Bonus Features (future scope):
🌐 Multi-language translation (English ↔ Hindi)
💬 Chat Mode for custom queries (e.g., “Which providers need re-verification?”)
📅 Automated daily validation cycles via scheduled tasks

🛠️ Tech Stack
⚡ Streamlit → Frontend UI Framework
🤖 Google Gemini API → AI backend for text comprehension and validation
📄 PyPDF2 → PDF data extraction
🖨️ FPDF → Export validated records
🌍 BeautifulSoup / Requests → Web scraping for provider websites
🐍 Python 3.10+

🚀 Run Locally & Setup

🟢 Step 1: Clone the repository
git clone https://github.com/NARAYAN790/ey-techathon-agentic-ai.git

🔵 Step 2: Navigate into project folder
cd ey-techathon-agentic-ai

🟣 Step 3: Create a virtual environment
python -m venv venv

🟠 Step 4: Activate the environment
Windows: venv\Scripts\activate
Mac/Linux: source venv/bin/activate

🟡 Step 5: Install dependencies
pip install -r requirements.txt

🔴 Step 6: Add your API key
Create/Edit .streamlit/secrets.toml and add:
GEMINI_API_KEY = "your-api-key-here"

⚫ Step 7: Run the Streamlit app
streamlit run app.py


🌐 Demo Flow
1️⃣ Upload sample provider dataset or scanned credential PDF
2️⃣ The AI agent validates names, contact info, and licenses
3️⃣ View a summary report with discrepancies and confidence scores
4️⃣ Export results as PDF/TXT
5️⃣ (Optional) Explore translation or custom chat validation modes

💡 Future Extensions
☁️ Vertex AI → Scale for enterprise-level directory validation
📱 Gemma → On-device deployment for healthcare privacy
🔗 API Integration → Direct sync with NPI Registry, State License APIs, and Google Maps

👨‍💻 Author
Narayan Gupta
🎓 B.Tech in Electronics & Communication – Dr. A.I.T.D Kanpur
💡 Interests: AI, NLP, Data Science, Generative AI

🌐 LinkedIn
 | 🌐 GitHub
 | 🌐 Project Repo

🏆 Acknowledgements
Developed for EY Techathon 6.0 – Challenge VI (Firstsource)
Powered by Google Gemini API + Streamlit
