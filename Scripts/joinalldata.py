import pandas as pd

def combine_excel_files(file1, file2, key_fields, output_file):
    # Read the Excel files
    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)

    # Perform full outer join on the specified key fields
    merged_df = pd.merge(df1, df2, on=key_fields, how='outer', suffixes=('_file1', '_file2'))

    # Save the merged DataFrame to a new Excel file
    merged_df.to_excel(output_file, index=False)

    print(f"Combined file saved as: {output_file}")

# Example usage
file1_path = '../data/Branch_cli_all.xlsx'
file2_path = '../data/LeafArea/Mean_Control_PLA_J15.xlsx'
merge_keys = ['name']  # Replace with the common field(s) to merge on
output_path = '../data/Branch_cli_all.xlsx'

combine_excel_files(file1_path, file2_path, merge_keys, output_path)
