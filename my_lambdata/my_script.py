
# my_lambdata/my_script.py

import pandas

from my_lambdata.my_mod import splitdate
from my_lambdata.my_mod import temp_conv

df = pandas.DataFrame({"date": ["6/18/2018","10/5/2020"]})
print("output", splitdate(df, "date"))

print("output", temp_conv(32,False))


#python -m my_lambdata.my_script
#TEST
# print("HELLO WORLD")
# df = pandas.DataFrame({"state": ["CT","CO","CA","TX"]})
# print(df.head())
# print("--------------")
# n = 5
# print("NUMBER",n)
# print("ENLARGED NUMBER", enlarge(n)) #invoking the function