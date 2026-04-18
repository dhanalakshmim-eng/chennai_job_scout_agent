import os
from crewai import Agent, Task, Crew, Process, LLM
class ChennaiJobScoutAgent:
    def __init__(self):
        groq_api_key = os.getenv("GROQ_API_KEY")

        if not groq_api_key:
            raise ValueError("❌ GROQ_API_KEY not set in system environment")

        self.groq_llm = LLM(
            model="groq/llama-3.1-8b-instant",
            api_key=groq_api_key,
            temperature=0.1,
            max_tokens=500,
            top_p=0.9
        )

    def crew(self):
        agent = Agent(
            role=f"Expert {{job_domain}} Career Consultant",
            goal=f"Analyze the market and resume specifically for the {{job_domain}} sector in Chennai,Help user find jobs, analyze resume, and prepare interview",
            backstory="Expert in Chennai tech hiring having 20+ years of experience",
            llm=self.groq_llm,
            verbose=False,
            allow_delegation=False
        )
        task = Task(
            description="""
            ### CRITICAL LOGIC RULE:
            Analyze the relationship between the user's resume and the requested {job_domain}. 
            - If the resume is technical (CS/IT) and the {job_domain} is NOT (e.g., Civil, Mechanical, Healthcare), do NOT suggest software roles.
            - If there is a domain mismatch, the 'Match Score' must be LOW (under 30%) and the 'Missing Skills' must list the ACTUAL CORE requirements of the requested {job_domain}.
            ### UNIVERSAL ALIGNMENT RULE:
            1. The {job_domain} provided by the user is the ABSOLUTE source of truth for the analysis.
            2. Evaluate 'Missing Skills' by comparing the resume to the standard requirements of the {job_domain} market.
            3. Do NOT let projects or keywords in the resume (like 'Telemedicine' or 'Construction') bleed into the analysis of a different domain. 
            4. If the resume is in Domain A and the user asks for Domain B, the 'Missing Skills' MUST be the core technical skills of Domain B that the candidate lacks.
            ### TASK STEPS:
            Based on the resume below:
            {resume_text}

            Do the following for {job_domain} roles in Chennai:

            1. List 3-5 job roles from top companies in THAT SPECIFIC SECTOR.
               - Include: Job Title, Company, 2 key skills
            
            2. Identify COMMON SKILLS required across that specific {job_domain} market.

            3. Analyze the resume and give:
               - Match Score (%) based on genuine alignment.
               - Missing Skills (GROUPED into relevant categories for the domain).

            4. Give 3-4 important interview questions with SHORT answers (max 10 words each).

            ### FORMAT STRICTLY:
            # Add the 'Candidate' line here
            ### 🔹 Analysis for: [Full Name from Resume]
            ### 🔹 Top Job Roles
            - Role | Company | Skills

            ### 🔹 Common Skills in Market
            - skill1, skill2, skill3...

            ### 🔹 Resume Match
            Score: XX%
            
            ### 🔹 Missing Skills
            (Group these by category relevant to the {job_domain})

            ### 🔹 Interview Prep
            Q1: [Question] -> A1: [Answer]
            Q2: [Question] -> A2: [Answer]
            
            Keep it clean, structured, and professional.
            """,
            expected_output="A professional, domain-accurate placement report.",
            agent=agent
        )
        return Crew(
            agents=[agent],
            tasks=[task],
            process=Process.sequential,
            verbose=False
        )
