import pandas as pd

def get_number_of_files():
    return int(input("Enter the number of files: "))

def get_file_names(num_files):
    file_names = []
    for i in range(num_files):
        file_name = input(f"Enter the name of file {i+1} (with extension): ")
        file_names.append(file_name)
    return file_names

def get_common_column():
    return input("Enter the common column name to join on: ")

def get_output_file_name():
    return input("Enter the output file name (with extension): ")

def join_files(file_names, common_column):
    # Load the first file
    df = pd.read_excel(file_names[0])
    
    # Iterate over the remaining files and join them
    for file_name in file_names[1:]:
        temp_df = pd.read_excel(file_name)
        df = df.merge(temp_df, on=common_column, how='inner')
    
    return df

if __name__ == "__main__":
    num_files = get_number_of_files()
    file_names = get_file_names(num_files)
    common_column = get_common_column()
    output_file_name = get_output_file_name()
    
    # Join the files
    joined_df = join_files(file_names, common_column)
    
    # Save the result to a new Excel file
    joined_df.to_excel(output_file_name, index=False)
    
    print(f"Joined data has been saved to {output_file_name}")
