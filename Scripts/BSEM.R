
# Install cmdstanr from the Stan development team
install.packages("cmdstanr", repos = c("https://mc-stan.org/r-packages/", getOption("repos")))

library(brms)
library(cmdstanr)

# Install CmdStan (this downloads and compiles it)
install_cmdstan()

# Load your data
library(readxl)
pheno <- read_excel("C:/Users/uqmasim/Documents/My PhD/Branch_Prediction/data/Branching/pheno_pilot_adj_trans2_2.xlsx")

# Convert grouping variable if needed
pheno$group <- as.factor(pheno$blk)  # or use another grouping variable
# Define SEM paths
mod1 <- bf(FloweringT ~ LeafSize + (1|group)) + gaussian()
mod2 <- bf(NoRosBr ~ FloweringT + LeafSize + (1|group)) + lognormal()

# Fit the SEM
MySEMmod <- brm(mod1 + mod2 + set_rescor(FALSE), data = pheno,
                control = list(adapt_delta = 0.99, max_treedepth = 15),
                chains = 3, cores = 3, threads = threading(4),
                backend = "cmdstanr", iter = 2000)

# Summarize and check
summary(MySEMmod)
plot(MySEMmod)
pp_check(MySEMmod, resp = "FloweringT")
pp_check(MySEMmod, resp = "NoRosBr")
