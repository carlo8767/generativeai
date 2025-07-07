import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from IPython.core.display_functions import display

if __name__ == '__main__':

 file = pd.read_csv("penguins.csv")
 file.info()
 # Calculate the percentage of missing values for each feature
 nan_percentage = (file.isna().mean() * 100).sort_values(ascending=False)

 plt.figure(figsize=(10, 6))
 sns.barplot(x=nan_percentage.index, y=nan_percentage.values, palette="viridis")
 plt.title("Percentage of Missing Values by Feature in Penguins Dataset", fontsize=16)
 plt.ylabel("Percentage of Missing Values", fontsize=14)
 plt.xlabel("Features", fontsize=14)
 plt.xticks(rotation=45, ha="right", fontsize=12)
 plt.yticks(fontsize=12)
 plt.tight_layout()
 plt.show()