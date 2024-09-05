import pandas as pd

# Step 1: Load the Data
# Replace 'your_file_path.csv' with the actual file path or URL of the dataset
# Use a delimiter argument if the data is separated by a character other than a comma (e.g., | or ;)
# For us we need to use | as the delimiter
data = pd.read_csv('https://data.cms.gov/sites/default/files/2023-04/67157de9-d962-4af0-bf0e-3578b3afec58/inpatient.csv', sep='|')

# Display the first few rows of the dataset to understand its structure
print(data.head())
# print(data['ICD_DGNS_CD7'])
# Step 2: Explore the Dataset
# Identify the columns related to medical codexes (e.g., ICD codes, DRG codes)
# Assuming 'ICD_CODE', 'DRG_CODE', and 'HCPCS_CODE' are the columns containing codex data

#ICD_DGNS codes 

icd_DGNS_code8 = data['ICD_DGNS_CD8']
icd_DGNS_code9 = data['ICD_DGNS_CD9']
icd_DGNS_code10 = data['ICD_DGNS_CD10']

#ICD_prcdr_codes
icd_prcdr_code5 = data['ICD_PRCDR_CD5']
icd_prcdr_code7 = data['ICD_PRCDR_CD7']
icd_prcdr_code10 = data['ICD_PRCDR_CD10']

#CLM_DRG_CD
clm_drg_code = data['CLM_DRG_CD']
#hcpcs_code
hcpcs_codes = data['HCPCS_CD']

# Step 3: Analyze the Frequency of Each Unique Value
# Calculate the frequency of unique values in each codex column

# Frequency count for ICD codes
icd_DGNS_frequency8 = icd_DGNS_code8.value_counts()
print("ICD Codes Frequency:\n", icd_DGNS_frequency8)

icd_DGNS_frequency9 = icd_DGNS_code9.value_counts()
print("ICD Codes Frequency:\n", icd_DGNS_frequency9)

icd_DGNS_frequency10 = icd_DGNS_code10.value_counts()
print("ICD Codes Frequency:\n", icd_DGNS_frequency10)

# Frequency count for ICD_PRCDR codes
icd_prcdr_frequency5 = icd_prcdr_code5.value_counts()
print("ICD Codes Frequency:\n", icd_prcdr_frequency5)

icd_prcdr_frequency7 = icd_prcdr_code7.value_counts()
print("ICD Codes Frequency:\n", icd_prcdr_frequency7)

icd_prcdr_frequency10 = icd_prcdr_code10.value_counts()
print("ICD Codes Frequency:\n", icd_prcdr_frequency10)

# Frequency count for DRG codes
drg_frequency = clm_drg_code.value_counts()
print("DRG Codes Frequency:\n", drg_frequency)

# Frequency count for HCPCS codes
hcpcs_frequency = hcpcs_codes.value_counts()
print("HCPCS Codes Frequency:\n", hcpcs_frequency)

# Step 4: Handle Missing Data (if any)
# Check for missing values in codex-related columns
#ICD_DGNS codes
missing_icd_DGNS_code8 = icd_DGNS_code8.isnull().sum()
missing_icd_DGNS_code9 = icd_DGNS_code9.isnull().sum()
missing_icd_DGNS_code10 = icd_DGNS_code10.isnull().sum()

#ICD_prcdr codes
missing_icd_prcdr_code5 = icd_prcdr_code5.isnull().sum()
missing_icd_prcdr_code7 = icd_prcdr_code7.isnull().sum()
missing_icd_prcdr_code10 = icd_prcdr_code10.isnull().sum()

#Drug_code
missing_drg = clm_drg_code.isnull().sum()

#hcpcs_code
missing_hcpcs = hcpcs_codes.isnull().sum()

print(f"Missing ICD-8 Diagnosis Codes: {missing_icd_DGNS_code8}")
print(f"Missing ICD-9 Diagnosis Codes: {missing_icd_DGNS_code9}")
print(f"Missing ICD-10 Diagnosis Codes: {missing_icd_DGNS_code10}")
print(f"Missing ICD-5 procedure Codes: {missing_icd_prcdr_code5}")
print(f"Missing ICD-7 procedure Codes: {missing_icd_prcdr_code7}")
print(f"Missing ICD-10 procedure Codes: {missing_icd_prcdr_code10}")
print(f"Missing CLM DRUG Codes: {missing_drg}")
print(f"Missing HCPCS Codes: {missing_hcpcs}")

# Example of handling missing data by filling with a placeholder
#data['ICD_DGNS_CD8'].fillna('MISSING', inplace=True)
# Not sure if this is the fix but it doesnt give error. DOnt think this working. Pandas website doesnt give enough info for quick fix.
data.fillna({'ICD_DGNS_CD8': 'Missing'},inplace=True)
data.fillna({'ICD_DGNS_CD9': 'Missing'},inplace=True)
data.fillna({'ICD_DGNS_CD10': 'Missing'},inplace=True)
data.fillna({'ICD_PRCDR_CD5': 'Missing'},inplace=True)
data.fillna({'ICD_PRCDR_CD7': 'Missing'},inplace=True)
data.fillna({'ICD_PRCDR_CD10': 'Missing'},inplace=True)
data.fillna({'CLM_DRG_CD': 'Missing'},inplace=True)
data.fillna({'HCPCS_CD': 'Missing'},inplace=True)


# Step 5: Summary of Findings
# Provide a summary of the most common codes
# Here we'll just print the top 5 most common codes for each category
print("Top 5 Most Common ICD-8 diagnosis Codes:\n", icd_DGNS_frequency8.head(5))
print("Top 5 Most Common ICD-9 diagnosis Codes:\n", icd_DGNS_frequency9.head(5))
print("Top 5 Most Common ICD-10 diagnosis Codes:\n", icd_DGNS_frequency10.head(5))
print("Top 5 Most Common ICD-5 procedure Codes:\n", icd_prcdr_frequency5.head(5))
print("Top 5 Most Common ICD-7 procedure Codes:\n", icd_prcdr_frequency7.head(5))
print("Top 5 Most Common ICD-10 procedure Codes:\n", icd_prcdr_frequency10.head(5))
print("Top 5 Most Common CLM DRG Codes:\n", drg_frequency.head(5))
print("Top 5 Most Common HCPCS Codes:\n", hcpcs_frequency.head(5))

# Additional Analysis Example
# Are there any patterns? For instance, let's see if certain DRG codes are more common
# when ICD codes are specific values (e.g., 'E11' for Type 2 Diabetes)
diabetes_related = data[data['ICD_DGNS_CD10'].str.contains('E11', na=False)]
common_drg_for_diabetes = diabetes_related['CLM_DRG_CD'].value_counts()
print("Most Common DRG Codes for Patients with ICD Code E11 (Type 2 Diabetes):\n", common_drg_for_diabetes)

