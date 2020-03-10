
# my_lambdata/my_script.py

import pandas

from my_lambdata.my_mod import enlarge

print("HELLO WORLD")

df = pandas.DataFrame({"state": ["CT","CO","CA","TX"]})
print(df.head())

print("--------------")


n = 5
print("NUMBER",n)
print("ENLARGED NUMBER", enlarge(n)) #invoking the function