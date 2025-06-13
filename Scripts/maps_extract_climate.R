# Load required libraries
library(readxl)
library(writexl)
library(geodata)
library(raster)
library(dplyr)

# Read Excel file (replace with your actual file path)
input_data <- read_excel("C:/Users/uqmasim/Documents/My PhD/Branch_Prediction/data/FT/1001_Arabidopsis_accession_details.xlsx")


colnames(input_data)[colnames(input_data) %in% c("Lat", "Latitude")] <- "latitude"
colnames(input_data)[colnames(input_data) %in% c("Long", "Longitude")] <- "longitude"

coords <- input_data %>% select(longitude, latitude)
coords_vect <- vect(as.data.frame(coords), geom = c("longitude", "latitude"), crs = "EPSG:4326")


climate_vars <- c("tavg", "tmin", "tmax", "prec", "srad", "wind", "vapr")
raster_path <- tempdir()

for (var in climate_vars) {
  message(paste("Processing:", var))
  raster_stack <- worldclim_global(var = var, res = 0.5, path = raster_path)
  extracted <- terra::extract(raster_stack, coords_vect)
  input_data[[paste0(var, "_mean")]] <- rowMeans(extracted[,-1], na.rm = TRUE)
}


# Save updated data to Excel
write_xlsx(input_data, "C:/Users/uqmasim/Documents/My PhD/Branch_Prediction/data/FT/Climate_output.xlsx")
