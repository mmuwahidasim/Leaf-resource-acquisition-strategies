# Load required packages
library(ggplot2)
library(ggforce)

# Define nodes (variables and their positions)
nodes <- data.frame(
  name = c(
    "Photoperiod", "Temperature", "Light Quality", "Radiation", "Water", "Nutrient",              # Inputs
    "Flowering Time", "Leaf Number", "Leaf Area Index",                                            # Intermediate
    "Height", "Biomass", "Total Branch Number"                                                    # Outputs
  ),
  type = c(rep("input", 6), rep("intermediate", 3), rep("output", 3)),
  x = c(1, 2, 3, 4, 5, 6,  # Inputs
        2, 3, 4,           # Intermediate
        2.5, 3.5, 4.5),    # Outputs
  y = c(rep(3, 6), rep(2, 3), rep(1, 3))  # Levels: 3 = Input, 2 = Intermediate, 1 = Output
)

# Define edges (influences)
edges <- data.frame(
  from = c(
    # Inputs to intermediates and outputs
    rep(c("Photoperiod", "Temperature", "Light Quality", "Radiation", "Water", "Nutrient"), each = 6),
    # Flowering Time's influence
    rep("Flowering Time", 5),
    # Leaf Number's influence
    rep("Leaf Number", 3),
    # LAI influences
    rep("Leaf Area Index", 3),
    # Biomass influences
    rep("Biomass", 2),
    # Height to Branch Number
    "Height"
  ),
  to = c(
    # Inputs
    "Flowering Time", "Leaf Number", "Leaf Area Index", "Height", "Biomass", "Total Branch Number",
    "Flowering Time", "Leaf Number", "Leaf Area Index", "Height", "Biomass", "Total Branch Number",
    "Flowering Time", "Leaf Area Index", "Total Branch Number", "Height", "Biomass", "Total Branch Number",
    "Flowering Time", "Leaf Number", "Leaf Area Index", "Height", "Biomass", "Total Branch Number",
    "Flowering Time", "Leaf Number", "Leaf Area Index", "Height", "Biomass", "Total Branch Number",
    "Flowering Time", "Leaf Number", "Leaf Area Index", "Height", "Biomass", "Total Branch Number",
    
    # Flowering Time
    "Leaf Number", "Leaf Area Index", "Height", "Biomass", "Total Branch Number",
    
    # Leaf Number
    "Leaf Area Index", "Height", "Biomass",
    
    # LAI
    "Biomass", "Height", "Light Quality",
    
    # Biomass
    "Height", "Total Branch Number",
    
    # Height to Branch Number
    "Total Branch Number"
  )
)

# Merge positions for arrows
edges <- merge(edges, nodes[, c("name", "x", "y")], by.x = "from", by.y = "name")
edges <- merge(edges, nodes[, c("name", "x", "y")], by.x = "to", by.y = "name", suffixes = c("_from", "_to"))

# Plot
ggplot() +
  # Arrows for edges
  geom_segment(data = edges, aes(x = x_from, y = y_from, xend = x_to, yend = y_to),
               arrow = arrow(length = unit(0.15, "inches")), color = "grey40") +
  
  # Nodes
  geom_point(data = subset(nodes, type == "input"),
             aes(x = x, y = y), shape = 21, fill = "green3", size = 8, stroke = 1.5) +
  geom_rect(data = subset(nodes, type != "input"),
            aes(xmin = x - 0.5, xmax = x + 0.5, ymin = y - 0.25, ymax = y + 0.25),
            fill = "white", color = "black") +
  
  # Node labels
  geom_text(data = nodes, aes(x = x, y = y, label = name), size = 3) +
  
  # Aesthetic tuning
  theme_minimal() +
  theme(axis.title = element_blank(),
        axis.text = element_blank(),
        axis.ticks = element_blank(),
        panel.grid = element_blank()) +
  coord_fixed()

