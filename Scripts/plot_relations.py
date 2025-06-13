import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset
# Replace 'your_data.csv' with the path to your actual dataset

data = pd.read_excel('../data/BrCli.xlsx', engine='openpyxl')


# Remove all rows with null values
data_cleaned = data.dropna()

# Define the target field
target_field = 'Br_Cauline'  # Replace with the actual target column name


# Generate line plots of each input field against the target field
input_fields = [col for col in data_cleaned.columns if col != target_field]

for field in input_fields:
    plt.figure(figsize=(10, 6))
    plt.plot(data_cleaned[field], data_cleaned[target_field], marker='o')
    plt.title(f'{field} vs {target_field}')
    plt.xlabel(field)
    plt.ylabel(target_field)
    plt.grid(True)
    plt.show()
