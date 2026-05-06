# Hate Speech Classification using RNN & GRU

## Problem Statement
The objective of this project is to build a binary text classification model that can automatically detect hate speech in tweets using Deep Learning techniques.

The project uses:
- Simple RNN
- GRU (Gated Recurrent Unit)

to classify tweets into:
- **0 → Non-Hate Speech**
- **1 → Hate Speech**

The dataset consists of tweets along with corresponding labels indicating whether the tweet contains hate speech or not.

---

# Dataset
The dataset contains two important columns:
- `tweet` → Text data
- `label` → Target variable

Only these two columns were used for model training.

---

# Project Workflow

## 1. Data Loading
The dataset was loaded and only the required columns were selected for further processing.

---

# 2. Text Preprocessing

The tweets were cleaned before feeding them into the model.

## Cleaning Steps Performed

### Convert text to lowercase
All tweets were converted into lowercase format to maintain consistency.

### Remove @mentions
User mentions were removed from tweets.

### Remove URLs
Links and URLs were removed because they do not contribute significantly to sentiment or hate speech detection.

### Remove special characters and numbers
Special symbols, punctuation, and numbers were removed to keep only meaningful textual information.

### Remove extra spaces
Unnecessary spaces were removed to standardize the text.

---

# 3. Tokenization & Vocabulary Creation

The cleaned tweets were tokenized into words.

## Vocabulary Creation Approach

A vocabulary was created using the most frequent words from the dataset.

### Vocabulary Size
The top **5000 most frequent words** were selected for the vocabulary.

Special tokens used:
- `<PAD>` → Used for padding sequences
- `<OOV>` → Used for unknown words not present in the vocabulary

---

# 4. Text to Sequences

Each tweet was converted into integer sequences based on the created vocabulary.

---

# 5. Sequence Padding

All sequences were padded to a fixed length to ensure uniform input size for the neural network.

### Why Padding?
Neural networks require equal-length input sequences for efficient batch processing.

---

# 6. Train-Test Split

The dataset was split into:
- **80% Training Data**
- **20% Testing Data**

Stratified sampling was used to maintain the class distribution in both training and testing sets.

---

# 7. Model Architecture

Two Deep Learning models were implemented.

---

# Model 1: Simple RNN

## Architecture
- Embedding Layer
- Simple RNN Layer
- Dense Output Layer with Sigmoid Activation

### Purpose
The Simple RNN model captures sequential information from tweet text for binary classification.

---

# Model 2: GRU

## Why GRU?
GRU helps solve the vanishing gradient problem faced by traditional RNNs and captures long-term dependencies more effectively.

GRU generally performs better on sequential text data.

## Architecture
- Embedding Layer
- GRU Layer
- Dense Output Layer with Sigmoid Activation

---

# 8. Model Training

## Training Configuration

| Parameter | Value |
|---|---|
| Loss Function | Binary Crossentropy |
| Optimizer | Adam |
| Epochs | 10 |
| Batch Size | 32 |

---

# 9. Model Evaluation

The models were evaluated using:
- Accuracy
- Confusion Matrix
- F1-Score

---

# Results

GRU achieved better performance compared to Simple RNN due to its ability to capture contextual dependencies more effectively.

---

# Technologies Used

- Python
- Pandas
- NumPy
- TensorFlow / Keras
- Scikit-learn
- Matplotlib

---

# How to Run the Project

1. Clone the repository
2. Install the required dependencies
3. Run the notebook or Python script
4. Train and evaluate the model

---

# Future Improvements

- Use LSTM and Bidirectional LSTM
- Use pretrained embeddings like Word2Vec or GloVe
- Apply Attention Mechanism
- Perform Hyperparameter Tuning
- Deploy using Streamlit or Flask

---

# Conclusion

This project demonstrates how Deep Learning models like Simple RNN and GRU can be used for hate speech detection from tweets.

The project covers:
- Text preprocessing
- Vocabulary creation
- Sequence modeling
- RNN/GRU implementation
- Model evaluation

GRU provided improved performance due to better handling of sequential dependencies in textual data.
