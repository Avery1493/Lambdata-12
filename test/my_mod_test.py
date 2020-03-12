
# test/my_mod_test.py
# python -m unittest  test.my_mod_test

import unittest

from my_lambdata.my_mod import temp_conv   

class TestMyMod(unittest.TestCase):

    def test_temp_conv(self):
        self.assertEqual(temp_conv(0),33)
        
   

if __name__ == '__main__':
    unittest.main()