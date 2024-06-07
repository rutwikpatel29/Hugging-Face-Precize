# generate_report.py
import requests

def fetch_top_models():
    url = "https://huggingface.co/api/models"
    params = {"sort": "downloads", "direction": -1, "limit": 10}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def generate_report(models):
    report = "Top 10 Downloaded Models on Hugging Face:\n\n"
    for model in models:
        report += f"Model: {model['modelId']}, Downloads: {model['downloads']}\n"
    with open("/reports/top_models_report.txt", "w") as f:
        f.write(report)

def main():
    models = fetch_top_models()
    generate_report(models)
    print("Report generated successfully!")

if __name__ == "__main__":
    main()
