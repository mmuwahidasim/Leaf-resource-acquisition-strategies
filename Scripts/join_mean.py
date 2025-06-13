import pandas as pd

def get_file_name():
    return input("Enter the file name (with extension): ")

def get_number_of_fields():
    return int(input("Enter the number of fields to join on: "))

def get_common_columns(num_fields):
    common_columns = []
    for i in range(num_fields):
        column_name = input(f"Enter the name of common column {i+1}: ")
        common_columns.append(column_name)
    return common_columns

def get_output_file_name():
    return input("Enter the output file name (with extension): ")

def calculate_mean_for_other_fields(df, common_columns):
    return df.groupby(common_columns).mean().reset_index()

if __name__ == "__main__":
    file_name = get_file_name()
    num_fields = get_number_of_fields()
    common_columns = get_common_columns(num_fields)
    output_file_name = get_output_file_name()
    
    # Load the data
    data = pd.read_excel(file_name)
    
    # Calculate the mean for other fields
    mean_df = calculate_mean_for_other_fields(data, common_columns)
    
    # Save the result to a new Excel file
    mean_df.to_excel(output_file_name, index=False)
    
    print(f"Mean values for other fields have been saved to {output_file_name}")
