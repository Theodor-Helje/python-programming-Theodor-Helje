import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import data_utils

#1
student_mat = pd.read_csv("Data\student-mat-missing-data.csv")
print(f"1b: head:\n{student_mat.head()}\n")
print(f"1b: info:\n{student_mat.info()}\n")
print(f"1b: describe:\n{student_mat.describe()}\n")
print(f"1b: value_counts:\n{student_mat.value_counts()}\n")
print(f"1b: columns:\n{student_mat.columns}\n")

data_utils.plot_missing_df_values(student_mat)

print(f"1e: rows where freetime is NaN:\n{student_mat[student_mat['freetime'].isna()]}\n")
print(f"1f: rows where freetime or age is NaN:\n{student_mat[
    student_mat['freetime'].isna() | student_mat['age'].isna()]}\n")
print(f"1g: proportion of rows with several NaN values:\n{
    len(student_mat[student_mat.isna().sum(axis=1) > 1]) / len(student_mat)}\n")

#2
student_clean = student_mat[student_mat.isna().sum(axis=1) < 2]
print(f"2a: rows with several NaN values dropped:\n{student_mat}\n")
data_utils.plot_missing_df_values(student_clean)

sns.countplot(data=student_clean, x='age', palette='pastel')
plt.title("2b: Age distribution")
plt.show()

print(f"2c: Check which columns can determine age:\n{student_clean.columns}\n")

print(f"2d: Check which unique values are in 'higher'\n{student_clean['higher'].unique()}\n")

fig, axes = plt.subplots(1, 3, figsize=(10,3))
sns.countplot(data=student_clean, x='age', palette='pastel', hue='age', ax=axes[0])
axes[0].set_title("Total age distribution")

sns.countplot(x=student_clean.loc[
    student_clean['higher'] == "yes", 'age'], palette='pastel', ax=axes[1])
axes[1].set_title("Distribution when higher")

sns.countplot(x=student_clean.loc[
    student_clean['higher'] == "no", 'age'], palette='pastel', ax=axes[2])
axes[2].set_title("Distribution when not higher")

plt.show()

student_clean['alcohol'] = student_clean['Dalc'] + student_clean['Walc']
print(f"2f: add 'alcohol' column:\n{student_clean['alcohol']}\n")
sns.barplot(data=student_clean, x='age', y='alcohol', palette='pastel')
plt.title("2g: Alcohol consumption vs age")
plt.show()

median_drinking_age = student_clean.loc[student_clean['age'].isin([16, 17, 18]), 'age'].median()
student_clean['age'] = student_clean.apply(
    lambda row: row['age'] if not pd.isna(row["age"]) 
        else 15 if row["alcohol"] < 4 
        else median_drinking_age, 
    axis=1
    )
print(f"2h: number of NaN values after filling in age values:\n{student_clean.isna().sum()}\n")
#data_utils.plot_missing_df_values(student_clean)

sns.barplot(data=student_clean, x='age', y='freetime',hue='freetime', palette='pastel')
plt.show()