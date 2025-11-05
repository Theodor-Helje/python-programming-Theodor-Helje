import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import data_utils

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