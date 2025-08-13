import pandas as pd



if __name__ == '__main__':

    file = pd.read_csv("olympics_1896_2004.csv", skiprows=5)
    print(file.sample(5))
    city = ["London", "Rio", "Tokila"]
    nation = ["England", "Brasil", "Japan"]
    ns = pd.DataFrame({"City": pd.Series(city)})
    combination = zip(city, nation)
    print(pd.DataFrame(combination, columns= ["City", "Nation"]))
    city = ["London", "Rio", "Tokyo"]
    start_date = ["07-27-2012", "5th Aug, 2016", "23rd Jul, 2021"]
    end_date = ["12th Aug, 2012", "21-08-2016", "8th Aug, 2021"]
    pd.to_datetime()
    """
    {1} MANIPULATE THE LIST OF THE AVAILABLE COMMAND
    print(dir(file))  # all method available in python YO
    {2} CREATING A SERIES AND DATA FRAME
    city = ["London", "Rio", "Tokila"]
    nation = ["England", "Brasil", "Japan"]
    ns = pd.DataFrame({"City": pd.Series(city)})
    print(ns["City"])
    {3} COMBINATION STRUCTURE
     combination = zip(city, nation)
    print(pd.DataFrame(combination, columns= ["City", "Nation"]))
    {4} WORKING WITH DATA
    city = ["London", "Rio", "Tokyo"]
    start_date = ["07-27-2012", "5th Aug, 2016", "23rd Jul, 2021"]
    end_date = ["12th Aug, 2012", "21-08-2016", "8th Aug, 2021"]
    games["Start Date"] = pd.to_datetime(games["Start Date"], format='mixed')
    games["End Date"] = pd.to_datetime(games["End Date"], format='mixed')
    {4} COMBINIG DATA FRAME
    pd.concat?
    

    """


