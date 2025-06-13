# Load necessary libraries
library(readxl)
library(ggplot2)
library(akima)
library(ggrepel)
library(dplyr)

# Read data
input_file2 <- "C:/Users/uqmasim/Documents/My PhD/Branch_Prediction/data/Branching/Ara_Clim_052025.csv"
pheno2 <- read.csv(input_file2)
input_file <- "C:/Users/uqmasim/Documents/My PhD/Branch_Prediction/data/Br_prd_cross/all_noLA_I.xlsx"
pheno <- read_excel(input_file)

data <- merge(pheno, pheno2, by.x = "ID", by.y = "Accession.ID", all = TRUE)

# Ensure required columns exist
if (!all(c("latitude", "longitude", "prec_mean", "group") %in% colnames(data))) {
  stop("Missing one or more required columns: latitude, longitude, prec_mean, group")
}

# Interpolate prec_mean for contours
interp_data <- with(data, interp(x = longitude, y = latitude, z = prec_mean, duplicate = "mean"))
interp_df <- expand.grid(x = interp_data$x, y = interp_data$y)
interp_df$z <- as.vector(interp_data$z)

# Start plotting
p <- ggplot() +
  # Add contours
  geom_contour_filled(data = interp_df, aes(x = x, y = y, z = z), alpha = 0.7) +
  scale_fill_viridis_d(name = "prec_mean") +
  
  # Add red dots for individual data points
  geom_point(data = data, aes(x = longitude, y = latitude), color = "red", size = 2) +
  
  # Add region names using ggrepel
  geom_text_repel(
    data = data %>%
      group_by(group) %>%
      summarize(longitude = mean(longitude), latitude = mean(latitude), .groups = "drop"),
    aes(x = longitude, y = latitude, label = group),
    size = 4,
    fontface = "bold"
  ) +
  
  # Clean style with no grids
  theme_minimal() +
  theme(
    panel.grid.major = element_blank(),
    panel.grid.minor = element_blank()
  ) +
  
  labs(
    title = "Mean Precipitation Map by Region",
    x = "Longitude",
    y = "Latitude"
  ) +
  coord_fixed()

# Print the plot
print(p)

