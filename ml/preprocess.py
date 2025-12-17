import re
from nltk.corpus import stopwords

STOPWORDS = set(stopwords.words("english"))

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"http\S+", "", text)      # remove links
    text = re.sub(r"\W+", " ", text)         # remove special chars
    text = re.sub(r"\d+", "", text)           # remove numbers

    tokens = text.split()
    tokens = [t for t in tokens if t not in STOPWORDS]

    return " ".join(tokens)
