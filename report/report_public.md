# 	Title




### Anonymized Data attributes

| name       | sex  | evote | dob        | zip        | education | citizenship | marital_status | party |
| ---------- | ---- | ----- | ---------- | ---------- | --------- | ----------- | -------------- | ----- |
| Anonymized | -    | -     | Anonymized | Anonymized | -         | Anonymized  | Anonymized     | -     |



### Methods used for anonymization

| name        | sex  | evote | dob/ age                                              | zip                                | education | citizenship                                           | marital_status | party |
| ----------- | ---- | ----- | ----------------------------------------------------- | ---------------------------------- | --------- | ----------------------------------------------------- | -------------- | ----- |
| Suppression | -    | -     | Generalization and local suppression for k-anonymity. | Local suppression for k-anonymity. | -         | Generalization and local suppression for k-anonymity. | Suppression    | -     |



### More Detail

| name    | sex  | evote                                                        | dob/ age | zip                | education | citizenship                        | marital_status | party |
| ------- | ---- | ------------------------------------------------------------ | -------- | ------------------ | --------- | ---------------------------------- | -------------- | ----- |
| Removed | -    | 1 (<31)<br />2 (31-45)<br />3(46-65)<br />4(>65) <br />, 21 values supressed |          | 4 values supressed | -         | Danish or Other, 1 value supressed | Removed        | -     |

Age was calculated by taking the birth year minus 2020.