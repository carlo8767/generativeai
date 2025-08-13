
import pandas as ps

if __name__ == '__main__':
 ps.set_option("display.max_columns", None)  # show all columns
 ps.set_option("display.width", None)

 file = ps.read_csv("olympics_1896_2004.csv", skiprows=5)
 # file = file.set_index("Athlete Name")
 file = file.set_index("Athlete Name")  # AND I ABLE TO SORT THE ELEMENT
 print(file.index)
 print(file.loc["LEWIS, Carl", ["Year", "Event", "Medal" == "Gold"]])

 """
 {1} Index allow me  to pick a specific event 
  file = ps.read_csv("olympics_1896_2004.csv", skiprows=5, header=None)
  print(file.sample(5))
  print(file.sample(5))
  # SET THE INDEX
  file = file.set_index("Athlete Name") # AND I ABLE TO SORT THE ELEMENT
  print(file.index)
   print(file.iloc[0, 5]) # VISUALIZE THE COLUMN AND AVOID TO WRITE THE COLUMNS
    no = file["Athlete Name"].str.contains("LEWIS, Carl", na=False) # Series
  #  SPECIFY SPECIFY THE LOCATION
  print(file.loc["LEWIS, Carl", ["Year", "Event", "Medal"] ])
  print(file.loc["LEWIS, Carl", :]) # SHORT CUT
   

  

 
 
 
 
 
 """