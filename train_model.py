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

# Split rows using comma to task_description & priority
rows = [line.split(",") for line in dataset]
df = pd.DataFrame(rows, columns=["task_description", "priority"])

# Replace priority from string to integer
df["priority"] = df["priority"].map({"low": 0, "high": 1})

# Text vectorization
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["task_description"])
y = df["priority"]

# Model training
model = LogisticRegression()
model.fit(X, y)


joblib.dump(model, "priority_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
