import unittest
import unitTesting

class TestCap(unittest.TestCase):
  def test_one_word(self):
    text = 'python'
    result = unitTesting.cap_text(text)
    self.assertEqual(result, 'Python')

  def test_multiple_words(self):
    text = 'monty python'
    result = unitTesting.cap_text(text)
    self.assertEqual(result, 'Monty Python')

if __name__== '__main__':
  unittest.main()