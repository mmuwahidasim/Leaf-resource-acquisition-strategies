import pandas as pd

# === Parameters ===
input_file = 'C:/Users/uqmasim/Documents/My PhD/Branch_Prediction/data/Branching/pheno_pilot_adj_trans2_2.xlsx'   # Replace with your input file path
output_file = 'C:/Users/uqmasim/Documents/My PhD/Branch_Prediction/data/Branching/pilot_data.xlsx' # Replace with your desired output file path

# === Read the Excel file ===
df = pd.read_excel(input_file)

# === Replace NaN values with empty strings ===
df_filled = df.fillna('')

# === Write the cleaned DataFrame back to Excel ===
df_filled.to_excel(output_file, index=False)

print(f"✅ Saved file with NA replaced by empty string to: {output_file}")
