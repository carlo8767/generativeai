import pandas as ps


if __name__ == '__main__':
  # pandas cook book https://pandas.pydata.org/docs/user_guide/cookbook.html#cookbook
  filename = "olympics_1896_2004.csv"
  print("Hello")
  # THERE ARE MULTIPLE COMMAND FOR PANDAS https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html # apt update; apt install git

  file = ps.read_csv(filename, skiprows=5)
  print(file.columns)
  print(file.Year.unique())


  """
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
  SELECT A SERIES I CAN ACCESS DIRECTLY WITH AN ATTRIBUTE
   print(file.columns) VISUALIZE ALL THE COLUMNS
  print(file.Year.unique()) # PRINT UNIQUE
  print(file.columns)
  for s in file.columns:
  print(file[s].unique())
  print(file.Year.value_counts(normalize=True)) # COUNT 
  oo.Medal.value_counts() # COUNT

  """

  # SEP separate the file for a specific char