# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# def calculate_correlation(file_name, exclude_fields):
#     # Load the data
#     data = pd.read_excel(file_name)
    
#     # Drop the excluded fields
#     data = data.drop(columns=exclude_fields)
    
#     # Drop rows with NULL values
#     data = data.dropna()
    
#     # Calculate the correlation matrix
#     correlation_matrix = data.corr()
    
#     return correlation_matrix

# def plot_correlation_matrix(correlation_matrix):
#     plt.figure(figsize=(10, 8))
#     mask = (correlation_matrix > 0.2) | (correlation_matrix < -0.2)
#     sns.heatmap(correlation_matrix, annot=mask, cmap='coolwarm', fmt='.2f')
#     plt.title('Correlation Matrix (|r| > 0.2 annotated)')
#     plt.show()

# # Example usage
# file_name = '../data/Br_prd_cross.xlsx'  # Replace with your actual file name
# exclude_fields = ['batch', 'rep','set','blk','col','row','Accession_ID','latitude','longitude','acc','id','Br_Main','Br_Cauline','Br_Basal','NoRosLeaf','LeafSize:No','NoRosBr:LeafSize','NoRosBud','NoRosBud1','NoRosBud2','BoltingT','BFI','FT10_mean','FT10_se','FT10se']  # Replace with actual fields to exclude

# correlation_matrix = calculate_correlation(file_name, exclude_fields)
# print("Correlation Matrix:")
# print(correlation_matrix)
# plot_correlation_matrix(correlation_matrix)

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score

# Load the Excel file
df = pd.read_excel('../data/Br_prd_cross/matched_records.xlsx')  # Update the path if needed

# Define your x and y variable pairs with color
xy_pairs = [
    ('NoRosBr', 'Br_Basal', 'RosBr#', 'black'),  # Rosette in black
    ('NoCaulBr', 'Br_Cauline', 'CaulBr#', 'gray')  # Cauline in gray
]

# Initialize the plot
plt.figure(figsize=(9,9))

# Plot each pair
for x_col, y_col, label, color in xy_pairs:
    x = df[x_col]
    y = df[y_col]
    
    # Scatter plot
    plt.scatter(x, y, alpha=0.6, label=f'{label} Data', color=color)

    # Fit and plot regression line
    m, b = np.polyfit(x, y, 1)
    y_pred = m * x + b
    plt.plot(x, y_pred, label=f'{label} Fit', linestyle='--', color=color)

    # R² score
    r_squared = r2_score(y, y_pred)
    
    # Annotate R²
    plt.text(0.05, 0.9 - 0.05 * xy_pairs.index((x_col, y_col, label, color)), 
             f"{label} $R^2$ = {r_squared:.3f}", 
             transform=plt.gca().transAxes,size=30)

# Plot formatting
plt.xticks(rotation=0, ha='right', fontsize=30)
plt.yticks(rotation=0, va='center', fontsize= 30)
plt.xlabel('Measured Value', fontsize=30)
plt.ylabel('Imputed Value', fontsize=30)
plt.title(' ')
plt.grid(True)
plt.legend()
plt.tight_layout()

# Show the plot
plt.show()











# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import numpy as np

# def calculate_correlation(file_name, include_fields, rename_dict):
#     data = pd.read_excel(file_name)
#     data = data[include_fields].dropna()
#     data = data.rename(columns=rename_dict)
#     return data.corr()

# def plot_dual_correlation_matrix(corr1, corr2, annotate_threshold=0.2,dpi=150):
#     # Shape and mask
#     mask_upper = np.triu(np.ones_like(corr1, dtype=bool), k=1)
#     mask_lower = np.tril(np.ones_like(corr2, dtype=bool), k=-1)
#     mask_diag = np.eye(len(corr1), dtype=bool)

#     # Base matrix
#     matrix = np.where(mask_upper, corr1, np.nan)
#     matrix = np.where(mask_lower, corr2, matrix)
#     matrix = np.where(mask_diag, np.nan, matrix)

#     # Create annotations
#     annotations = np.empty_like(corr1, dtype=object)
#     for i in range(len(corr1)):
#         for j in range(len(corr1)):
#             if i == j:
#                 annotations[i, j] = " "
#             elif i < j and abs(corr1.iloc[i, j]) > annotate_threshold:
#                 annotations[i, j] = f"{corr1.iloc[i, j]:.2f}"
#             elif i > j and abs(corr2.iloc[i, j]) > annotate_threshold:
#                 annotations[i, j] = f"{corr2.iloc[i, j]:.2f}"
#             else:
#                 annotations[i, j] = "  "

#     # Custom diverging colormap: Purple (#88419d) to White to Forest Green (#006400)
#     from matplotlib.colors import LinearSegmentedColormap
#     custom_cmap = LinearSegmentedColormap.from_list("custom_corr", ['#88419d', 'white', '#006400'])

#     plt.figure(figsize=(12, 10))
#     sns.heatmap(
#         matrix,
#         annot=annotations,
#         fmt='',
#         cmap=custom_cmap,
#         vmin=-1,
#         vmax=1,
#         square=True,
#         linewidths=0.5,
#         linecolor='gray',
#         xticklabels=corr1.columns,
#         yticklabels=corr1.columns,
#         # cbar_kws={"label": "Correlation Coefficient (r)"}
#     )

#     plt.title("Correlation Coefficients(Upper Triangle: Imputed Vs Lower Triangle: Measured)", fontsize=14)
#     plt.xticks(rotation=45, ha='right',fontsize=19)
#     plt.yticks(rotation=45, va='center',fontsize=14)
#     plt.tight_layout()
#     plt.show()


# # File paths for both datasets
# file1 = '../data/Br_prd_cross/all_noLA_I.xlsx'
# file2 = '../data/Br_prd_cross/BrP_alldata.xlsx'

# # Columns and renaming
# include_fields = ['Total_Br' ,'NoCaulBr', 'NoRosBr',  'FloweringT' , 'LeafSize','AgBiomass', 'PlantHeight', 'tavg_mean', 'prec_mean']
# rename_dict = {
#     'AgBiomass': 'Biomass',
#     'LeafSize': 'LeafSize',
#     'NoRosBr': 'RosBr#',
#     'Total_Br': 'TotBr#',
#     'PlantHeight': 'PlantH',
#     'prec_mean': 'Prec',
#     'NoCaulBr': 'CaulBr#',
#     'tavg_mean': 'Temp',
#     'FloweringT': 'FlowerT'
# }

# # Calculate both correlation matrices
# corr1 = calculate_correlation(file1, include_fields, rename_dict)
# corr2 = calculate_correlation(file2, include_fields, rename_dict)

# # Plot combined matrix
# plot_dual_correlation_matrix(corr1, corr2, annotate_threshold=0.2,dpi=150)
