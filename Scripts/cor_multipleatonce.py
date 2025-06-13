import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def calculate_correlation(file_names, exclude_fields):
    correlation_matrices = {}
    
    for file_name in file_names:
        # Load the data
        data = pd.read_excel(file_name, engine='openpyxl')
        
        # Drop the excluded fields
        data = data.drop(columns=exclude_fields, errors='ignore')
        
        # Keep only numeric columns
        data = data.select_dtypes(include=[float, int])
        
        # Drop rows with NULL values
        data = data.dropna()
        
        # Calculate the correlation matrix
        correlation_matrix = data.corr()
        
        # Store the correlation matrix with the file name as the key
        correlation_matrices[file_name] = correlation_matrix
    
    return correlation_matrices

def plot_correlation_matrix(correlation_matrix, file_name):
    plt.figure(figsize=(10, 8))
    mask = correlation_matrix.abs() <= 0.2
    annot = correlation_matrix.where(~mask).round(2).astype(str)
    annot[mask] = '*'
    sns.heatmap(correlation_matrix, mask=False, annot=annot, cmap='coolwarm', fmt='', cbar_kws={'label': 'Correlation Coefficient'})
    plt.title(f'Correlation Matrix for {file_name} (|r| > 0.2 annotated, * otherwise)')
    plt.show()



# Example usage
file_names = [
    '../data/Br_prd_cross/all_noLA.xlsx',
    '../data/Br_prd_cross/all_noLA_I.xlsx',
    '../data/Br_prd_cross/Climate_output.xlsx',
    '../data/Br_prd_cross/Mean_Control_PLA_J15.xlsx',
    '../data/Br_prd_cross/mSchmitt_PNAS19_Br.xlsx',
    '../data/Br_prd_cross/pheno_pilot.xlsx',
    '../data/Br_prd_cross/LA_I.xlsx',
    '../data/Br_prd_cross/BrL_I.xlsx',
    '../data/Br_prd_cross/BrP_I.xlsx',
    '../data/Br_prd_cross/ftcli_I.xlsx'
]

exclude_fields = [
    'ABRC','name','ID','Ecotype','batch', 'rep', 'set', 'blk', 'col', 'row',
    'AccessionID','Accession_ID','Name','CS Number','Country','Collector','AdmixtureGroup',
    'Sequencedby','latitude', 'longitude', 'acc', 'id'
]

correlation_matrices = calculate_correlation(file_names, exclude_fields)

for file_name, correlation_matrix in correlation_matrices.items():
    print(f"Correlation Matrix for {file_name}:")
    print(correlation_matrix)
    plot_correlation_matrix(correlation_matrix, file_name)
