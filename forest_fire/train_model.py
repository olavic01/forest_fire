"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Dummy data
data = {
    'temperature': [35, 22, 28, 40, 25, 30, 18, 27, 33, 19],
    'humidity': [20, 65, 45, 10, 70, 30, 80, 50, 25, 75],
    'wind_speed': [15, 5, 10, 20, 6, 12, 4, 8, 14, 5],
    'rainfall': [0, 5, 0.2, 0, 10, 0, 12, 0.1, 0, 15],
    'fire': [1, 0, 0, 1, 0, 1, 0, 0, 1, 0]  # 1 = Fire Risk, 0 = No Risk
}

df = pd.DataFrame(data)

# Features and target
X = df[['temperature', 'humidity', 'wind_speed', 'rainfall']]
y = df['fire']

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'forest_fire_model.pkl')

print("Model trained and saved as forest_fire_model.pkl")
"""
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

# Load dataset
data_path = os.path.join('datasets', 'forestfires.csv')
df = pd.read_csv(data_path)

# Encode categorical month and day
df['month'] = df['month'].astype('category').cat.codes
df['day'] = df['day'].astype('category').cat.codes

# Target column: we'll predict if area > 0 (fire occurred)
df['fire_occurred'] = df['area'].apply(lambda x: 1 if x > 0 else 0)

# Define features and target
X = df.drop(columns=['area', 'fire_occurred'])
y = df['fire_occurred']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Save model
joblib.dump(model, 'forest_fire_model.pkl')
print("Model trained and saved as forest_fire_model.pkl")
