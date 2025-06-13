# Install and load necessary packages
install.packages("missForest")
install.packages("readxl")
install.packages("writexl")
library(missForest)
library(readxl)
library(writexl)

# Read the dataset
data <- read_excel("C:/Users/uqmasim/Documents/My PhD/Branch_Prediction/Data/LeafArea/test_null_val_fille_missMDA.xlsx", na = c("", "NA"))
data <- as.data.frame(data)

# Separate numeric and non-numeric columns
numeric_data <- data[sapply(data, is.numeric)]
non_numeric_data <- data[sapply(data, Negate(is.numeric))]

# Impute numeric data using missForest
set.seed(123)
imputed_numeric <- missForest(numeric_data)$ximp

# Impute categorical (non-numeric) data using mode
impute_mode <- function(x) {
  mode_val <- names(sort(table(x), decreasing = TRUE))[1]
  x[is.na(x)] <- mode_val
  return(x)
}
imputed_non_numeric <- as.data.frame(lapply(non_numeric_data, impute_mode))

# Combine the imputed datasets
completed_data <- cbind(imputed_numeric, imputed_non_numeric)

# Save the completed data to an Excel file
write_xlsx(completed_data, "C:/Users/uqmasim/Documents/My PhD/Branch_Prediction/Data/LeafArea/completed_dataMF.xlsx")

# Show the first few rows
print(head(completed_data))
