
# pytest test/alt_mod_test.py

import pandas

from my_lambdata.my_mod import temp_conv , splitdate 

def test_temp_conv():
    assert temp_conv(0) == 32
        
def test_split_date():
    df = pandas.DataFrame({"date": ["6/18/2018", "10/5/2020"]})
    df = splitdate(df, "date")
    assert 'hour' in df.columns.tolist()