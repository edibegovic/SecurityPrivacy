from scipy.stats import chisquare, ttest_ind
import pandas as pd
import matplotlib as pyplot

#  In other words, it tells you if your sample data represents the data you would expect 
#  to find in the actual population. 
# A chi-square goodness of fit test determines if a sample data matches a population. For more details on this type, see: Goodness of Fit Test.
# A chi-square test for independence compares two variables in a contingency table to see if they are related. In a more general sense, it tests to see whether distributions of categorical variables differ from each another.
# A very small chi square test statistic means that your observed data fits your expected data extremely well. In other words, there is a relationship.
# A very large chi square test statistic means that the data does not fit very well. In other words, there isn’t a relationship.

#A - Non-Anon

private_data = pd.read_excel("C:/Users/hogni/Documents/GitHub/SecurityPrivacy/data/original_excel_files/private_dataB.xlsx")
public_data = pd.read_excel("C:/Users/hogni/Documents/GitHub/SecurityPrivacy/data/original_excel_files/public_data_registerB.xlsx")

zero = len(public_data[public_data["last_voted"] == 0])
one = len(public_data[public_data["last_voted"] == 1])
public_sum = zero + one

private_zero = len(private_data[private_data["evote"] == 0])
private_one = len(private_data[private_data["evote"] == 1])
private_sum = private_zero + private_one

chisquare([private_zero/private_sum, private_one/private_sum], f_exp=[zero/public_sum, one/public_sum])

#A - Anon

private_data = pd.read_csv("C:/Users/hogni/Documents/GitHub/SecurityPrivacy/kanon2.csv")
public_data = pd.read_excel("C:/Users/hogni/Documents/GitHub/SecurityPrivacy/data/original_excel_files/public_data_registerB.xlsx")

zero = len(public_data[public_data["last_voted"] == 0])
one = len(public_data[public_data["last_voted"] == 1])
public_sum = zero + one

private_zero = len(private_data[private_data["evote"] == 0])
private_one = len(private_data[private_data["evote"] == 1])
private_sum = private_zero + private_one

chisquare([private_zero/private_sum, private_one/private_sum], f_exp=[zero/public_sum, one/public_sum])

#B

# The null hypothesis states that there is no relationship between the two variables being studied (one variable does not affect the other). 
# It states the results are due to chance and are not significant in terms of supporting the idea being investigated. 
# Thus, the null hypothesis assumes that whatever you are trying to prove did not happen.
# The alternative hypothesis is the one you would believe if the null hypothesis is concluded to be untrue.

# The alternative hypothesis states that the independent variable did affect the dependent variable, and the results are significant in terms of 
# supporting the theory being investigated (i.e. not due to chance).

# How do you know if a p-value is statistically significant?
# The level of statistical significance is often expressed as a p-value between 0 and 1. The smaller the p-value, the stronger the evidence that you should reject the null hypothesis.

# A p-value less than 0.05 (typically ≤ 0.05) is statistically significant. 
# It indicates strong evidence against the null hypothesis, as there is less than a 5% probability the null is correct (and the results are random). 
# Therefore, we reject the null hypothesis, and accept the alternative hypothesis.

#Evote - Non-Anon

private_data = pd.read_excel("C:/Users/hogni/Documents/GitHub/SecurityPrivacy/data/original_excel_files/private_dataB.xlsx")

tStat, pValue = 0, 0

vote = private_data[private_data["evote"] != 2]
#vote["Int_party"] = vote["party"].apply(lambda x: int("1") if x == "Red" else int("2"))
vote
inperson = vote[vote["evote"] == 0]
e_vote = vote[vote["evote"] == 1]

inperson_1 = len(inperson[inperson["party"] == "Red"])
inperson_2 = len(inperson[inperson["party"] == "Green"])
inperson_sum = inperson_1 + inperson_2

inperson_sum

evote_1 = len(e_vote[e_vote["party"] == "Red"])
evote_2 = len(e_vote[e_vote["party"] == "Green"])
evote_sum = evote_1 + evote_2

evote_sum

total_sum = inperson_sum + evote_sum

print(f"Inperson ratio: Red {(inperson_1/inperson_sum) * 100} Green {(inperson_2/inperson_sum) * 100} \nEvote ratio: Red {(evote_1/evote_sum) * 100} Green {(evote_2/evote_sum) * 100} ")

# print(f"E-vote: Red {(inperson_1/total_sum)*100} Green {(inperson_2/total_sum)*100} \nInperson: Red {(evote_1/total_sum)*100} Green {(evote_2/total_sum)*100}")

# tStat, pValue = ttest_ind(inperson["Int_party"], e_vote["Int_party"])
# print("P-Value:{0} T-Statistic:{1}".format(pValue,tStat))

#Evote - Anon

private_data = pd.read_csv("C:/Users/hogni/Documents/GitHub/SecurityPrivacy/kanon2.csv")

tStat, pValue = 0, 0

vote = private_data[private_data["evote"] != 2]
vote["Int_party"] = vote["party"].apply(lambda x: int("1") if x == "Red" else int("2"))

inperson = vote[vote["evote"] == 0]
e_vote = vote[vote["evote"] == 1]

tStat, pValue = ttest_ind(inperson["Int_party"], e_vote["Int_party"])
print("P-Value:{0} T-Statistic:{1}".format(pValue,tStat))

# C

#Evote - Non-Anon

private_data = pd.read_excel("C:/Users/hogni/Documents/GitHub/SecurityPrivacy/data/original_excel_files/private_dataB.xlsx")

tStat, pValue = 0, 0

vote = private_data[private_data["evote"] != 2]
vote["Int_party"] = vote["party"].apply(lambda x: int("1") if x == "Red" else int("2"))

inperson = vote[vote["evote"] == 0]
e_vote = vote[vote["evote"] == 1]

e_vote["age"] = e_vote["dob"].apply(lambda x: 2020 - x.year)
e_vote = e_vote[["sex","age","zip","citizenship","marital_status","Int_party"]]

inperson["age"] = inperson["dob"].apply(lambda x: 2020 - x.year)
inperson = inperson[["sex","age","zip","citizenship","marital_status","Int_party"]]

e_vote
tStat, pValue = ttest_ind(inperson["Int_party"], e_vote["Int_party"])
print("P-Value:{0} T-Statistic:{1}".format(pValue,tStat))
