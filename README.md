
# 📧 AI Powered Email Spam Detection using NLP

An end-to-end AI-powered web application that authenticates users via **Google OAuth 2.0**, fetches **live Gmail emails**, and classifies them as **Spam / Not Spam** using **Natural Language Processing (NLP)** and **Machine Learning**, with results displayed through a clean, minimal web interface.

---

## 🚀 Overview

Email spam remains a major cybersecurity and productivity challenge.
This project demonstrates how **AI and NLP** can be applied to **real-world email data** by integrating directly with Gmail using official Google APIs.

Unlike traditional spam detection demos that work on static datasets, this application:

* Connects to a **real Gmail inbox**
* Processes emails **in real time**
* Performs **on-the-fly spam classification**
* Displays predictions with confidence scores in a web UI

---

## ✨ Key Features

* 🔐 **Google OAuth 2.0 Authentication**

  * Secure login using Google accounts
  * No passwords stored
  * Read-only Gmail access

* 📥 **Live Gmail Inbox Analysis**

  * Fetches recent emails using Gmail API
  * Extracts sender, subject, and body content
  * Handles both plain-text and HTML emails

* 🧠 **AI-Powered Spam Detection**

  * NLP-based text preprocessing
  * Machine Learning classification
  * Confidence scoring for predictions

* 🎨 **Minimal Web UI**

  * Clean, whitespace-focused design
  * Spam / Not Spam badges
  * Confidence percentage display
  * Built with FastAPI + Jinja2

* 🔒 **Privacy-Focused**

  * Emails are processed **in-memory only**
  * No email content is stored
  * No data is logged or persisted

---

## 🧠 How It Works (System Flow)

```
User Login (Google OAuth)
        ↓
Gmail API (Read Inbox)
        ↓
Email Text Extraction
        ↓
NLP Preprocessing
        ↓
ML Spam Classifier
        ↓
Prediction + Confidence
        ↓
Web UI Visualization
```

---

## 🧪 Machine Learning & NLP Pipeline

### 📊 Dataset

* **SpamAssassin Public Corpus**

  * `spam` → spam emails
  * `easy_ham` → legitimate emails

### 🛠 NLP Processing

* Lowercasing
* URL removal
* Special character removal
* Stopword removal (NLTK)

### 🤖 Model

* **TF-IDF Vectorization**
* **Multinomial Naive Bayes Classifier**
* Lightweight, fast, and explainable

### 🎯 Output

* Label: `Spam`, `Not Spam`, or `Suspicious`
* Confidence score (%)

---

## 🧰 Tech Stack

### Backend

* Python
* FastAPI
* Gmail API
* Google OAuth 2.0

### Machine Learning

* Scikit-learn
* NLTK
* Pandas
* TF-IDF + Naive Bayes

### Frontend

* Jinja2 Templates
* HTML & CSS
* Minimal UI design

### Deployment

* Render (optional)
* GitHub for version control

---

## 📁 Project Structure

```
ai-email-spam-detector/
│
├── main.py                  # FastAPI application
├── services/
│   └── gmail_service.py     # Gmail API integration
│
├── ml/
│   ├── preprocess.py        # NLP text cleaning
│   ├── train_model.py       # Model training
│   ├── predict.py           # Spam prediction logic
│   └── prepare_dataset.py   # Dataset preparation
│
├── dataset/
│   ├── spam/
│   ├── ham/
│   └── spam_large.csv
│
├── templates/
│   ├── base.html
│   └── inbox.html
│
├── static/
│   └── css/
│       └── style.css
│
├── requirements.txt
├── start.sh
└── README.md
```

---

## 🖥️ Running the Project Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/charaantejj/ai-email-spam-detector.git
cd ai-email-spam-detector
```

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Google OAuth

* Create OAuth Client ID (Web Application)
* Add redirect URI:

  ```
  http://localhost:8000/auth/callback
  ```
* Download `client_secret.json`
* Place it in project root (ignored by Git)

### 5️⃣ Train the Model

```bash
python -m ml.prepare_dataset
python -m ml.train_model
```

### 6️⃣ Run the Server

```bash
python -m uvicorn main:app --reload
```

### 7️⃣ Open in Browser

```
http://127.0.0.1:8000/login
```

---

## 🌍 Deployment (Optional)

The application can be deployed on **Render**:

* Uses `requirements.txt`
* Uses `start.sh`
* OAuth redirect URI updated to production URL
* Secrets managed securely via environment variables

---

## 📸 Screenshots

*Add screenshots here for better presentation.*

```
screenshots/
├── login.png
├── inbox.png
└── spam_detection.png
```

---

## 📌 Use Cases

* AI-powered email filtering
* NLP experimentation on real text data
* Secure OAuth-based applications
* Cybersecurity & spam analysis demos

---

## ⚠️ Disclaimer

This project is intended for **educational and demonstration purposes only**.
The application does **not store** any user emails or personal data.

---

## 👨‍💻 Author

**Your Name**
Final Year Project / Personal AI Project
GitHub: [https://github.com/charaantejj]

---

## ⭐ Final Note

This project demonstrates a **real-world AI pipeline** by combining:

* Secure authentication
* Live data ingestion
* NLP & machine learning
* Clean UI presentation

It is designed to be **practical, explainable, and resume-ready**.
