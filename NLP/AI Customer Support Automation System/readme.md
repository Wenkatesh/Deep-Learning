# 🎫 AI Ticket Automation System

An AI-powered customer support ticket automation system that leverages **DistilBERT**, **LangChain**, and **Groq LLM** to automate ticket classification, priority prediction, ticket summarization, and intelligent customer response generation.

## Features

-  Automatic Ticket Category Classification using a fine-tuned DistilBERT model.
-  Automatic Priority Prediction (Low, Medium, High) using a fine-tuned DistilBERT model.
- Automatic Team Assignment based on the predicted ticket category.
-  AI-powered Ticket Summarization using Groq LLM.
- Professional Customer Response Generation using LangChain and Groq.
- Interactive Streamlit web interface.

##  System Architecture

```
Customer Ticket
        │
        ▼
DistilBERT Ticket Classifier
        │
        ▼
Ticket Category
        │
        ├──────────────┐
        ▼              ▼
DistilBERT      Team Assignment
Priority
        │
        ▼
Groq LLM
Ticket Summary
        │
        ▼
Groq LLM
Customer Response
        │
        ▼
Streamlit UI
```


##  Tech Stack

### Programming Language
- Python

### Machine Learning
- DistilBERT
- PyTorch
- Hugging Face Transformers

### Large Language Model
- Groq Llama 3.3 70B
- LangChain

### Frontend
- Streamlit

### Other Libraries
- Scikit-learn
- Pickle
- python-dotenv


## Project Structure

```
AI-Ticket-Automation-System/

│
├── app.py
├── requirements.txt
├── .env
│
├── ticket_classifier_files/
│
├── priority_classifier_files/
│
├── queue_label_encoder.pkl
├── priority_label_encoder.pkl
│
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/AI-Ticket-Automation-System.git

cd AI-Ticket-Automation-System
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a **.env** file

```
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

Run the application

```bash
streamlit run app.py
```

---

##  Workflow

1. User enters a customer support ticket.
2. DistilBERT predicts the ticket category.
3. DistilBERT predicts the ticket priority.
4. The system assigns the appropriate support team.
5. Groq LLM generates a concise ticket summary.
6. Groq LLM generates a professional customer response.
7. Results are displayed through the Streamlit interface.


##  Ticket Categories

- Technical & System Support
- Product & Customer Support
- Account & Billing Support

---

##  Priority Levels

- Low
- Medium
- High

---


## 🎯 Future Enhancements

- Multi-language ticket support.
- Sentiment Analysis.
- Email integration.
- Automatic ticket routing.
- Knowledge Base Retrieval (RAG).
- Support dashboard with analytics.
- Database integration for ticket history.

---

## 👨‍💻 Author

**Madaparthi Venkatesh**
