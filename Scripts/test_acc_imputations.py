import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Load the Excel files
original_df = pd.read_excel('../data/LeafArea/test_missing_impute.xlsx')
missing_df = pd.read_excel('../data/LeafArea/test_null_val_fille_missMDA.xlsx')
imputed_df = pd.read_excel('../data/LeafArea/completed_dataMF.xlsx')

# Keep only numeric columns
numeric_cols = original_df.select_dtypes(include=[np.number]).columns
original_df = original_df[numeric_cols]
missing_df = missing_df[numeric_cols]
imputed_df = imputed_df[numeric_cols]

# Identify missing positions
missing_mask = missing_df.isna()

# Extract only the imputed values at missing positions
original_values = original_df[missing_mask]
imputed_values = imputed_df[missing_mask]

# Convert to flattened arrays
original_flat = original_values.values.flatten()
imputed_flat = imputed_values.values.flatten()

# Filter out any remaining NaNs (just in case)
valid_mask = np.isfinite(original_flat) & np.isfinite(imputed_flat)
original_clean = original_flat[valid_mask]
imputed_clean = imputed_flat[valid_mask]

# Compute metrics
rmse = np.sqrt(mean_squared_error(original_clean, imputed_clean))
mae = mean_absolute_error(original_clean, imputed_clean)

print(f"RMSE: {rmse:.4f}")
print(f"MAE: {mae:.4f}")