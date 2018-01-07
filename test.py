from unittest import TestCase
from main import main

class TestMain(TestCase):
    
    day = ["2017-12-15 00:00:00", "2017-12-16 00:00:00", "2017-12-17 00:00:00", "2017-12-18 00:00:00", "2017-12-19 00:00:00"]
    price = ["17771.899999999998", "19498.683333333334", "19289.785", "18961.856666666667", "17737.111666666668"]
    dataset = list(zip(day, price))
    
    request = main()
    
    def test_max_rise(self):
        testing = self.request.max_rise(self.dataset)
        self.assertEqual(testing[0], 9.716368724409527)
        self.assertEqual(testing[1], '2017-12-16 00:00:00')
        
    def test_max_fall(self):
       testing = self.request.max_fall(self.dataset)
       self.assertEqual(testing[0], -6.4589930275815055)
       self.assertEqual(testing[1], '2017-12-19 00:00:00')
       
    def test_max_price(self):     
        testing = self.request.max_price(self.dataset)
        self.assertEqual(testing[0], 19498.683333333334)
        self.assertEqual(testing[1], '2017-12-16 00:00:00')
