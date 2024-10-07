import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier
import model_building.model_io as model_io

model = RandomForestClassifier(n_estimators=100, random_state=42)

bank_data = pd.read_csv('cleaned_bank_marketing.csv')

X = bank_data.drop('deposit', axis=1)
y = bank_data['deposit']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model on the training data
model.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Save the trained model to a file
model_io.save_model(model, 'random_forest_model.joblib')

# Load the saved model from the file
loaded_model = model_io.load_model('random_forest_model.joblib')

# Make predictions using the loaded model
loaded_y_pred = loaded_model.predict(X_test)

print("Loaded Model Accuracy:", accuracy_score(y_test, loaded_y_pred))
print("Loaded Model Classification Report:")
print(classification_report(y_test, loaded_y_pred))