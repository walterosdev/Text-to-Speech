# 🧠 Automated Article Summarization & Text-to-Speech System

A Python-based application that extracts articles from the web, processes and summarizes the text, and converts it into speech audio.

---

## 🚀 Features

* 🌐 Extract article content from a URL
* 🧠 Automatic language detection
* ✂️ Text preprocessing and cleaning
* 📄 Summarization of content
* 🔊 Text-to-Speech (TTS) audio generation

---

## 🧪 Example

Input:

```bash
python main.py
```

Output:

* Article title and author
* Processed and summarized text
* Generated audio file in `/audios`

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/walterosdev/Text-to-Speech.git
cd Text-to-Speech
```

---

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Download NLTK data (required)

```bash
python -c "import nltk; nltk.download('stopwords')"
```

---

## ▶️ Usage

Edit the URL inside `main.py`:

```python
url = "https://example.com/article"
```

Run the application:

```bash
python main.py
```

---

## 📁 Project Structure

```bash
.
├── main.py
├── article_service.py
├── text_processor.py
├── summarizer.py
├── tts_service.py
├── audios/
├── requirements.txt
└── README.md
```

---

## 🛠️ Technologies Used

* Python 3
* NLTK
* gTTS
* BeautifulSoup
* Newspaper3k

---

## ⚠️ Notes

* Ensure internet connection for article extraction
* NLTK resources must be downloaded before running
* Audio files are saved locally in the `/audios` directory

---

## 📌 Future Improvements

* Web interface (Flask / FastAPI)
* CLI arguments support
* Multi-language voice options
* PDF support

---

## 👨‍💻 Author

Developed by **WalterosDev**
