import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.metrics import mean_squared_error
import numpy as np

def train_neural_network(file_name, target_field, fields_to_remove):
    # Load the data
    df = pd.read_excel(file_name)
    
    # Drop the fields to remove
    df = df.drop(columns=fields_to_remove)
    
    # Remove rows with null values
    df = df.dropna()
    
    # Select the input fields and target field
    X = df.drop(columns=[target_field])
    y = df[target_field]
    
    # Standardize the input features
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and train the neural network
    model = Sequential()
    model.add(Dense(256, input_dim=X_train.shape[1], activation='relu'))
    model.add(Dense(128, input_dim=X_train.shape[1], activation='relu'))
    model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(1))  # Output layer for regression
    
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(X_train, y_train, epochs=50, batch_size=2, verbose=1)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Calculate mean squared error
    mse = mean_squared_error(y_test, y_pred)
    
    return mse

# Get input from the user
file_name = input("Enter the input file name (with .xlsx extension): ")
target_field = input("Enter the target field name: ")
fields_to_remove = input("Enter the fields to remove separated by commas: ").split(',')

# Call the function with user inputs
mse = train_neural_network(file_name, target_field, fields_to_remove)
print("Mean Squared Error:", mse)

# Convert MSE to MAE
mae = np.sqrt(np.pi / 2 * mse)

print(f"Approximate MAE: {mae}")
