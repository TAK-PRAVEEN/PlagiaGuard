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
├── app.py                # Main FastAPI app
├── src                   # Source Python File
    ├── model.py          # Core logic for AST + embeddings
├── Notebooks             # Notebook
    ├── logic.ipynb       # Logic created Notebook
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
Praveen Tak – <a href="https://www.linkedin.com/in/praveen-tak-50b669272/">LinkedIn Profile</a>

Team: Hash Splinters

---

## 📄 License
This project is open-source and available under the MIT License.

