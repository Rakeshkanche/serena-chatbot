# judge.py
import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib

# Load model and encoder
model = joblib.load("emotion_model.pkl")
encoder = joblib.load("label_encoder.pkl")

# Load dataset
df = pd.read_csv("data/chatbot_emotion_diagnosis_treatment.csv", sep="\t")
features = ['Mood Score (1-10)', 'Symptom Severity (1-10)', 'Stress Level (1-10)', 'Sleep Quality (1-10)']
X = df[features]
y_true = encoder.transform(df['AI-Detected Emotional State'])
y_pred = model.predict(X)

# Evaluation
def evaluate_model():
    acc = accuracy_score(y_true, y_pred)
    conf = confusion_matrix(y_true, y_pred)
    report = classification_report(y_true, y_pred, target_names=encoder.classes_, output_dict=True)
    return {
        "accuracy": acc,
        "confusion_matrix": conf.tolist(),
        "classification_report": report
    }
