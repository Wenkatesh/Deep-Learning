# 🎫 AI Ticket Automation System

An AI-powered customer support ticket automation system that leverages **DistilBERT**, **LangChain**, and **Groq LLM** to automate ticket classification, priority prediction, ticket summarization, and intelligent customer response generation.

## Features

-  Automatic Ticket Category Classification using a fine-tuned DistilBERT model.
-  Automatic Priority Prediction (Low, Medium, High) using a fine-tuned DistilBERT model.
- Automatic Team Assignment based on the predicted ticket category.
-  AI-powered Ticket Summarization using Groq LLM.
- Professional Customer Response Generation using LangChain and Groq.
- Interactive Streamlit web interface.


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

# Project Workflow

## 1. Data Collection

- Collected a customer support ticket dataset containing ticket descriptions, ticket types, and priority labels.
- Used the dataset as the foundation for training the classification models.

## 2. Data Cleaning & Preprocessing

Performed extensive preprocessing to improve model performance.

### Text Cleaning

- Converted text to lowercase.
- Removed HTML tags.
- Removed URLs.
- Removed special characters.
- Removed extra whitespace.
- Removed unnecessary punctuation.
- Removed placeholder values (e.g., `{amount}`, `{product_name}`).
- Filtered English-language tickets.
- Removed duplicate records.
- Handled missing values.

## 3. Ticket Category Engineering

The original dataset contained multiple support categories.

### Original Categories

- Technical Support
- IT Support
- Service Outages and Maintenance
- Product Support
- Customer Service
- General Inquiry
- Sales and Pre-Sales
- Billing and Payments
- Returns and Exchanges
- Human Resources

To simplify the classification task and improve model performance, similar classes were merged into three business-friendly categories.

| Original Category | Final Category |
|------------------|----------------|
| Technical Support | Technical & System Support |
| IT Support | Technical & System Support |
| Service Outages and Maintenance | Technical & System Support |
| Product Support | Product & Customer Support |
| Customer Service | Product & Customer Support |
| General Inquiry | Product & Customer Support |
| Sales and Pre-Sales | Product & Customer Support |
| Billing and Payments | Account & Billing Support |
| Returns and Exchanges | Account & Billing Support |
| Human Resources | Account & Billing Support |

## 4. Label Encoding

Used Scikit-learn LabelEncoder to convert:

- Ticket Categories
- Priority Labels

into numerical values for model training.

Saved encoders using Pickle for inference.

```
queue_label_encoder.pkl
priority_label_encoder.pkl
```


## 5. Tokenization

Used the DistilBERT tokenizer from Hugging Face.

```
DistilBertTokenizerFast
```

Each ticket was tokenized with:

- Padding
- Truncation
- Maximum sequence length

to prepare inputs for DistilBERT.


## 6. Model Training

Two independent DistilBERT models were fine-tuned.

### Ticket Category Classifier

Input

```
Customer Ticket
```

Output

```
Technical & System Support

Product & Customer Support

Account & Billing Support
```

---

### Priority Classifier

Input

```
Customer Ticket
```

Output

```
Low

Medium

High
```

---

## 7. Model Evaluation

Evaluated both models using:

- Accuracy
- Precision
- Recall
- F1-Score

Training was performed using the Hugging Face Trainer API.

Models were saved using:

```
model.save_pretrained()
tokenizer.save_pretrained()
```

---

## 8. Model Export

Saved trained models for deployment.

```
ticket_classifier_files/

priority_classifier_files/
```

Each folder contains:

- config.json
- model.safetensors
- tokenizer.json
- tokenizer_config.json
- vocab.txt
- special_tokens_map.json

---

## 9. AI-Powered Ticket Automation

The deployed application performs the following pipeline:

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
DistilBERT      Assigned Team
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
Streamlit Application
```

---

## 10. Team Assignment

The predicted ticket category is automatically mapped to the responsible support team.

| Category | Assigned Team |
|----------|---------------|
| Technical & System Support | Technical Support Team |
| Product & Customer Support | Customer Success Team |
| Account & Billing Support | Billing Team |

---

## 11. AI Features

Groq Llama 3.3 is used to:

- Generate ticket summaries.
- Generate professional customer support responses.
- Improve customer service automation.

---

## 12. Streamlit Deployment

Developed an interactive Streamlit application that allows users to:

- Enter customer tickets.
- Predict ticket category.
- Predict ticket priority.
- Automatically assign the responsible support team.
- Generate ticket summaries.
- Generate AI-powered customer support responses.

---

## Technologies Used

- Python
- DistilBERT
- Hugging Face Transformers
- PyTorch
- Scikit-learn
- LangChain
- Groq Llama 3.3
- Streamlit
- Pickle
- python-dotenv

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
