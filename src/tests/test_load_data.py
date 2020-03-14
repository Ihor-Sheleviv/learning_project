import unittest
from load_data import load_data

class TestLoadData(unittest.TestCase):

    def test_load_one_goods(self):
        goods = [['Coca-cola',16.00,26]]
        path = 'd:\\2020\\ITM\\KN-19\\TP\\test\\'
        file = 'test_one.dat'
        
        self.assertListEqual(load_data(path,file), goods)

    def test_load_empty_goods(self):
        goods = []
        path = 'd:\\2020\\ITM\\KN-19\\TP\\test\\'
        file = 'test_empty.dat'
        
        self.assertListEqual(load_data(path,file), [])

    def test_load_many_goods(self):
        goods = [['Coca-cola',16.00,26],['Coca-cola',16.00,26]]
        path = 'd:\\2020\\ITM\\KN-19\\TP\\test\\'
        file = 'test_many.dat'
        
        self.assertListEqual(load_data(path,file), goods)    
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
    
