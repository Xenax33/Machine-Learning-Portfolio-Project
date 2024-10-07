import pandas as pd
bank_data = pd.read_csv('bank.csv')
bank_data.fillna('unknown', inplace=True)
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
categorical_cols = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'poutcome']
for col in categorical_cols:
    bank_data[col] = le.fit_transform(bank_data[col])


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
bank_data[['age', 'balance', 'day', 'duration', 'campaign', 'pdays', 'previous']] = scaler.fit_transform(bank_data[['age', 'balance', 'day', 'duration', 'campaign', 'pdays', 'previous']])
bank_data.to_csv('cleaned_bank_marketing.csv', index=False)