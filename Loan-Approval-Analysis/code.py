# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank = pd.DataFrame(pd.read_csv(path))
categorical_var = bank.select_dtypes(include='object')
print(categorical_var)
numerical_var = bank.select_dtypes(include='number')
print(numerical_var)

# code ends here


# --------------
# code starts here
banks = bank.drop('Loan_ID',axis=1)
null_values=banks.isnull().sum()
print(null_values)
bank_mode = banks.mode
banks = banks.fillna(bank_mode)
print(banks)
#code ends here


# --------------
# Code starts here
avg_loan_amount = pd.pivot_table(banks,index=['Gender', 'Married', 'Self_Employed'],values='LoanAmount')
print(avg_loan_amount)
# code ends here



# --------------
# code starts here
se = banks['Self_Employed']=='Yes'
nse = banks['Self_Employed']=='No'
l = banks['Loan_Status']=='Y'
tc = banks[l]['Loan_Status'].value_counts()
loan_approved_se = banks[se & l]['Self_Employed'].value_counts()['Yes']
loan_approved_nse = banks[nse & l]['Self_Employed'].value_counts()['No']
print(loan_approved_nse, loan_approved_se)
percentage_se = (loan_approved_se*100/614)
percentage_nse = (loan_approved_nse*100/614)
print(percentage_nse, percentage_se)
# code ends here


# --------------
# code starts here
def lat(months):
    return months/12
loan_term = banks['Loan_Amount_Term'].apply(lambda x:lat(x))
print(loan_term)
big_loan_term = len(loan_term[loan_term>=25.0].values)
print(big_loan_term)

# code ends here


# --------------
# code starts here
loan_groupby = banks.groupby('Loan_Status')
loan_groupby = loan_groupby['ApplicantIncome','Credit_History']
mean_values = loan_groupby.mean()


# code ends here


