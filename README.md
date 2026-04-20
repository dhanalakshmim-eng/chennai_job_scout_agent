# 🚀 Chennai Job Scout Agent

An AI-powered career assistant that analyzes resumes, matches them with Chennai job market demands, and provides personalized job roles, skill gaps, and interview preparation.

---

## 📌 Project Overview

This project uses CrewAI to build an intelligent agent that:

* 🔍 Identifies relevant job roles in Chennai based on domain
* 📊 Analyzes resume alignment with industry requirements
* 🧠 Detects skill gaps with categorized insights
* 🎯 Generates interview questions with concise answers

---

## 🛠️ The Technical Stack

| Component         | Technology                                  |
| ----------------- | ------------------------------------------- |
| Agentic Framework | CrewAI (Task & Agent Orchestration)         |
| LLM Interface     | Groq (Llama-3.1-8b-instant)                 |
| User Interface    | Streamlit (State Management & File Uploads) |
| Logic Layer       | Python (Custom Context Guardrails)          |
| Parsing           | python-docx / PyPDF2                        |

---

## ⚙️ Setup Instructions

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 2️⃣ Install Dependencies

```bash
pip install --upgrade pip setuptools wheel
pip install crewai crewai-tools python-dotenv streamlit
```

---

### 3️⃣ Fix Dependency Issues (if any)

```bash
pip uninstall -y pydantic pydantic-core crewai
pip cache purge
pip install pydantic==2.7.4
pip install pydantic-core==2.18.4
pip install crewai crewai-tools --no-cache-dir
pip install "starlette<0.48.0"
```

---

### 4️⃣ Verify Installation

```bash
python -c "import crewai; print('CrewAI OK')"
```

---

## 🏗️ Project Initialization

```bash
crewai create crew chennai-job-scout-agent
cd chennai_job_scout_agent
pip install crewai crewai-tools python-dotenv
```

---

## 🔑 Environment Setup

Create a `.env` file in project root:

```env
GROQ_API_KEY=your_api_key_here
```

---

## 📁 Project Structure

```
chennai_job_scout_agent/
│
├── AGENTS.md
├── README.md
├── app.py
├── debug_env.py
├── .gitignore
├── pyproject.toml
├── requirements.txt
│
├── knowledge/
│   └── resume.txt
│
├── src/
│   └── chennai_job_scout_agent/
│       ├── crew.py
│       ├── main.py
│       ├── tools/
│       │   └── job_scraper.py
│       │   └── custom_tool.py
│       └── utils/
│           └── save_output.py
│
└── uv.lock
```

---

## 🚀 Core System Features

### 🧠 Specialized Agent Persona (Single-Agent Architecture)

A single intelligent agent designed as a domain-aware career consultant.

### 🔀 Dynamic Domain Routing

Adapts analysis based on user-provided job domain (AI, Data, Civil, etc.).

### 📄 Semantic Resume Parsing

Extracts meaningful information from resumes (PDF/DOCX/TXT).

### 📊 Automated Skill-Gap Mapping

Identifies missing skills by comparing resume with market requirements.

### 📍 Localized Market Intelligence

Focuses on Chennai-specific companies, roles, and hiring trends.

---

## 🤖 Advanced AI Logic

### 🛡️ Universal Alignment Guardrails

Ensures analysis strictly follows the selected job domain.

### 📉 Context-Specific Match Scoring

Generates realistic match scores based on true alignment.

### 🎯 Intelligent Interview Preparation

Creates domain-relevant interview questions with concise answers.

### ⚡ Token-Optimized Processing

Designed to work within API limits efficiently.

### 🚫 Domain Mismatch Detection

Detects when resume and job domain don’t align and adjusts output accordingly.

---

## 🚀 How to Run

### Streamlit UI

```bash
streamlit run app.py
```

---


## 🧪 Test Cases Passed

## 🧪 Test Cases & Sample Outputs

| Test Case | Description | Sample Output | Result |
|----------|------------|--------------|--------|
| TC-01 | Resume Parsing | Extracted candidate details: Name, Skills (Python, SQL), Projects | ✅ PASSED |
| TC-02 | Domain Routing | Input: *AI* → Suggested roles: ML Engineer, AI Engineer | ✅ PASSED |
| TC-03 | Context Isolation | Resume keyword "Telemedicine" ignored for AI domain analysis | ✅ PASSED |
| TC-04 | Extreme Mismatch | Resume: Horticulture → Domain: Java → Match Score: **< 20%** | ✅ PASSED |
| TC-05 | Low Match Scoring | Non-technical resume → AI domain → Score: **10–30%** | ✅ PASSED |
| TC-06 | Skill Gap Detection | Missing Skills: TensorFlow, Django, AWS (correctly identified) | ✅ PASSED |

---

### 📊 Sample Output 
## 🎬 Demo Video

[Watch Demo](https://youtu.be/ueSp573qrzI?si=SUVRU3lnn9xFYfx5)

---

## ⚡ Optimization Techniques Used

* Reduced token usage (`max_tokens=500`)
* Disabled verbose logs
* Removed external tools to prevent API errors
* Switched to Groq for faster inference
* Converted multi-agent → single-agent for stability

---

## 🧠 Key Learning

* Agent-based AI system design
* Prompt engineering for structured outputs
* Resume-job alignment logic
* Handling API rate limits and errors
* Building deployable AI applications

---

## 📈 Future Improvements

* Multi-agent architecture (Researcher + Analyst + Strategist)
* Real-time job scraping integration
* ATS score improvement suggestions
* Deployment on Hugging Face / Cloud

---

## 🙌 Author

**Dhana Lakshmi M**
AI & Data Enthusiast | Aspiring Software Engineer

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
