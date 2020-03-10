
# my_lambdata/my_mod.py
import pandas
from pandas import to_datetime

def splitdate(df, column):
    """
    Pram df is a dataframe
    Pram column is a column header surrounded in quotes
    the columns should contain date values
    Function will split the date into multiple columns
    """
    df= df.copy()
    df[column] = to_datetime(df[column])
    df['month'] = df[column].dt.month
    df['day'] = df[column].dt.day
    df['year'] = df[column].dt.year

    return df
if __name__ == "__main__":
    df = pandas.DataFrame({"date": ["6/18/2018","10/5/2020"]})
    print("output", splitdate(df, "date"))


def temp_conv(degrees,metric=True):
    """
    Parm degrees is the temperature as integer or float
    Parm metric is the unit degrees is measured in
    Default metric is True, meaning Celcius 
    Metric = False, mean Fahrenheit 
    """
    d = degrees
    if metric == True:
        temp = (d * 9/5) + 32
        return temp
    else:
        temp = (d - 32) * 5/9
        return temp

if __name__ == "__main__":
    print("output", temp_conv(32,False))











#TEST
# def enlarge(n):
#     """
#     Parm n is a number
#     Function will enlarge the number
#     """
#     return n * 100


# # this code breaks our ability to import enlarge from other files
# # print("HELLO")
# # y = int(input("Please choose a number"))
# # print(y, enlarge(y))


# if __name__ == "__main__":
#     # only run this code IF this script is invoked from the command line
#     # not if it is imported from another
#     print("HELLO")
#     y = int(input("Please choose a number"))
#     print(y, enlarge(y))

