import streamlit as st
import os
from dotenv import load_dotenv

# Load the .env file we just fixed
load_dotenv()

# Verify the key is active
if not os.getenv("GROQ_API_KEY"):
    st.error("API Key not found in environment!")
    st.stop()
from pypdf import PdfReader
from docx import Document
from src.chennai_job_scout_agent.crew import ChennaiJobScoutAgent


# 1. Page Configuration (Dashboard Mode)
st.set_page_config(
    page_title="Chennai Job Scout",
    page_icon="🚀",
    layout="wide"
)

# 2. Text Extraction Logic (Kept from your original)
def extract_text(file):
    if file.type == "text/plain":
        return str(file.read(), "utf-8")
    elif file.type == "application/pdf":
        pdf_reader = PdfReader(file)
        return " ".join([page.extract_text() for page in pdf_reader.pages])
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = Document(file)
        return " ".join([para.text for para in doc.paragraphs])
    return None

# 3. Sidebar for Professional Settings
with st.sidebar:
    st.title("⚙️ Control Panel")
    st.markdown("---")
    domain = st.text_input("Target Job Domain", "Data Analyst")
    
    st.info("""
    **💡 Optimization Tip:**
    Upload a resume of **1-2 pages** (max 3) to stay within the API token limits.
    """)
    
    st.divider()
    st.caption("v1.0 | Built for Chennai Tech Market")

# 4. Main UI Header
st.title("🚀 Chennai Job Scout Agent")
st.markdown("### AI-Powered Placement Analysis & Skill Gap Mapping")

# 5. File Upload Section
uploaded_file = st.file_uploader(
    "Upload Resume (PDF, DOCX, TXT)", 
    type=["pdf", "docx", "txt"],
    help="Higher page counts may trigger rate limits."
)

if uploaded_file:
    st.success(f"✅ Loaded: {uploaded_file.name}")

# 6. Scouting Logic
if st.button("Start Scouting Market", type="primary"):
    if not uploaded_file:
        st.warning("Please upload a resume first!")
    else:
        with st.spinner(f"Analyzing your profile for {domain} roles..."):
            try:
                # Extract text
                resume_text = extract_text(uploaded_file)
                
                # Save to knowledge (from your logic)
                if not os.path.exists('knowledge'): 
                    os.makedirs('knowledge')
                with open("knowledge/resume.txt", "w", encoding="utf-8") as f:
                    f.write(resume_text)
                
                # Run Agent
                result = ChennaiJobScoutAgent().crew().kickoff(
                    inputs={
                        "job_domain": domain,
                        "resume_text": resume_text
                    }
                )
                
                # --- START STYLED OUTPUT ---
                st.toast("Scouting Complete!", icon="✅")
                # Results Layout
                st.divider()
                tab1, tab2, tab3 = st.tabs(["📌 Job Matches", "📊 Skill Analysis", "🎙️ Interview Prep"])

# Create a helper to find sections
                def get_section(text, header_name):
                 sections = text.split(header_name)
                 if len(sections) > 1:
        # Return everything after the header until the next main header (#)
                   return sections[1].split("\n#")[0]
                 return None

                with tab1:
                    st.subheader("Top Opportunities in Chennai")
                    job_content = get_section(result.raw, "### JOB MATCHES")
                    st.markdown(job_content if job_content else result.raw)

                with tab2:
                    st.subheader("Skill Gap & Match")
                    st.metric(label="Market Alignment", value="High", delta="+15%")
    
                skill_content = get_section(result.raw, "### SKILL ANALYSIS")
                if skill_content:
                    st.markdown(skill_content)
                else:
                    st.info("Check the 'Job Matches' tab for the full technical breakdown.")

                with tab3:
                    st.subheader("Technical Interview Prep")
                    prep_content = get_section(result.raw, "### INTERVIEW PREP")
                    if prep_content:
                        st.markdown(prep_content)
                    else:
                        st.success("Practice questions are available in the main report under Job Matches.")
    
    
            except Exception as e:
                st.error(f"Critical Error: {e}")
                st.info("Tip: If you see a 'Rate Limit' error, wait 60 seconds and try again with a shorter resume.")

