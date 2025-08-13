import pandas as pd


if __name__ == '__main__':
  pd.set_option("display.max_columns", None)  # show all columns
  pd.set_option("display.width", None)
  model = pd.read_csv("second_olymipic.csv")
  ns = model.City.isna().sum()
  model = model.City.fillna(value = "Beijing" )
  model = [model.City.isna()]
  print(model)



  """
    1. COMBINTATION
         pd.set_option("display.max_columns", None)  # show all columns
         pd.set_option("display.width", None)
         start = pd.DataFrame({"city": ["London", "Rio", "Tokyo"],
                          "start_date": ["27th Jul, 2012", "5th Aug, 2016", "23rd July, 2021"]})
         end = pd.DataFrame({"city": ["London", "Tokyo", "Paris"],
                    "end_date": ["12th Aug, 2012", "8th Aug, 2021", "11th Aug, 2024"]})

    
        # combination = pd.concat([start, end], axis=1)
        # WE HAVE THE COLUMNS CITY TOGHETHER
        # print(combination)
    
    2. LEFT JOIN
          left_join_combination = pd.merge(left=start, right = end, on = "city", how= "inner")
          print(left_join_combination)
    3. OUTER JOIN
     right_join_combination = pd.merge(left=start, right=end, on="city", how="outer")
    print(right_join_combination)
    4. COMBINING DATASET
      capitalize the columns 
    5.WORKING WITH MISSING VALUES 
     ns = model.City.isna().sum()
     # FILL THE VALUE WITH NULL VALUE 
     model = model.City.fillna(value = "Beijing" ) 
    
    
    
    
    """