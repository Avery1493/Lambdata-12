
# test/my_mod_test.py
# python -m unittest  test.my_mod_test

import unittest
import pandas

from my_lambdata.my_mod import temp_conv, splitdate  

class TestTempConv(unittest.TestCase):

    def test_temp_conv(self):
        self.assertEqual(temp_conv(0),32)
        

class TestSplitDate(unittest.TestCase):  
    
    def test_split_date(self):
        df = pandas.DataFrame({"date": ["6/18/2018", "10/5/2020"]})
        df = splitdate(df, "date")
        self.assertTrue('month' in df.columns.tolist())


if __name__ == '__main__':
    unittest.main()