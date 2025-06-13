# Load required libraries
library(readxl)
library(writexl)
library(missForest)
library(missMDA)
library(dplyr)

# Function to detect linear vs non-linear relationships among numeric variables
detect_relationship_type <- function(df_num) {
  
  cor_matrix <- cor(df_num, use = "pairwise.complete.obs")
  variable_pairs <- combn(colnames(cor_matrix), 2, simplify = FALSE)
  
  linear_pairs <- list()
  nonlinear_pairs <- list()
  
  for (pair in variable_pairs) {
    var1 <- pair[1]
    var2 <- pair[2]
    corr_value <- cor_matrix[var1, var2]
    
    if (!is.na(corr_value) && abs(corr_value) > 0.4) {
      linear_pairs[[paste(var1, var2, sep = " ~ ")]] <- corr_value
    } else if (!is.na(corr_value)) {
      nonlinear_pairs[[paste(var1, var2, sep = " ~ ")]] <- corr_value
    }
  }
  
  cat("✅ Linear relationships (|correlation| > 0.4):\n")
  if (length(linear_pairs) > 0) {
    print(linear_pairs)
  } else {
    cat("None detected.\n")
  }
  
  cat("\n✅ Non-linear or weak relationships (|correlation| ≤ 0.4):\n")
  if (length(nonlinear_pairs) > 0) {
    print(nonlinear_pairs)
  } else {
    cat("None detected.\n")
  }
  
  if (length(linear_pairs) > 0) {
    return("linear")
  } else {
    return("nonlinear")
  }
}

# Main function for conditional imputation
conditional_imputation <- function(data, exclude_fields = NULL) {
  
  # Separate columns to exclude from imputation
  excluded_data <- data %>% select(all_of(exclude_fields))
  data_for_imputation <- data %>% select(-all_of(exclude_fields))
  
  # Separate numeric and categorical columns
  num_data <- data_for_imputation %>% select(where(is.numeric))
  num_data <- num_data %>% select(where(~ sd(., na.rm = TRUE) != 0))
  cat_data <- data_for_imputation %>% select(where(~is.factor(.) || is.character(.)))
  
  # Detect relationship type
  rel_type <- detect_relationship_type(num_data)
  
  # Apply imputation
  if (rel_type == "linear") {
    cat("\n➡ Using missMDA (PCA-based) imputation.\n")
    ncp <- estim_ncpPCA(num_data, method = "Regularized")$ncp
    imputed <- imputePCA(num_data, ncp = ncp)$completeObs
  } else {
    cat("\n➡ Using missForest (non-linear) imputation.\n")
    imputed <- missForest(num_data)$ximp
  }
  
  # Combine all pieces together
  final_data <- bind_cols(imputed, cat_data, excluded_data)
  return(final_data)
}

# === USER-LEVEL CODE ===

# Read input Excel file
input_file <- "C:/Users/uqmasim/Documents/My PhD/Branch_Prediction/data/Br_prd_cross/ftcli_I.xlsx"
df <- read_excel(input_file)

# Specify fields NOT to impute (e.g., IDs, targets, etc.)
fields_to_exclude <- c("latitude", "longitude")  # Replace with your own
library(dplyr)

data %>% select(all_of(exclude_fields))

# Run conditional imputation
imputed_df <- conditional_imputation(data)

# Write to output Excel file
output_file <- "C:/Users/uqmasim/Documents/My PhD/Branch_Prediction/data/Br_prd_cross/all_noLA_I.xlsx"
write_xlsx(imputed_df, output_file)

cat("\n✅ Imputed data saved to:", output_file, "\n")
