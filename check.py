import unittest

def check(x):
    if x>=100:
        return True
    else:
        return False

class MyTest(unittest.TestCase):  

    def test(self):  
        self.assertTrue(check(99)) 

if __name__ == '__main__':
    unittest.main()
