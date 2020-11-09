# 	SDC for Voting Survey

###### Edi Begovic (edbe)  ·  Gergo Koncz (geko)  ·  Høgni Jacobsen (hoja)



### Introduction

We use the sdcMicro web interface to analyse the relationships between the different variables to determine how much they influence each other. As we have no knowledge about the the full population, we cannot say anything about population frequency and therefore we'll be approaching the anonymization in a more conservative way. 



### Methodology

We start out by removing any direct identifiers; this just includes the names, which also carry no utility for the analysis. We assign all other 

##### Recoding

Apart from *DOB* (*date for birth*), all other key variables are categorical, but contain many different values and thus increases uniqueness. We therefore group them..

| Variable              | Grouping                                                     | k2-anonymity violation |
| :-------------------- | ------------------------------------------------------------ | ---------------------- |
| Original              | -                                                            | 199 · 100%             |
| DOB (*date of birth*) | Young (<31)<br />Getting there (31-45)<br />Middle (46-65)<br />Old (>65) | 183 · 92%              |
| Citizenship           | Danish<br />Other                                            | 183 · 92%              |

##### Suppression

After recoding, we let sdcMicro apply local suppression to achieve 2k-anonymity. We do not specify any importance vector, as very few suppressions are needed.

| Variable    | Number of supressed values | ∆%    |
| :---------- | -------------------------- | ----- |
| Age         | 21                         | 10.5% |
| Zip         | 4                          | 2%    |
| Citizenship | 1                          | 0.5%  |

##### 

##### Perturbation

Given the analytical purposes for the data, we determine that we don't need to preserve any relationships between the demographical variables. This has to be specified very clearly to the end-user of the data, as any other analysis based on the data would be incorrect. 



### Assessing Utility

To asses the utility of the modified data, we checked the 90% confidence intervals on the proportions of red/green votes for each categorical value. 



### Answering A-C

###### A)	

This question is answered in the same way for the original and anonymized data. As we do not anonymize the voting location nor the party that was voted for. We can therefore perform a Chi-squared test on votes for each party by location. 

The sample, "private_dataB.xlsx" or "", is read and separated into two data frames, one containing e-voters and another containing in person voters.

The votes for each party, Green and Red, are then summed for each voting location. A Chi-squared test is then performed on the summed values from the sample and the totals from the population, "public_data_resultsB.xlsx".

###### B)

This question is answered in the same way for the original and anonymized data. Using "private_dataB.xlsx" or "" we separate this into two data frames, one containing e-voters and another containing in person voters. The parties in the data frame are then converted into integer representations. 

A P-Value is then performed on these values.

###### C)

