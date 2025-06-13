import pandas as pd

def categorize_columns(file_name, column_names, output_file_name):
    # Read the Excel file
    df = pd.read_excel(file_name)
    
    for column in column_names:
        # Check if the column is empty
        if df[column].isnull().all():
            df[column + '_category'] = None
            continue
        
        # Calculate mean and standard deviation
        mean = df[column].mean()
        std_dev = df[column].std()
        
        # Define the categorization function
        def categorize(value):
            if pd.isnull(value):
                return None
            elif value < mean - std_dev:
                return 0
            elif value > mean + std_dev:
                return 2
            else:
                return 1
        
        # Apply the categorization function to the column
        df[column + '_category'] = df[column].apply(categorize)
    
    # Save the updated DataFrame to a new Excel file
    df.to_excel(output_file_name, index=False)
    
    return df

# Get input from the user
file_name = input("Enter the input file name (with .xlsx extension): ")
column_names = input("Enter the column names separated by commas: ").split(',')
output_file_name = input("Enter the output file name (with .xlsx extension): ")

# Call the function with user inputs
categorized_df = categorize_columns(file_name, column_names, output_file_name)
print("Categorized data saved to:", output_file_name)
print(categorized_df)
