import json

def save_json(result, filename="output.json"):
    """Saves the CrewAI result object into a clean, readable JSON format."""
    try:
        # We extract the 'raw' string which contains the final Markdown report
        data_to_save = {
            "status": "success",
            "final_report": result.raw,
            "individual_task_results": [str(t) for t in result.tasks_output]
        }
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data_to_save, f, indent=4)
        print(f"✅ Successfully saved to {filename}")
    except Exception as e:
        print(f"❌ Error saving JSON: {e}")