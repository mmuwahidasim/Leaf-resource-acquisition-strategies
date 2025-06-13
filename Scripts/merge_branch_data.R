install.packages("readxl")
install.packages("writexl")

install.packages("tidyverse")  # Installs tibble and many other useful packages
library(tidyverse)

library(readxl)
library(writexl)

FtCli <- "C:/Users/uqmasim/Documents/My PhD/Branch_Prediction/data/Br_prd_cross/ftcli_I.xlsx"  # Replace with your file path
phenoftcli <- read_excel(FtCli)
Brpilot <- "C:/Users/uqmasim/Documents/My PhD/Branch_Prediction/data/Br_prd_cross/BrP_I.xlsx"  # Replace with your file path
phenobrpilot <- read_excel(Brpilot)
LA <- "C:/Users/uqmasim/Documents/My PhD/Branch_Prediction/data/Br_prd_cross/LA_I.xlsx"  # Replace with your file path
phenola <- read_excel(LA)
BrLit <- "C:/Users/uqmasim/Documents/My PhD/Branch_Prediction/data/Br_prd_cross/BrL_I.xlsx"  # Replace with your file path
phenobrlit <- read_excel(BrLit)
loc <- "C:/Users/uqmasim/Documents/My PhD/Branch_Prediction/data/Br_prd_cross/locations.xlsx"  # Replace with your file path
locations <- read_excel(loc)
allda <- "C:/Users/uqmasim/Documents/My PhD/Branch_Prediction/data/Br_prd_cross/ALL_noLA_I.xlsx"  # Replace with your file path
alld <- read_excel(allda)


br = merge(phenobrlit, phenobrpilot, by.x = "ID", by.y = "ID",all=T)
#brla=merge(br, phenola, by.x = "acc", by.y = "ABRC", all = T)
glimpse(br)
brft=merge(br, phenoftcli, by.x = "ID", by.y = "id", all = T)
#merge1 <- merge(brla, phenoftcli, by.x = "acc", by.y = "CS Number", all = TRUE)

## Then merge on the second field
#merge2 <- merge(brla, phenoftcli, by.x = "ID", by.y = "id", all = TRUE)


## Ensure both data frames have the same columns in the same order
#common_cols <- intersect(names(merge1), names(merge2))
#merge1_aligned <- merge1[, common_cols]
#merge2_aligned <- merge2[, common_cols]

# Now bind and remove duplicates
#pheno_final <- unique(rbind(merge1_aligned, merge2_aligned))
pheno_final <-brft
#glimpse(pheno_final)
# Save the completed data to an Excel file
write_xlsx(pheno_final, "C:/Users/uqmasim/Documents/My PhD/Branch_Prediction/data/Br_prd_cross/all_noLA.xlsx")

loc_data=merge(alld, locations, by.x = "AccessionID", by.y = "AccessionID", all = T)
pheno_final2 <-loc_data
#glimpse(pheno_final)
# Save the completed data to an Excel file
write_xlsx(pheno_final2, "C:/Users/uqmasim/Documents/My PhD/Branch_Prediction/data/Br_prd_cross/loc_all.xlsx")
