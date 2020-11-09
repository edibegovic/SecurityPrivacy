from scipy.stats import chisquare, ttest_ind
import pandas as pd

#A

private_data = pd.read_excel("C:/Users/hogni/Documents/GitHub/SecurityPrivacy/data/original_excel_files/private_dataB.xlsx")
public_data = pd.read_excel("C:/Users/hogni/Documents/GitHub/SecurityPrivacy/data/original_excel_files/public_data_registerB.xlsx")

zero = len(public_data[public_data["last_voted"] == 0])
one = len(public_data[public_data["last_voted"] == 1])
public_sum = zero + one

private_zero = len(private_data[private_data["evote"] == 0])
private_one = len(private_data[private_data["evote"] == 1])
private_sum = private_zero + private_one

chisquare([private_zero/private_sum, private_one/private_sum], f_exp=[zero/public_sum, one/public_sum])

#B

#Evote
tStat, pValue = 0, 0

vote = private_data[private_data["evote"] != 2]
vote["Int party"] = vote["party"].apply(lambda x: int("1") if x == "Red" else int("2"))

inperson = vote[vote["evote"] == 0]
e_vote = vote[vote["evote"] == 1]

tStat, pValue = ttest_ind(inperson["Int party"], e_vote["Int party"])
print("P-Value:{0} T-Statistic:{1}".format(pValue,tStat))
