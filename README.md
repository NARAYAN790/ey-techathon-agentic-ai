🏥 Agentic AI for Provider Data Validation and Directory Management

An EY Techathon 6.0 Project built with Google Gemini API + Streamlit

🚨 Problem Statement
Healthcare payers maintain millions of provider records — names, addresses, contact info, and licenses — yet 40–80% of this data is inaccurate.
Manual validation is time-consuming, error-prone, and expensive, causing patient frustration, compliance risks, and inefficient operations.

💡 Our Solution
We built an Agentic AI-powered system that autonomously validates and enriches healthcare provider data using AI-driven document understanding and public data APIs.

Users can:
📂 Upload provider directories or credential PDFs  
🔍 View verified and corrected details instantly  
📊 Check confidence scores and flagged inconsistencies  
⬇️ Export updated records in PDF or TXT formats  

This reduces human effort, ensures accuracy, and keeps directories compliant and up to date.

✨ Core Features
🩺 Provider Validation Agent → Cross-verifies contact info via NPI Registry, Google Maps, and public APIs  
🧠 Information Enrichment Agent → Fills missing details (specialties, affiliations, licenses)  
📄 Document Parser → Extracts structured data from scanned PDFs and text files  
📊 Quality Assurance Agent → Generates confidence scores and highlights errors  
⬇️ Export Options → Download validated reports and provider profiles  

🔮 Bonus Features (Future Scope):
🌐 Multi-language support (English ↔ Hindi)  
🧾 OCR for handwritten forms  
⚙️ Automated daily validation scheduler  

🛠️ Tech Stack
⚡ Streamlit → Interactive UI framework  
🤖 Google Gemini API → AI backend for data extraction & reasoning  
📄 PyPDF2 / FPDF → For reading and exporting documents  
🌍 BeautifulSoup + Requests → Web scraping and data validation  
🐍 Python 3.10+  

---

🧭 Judge Walkthrough
1️⃣ Upload a sample provider dataset (CSV or scanned PDF)  
2️⃣ The AI validates each provider’s data and highlights inconsistencies  
3️⃣ View summarized validation report with confidence scores  
4️⃣ Export updated provider directory as PDF or TXT  
5️⃣ (Optional) Ask: “Which providers have missing licenses?”  

---

💡 Future Extensions
☁️ Vertex AI Integration → For scalable data pipelines  
📱 Gemma Deployment → Lightweight on-device privacy version  
🔗 API Expansion → Connect to state medical boards and insurance registries  

👨‍💻 Author  
Narayan Gupta  
🎓 B.Tech in Electronics & Communication – Dr. A.I.T.D Kanpur  
💡 Interests: AI, NLP, Data Science, Generative AI  

🌐 [LinkedIn](https://www.linkedin.com/in/narayan-gupta-19903028b) | 🌐 [GitHub](https://github.com/NARAYAN790) | 🌐 [Project Repo](https://github.com/NARAYAN790/ey-techathon-agentic-ai)  

🏆 Acknowledgements  
Developed for **EY Techathon 6.0 – Challenge VI (Firstsource)**  
Powered by **Google Gemini API + Streamlit**

