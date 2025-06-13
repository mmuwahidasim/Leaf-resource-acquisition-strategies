import pandas as pd

def split_by_category(file_name, field_name):
    # Load the data
    df = pd.read_excel(file_name)
    
    # Get unique categories in the specified field
    categories = df[field_name].unique()
    
    # Create separate files for each category
    for category in categories:
        # Filter the DataFrame for the current category
        category_df = df[df[field_name] == category]
        
        # Create a file name for the category
        category_file_name = f"{field_name}_{category}.xlsx"
        
        # Save the filtered DataFrame to a new Excel file
        category_df.to_excel(category_file_name, index=False)
        
        print(f"File created for category '{category}': {category_file_name}")

# Get input from the user
file_name = input("Enter the input file name (with .xlsx extension): ")
field_name = input("Enter the field name to split by: ")

# Call the function with user inputs
split_by_category(file_name, field_name)
