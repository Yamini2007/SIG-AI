# SIG-AI-II-Tasks

CHAT BOT --README
Technologies Used
Python: Programming language for backend logic and handling API requests.

Streamlit: A Python library used for building the web interface for the chatbot.

Groq API: A language model that powers the chatbot's ability to generate responses.

Requests: Python library for making HTTP requests to the Groq API.

GitHub: Version control and hosting the code for the project.

Features:
Groq API Integration: Uses Groq’s language model to generate responses based on user input.

Streamlit Deployment: Deployed the chatbot as a web app for easy access via any browser.

Interactive UI: Simple, easy-to-use interface that accepts user queries and provides responses.

How the Chatbot Works:
User Input: Users enter a query in the input box.

Groq API Call: The input is sent to the Groq API for processing.

Response: The chatbot displays the generated response in the UI.

Deployement--Streamlit Deployement
users can access my chatbot online at:https://sig-ai-ii-tasks-4nthu97cvqq73gmr3rk8gz.streamlit.app/

Project Description
This project is a text-based chatbot built using the Groq API for language model inference and Streamlit for deployment. The chatbot answers general queries and provides a user-friendly interface for interaction.

The chatbot is deployed as a web app, which can be accessed through any browser.
coomands  i used:
1)git init-to initialize a git repository
2)git add .-add files to staging
3)git commit -m "Initial commit"-for commit changes
4)git push -u origin main -for pushing code to github
5)cd "C:\path\to\project"-for navigating into project folder
6)python -m venv venv-for creating virtual environment(venv)
7).\venv\Scripts\activate-for activating virtual environment
8)cd path\to\folder --allows us to move to directory(folder)
9)dir -to verify files in current directory

i created chatbot_project as folder in that i ctreated app.py,chaatbot.py,Procfile,requirements.txt,venv


---

## 📌 Project: Handwritten Digit Recognition using CNN

This project uses a Convolutional Neural Network (CNN) to classify handwritten digits (0–9) from the MNIST dataset.

### 🔧 Tools Used:
- Google Colab
- TensorFlow / Keras
- MNIST Dataset (28x28 grayscale digits)

### ✅ What it Does:
- Trains a CNN on MNIST
- Achieves ~99% test accuracy
- Lets you test your own image (after preprocessing)

### 📁 Notebook:
[handwritten_digit_recognition.ipynb](./handwritten_digit_recognition.ipynb)

### 🖼️ Sample Output:
![Prediction](my_digit.png) <!-- if you uploaded a test image -->



# Sentiment Analysis Using LSTM (IMDb Movie Reviews)

This project performs sentiment analysis on IMDb movie reviews using a Long Short-Term Memory (LSTM) neural network. It classifies each review as either **positive** or **negative** based on the text.

---

## 📌 Project Summary

- **Dataset**: IMDb movie reviews (built-in from Keras)
- **Model**: LSTM (Long Short-Term Memory)
- **Tools Used**: TensorFlow / Keras, Python
- **Accuracy Achieved**: ~86.37%
- **Output**: Predicts whether a review is Positive 😀 or Negative 😠

---

## 🚀 How It Works

1. Load and preprocess the IMDb dataset  
2. Pad sequences to ensure all reviews are the same length  
3. Build and train an LSTM model using Keras  
4. Evaluate the model on test data  
5. Test sentiment predictions on custom reviews

---

## 🧠 Sample Prediction Output

```python
Review: "The movie was absolutely fantastic, I loved it."
Prediction Score: 0.89
Predicted Sentiment: Positive 😀


