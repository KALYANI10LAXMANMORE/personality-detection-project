import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("dataset.csv")

# Features & Labels
X = df['text']
y = df['label']

# Convert text to numbers
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# Train model
model = LogisticRegression()
model.fit(X_vec, y)

# Prediction function
def predict_personality(text):
    text_vec = vectorizer.transform([text])
    prediction = model.predict(text_vec)[0]
    confidence = model.predict_proba(text_vec).max()
    return prediction, confidence