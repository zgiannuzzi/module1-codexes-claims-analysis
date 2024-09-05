# HHA 507 Assignment 1 report. 

### The steps took in my analysis.
 - Loaded in Data from https://data.cms.gov/sites/default/files/2023-04/67157de9-d962-4af0-bf0e-3578b3afec58/inpatient.csv
 - Seperated data in 4 seperate data sets 
    - ICD diagnosis codes 8-10
    - ICD Procedure codes 5,7,10
    - CLM drug codes
    - HCPCS codes
 - Calculated frequency values
 - Hnadled any missing data/filled in empty data
 - Grabed the most used codes
 - Made a comparison of diabetes codes. 

### The purpose of each part of code.
The purpose includes just snippets of code but this was done on all the data that was pulled in.

Load in data 
``` python
   data = pd.read_csv('https://data.cms.gov/sites/default/files/2023-04/67157de9-d962-4af0-bf0e-3578b3afec58/inpatient.csv', sep='|')
```

Assigns icd_DGNS_code8 to column in data set.
``` python
    icd_DGNS_code8 = data['ICD_DGNS_CD8']
```

Gets the most used codes for ICD diagnoses codes and prints them out.
``` python
    icd_DGNS_frequency8 = icd_DGNS_code8.value_counts() and print("ICD Codes Frequency:\n", icd_DGNS_frequency8)
```    

Check for missing values in codex-related columns 
``` python
    missing_icd_DGNS_code8 = icd_DGNS_code8.isnull().sum()
    print(f"Missing ICD-8 Diagnosis Codes: {missing_icd_DGNS_code8}")
```

Handled missing data by filling with a placeholder
``` python
    data.fillna({'ICD_DGNS_CD8': 'Missing'},inplace=True)
```

Print the top 5 most common codes for each category
``` python
    print("Top 5 Most Common ICD-8 diagnosis Codes:\n", icd_DGNS_frequency8.head(5))
```

Analysis on data 
``` python
    diabetes_related = data[data['ICD_DGNS_CD10'].str.contains('E11', na=False)]
    common_drg_for_diabetes = diabetes_related['CLM_DRG_CD'].value_counts()
    print("Most Common DRG Codes for Patients with ICD Code E11 (Type 2 Diabetes):\n", common_drg_for_diabetes)
```

Key findings from your analysis, including any patterns or anomalies you discovered.

Any challenges you faced and how you overcame them
 - Understanding what each column in the dataset was. Found helpful website that broke down each column.
 - https://resdac.org/cms-data/files/ip-ffs/data-documentation
 - Got following message: data['ICD_DGNS_CD5'].fillna('MISSING', inplace=True)
<stdin>:1: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.
The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.
For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.
 - Changed lines to match recomended formating however not sure if correct when I would try and print I would still get none. 
``` python
    data.fillna({'ICD_DGNS_CD7': 'Missing'},inplace=True)
```
 

Reflect on the implications of your findings for healthcare providers and policy makers.
- Should be noted that this type of data manipultaion should be made sure that it is done corerectly and accurately
- Based on Comparison analysis diabetes is still up there as one of the most common ICD-10 codes























