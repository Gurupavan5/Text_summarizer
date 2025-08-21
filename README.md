Website Summarizer (Notebook Demo)

This is a Jupyter Notebook demo that:
- Scrapes a website with **BeautifulSoup**
- Cleans the text (removing scripts, styles, navigation, etc.)
- Summarizes the content using **OpenAI GPT-4**

📦 Requirements
- Python 3.9+
- Jupyter Notebook

Install dependencies:
```bash
pip install -r requirements.txt



🐍 Website Summarizer with Ollama

A simple web app that summarizes any website.  
Paste a URL → it scrapes the text → sends it to a local Ollama model (like DeepSeek) → and shows a summary.  

---

🚀 Features
- Scrapes text using **BeautifulSoup** (ignores scripts, images, styles).
- Summarizes content with **Ollama** models (e.g., `deepseek-r1`, `mistral`, `llama2`).
- Simple **Flask** web interface.

---

⚡ Installation

1. Clone this repo:
   ```bash
   git clone https://github.com/YOUR_USERNAME/web-summarizer.git
   cd web-summarizer

