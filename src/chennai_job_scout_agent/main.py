from chennai_job_scout_agent.crew import ChennaiJobScoutAgent

def run():
    job_domain = input("Enter job domain: ")

    result = ChennaiJobScoutAgent().crew().kickoff(
        inputs={"job_domain": job_domain}
    )

    print("\nFINAL OUTPUT:\n")
    print(result)

if __name__ == "__main__":
    run()
