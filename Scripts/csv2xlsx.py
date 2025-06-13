import pandas as pd

def get_file_name():
    return input("Enter the file name (with extension): ")

def get_file_type():
    return input("Enter the file type (csv or tsv): ").strip().lower()

def get_excel_file_name():
    return input("Enter the output Excel file name (with extension): ")

def convert_to_excel(file_name, file_type, excel_file_name):
    # Load the data based on file type
    if file_type == 'csv':
        data = pd.read_csv(file_name)
    elif file_type == 'tsv':
        data = pd.read_csv(file_name, sep='\t')
    else:
        print("Unsupported file type. Please enter 'csv' or 'tsv'.")
        return
    
    # Save the data to an Excel file
    data.to_excel(excel_file_name, index=False)
    
    print(f"{file_type.upper()} file '{file_name}' has been converted to Excel file '{excel_file_name}'")

if __name__ == "__main__":
    file_name = get_file_name()
    file_type = get_file_type()
    excel_file_name = get_excel_file_name()
    
    convert_to_excel(file_name, file_type, excel_file_name)
