import pandas as ps


if __name__ == '__main__':
  # pandas cook book https://pandas.pydata.org/docs/user_guide/cookbook.html#cookbook
  filename = "olympics_1896_2004.csv"
  print("Hello")
  # THERE ARE MULTIPLE COMMAND FOR PANDAS https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html # apt update; apt install git

  new_colum = ['Year', 'City', 'Sports', 'Discipline', 'Athletes Names', 'NOC', 'Gender',
               'Event', 'Event Gender', 'Medal', 'Position']
  file = ps.read_csv(filename, skiprows=5, names=new_colum, header=0)
  print(file)




  """
  {1}
   ps.set_option("display.max_columns", None)  # show all columns
   ps.set_option("display.width", None)
  OTHER USEFUL METHOD
  file.sample() random 3 row
  print(file.sample(5)) # RANDOMLY SHOW ROW
  print(file.head(3)) # SHOW HEAD
  print(file.tail) # SHOW FROM THE BUTTON
  file.info() SEE INFORMATION OF  THE DATA TYPE
  print(file.describe()) # STATISTICAL VALUE
   ps.get_option # SET UP VISUALIZATION ROW NUMBER OF COLUMSN
  """

  """
  {2}
  SELECT A SERIES I CAN ACCESS DIRECTLY WITH AN ATTRIBUTE
   print(file.columns) VISUALIZE ALL THE COLUMNS
  print(file.Year.unique()) # PRINT UNIQUE
  print(file.columns)
  for s in file.columns:
  print(file[s].unique())
  print(file.Year.value_counts(normalize=True)) # COUNT 
  oo.Medal.value_counts() # COUNT
  """

  """
   {2}
   RENAME A SERIES
   mapper = {"Athlete Name": "Athlete_Name" }
   file = file.rename(columns=mapper) # YOU CAN COMBINING AS WELL, AND YOU CAN SPECIFY DIRECTY THE DICTIONARY IN COLUMNS
   file.info()
   file.columns = columns
   YOU CAN RENAME THE COLUMS DIRECTLY IN THE READ CSV
    new_colum = ['Year', 'City', 'Sports', 'Discipline', 'Athletes Names', 'NOC', 'Gender',
               'Event', 'Event Gender', 'Medal', 'Position']
  file = ps.read_csv(filename, skiprows=5, names=new_colum, header=0)

  
  
  """

  # SEP separate the file for a specific char