import unittest
from translator import english_to_french, french_to_english  

class TestTranslation(unittest.TestCase):
    
    def test_english_to_french(self):
        self.assertEqual(english_to_french("Hi"), "Bonjour")  
        self.assertNotEqual(english_to_french("Hi"), "Hello")  

    def test_french_to_english(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")  
        self.assertNotEqual(french_to_english("Bonjour"), "Bonjour")  

if __name__ == '__main__':
    unittest.main()

