import streamlit as st
import torch
import pickle
import os

from dotenv import load_dotenv

from transformers import (
    DistilBertTokenizerFast,
    DistilBertForSequenceClassification,
)

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

st.set_page_config(
    page_title="AI Ticket Automation System",
    page_icon="🎫",
    layout="wide",
)

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


@st.cache_resource
def load_models():

    ticket_tokenizer = DistilBertTokenizerFast.from_pretrained(
        "ticket_classifier_files"
    )

    ticket_model = DistilBertForSequenceClassification.from_pretrained(
        "ticket_classifier_files"
    )

    priority_tokenizer = DistilBertTokenizerFast.from_pretrained(
        "priority_classifier_files"
    )

    priority_model = DistilBertForSequenceClassification.from_pretrained(
        "priority_classifier_files"
    )

    with open("queue_label_encoder.pkl", "rb") as f:
        ticket_encoder = pickle.load(f)

    with open("priority_label_encoder.pkl", "rb") as f:
        priority_encoder = pickle.load(f)

    return (
        ticket_tokenizer,
        ticket_model,
        priority_tokenizer,
        priority_model,
        ticket_encoder,
        priority_encoder,
    )


(
    ticket_tokenizer,
    ticket_model,
    priority_tokenizer,
    priority_model,
    ticket_encoder,
    priority_encoder,
) = load_models()


@st.cache_resource
def load_llm():

    return ChatGroq(
        api_key=GROQ_API_KEY,
        model="llama-3.3-70b-versatile",
        temperature=0.3,
    )


llm = load_llm()


def predict_ticket(text):

    inputs = ticket_tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=256,
    )

    with torch.no_grad():

        outputs = ticket_model(**inputs)

    prediction = torch.argmax(outputs.logits, dim=1).item()

    category = ticket_encoder.inverse_transform([prediction])[0]

    return category


def predict_priority(text):

    inputs = priority_tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=256,
    )

    with torch.no_grad():

        outputs = priority_model(**inputs)

    prediction = torch.argmax(outputs.logits, dim=1).item()

    priority = priority_encoder.inverse_transform([prediction])[0]

    return priority


def assign_team(category):

    mapping = {

        "Technical & System Support":
            "Technical Support Team",

        "Product & Customer Support":
            "Customer Success Team",

        "Account & Billing Support":
            "Billing Team",

    }

    return mapping.get(category, "Customer Support")


summary_prompt = ChatPromptTemplate.from_template(
"""
Summarize the following customer ticket in one concise sentence.

Customer Ticket:

{ticket}
"""
)


def generate_summary(ticket):

    chain = summary_prompt | llm

    response = chain.invoke(
        {
            "ticket": ticket
        }
    )

    return response.content


response_prompt = ChatPromptTemplate.from_template(
"""
You are an experienced customer support executive.

Customer Ticket

{ticket}

Predicted Category

{category}

Predicted Priority

{priority}

Assigned Team

{team}

Generate a professional customer support response.

Instructions:

- Be polite.
- Acknowledge the issue.
- Explain the next steps.
- Mention the assigned team.
- Keep the response under 120 words.
"""
)


def generate_response(ticket, category, priority, team):

    chain = response_prompt | llm

    response = chain.invoke(
        {
            "ticket": ticket,
            "category": category,
            "priority": priority,
            "team": team,
        }
    )

    return response.content

st.title("🎫 AI Ticket Automation System")

ticket = st.text_area(
    "Enter Customer Ticket",
    height=200
)

if st.button("Analyze Ticket", use_container_width=True):

    if ticket.strip() == "":
        st.warning("Please enter a customer ticket.")

    else:

        with st.spinner("Analyzing ticket..."):

            category = predict_ticket(ticket)

            priority = predict_priority(ticket)

            team = assign_team(category)

            summary = generate_summary(ticket)

            response = generate_response(
                ticket,
                category,
                priority,
                team,
            )

        st.success("Ticket analyzed successfully!")

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("📂 Ticket Category")
            st.info(category)

            st.subheader("👨‍💻 Assigned Team")
            st.info(team)

        with col2:

            st.subheader("⚡ Priority")

            priority_lower = priority.lower()

            if priority_lower == "high":
                st.error(priority)

            elif priority_lower == "medium":
                st.warning(priority)

            elif priority_lower == "low":
                st.success(priority)

            elif priority_lower == "critical":
                st.error("🚨 " + priority)

            else:
                st.info(priority)

            st.subheader("📝 Ticket Summary")
            st.write(summary)

        st.divider()

        st.subheader("🤖 AI Generated Customer Response")

        st.write(response)

        st.divider()

        st.subheader("📄 Original Customer Ticket")

        st.text_area(
            "Customer Ticket",
            value=ticket,
            height=170,
            disabled=True,
        )