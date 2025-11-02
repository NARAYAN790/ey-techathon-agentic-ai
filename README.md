🏥 Agentic AI for Provider Data Validation and Directory Management

An EY Techathon 6.0 Project (Challenge VI – Firstsource) built with Google Gemini API + Streamlit

🚨 Problem Statement
Healthcare payers maintain millions of provider records — names, addresses, contact info, and licenses — yet 40–80% of this data is inaccurate.
Manual validation is time-consuming, error-prone, and expensive, leading to member frustration, regulatory risks, and operational inefficiency.

💡 Our Solution
We built an Agentic AI system that autonomously validates, enriches, and manages healthcare provider data using AI-driven document understanding + public data APIs.

Users can:
📂 Upload provider directories or scanned PDFs
🔍 Automatically validate contact and license information
📊 View enriched profiles with confidence scores
❓ Ask queries (e.g., “Which providers have missing licenses?”)
⬇️ Export validated data and reports (PDF/TXT)

This empowers healthcare payers to maintain accurate, compliant, and updated provider directories — cutting down manual work and improving patient experience.

✨ Core Features
🩺 Provider Validation Agent → Cross-verifies names, contact info, and licenses using NPI Registry, Google Maps, and public APIs
🧠 Information Enrichment Agent → Fills missing fields like specialties, affiliations, certifications
📄 Document Parser → Extracts structured data from PDFs and scanned forms
📊 Quality Assurance Agent → Flags inconsistencies, generates confidence scores, and prepares validation reports
🌐 Multi-Language Support → English ↔ Hindi ↔ Marathi ↔ Tamil
⬇️ Export Options → Download validated reports as PDF or TXT

🛠️ Tech Stack
⚡ Streamlit → UI Framework
🤖 Google Gemini API → AI backend
📄 PyPDF2 → PDF data extraction
🖨️ FPDF → Report export
🌍 BeautifulSoup + Requests → Web scraping for data validation
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


🧭 Judge Walkthrough
1️⃣ Upload a provider directory (CSV or scanned PDF)
2️⃣ View auto-validated profiles with enriched data
3️⃣ Ask: “Which providers have outdated licenses?” → AI explains clearly
4️⃣ View confidence scores and flagged entries
5️⃣ Export final validated provider directory

💡 Future Extensions
☁️ Vertex AI Integration → Scale for enterprise use
📱 Gemma Deployment → On-device privacy-focused version
🔗 API Integration → NPI Registry, State Medical Boards, Google Maps
⚙️ Automated Scheduling → Daily re-validation of provider records

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
