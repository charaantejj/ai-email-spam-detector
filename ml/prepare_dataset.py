import os
import pandas as pd

data = []

BASE_DIR = "dataset"

for label in ["ham", "spam"]:
    folder_path = os.path.join(BASE_DIR, label)

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        try:
            with open(file_path, errors="ignore") as f:
                text = f.read()
                data.append({
                    "label": label,
                    "text": text
                })
        except Exception as e:
            continue

df = pd.DataFrame(data)
df.to_csv("dataset/spam_large.csv", index=False)

print("✅ Dataset prepared successfully!")
print(df.head())
