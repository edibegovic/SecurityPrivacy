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

private_sdc <- createSdcObj(private_data, keyVars = c("name", "sex", 
                                                      "evote", "citizenship",
                                                      "zip", "marital_status",
                                                      "education"), 
                            sensibleVar = c("party"), numVars = c("age"))

# check some naive stuff

private_sdc

