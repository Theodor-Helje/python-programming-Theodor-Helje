import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def plot_missing_df_values(df):
    """plot and show the number of null values in the columns in a df"""
    df = df.loc[:, df.isna().any()].isna().sum().reset_index()
    df.columns = ['Column', 'Missing values']
    sns.barplot(data=df, x='Column', y='Missing values', palette='pastel')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.title("Null values:")
    plt.show()