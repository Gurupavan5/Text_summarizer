from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup
import ollama

app = Flask(__name__)

def summarize_with_ollama(text):
    # Send to Ollama locally
    response = ollama.chat(
        model="deepseek-r1:1.5b",  # change to your model
        messages=[{"role": "user", "content": f"Summarize this webpage:\n\n{text}"}]
    )
    return response["message"]["content"]

def scrape_website(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")

    if soup.body:
        for tag in soup.body(["script", "style", "img", "input"]):
            tag.decompose()
        return soup.body.get_text(separator="\n", strip=True)
    return "No readable content found."

@app.route("/", methods=["GET", "POST"])
def index():
    summary = None
    if request.method == "POST":
        url = request.form["url"]
        text = scrape_website(url)
        summary = summarize_with_ollama(text)
    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
