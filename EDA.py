import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# -----------------------------
# 1. Load Dataset
# -----------------------------
df = pd.read_csv('Banking.csv')
print("\n📊 First 5 Rows of the Dataset:\n", df.head(5))

# -----------------------------
# 2. Income Band Creation
# -----------------------------
bins = [0, 100000, 300000, float('inf')]
labels = ["low", "medium", "high"]
df['Income Band'] = pd.cut(df['Estimated Income'], bins=bins, labels=labels, right=False)

df['Income Band'].value_counts().plot(kind='bar')
plt.title("Income Band Distribution")
plt.xlabel("Income Band")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# -----------------------------
# 3. Value Counts for Categorical Columns
# -----------------------------
categorical_cols = df[[
    "BRId", "GenderId", "IAId", "Amount of Credit Cards", "Nationality",
    "Occupation", "Fee Structure", "Loyalty Classification",
    "Properties Owned", "Risk Weighting", "Income Band"
]].columns

for col in categorical_cols:
    print(f"\n📌 Value Counts for '{col}':")
    print(df[col].value_counts())

# -----------------------------
# 4. Count Plots for Categorical Columns
# -----------------------------
for i, predictor in enumerate(categorical_cols):
    plt.figure(i)
    sns.countplot(data=df, x=predictor, palette='pastel')
    plt.title(f'Count of {predictor}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# -----------------------------
# 5. Count Plots with Nationality Hue
# -----------------------------
for i, predictor in enumerate(categorical_cols):
    plt.figure(i)
    sns.countplot(data=df, x=predictor, hue='Nationality', palette='Set2')
    plt.title(f'{predictor} vs Nationality')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# -----------------------------
# 6. Histogram for Categorical Columns (Excluding Occupation)
# -----------------------------
for col in categorical_cols:
    if col == "Occupation":
        continue
    plt.figure(figsize=(8, 4))
    sns.histplot(df[col])
    plt.title(f'Histogram of {col}')
    plt.xlabel(col)
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

# -----------------------------
# 7. Univariate Analysis of Numerical Columns
# -----------------------------
numerical_cols = [
    'Estimated Income', 'Superannuation Savings', 'Credit Card Balance',
    'Bank Loans', 'Bank Deposits', 'Checking Accounts', 'Saving Accounts',
    'Foreign Currency Account', 'Business Lending'
]

plt.figure(figsize=(15, 10))
for i, col in enumerate(numerical_cols):
    plt.subplot(4, 3, i + 1)
    sns.histplot(df[col], kde=True)
    plt.title(col)
plt.tight_layout()
plt.show()

# -----------------------------
# 8. Correlation Matrix of Numerical Columns
# -----------------------------
correlation_matrix = df[numerical_cols].corr()
plt.figure(figsize=(12, 12))
sns.heatmap(correlation_matrix, annot=True, cmap='crest', fmt=".2f")
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()

# -----------------------------
# 9. DataFrame Shape
# -----------------------------
print("\n📐 Shape of the DataFrame:", df.shape)

# -----------------------------
# 10. DataFrame Info
# -----------------------------
print("\n📋 DataFrame Info:")
df.info()

# -----------------------------
# 11. Estimated Income Column
# -----------------------------
print("\n💰 Estimated Income Column:\n", df["Estimated Income"])

# -----------------------------
# 12. Value Counts for Selected Categorical Columns
# -----------------------------
categorical_cols = df[[
    "Risk Weighting", "Nationality", "Occupation", "Fee Structure",
    "Loyalty Classification", "Properties Owned", "Risk Weighting",
    "Occupation", "Income Band"
]].columns

for col in categorical_cols:
    print(f"\n📌 Value Counts for '{col}':")
    print(df[col].value_counts())

# -----------------------------
# 13. Descriptive Statistics
# -----------------------------
print("\n📊 Descriptive Statistics for Numerical Columns:")
print(df.describe())

# -----------------------------
# 14. Missing Values
# -----------------------------
missing_values = df.isnull().sum()
print("\n❗ Missing Values per Column:\n", missing_values)

# -----------------------------
# 15. Convert 'Joined Bank' to Datetime
# -----------------------------
df['Joined Bank'] = pd.to_datetime(df['Joined Bank'], format='%d-%m-%Y')
print("\n📅 Data Type of 'Joined Bank':", df['Joined Bank'].dtype)

# -----------------------------
# 16. Correlation Matrix of Extended Numerical Features
# -----------------------------
numerical_cols = [
    'Age', 'Estimated Income', 'Superannuation Savings', 'Credit Card Balance',
    'Bank Loans', 'Bank Deposits', 'Checking Accounts', 'Saving Accounts',
    'Foreign Currency Account', 'Business Lending', 'Properties Owned'
]

correlation_matrix = df[numerical_cols].corr()
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Numerical Features')
plt.tight_layout()
plt.show()

# -----------------------------
# 17. Univariate Analysis of Extended Numerical Columns
# -----------------------------
numerical_cols = [
    'Fee Structure', 'Age', 'Estimated Income', 'Superannuation Savings',
    'Credit Card Balance', 'Bank Loans', 'Bank Deposits', 'Checking Accounts',
    'Saving Accounts', 'Foreign Currency Account', 'Business Lending'
]

plt.figure(figsize=(15, 10))
for i, col in enumerate(numerical_cols):
    plt.subplot(4, 3, i + 1)
    sns.histplot(df[col], kde=True)
    plt.title(col)
plt.tight_layout()
plt.show()