# 🧠 Forward & Backpropagation from Scratch

## 📌 Project Overview
This project demonstrates a **step-by-step mathematical implementation of Forward Propagation and Backpropagation** in a simple neural network.

Instead of relying on deep learning libraries, the entire learning process is derived manually to build a strong understanding of how neural networks actually work.

## 🏗️ Architecture
- **Input Layer:** 2 inputs  
- **Hidden Layer:** 1 neuron  
- **Output Layer:** 1 neuron  
- **Activation Function:** Sigmoid  
- **Loss Function:** Mean Squared Error (MSE)  
- **Bias:** Not used  

## ⚙️ What’s Implemented

### 🔹 Forward Propagation
- Computed weighted sum of inputs  
- Applied sigmoid activation  
- Generated final prediction  

### 🔹 Loss Calculation
- Calculated error using squared loss  
- Compared predicted vs actual output  

### 🔹 Backpropagation
- Applied **chain rule** step-by-step  
- Derived gradients for:
  - ∂L/∂w₁  
  - ∂L/∂w₂  
  - ∂L/∂w₃  
- Understood gradient flow across layers  

### 🔹 Weight Updates
- Updated weights using **gradient descent**  
- Applied learning rate manually  


## 📊 Key Learning Outcomes
- Deep understanding of how neural networks learn  
- Clear intuition of **gradient flow and error propagation**  
- Strong foundation in **derivatives and chain rule in ML**  
- Ability to derive and debug training logic without frameworks  
