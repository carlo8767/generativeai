import pandas as ps




if __name__ == '__main__':
    filename = "panda_hello/olympics_1896_2004.csv"
    oo = ps.read_csv(filename, skiprows=5)

    # WHAT IS THE TIME RANGE COVERED IN THIS DATA SET?
    range_year = oo.Year.cummax().unique()
    size_year = range_year[len(range_year)-1]-range_year[0]
    print(f'The range is between {range_year[0]} and {range_year[len(range_year)-1]}')
    # WHAT ARE THE MISSING OLYMPICS YEAR?
    begin_year = range_year[0]
    for i, v in enumerate(range_year):

        if i == 0:
            continue
        else:
          begin_year += 4
          if begin_year == v:
                continue
          else:

              while True:
                  if begin_year == v:
                      begin_year = v
                      break
                  print(f'The missing year are {begin_year}')
                  begin_year += 4

    # WHAT ARE THE TYPE OF MEDAL AWARDED?
    for v in oo.Medal.unique():
        print(f'The medal awarded are {v}')
    # ACROSS ALL THE OLYMPIC GAMES HOW MANY GOLD SILVER, AND BRONZE MODEL HAVE THERE BEEN?
    print(f'These are the number of medal {oo.Medal.value_counts()}')
    # WHAT ARE THE VARIOUS NATIONAL OLIMPIC COMMIT?
    print(oo.NOC.unique())
    # WHAT DOES THE NOC "ZZX" represent?
    print(oo.columns)

