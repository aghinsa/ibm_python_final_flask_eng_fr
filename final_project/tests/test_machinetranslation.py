import unittest

from machinetranslation.translator import englishToFrench,frenchToEnglish

class TestTranslation(unittest.TestCase):
    def test_englishToFrenchNull(self):
        self.assertEqual("",englishToFrench(""))
    
    def test_englishToFrench(self):
        self.assertEqual("Bonjour",englishToFrench("Hello"))
    
    def test_frenchToEnglishNull(self):
        self.assertEqual("",frenchToEnglish(""))
    
    def test_frenchToEnglish(self):
        self.assertEqual("Hello",frenchToEnglish("Bonjour"))

if __name__ == '__main__':
    unittest.main()

