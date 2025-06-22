# PlagiaGuard 🚫📄

**AI-Powered Code Plagiarism Detector**

PlagiaGuard is a smart system designed to detect plagiarism in programming assignments by analyzing the logic of the code, not just its syntax. It uses Abstract Syntax Trees (AST), semantic similarity (embeddings), and GitHub code matching to identify potential plagiarism even when the code is slightly modified.

---

## 🔍 Features

- 🔎 **Logic-level plagiarism detection** using AST comparison
- 🧠 **AI-based semantic similarity scoring** with Sentence Transformers
- 🌐 **Online match detection** via GitHub Search API
- 📊 **Similarity score generation** and result reporting
- 💡 Designed for educators, institutions, and coding platforms

---

## 🛠️ Tech Stack

| Layer        | Tools / Frameworks         |
|--------------|-----------------------------|
| Frontend     | HTML & CSS                   |
| Backend      | Python, FastAPI (optional)    |
| Code Analysis| Python `ast`, `difflib`     |
| AI/ML        | Sentence Transformers        |
| External API | GitHub Code Search API       |

---

## 👀 Preview
<img src="https://private-user-images.githubusercontent.com/132296372/457261195-43daf9a9-9921-4f2b-8465-520bd9f83b40.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTA0MDYyMTUsIm5iZiI6MTc1MDQwNTkxNSwicGF0aCI6Ii8xMzIyOTYzNzIvNDU3MjYxMTk1LTQzZGFmOWE5LTk5MjEtNGYyYi04NDY1LTUyMGJkOWY4M2I0MC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNjIwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDYyMFQwNzUxNTVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT05YzVmMDBkMjIxNmI3MDdiNzk3ZTAxNjU3MDY4ZjE1YWFjMmY5N2Q3MzA0NjRlZmI5ZTJmNGE3NzRjOTQ5OWM1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.fWOrE_HYO-_r_jCnrP3gfcXerrurxPQav_HJ6lu0a6Q" width="1000" alt="Home Page"> <img src="https://private-user-images.githubusercontent.com/132296372/457261196-100b0362-5451-4cf9-add5-b45ab4b0be21.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTA0MDYyMTUsIm5iZiI6MTc1MDQwNTkxNSwicGF0aCI6Ii8xMzIyOTYzNzIvNDU3MjYxMTk2LTEwMGIwMzYyLTU0NTEtNGNmOS1hZGQ1LWI0NWFiNGIwYmUyMS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNjIwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDYyMFQwNzUxNTVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1jMjRhOTUwYThjMWIyNjI5ZDNjMGQwN2QzN2Y4MTgzMDllOGU5MjRhODRiMTg2ZDFiOTM4OWZlNWEyNDE1ZWU1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.6BqXLNifxnsRhjvUjf31joBmVobFsDvhAp490ofLPc8" width="1000" alt="Result Page">

---

## 🔁 Workflow

1. User submits a code file.
2. Code is parsed into an AST (Abstract Syntax Tree).
3. Semantic embeddings are generated and compared.
4. GitHub is queried for potential code matches.
5. A similarity score and feedback report are generated.

---

## 📂 Project Structure

```bash
PlagiaGuard/
├── static/           # Static files 
│   ├── style.css
│   └── table.css
├── templates/             # HTML templates
│   ├── home.html         # Homepage
│   ├── table.html        # Results
├── app.py                # Main FastAPI app
├── src                   # Source Python File
│    ├── model.py          # Core logic for AST + embeddings
├── Notebooks             # Notebook
│   ├── logic.ipynb       # Logic created Notebook
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 🚀 Getting Started
1. Clone the Repo
```bash
git clone https://github.com/TAK-PRAVEEN/PlagiaGuard.git
cd PlagiaGuard
```
2. Install Dependencies
```bash
pip install -r requirements.txt
```
3. Run the App
```bash
uvicorn app:app --reload
```

---

## 📊 Use Cases
- 👩‍🏫 Educators – check student submissions for originality

- 🧑‍💻 Coding platforms – ensure assignment integrity

- 🏢 Recruiters – validate test submissions in hiring

---

## 🔐 Disclaimer
PlagiaGuard is a research/educational project. It does not guarantee 100% accuracy and should be used as a support tool alongside human judgment.

---

## 🙌 Contributors
Praveen Tak – <a href="https://www.linkedin.com/in/praveen-tak-50b669272/" target="_blank">LinkedIn Profile</a>

Team: Hash Splinters

---

## 📄 License
This project is open-source and available under the MIT License.

