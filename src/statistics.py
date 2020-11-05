
import pandas as pd
import matplotlib
matplotlib.use('qt5Agg')
import matplotlib.pyplot as plt

base = "../data/original_excel_files/"

pdata = pd.read_excel(base + "private_dataB.xlsx")
register_public = pd.read_excel(base + "public_data_registerB.xlsx")
results_public = pd.read_excel(base + "public_data_resultsB.xlsx")

# ------------------------------------------------
# Convert EXCEL to CSV
current_df = base + "public_data_resultsB.xlsx"
df.to_csv(current_df[:-5]+".csv")

pdata.columns

# ------------------------------------------------
# Vote distribution ZIP
pdata_zip = pdata.groupby(['zip', 'party']) \
    .size() \
    .unstack(level=1) \
    [[ "Green", "Red" ]] \
    .apply(lambda x: x*100/sum(x), axis=1)

pdata_zip.plot(kind = 'bar', stacked=True, color=['g', 'r'])
plt.show()


# ------------------------------------------------
# Vote distribution AGE
pdata_age = pdata.groupby([(pdata.dob.dt.year//10)*10, "party"]) \
    .size() \
    .unstack(level=-1) \
    [[ "Green", "Red" ]] \
    .fillna(0) \
    .apply(lambda x: x*100/sum(x), axis=1)

pdata_age.plot(kind = 'bar', stacked=True, color=['g', 'r'])
plt.show()

# ------------------------------------------------
# Vote distribution EDUCATION
pdata_age = pdata.groupby(["education", "party"]) \
    .size() \
    .unstack(level=-1) \
    [[ "Green", "Red" ]] \
    .fillna(0) \

pdata_age.plot(kind = 'bar', stacked=True, color=['g', 'r'])
plt.show()




