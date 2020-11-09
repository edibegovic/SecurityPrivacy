# 	SDC for Voting Survey

###### Edi Begovic (edbe)  ·  Gergo Koncz (geko)  ·  Høgni Jacobsen (hoja)



### Introduction

We use the sdcMicro web interface to analyse the relationships between the different variables to determine how much they influence each other. As we have no knowledge about the the full population, we cannot say anything about population frequency and therefore we'll be approaching the anonymization in a more conservative way.

We register all variables availeble in the public register as quasi-identifiers, such that *party* (voted for) is considered the only sensible variable. 



### Methodology

'We start out by removing any direct identifiers; this just includes the names, which also carry no utility for the analysis.

##### Recoding

Apart from *DOB* (*date for birth*), all other key variables are categorical, but contain many different values and thus increases uniqueness. We therefore split them into more corse groups, where we don't deem a high reduction in utility. Likewise, age is grouped into four ranges. 

| Variable              | Grouping                                                     | k2-anonymity violation |
| :-------------------- | ------------------------------------------------------------ | ---------------------- |
| Original              | -                                                            | 199 · 100%             |
| DOB (*date of birth*) | Young (<31)<br />Getting there (31-45)<br />Middle (46-65)<br />Old (>65) | 183 · 92%              |
| Citizenship           | Danish<br />Other                                            | 183 · 92%              |

As *educational background* is not considered publicly avalible, we decided to include it without any modification. This information is however - as with everything else - still susceptible for recognition by the end user. 

##### Suppression

After recoding, we let sdcMicro apply local suppression to achieve 2k-anonymity. We do not specify any importance vector, as very few suppressions are needed.

| Variable    | Number of supressed values | ∆%    |
| :---------- | -------------------------- | ----- |
| Age         | 21                         | 10.5% |
| Zip         | 4                          | 2%    |
| Citizenship | 1                          | 0.5%  |

After supression we achive 2k-annonymity as well as only having 4% of individuals violate k3-annonymity.

##### Perturbation

After suppression we have a very low percentage of voters violating 3k-anonymity and none violating 2k-anonimity, therefore we decided not to apply any perturbation to the data to keep more utility. We believe that This has to be specified very clearly to the end-user of the data, as any other analysis based on the data would be incorrect. 

### Auxiliary Data



### Assessing Utility

To asses the utility of the modified data, we checked the 95% confidence intervals on the proportions of red/green votes for each categorical value. 



### Uses for Analysis

###### A)	

This question is answered in the same way for the original and anonymized data. As we have not used any perturbative anonymization methods and neither voting locations nor any the party variable was suppressed, we can therefore perform a Chi-squared test on votes for each party by voting type. 

The data frame, "" or "", is separated into two data frames, one containing e-voters and another containing in person voters.

The votes for each party, Green and Red, are then summed for each voting location. A Chi-squared test is then performed on the summed values from the sample and the totals from the population, "public_data_resultsB.xlsx".

###### B)

This question is answered in the same way for the original and anonymized data. Using "private_dataB.xlsx" or "" we separate this into two data frames, one containing e-voters and another containing in person voters. The sum of votes for the Red and the Green party in each data frame are calculated. We now have the ration of Red and Green party votes for each voting method. The rations of in person and e-votes are then compared.



###### C)

The demographic factors used are "sex","age","zip","citizenship","marital_status" and "party".  The demographic factors are stored as tuples a long with the frequency of that tuple in the data frame. This question is answered in the same way for the original and anonymized data. Using "private_dataB.xlsx" or "" we separate this into two data frames, one containing e-voters and another containing in person voters. The parties in the data frame are then converted into integer representations. 

A P-Value is then performed on these values.

