import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from ml.preprocess import clean_text

# Load dataset
df = pd.read_csv("dataset/spam_large.csv")  # label, text

df["clean_text"] = df["text"].apply(clean_text)

# Vectorization
vectorizer = TfidfVectorizer(max_features=3000)
X = vectorizer.fit_transform(df["clean_text"])
y = df["label"].map({"ham": 0, "spam": 1})

# Train model
model = MultinomialNB()
model.fit(X, y)

# Save model & vectorizer
with open("ml/spam_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("ml/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Spam model trained and saved")
