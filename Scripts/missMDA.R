# Install and load the necessary packages
install.packages("missMDA")
install.packages("readxl")
install.packages("writexl")
library(missMDA)
library(readxl)
library(writexl)

# Read data from an XLSX file
data <- read_excel("C:/Users/uqmasim/Documents/My PhD/Branch_Prediction/Data/LeafArea/test_null_val_fille_missMDA.xlsx", na = c("", "NA"))

# Impute missing values in non-numerical data using mode imputation
impute_mode <- function(x) {
  mode_value <- names(sort(table(x), decreasing = TRUE))[1]
  x[is.na(x)] <- mode_value
  return(x)
}
imputed_non_numeric_data <- data.frame(lapply(non_numeric_data, impute_mode))


# Separate numerical and non-numerical columns
numeric_data <- data[sapply(data, is.numeric)]
non_numeric_data <- data[sapply(data, Negate(is.numeric))]

# Impute missing values in numerical data using missMDA
imputed_numeric_data <- imputePCA(numeric_data, ncp = 5)$completeObs


# Combine the imputed numerical and non-numerical data
completed_data <- cbind(imputed_numeric_data, imputed_non_numeric_data)

# Save the completed data to a new XLSX file
write_xlsx(completed_data, "C:/Users/uqmasim/Documents/My PhD/Branch_Prediction/Data/LeafArea/completed_data.xlsx")

# Print the first few rows of the completed data
print(head(completed_data))

