import unittest

def categorize_by_age(age):
    if 0 <= age <= 9:
        return "Child"
    elif 9 < age <= 18:
        return "Adolescent"
    elif 18 < age <= 65:
        return "Adult"
    elif 65 < age <= 150:
        return "Golden Age"
    else:
        return f"Invalid Age: {age}"
    
class TestCategorize(unittest.TestCase):  

    def test_child(self):  
        self.assertEqual(categorize_by_age(10), "Child") 

    def test_adolescent(self):  
        self.assertEqual(categorize_by_age(19), "Adolescent")

    def test_adult(self):  
        self.assertEqual(categorize_by_age(17), "Adult")

    def test_golden_age(self):  
        self.assertEqual(categorize_by_age(66), "Golden Age")

    def test_negative_age(self):  
        self.assertEqual(categorize_by_age(-1), "Invalid Age: -1")

    def test_too_old(self):  
        self.assertEqual(categorize_by_age(151), "Invalid Age: 151") 

 
 
if __name__ == '__main__':
    unittest.main()
