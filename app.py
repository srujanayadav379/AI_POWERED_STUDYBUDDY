import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# --- Load Gemini API Key ---
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("⚠️ Please set your GEMINI_API_KEY in a .env file.")
    st.stop()
genai.configure(api_key=api_key)

# --- Streamlit App UI ---
st.set_page_config(page_title="AI Study Buddy", page_icon="🎓", layout="wide")
st.title("🎓 AI-Powered Study Buddy (Google Gemini 2.5 Flash)")
st.write("Explain topics, summarize notes, and generate quizzes using **Google Gemini AI**.")

# Sidebar
st.sidebar.header("Options")
mode = st.sidebar.radio("Choose Task:", ["Explain Concept", "Summarize Notes", "Generate Quiz"])
temperature = st.sidebar.slider("Creativity Level", 0.0, 1.0, 0.3)

# Main Input
text_input = st.text_area("✏️ Enter your topic, notes, or text:")

# Generate Button
if st.button("🚀 Generate Result"):
    if text_input.strip():
        model = genai.GenerativeModel("gemini-2.5-flash")
        if mode == "Explain Concept":
            prompt = f"Explain this concept clearly and simply for a student:\n\n{text_input}"
        elif mode == "Summarize Notes":
            prompt = f"Summarize the following study notes into key points and a short summary:\n\n{text_input}"
        else:
            prompt = f"Generate 5 quiz questions with answers based on this content:\n\n{text_input}"

        with st.spinner("Generating with Gemini..."):
            try:
                response = model.generate_content(prompt)
                st.success("✅ Done!")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"❌ Gemini request failed: {e}")
    else:
        st.warning("Please enter some text first!")

st.caption("Powered by Google Gemini 2.5 Flash ⚡")
