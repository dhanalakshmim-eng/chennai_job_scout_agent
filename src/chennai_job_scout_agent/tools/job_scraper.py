import requests
from bs4 import BeautifulSoup

def scrape_jobs(domain="data"):
    url = f"https://www.indeed.com/jobs?q={domain}&l=Chennai"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []

    for job in soup.select(".job_seen_beacon")[:5]:
        title = job.select_one("h2").text.strip() if job.select_one("h2") else "N/A"
        company = job.select_one(".companyName").text.strip() if job.select_one(".companyName") else "N/A"
        location = job.select_one(".companyLocation").text.strip() if job.select_one(".companyLocation") else "N/A"

        jobs.append({
            "title": title,
            "company": company,
            "location": location
        })

    return jobs