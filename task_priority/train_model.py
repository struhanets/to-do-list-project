import joblib
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

dataset = [
    "Fix login bug on website,high",
    "Update user profile page,low",
    "Implement new API endpoint,high",
    "Refactor old code,low",
    "Write unit tests for API,high",
    "Clean up temporary files,low",
    "Optimize database queries,high",
    "Update documentation,low",
]

rows = [line.split(",") for line in dataset]
df = pd.DataFrame(rows, columns=["task_description", "priority"])

df["priority"] = df["priority"].map({"low": 0, "high": 1})

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["task_description"])
y = df["priority"]

model = LogisticRegression()
model.fit(X, y)


joblib.dump(model, "priority_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
