# 	SDC for Voting Survey

###### Edi Begovic (edbe)  ·  Gergo Koncz (geko)  ·  Høgni Jacobsen (hoja)



### Introduction

We use the sdcMicro web interface to analyse the relationships between the different variables to determine how much they influence each other. 

We register all variables available in the public register as quasi-identifiers, such that *party* (voted for) is considered the only sensible variable. 



### Methodology

We start out by removing any direct identifiers; this just includes the names, which also carry no utility for the analysis.

##### Recoding

Apart from *DOB* (*date for birth*), all other key variables are categorical but contain many different values and thus increases uniqueness. We therefore split them into more coarse groups, where we don't deem a high reduction in utility. Likewise, age is grouped into four ranges. 

| Variable              | Grouping                                         | k2-anonymity violation |
| :-------------------- | ------------------------------------------------ | ---------------------- |
| Original              | -                                                | 198 · 98%              |
| DOB (*date of birth*) | 1 (<31)<br />2 (31-45)<br />3(46-65)<br />4(>65) | 183 · 92%              |
| Citizenship           | Danish<br />Other                                | 183 · 92%              |

As *educational background* is not considered publicly available, we decided to include it without any modification. This information is however - as with everything else - still susceptible for recognition by the end user. 

##### Suppression

After recoding, we let sdcMicro apply local suppression to achieve 2k-anonymity. We do not specify any importance vector, as very few suppressions are needed.

| Variable    | Number of supressed values | %     |
| :---------- | -------------------------- | ----- |
| Age         | 21                         | 10.5% |
| Zip         | 4                          | 2%    |
| Citizenship | 1                          | 0.5%  |

After suppression we achieve 2k-anonymity as well as only having 8 individuals (4%) violate k3-anonymity.

##### Perturbation

After suppression we have a very low percentage of individuals violating 3k-anonymity and none violating 2k-anonymity, therefore we decided not to apply any perturbation to the data to keep more utility. We believe that This has to be specified very clearly to the end-user of the data, as any other analysis based on the data would be incorrect. 

### 

### Assessing Utility

To asses the utility of the modified data, we check the 95% confidence intervals on the proportions of red/green votes for each categorical value. This way we can be certain the the 



### Uses for Analysis

For the analytical purposes of the data, we'd argue that, apart from voting type and choice (*evote* and *party*, respectively), age in itself would suffice as argumentation for the skew in how electronic and paper ballots were cast. However, all of the demographical variables are correlated to various degrees and thus we decided to keep them all.

In respect to the analytical questions provided, we would attack them the same way with the anonymised data as with the non-anonymised. 

The difference in political preference from the survey and election results **(A)** can be compared by inspecting the method of voting (*evote*) and choice (*party*). One can

###### A)	

This question is answered in the same way for the original and anonymized data. As we have not used any perturbative anonymization methods and neither voting locations nor any the party variable was suppressed, we can therefore perform a Chi-squared test on votes for each party by voting type. 

The data frame, "" or "", is separated into two data frames, one containing e-voters and another containing in person voters.

The votes for each party, Green and Red, are then summed for each voting location. A Chi-squared test is then performed on the summed values from the sample and the totals from the population, "public_data_resultsB.xlsx".

###### B)

This question is answered in the same way for the original and anonymized data. Using "private_dataB.xlsx" or "" we separate this into two data frames, one containing e-voters and another containing in person voters. The sum of votes for the Red and the Green party in each data frame are calculated. We can now calculate the ratio of Red and Green party votes for each voting method. The ratio of in person and e-votes are then compared. If either method leans more than 10% either side of the other then we consider it a significant difference.

###### C)

The demographic factors used are "sex","zip","citizenship","marital_status" and "party" for the original dataset and xx xx x xx xx for the anonymized dataset.  For each dataset we follow the same steps as in B, separate them into two data frames, one containing e-voters and another containing in person voters. These two data fames are then further split along demographic lines.  Using "private_dataB.xlsx" or "" we separate this into two data frames, one containing e-voters and another containing in person voters. The parties in the data frame are then converted into integer representations. 



### Auxiliary Data

