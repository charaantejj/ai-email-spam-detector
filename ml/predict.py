import pickle
from ml.preprocess import clean_text

with open("ml/spam_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("ml/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

def predict_spam(text: str):
    clean = clean_text(text)
    vec = vectorizer.transform([clean])

    prediction = model.predict(vec)[0]
    probability = model.predict_proba(vec)[0][1]

    return {
        "label": "Spam" if prediction == 1 else "Not Spam",
        "confidence": round(probability * 100, 2)
    }
