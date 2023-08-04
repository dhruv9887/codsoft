# -*- coding: utf-8 -*-
"""CodSoft - TASK 1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16s-6Yk8DzmW7Qe8ZPb0nq5c3tvxAf3PL

# **CodSoft - TASK 1**

# **CREDIT CARD FRAUD DETECTION**
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

# Load the dataset
data = pd.read_csv('/content/drive/MyDrive/CodSoft/creditcard.csv')

# Handle missing values
data.dropna(inplace=True)

# Separate features and target
X = data.drop(['Class','Time'], axis=1)
y = data['Class']

# Normalize numerical features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 2: Splitting the Dataset
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Step 3: Model Selection and Training
# Choose a model (e.g., Logistic Regression)
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

# Step 4: Model Evaluation
# Make predictions
y_pred = model.predict(X_test)

# Calculate metrics
conf_matrix = confusion_matrix(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print("Confusion Matrix:\n", conf_matrix)
print("\nClassification Report:\n\n", classification_rep)