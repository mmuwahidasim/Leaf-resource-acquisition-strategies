# Load necessary libraries
library(readxl)
library(dplyr)
library(writexl)

# Read the Excel files
file1 <- read_excel("C:/Users/uqmasim/Documents/My PhD/Branch_Prediction/data/Br_prd_cross/locations.xlsx")
file2 <- read_excel("C:/Users/uqmasim/Documents/My PhD/Branch_Prediction/data/Br_prd_cross/all_noLA_I.xlsx")

# Ensure the ID columns are named the same and are of the same type
file1$ID <- as.character(file1$AccessionID)
file2$ID <- as.character(file2$AccessionID)

# Filter records from file2 where ID matches with file1
matched_records <- file2 %>% filter(AccessionID %in% file1$AccessionID)

# Write the matched records to a new Excel file
write_xlsx(matched_records, "C:/Users/uqmasim/Documents/My PhD/Branch_Prediction/data/Br_prd_cross/location_records_allimputed.xlsx")

