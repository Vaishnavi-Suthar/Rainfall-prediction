# 📦 Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib


# ================================
# ⿡ Load Dataset
# ================================
print("🔵 Loading dataset...")
data = pd.read_csv("train.csv")
print("✅ Dataset loaded successfully!")
print("📊 First 5 rows of dataset:")
print(data.head())

# ================================
# ⿢ Clean Dataset
# ================================
print("\n🔵 Checking for missing values...")
print(data.isnull().sum())

print("\n🔵 Removing missing values...")
data.dropna(inplace=True)
print("✅ Missing values removed.")
print("📏 Dataset shape after removing missing values:", data.shape)

# ================================
# ⿣ Define Features and Target
# ================================
print("\n🔵 Separating features and target variable...")
X = data.drop(['id', 'rainfall'], axis=1)
y = data['rainfall']  # assuming already binary 0/1
print("✅ Features and target separated.")
print(X)
print(y)

# ================================
# ⿤ Split Dataset into Train and Test
# ================================
print("\n🔵 Splitting dataset into training and testing sets (80-20 split)...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
print("✅ Dataset split completed.")
print(f"📈 Training set size: {X_train.shape[0]} samples")
print(f"📊 Testing set size: {X_test.shape[0]} samples")

# ================================
# ⿥ Scale Features
# ================================
print("\n🔵 Applying StandardScaler to features...")
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print("✅ Feature scaling completed.")

# ================================
# ⿦ Train Random Forest Classifier
# ================================
print("\n🔵 Training Random Forest Classifier...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)
print("✅ Model training completed.")

# ================================
# ⿧ Make Predictions
# ================================
print("\n🔵 Making predictions on the test set...")
y_pred = model.predict(X_test_scaled)
print("✅ Predictions completed.")

# ================================
# ⿨ Evaluate the Model
# ================================
print("\n🔵 Evaluating model performance...")
accuracy = accuracy_score(y_test, y_pred)
print(f"📊 Accuracy: {accuracy:.4f}")

print("\n📊 Classification Report:")
print(classification_report(y_test, y_pred))

print("\n📊 Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# ================================
# ⿩ Plot Feature Importances
# ================================
print("\n🔵 Plotting feature importances...")
importances = model.feature_importances_
feature_names = X.columns
feat_imp = pd.Series(importances, index=feature_names).sort_values(ascending=False)

plt.figure(figsize=(9, 6))
sns.barplot(x=feat_imp, y=feat_imp.index)
plt.xlabel('Feature Importance Score')
plt.ylabel('Features')
plt.title("Random Forest - Important Features")
plt.show()
print("✅ Feature importance plot displayed.")

# ================================
# 🔟 Save Model and Scaler
# ================================
print("\n🔵 Saving trained model and scaler to files...")
joblib.dump(model, "rainfall_predictor_model.pkl")
joblib.dump(scaler, "scaler.pkl")
print("✅ Model saved as 'rainfall_predictor_model.pkl'")
print("✅ Scaler saved as 'scaler.pkl'")

# ================================
# 🎉 Done!
# ================================
print("\n🎉 Training, evaluation, and saving completed successfully!") 