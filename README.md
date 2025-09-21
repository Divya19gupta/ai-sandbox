## 1) AI Sentiment Analysis Web App

A full-stack web application that performs **sentiment analysis** on user input using a pre-trained NLP model.

* **Frontend:** React.js + Bootstrap
* **Backend:** FastAPI + Hugging Face Transformers (PyTorch)
* **Model:** DistilBERT-based sentiment analysis pipeline

---

### Features

* User can type any sentence and get **sentiment prediction** (Positive / Negative) with confidence.
* Real-time API integration between React frontend and FastAPI backend.
* Easy to extend with other NLP or AI models.

---

### Project Structure

```
project-root/
│
├─ backend/
│  ├─ app.py          # FastAPI backend
│  ├─ requirements.txt
│
├─ frontend/
│  ├─ src/
│  │  ├─ App.js
│  │  ├─ SentimentAnalysis.js
│  │  └─ index.js
│  └─ package.json
│
└─ README.md
```

---

### Setup Instructions

#### 1. Backend Setup

1. Navigate to backend folder:

```bash
cd backend
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start FastAPI server:

```bash
uvicorn app:app --reload
```

* Server runs at `http://127.0.0.1:8000`
* You can test the API at `http://127.0.0.1:8000/docs`

---

#### 2. Frontend Setup

1. Navigate to frontend folder:

```bash
cd frontend
```

2. Install npm dependencies:

```bash
npm install
```

3. Start React app:

```bash
npm start
```

* React app runs at `http://localhost:3000`

---

#### 3. Connect & Test

1. Open [http://localhost:3000](http://localhost:3000) in your browser
2. Type a sentence in the input field
3. Press **Analyze** → Frontend calls FastAPI backend → Displays **sentiment label + confidence**

✅ You now have a working AI sentiment analysis web app!

---

### Tech Stack

| Layer    | Technology                          |
| -------- | ----------------------------------- |
| Frontend | React.js, Bootstrap                 |
| Backend  | FastAPI, Uvicorn                    |
| AI Model | Hugging Face Transformers (PyTorch) |

---

### Future Enhancements

* Replace default model with **Roberta or zero-shot classification** for better accuracy
* Add **history of analyzed sentences**

