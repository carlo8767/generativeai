import pandas as ps



if  __name__ == "__main__":

    oo = ps.read_csv('world_cup/world_cup.csv')
    # THIS IS A MULTIDIMENSIONAL ARRAY
    # INSERTION SORT
    ns = oo.TopScorrer.unique()
    index = 1
    dictionary_score = dict()
    concat = ""
    sum_gol = ""
    # CLEAN DATA
    for n in range(0, len(ns)):
        extract = ns[n]
        parts = extract.split("-")
        name = parts[0].strip()
        number = int(parts[1].strip())
        dictionary_score[name] = int(number)
    dictionary_score = sorted(dictionary_score.items(), key = lambda items: items [1])
    for k,v in dictionary_score:
        print(f'The best scores in FOOTBALL WORLD CUP  {k} total gol {v}')




