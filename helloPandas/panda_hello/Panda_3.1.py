import pandas as pd
import pandas as ps



if __name__ == '__main__':
 ps.set_option("display.max_columns", None)  # show all columns
 ps.set_option("display.width", None)


 dtype_mapper = {"Year": "int64",
                 "City": "string",
                 "Sport": "string",
                 "Discipline": "string",
                 "Athlete Name": "string",
                 "NOC": "string",
                 "Gender": "category",
                 "Event": "string",
                 "Event_gender": "category",
                 "Medal": "category"}
 file = ps.read_csv("olympics_1896_2004.csv", skiprows=5, dtype=dtype_mapper)
 print(file.dtypes)

 """
 print(file.dtypes) 
 file.Medal = file.Medal.astype("category") ASSIGN CATEGORY
 # ORDER THE CATEGORY IS NICE BUT IS VERIF FRAGILE 
  file.Medal = file.Medal.astype("category")
 print(file.dtypes)
 medal_order = {"Bronze", "Silver", "Gold"}
 pd.Categorical(file.Medal, categories=medal_order, ordered=True)
 file = file.sort_values(by=["Year", "Event", "Medal"], ascending = [True, True, True]).head(7)
 # BEFORE IT WAS NOT POSSIBLE BECAUSE THE MEDAL WAS A STRING
 print(file.sample(5))
  file.Medal = file.Medal.astype("category")
 medal_order = {"Bronze", "Silver", "Gold"}
 file.Medal = pd.Categorical(file.Medal, categories=medal_order, ordered=True)
 file.sort_values(by=["Medal", "Event", "Year"], ascending = [False, True, True])
 print(file)
 {2} MEMORY REDUCTION  WITH CATEGORY
 print(file.Medal.memory_usage)
 file.Medal = file.Medal.astype("category")
 print(file.Medal.memory_usage)
 {3} IMPROVE DATA ANALYSIS  
 dtype_mapper = {"Year": "int64",
                 "City": "string",
                 "Sport": "string",
                 "Discipline": "string",
                 "Athlete Name": "string",
                 "NOC": "string",
                 "Gender": "category",
                 "Event": "string",
                 "Event_gender": "category",
                 "Medal": "category"} 
 file = ps.read_csv("olympics_1896_2004.csv", skiprows=5, dtype=dtype_mapper)
 print(file.dtypes) # HOWEVER THIS CAN BE VERY FRAGILE AND YOU WILL SEE THAT GENDER IST STILL OBJECT DATA TYPE
 
 
 
 """



# ANALYSE GOAL
"""
5 - number - summary **
- Minimum
- Maximum
- Lower and Upper
quantile
- Median

- ** Mean & Standard
Deviation **

- ** Investigate
Outliers **

- ** Plots **
- Violin - Plot
- Box - plot
- Histogram
- Bar
charts
- Pie
charts
- ** Correlation
Matrix **
"""

if __name__ == '__main__':
  pass