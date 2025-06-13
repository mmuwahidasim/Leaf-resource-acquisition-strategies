import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error

def train_xgboost_model(file_name, target_field, fields_to_remove):
    # Load the data
    df = pd.read_excel(file_name)
    
    # Drop the fields to remove
    df = df.drop(columns=fields_to_remove)
    
    # Remove rows with null values
    df = df.dropna()
    
    # Select the input fields and target field
    X = df.drop(columns=[target_field])
    y = df[target_field]
    
    # Encode the target field if it's categorical
    if y.dtype == 'object':
        label_encoder = LabelEncoder()
        y = label_encoder.fit_transform(y)
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
    
    # Initialize and train the XGBoost regressor
    model = XGBRegressor(objective='reg:squarederror')
    model.fit(X_train, y_train)
    
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
mse = train_xgboost_model(file_name, target_field, fields_to_remove)
print("Mean Squared Error:", mse)
