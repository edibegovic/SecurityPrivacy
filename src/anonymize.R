library("sdcMicro")
library("shiny")
library("eeptools")
library("dplyr")

# TODO: set your workign directory to repo root
setwd('~/GitHub/SecurityPrivacy')

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

#private_data$age <- 2020 - as.numeric(format(private_data$dob, "%Y"))

private_data$age <- floor(age_calc(private_data$dob, units = "years"))

min(private_data$age) ## 19 so it must be recent
max(private_data$age)
hist(private_data$age) ## normally distributed around 40-45

#Age brackets.
private_data$age_group <- private_data$age
private_data$age_group <- ifelse((private_data$age<20) , '<20',private_data$age_group)
private_data$age_group <- ifelse((private_data$age>20 & private_data$age<=30) , '20-30',private_data$age_group)
private_data$age_group <- ifelse((private_data$age>30 & private_data$age<=40) , '30-40',private_data$age_group)
private_data$age_group <- ifelse((private_data$age>40 & private_data$age<=50) , '40-50',private_data$age_group)
private_data$age_group <- ifelse((private_data$age>50 & private_data$age<=60) , '50-60',private_data$age_group)
private_data$age_group <- ifelse((private_data$age>60 & private_data$age<=70) , '60-70',private_data$age_group)
private_data$age_group <- ifelse((private_data$age>70 & private_data$age<=80) , '70-80',private_data$age_group)
private_data$age_group <- ifelse((private_data$age>80 & private_data$age<=90) , '80-90',private_data$age_group)
private_data$age_group <- ifelse((private_data$age>90) , '>90',private_data$age_group)

#EU-Non, Eu

private_data$eu_citizen <- ifelse((private_data$citizenship == 'Austria' |
                           private_data$citizenship == 'Belgium' |
                           private_data$citizenship == 'Bulgaria' |
                           private_data$citizenship == 'Croatia' |
                           private_data$citizenship == 'Cyprus' |
                           private_data$citizenship == 'Czechia' |
                           private_data$citizenship == 'Denmark' |
                           private_data$citizenship == 'Estonia' |
                           private_data$citizenship == 'Finland' |
                           private_data$citizenship == 'France' |
                           private_data$citizenship == 'Germany' |
                           private_data$citizenship == 'Greece' |
                           private_data$citizenship == 'Hungary'|
                           private_data$citizenship == 'Ireland' |
                           private_data$citizenship == 'Italy' |
                           private_data$citizenship == 'Latvia' |
                           private_data$citizenship == 'Lithuania' | 
                           private_data$citizenship == 'Luxembourg' |
                           private_data$citizenship == 'Malta' |
                           private_data$citizenship == 'Netherlands' | 
                           private_data$citizenship == 'Poland' |
                           private_data$citizenship == 'Portugal' |
                           private_data$citizenship == 'Romania' |
                           private_data$citizenship == 'Slovakia' |
                           private_data$citizenship == 'Slovenia' |
                           private_data$citizenship == 'Spain' |
                           private_data$citizenship == 'Sweden'), 'EU','Non-EU')


# create sdcObject
private_sdc <- createSdcObj(private_data, keyVars = c("name", "sex", 
                                                      "evote", "citizenship",
                                                      "zip", "marital_status",
                                                      "education"), 
                            sensibleVar = c("party"), numVars = c("age"))

# check some naive stuff

private_sdc

private_data