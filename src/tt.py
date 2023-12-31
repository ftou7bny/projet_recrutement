import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder

# Charger votre DataFrame
df = pd.read_csv("simularity_file.csv")

# Use label encoding for 'main_cv'
label_encoder = LabelEncoder()
df['main_cv_encoded'] = label_encoder.fit_transform(df['main_cv'])

# Ensure that you have a variety of main_cv_encoded values in your test set
X_train, X_test, y_train, y_test = train_test_split(df[['main_cv_encoded']], df['similarity'], test_size=0.2, random_state=42)

# Check the unique values in X_test
print("Unique values in X_test:", X_test['main_cv_encoded'].unique())

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Create a DataFrame for prediction with all unique values of main_cv_encoded
df_pred = pd.DataFrame({'main_cv_encoded': range(df['main_cv_encoded'].min(), df['main_cv_encoded'].max() + 1)})

# Perform predictions
y_pred = model.predict(df_pred[['main_cv_encoded']])

# Print Mean Squared Error
mse = mean_squared_error(y_test, model.predict(X_test))
print(f"Mean Squared Error: {mse}")

# Plot the actual values
plt.scatter(X_test, y_test, label='Actual')

# Plot the predicted values
plt.plot(df_pred['main_cv_encoded'], y_pred, color='red', label='Predicted')

plt.xlabel('main_cv_encoded')
plt.ylabel('similarity')
plt.title('Linear Regression Results')
plt.legend()
plt.show()
