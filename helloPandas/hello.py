import pandas as ps


if __name__ == '__main__':
  # pandas cook book https://pandas.pydata.org/docs/user_guide/cookbook.html#cookbook
  filename = "olympics_1896_2004.csv"
  print("Hello")
  # THERE ARE MULTIPLE COMMAND FOR PANDAS https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
  file = ps.read_csv(filename, skiprows=5)
  print(file)