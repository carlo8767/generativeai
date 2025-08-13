import pandas as ps

if __name__ == '__main__':
   ps.set_option("display.max_columns", None)  # show all columns
   ps.set_option("display.width", None)
   oo = ps.read_csv("olympics_1896_2004.csv", skiprows=5)
   print(oo[(oo.NOC == "CHN")  & (oo.Medal == "Gold")])

   oo = oo.sort_values(by= ['Year', 'NOC'] , ascending = [False, True] )
   print(oo)
   """
   {1}
   print(df.shape)    SHAPE ATTRIBUTE
   IN PANDAS WE REFERS WITH AXIS 0 THE ROW WHILE THE COLUMN HAVE AXIS 1 
   oo.drop("Position", axis = 1) THIS IS NOT SUFFICIENT TO UPDATE THE DATA
   ps.read_csv("olympics_1896_2004.csv", skiprows=5, implace = True).oo.drop("Position", axis = 1) 
   Together and also without assign the variable. However, 
   if you use implace you cannot manipulate the data another time
   Get rid of raw 2 oo = oo.drop(2, axis = 0)
   oo = oo.drop([0,,1,2], axis = 0) BETTER USE A CHAIN APPROACH 
   {2}  
   # THIS CREATE A FILTER BOOLEAN SPECIFY THE CONDITION AND IT WILL RETURN AN ARRAY
   first_olympic = (oo.Year== 1896)
   print(oo[first_olympic]) reassign the array it will display only the olympic with 1896
   # MULTIPLE CONDITION FILTER
   first_olympic = (oo.Year == 1896) | (oo.Year == 1900) # I NEED TO SPECIFY THE CONDITION ENCLOSED TO THE BRACKET
   print(oo[(oo.City == "Athens") & ~ (oo.Year == 1900) ]) NOT COMMAND
   {3}
   # STRING METHOD
   oo.Event.str.capitalize().unique() # CAPITALIZE EVENT
   print(dir(oo.Event.str))  # VERIFY ALL THE STRING EVENT
   ps.set_option("display.max_columns", None)  # show all columns
   ps.set_option("display.width", None)
   oo = ps.read_csv("olympics_1896_2004.csv", skiprows=5)
   no = oo["Athlete Name"].str.contains("LATYNINA", na=False)
   print(oo[no])
   {4} SORT
   oo = oo.sort_values("Athlete Name") Always return a frame True or False
   oo = oo.sort_values(by= ['Year', 'NOC'])
   oo = oo.sort_values(by= ['Year', 'NOC'] , ascending = [False, True] ) ascending and descending order
   """
