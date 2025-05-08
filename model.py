# model.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
df = pd.read_csv("data/chatbot_emotion_diagnosis_treatment.csv", sep="\t")

# Define features and target
features = ['Mood Score (1-10)', 'Symptom Severity (1-10)', 'Stress Level (1-10)', 'Sleep Quality (1-10)']
X = df[features]
y = df['AI-Detected Emotional State']

# Encode target labels
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model and encoder
joblib.dump(model, "emotion_model.pkl")
joblib.dump(encoder, "label_encoder.pkl")

print("✅ Model and label encoder saved.")
