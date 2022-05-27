# Importing the module unittest 
import unittest

# Importing the script to be tested
import cap

# Creating a class for testing / Inheriting
class TestCap(unittest.TestCase):

    # Creating functions to test different situations 
    def test_one_word(self):
        # Setting the variables I need
        text = 'python'
        # Calling functions or classes passing in something
        result = cap.cap_text(text)
        # Using assertEqual to check if result is the expected
        self.assertEqual(result,'Python')
    
    def test_multiple_words(self):
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result,'Monty Python')

if __name__ == '__main__':
    unittest.main()