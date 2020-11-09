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



###### B)



###### C)

