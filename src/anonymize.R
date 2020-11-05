library("sdcMicro")
library("shiny")

# TODO: set your workign directory to repo root
setwd('~/git/SecurityPrivacy')

# for visual exploration

#sdc <- sdcApp()

# read the files
private_data <- read.csv("data/private_dataB.csv")
public_register_data <- read.csv("data/public_data_registerB.csv")
public_results_data <- read.csv("data/public_data_resultsB.csv")

# observe and transform variables
names(private_data)
head(private_data)

private_data$evote <- as.factor(private_data$evote)
private_data$zip <- as.factor(private_data$zip)

private_data$dob <- as.Date(private_data$dob)

private_data$age <- 2020 - as.numeric(format(private_data$dob, "%Y"))

min(private_data$age) ## 19 so it must be recent
hist(private_data$age) ## normally distributed around 40-45

# create sdcObject

private_sdc <- createSdcObj(private_data, keyVars = c("sex", 
                                                      "evote", "citizenship",
                                                      "zip", "marital_status"
                                                      "education", "age"), 
                            sensibleVar = "party")

# check some naive stuff

private_sdc

# ----------------------------------------------------------------------
#   
#   
#   Infos on 2/3-Anonymity:
#   
#   Number of observations violating
# - 2-anonymity: 196 (98.000%)
# - 3-anonymity: 200 (100.000%)
# - 5-anonymity: 200 (100.000%)
# 
# ----------------------------------------------------------------------

# group age to four categories
  
labels <- c("0-30", "31-45", "46-65", "65+")
private_sdc <- globalRecode(private_sdc, column="age", breaks = c(-1, 30, 45, 65, 120),
                            labels = labels)

hist(extractManipData(private_sdc)$age) # 1-4

private_sdc


# ----------------------------------------------------------------------
#   
#   
#   Infos on 2/3-Anonymity:
#   
#   Number of observations violating
# - 2-anonymity: 141 (70.500%) | in original data: 196 (98.000%)
# - 3-anonymity: 191 (95.500%) | in original data: 200 (100.000%)
# - 5-anonymity: 200 (100.000%) | in original data: 200 (100.000%)
# 
# ----------------------------------------------------------------------

# citizenship to Denmark and other
countries <- unique(private_data$citizenship)
denmark_idx <- which("Denmark" %in% countries)
other_countries <- countries[-denmark_idx]
other_countries


private_sdc <- groupAndRename(private_sdc, var = c("citizenship"), 
                    before = as.factor(other_countries), 
                    after = c("Other"))

private_sdc@manipKeyVars$citizenship

# remap education too

private_sdc <- groupAndRename(private_sdc, var = c("education"), 
                    before = c("Primary education", "Upper secondary education", "Vocational Education and Training (VET)", 
                               "Short cycle higher education", "Vocational bachelors educations", "Bachelors programmes", "Masters programmes",
                               "PhD programmes"), 
                    after = c("Short", "Short", "Medium", "Medium", "Long", "Longer", "Longer", "Longer"))

private_sdc@manipKeyVars$education


private_sdc@risk$global

private_sdc