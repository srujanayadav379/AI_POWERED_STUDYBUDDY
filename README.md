# AI Study Buddy (Google Gemini)

A Streamlit web app that helps students study smarter by using **Google Gemini 2.5 Flash** to:
- Explain complex topics in simple terms
- Summarize study notes
- Generate quizzes or flashcards

## Setup Instructions

### 1️⃣ Prerequisites
- Python 3.10+
- VS Code or any IDE
- Free Gemini API key → [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

### 2️⃣ Installation
```bash
pip install -r requirements.txt
```

### 3️⃣ Add API Key
Create a `.env` file in the project root and add:
```
GEMINI_API_KEY=your_google_gemini_api_key_here
```

### 4️⃣ Run Locally
```bash
streamlit run app.py
```
Then open [http://localhost:8501](http://localhost:8501)

### 5️⃣ Deploy to Google Cloud Run
```bash
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/ai-study-buddy
gcloud run deploy ai-study-buddy         --image gcr.io/YOUR_PROJECT_ID/ai-study-buddy         --platform managed         --region asia-south1         --allow-unauthenticated         --set-env-vars GEMINI_API_KEY=your_google_gemini_api_key_here
```

---
🧠 **Tip:** Gemini 2.5 Flash is fast, free, and excellent for educational AI projects.
