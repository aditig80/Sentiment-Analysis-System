# 🚀 Sentiment Analysis — End-to-End NLP System

<p align="center">
  <b>Fine-tuned DistilBERT for high-accuracy sentiment classification with real-time deployment</b>
</p>

<p align="center">
  <a href="https://0126439be1985b3dc3.gradio.live/"><img src="https://img.shields.io/badge/Live-Demo-blue?style=for-the-badge&logo=gradio"></a>
  <img src="https://img.shields.io/badge/Accuracy-93%25-brightgreen?style=for-the-badge">
  <img src="https://img.shields.io/badge/F1-0.92-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Model-DistilBERT-yellow?style=for-the-badge">
  <img src="https://img.shields.io/badge/API-FastAPI-green?style=for-the-badge&logo=fastapi">
  <img src="https://img.shields.io/badge/Docker-Enabled-blue?style=for-the-badge&logo=docker">
</p>

---

## 📌 Overview

This project is a **production-ready NLP system** that performs **binary sentiment classification** using a fine-tuned **DistilBERT** model trained on the IMDB dataset.

It covers the **complete ML lifecycle** — from preprocessing and training to deployment and monitoring.

---

## 🧠 Key Highlights

✨ Fine-tuned on **50,000 IMDB reviews**
✨ Achieved **93%+ accuracy** and **0.92 F1 score**
✨ Outperformed TF-IDF + Logistic Regression by **~5pp**
✨ Built **end-to-end NLP pipeline**
✨ Deployed using **FastAPI + Docker**
✨ Live demo via **Gradio (Hugging Face Spaces)**
✨ Tracked **10+ experiments with MLflow**

---

## 📊 Results

| Model                        | Accuracy  | F1 Score  | AUC-ROC   |
| ---------------------------- | --------- | --------- | --------- |
| TF-IDF + Logistic Regression | 88.4%     | 0.884     | —         |
| DistilBERT (Fine-tuned)      | **93.1%** | **0.931** | **0.978** |

---

## ⚙️ Tech Stack

* **Languages:** Python
* **ML/NLP:** PyTorch, Hugging Face Transformers
* **Backend:** FastAPI
* **Deployment:** Docker, Hugging Face Spaces (Gradio)
* **Tracking:** MLflow

---

## 🏗️ Architecture

```
User Input → Preprocessing → Tokenization → DistilBERT → Prediction → API Response
```

---

## 📁 Project Structure

```
.
├── notebooks/        # EDA, training, evaluation
├── api/              # FastAPI app + Dockerfile
├── models/           # (ignored) model weights hosted externally
├── mlruns/           # MLflow logs
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run

### 🔹 Clone Repository

```bash
git clone https://github.com/your-username/Sentiment-Analysis-System.git
cd Sentiment-Analysis-System
```

---

### 🔹 Run FastAPI

```bash
cd api
uvicorn main:app --reload
```

👉 Open: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

### 🔹 Run with Docker

```bash
docker build -t sentiment-api .
docker run -p 8000:8000 sentiment-api
```

---

## 🔌 API Usage

### Endpoint:

```
POST /predict
```

### Request:

```json
{
  "text": "This movie was absolutely amazing!"
}
```

### Response:

```json
{
  "sentiment": "positive",
  "confidence": 0.97
}
```

---

## 📈 MLflow Tracking

* Logged **10+ experiments**
* Compared hyperparameters & performance
* Stored model artifacts for reproducibility

---

## 🔍 Key Insights

⚠️ **Failure Cases Identified:**

* Sarcasm → “Great movie… not.”
* Double negatives
* Context-heavy sentences

---

## ⚡ Performance

* ⏱️ **Latency:** < 80ms (CPU)
* ⚡ FastAPI ensures scalable inference

---

## 🤗 Model Hosting

Model is hosted externally (Hugging Face) to keep repository lightweight.

---

## 🚧 Future Work

* Handle sarcasm using advanced context modeling
* Multi-class sentiment (positive/neutral/negative)
* Cloud deployment (AWS/GCP)
* CI/CD pipeline integration

---

## 👩‍💻 Author

**Aditi Gupta**
💻 Computer Science Student | ML & Full Stack Developer

---

## ⭐ Show Your Support

If you like this project, give it a ⭐ on GitHub!
