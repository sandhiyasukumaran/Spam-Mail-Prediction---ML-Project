# Spam Mail Classifier – ML-Based Email Filtering
A machine learning-powered web app that classifies emails as spam or legitimate using logistic regression and TF-IDF vectorization. Built with Scikit-Learn and Streamlit for an interactive, real-time classification experience

## Overview
This project focuses on detecting spam emails using classical NLP and ML techniques. A logistic regression model was trained on a dataset of 5000+ labeled emails and deployed in a Streamlit-based web app, allowing users to paste email content and get instant classification results.

## Features

- Real-time email spam detection via web interface

- TF-IDF vectorization for feature extraction

- Logistic Regression model trained on 5000+ labeled messages

- 96% accuracy on test set

- Clean, interactive GUI built with Streamlit

## Tech Stack

1. Language: Python
  
2. Libraries: Scikit-Learn, Pandas, Streamlit, Joblib

3. ML Pipeline: TfidfVectorizer + LogisticRegression

4. Deployment: Local or Streamlit Cloud


## Usage

1. Clone the repo

   ```bash
   git clone https://github.com/sandhiyasukumaran/Spam-Mail-Prediction---ML-Project.git
   ```

2. Navigate to the project directory which is the hr-gen2 folder if you're not already in it

   ```bash
   cd Spam Mail prediction
   ```

3. Set up virtual environment

   ```bash
   python -m venv venv
   ```
   ```bash
   .\venv\Scripts\activate
   ```
4. Install dependencies

   ```bash
   pip install streamlit scikit-learn joblib
   ```

5. Run the app

   ```bash
   streamlit run spam_app.py
   ```

## User Interface

Spam Email Example:
![image](https://github.com/user-attachments/assets/5c1964cd-6684-4fa0-8bcd-783911ac5f23)

Legitimate Email Example:
![image](https://github.com/user-attachments/assets/8ecb3f69-3014-4657-8b48-01cb89ed3c34)
