import unittest
# from gradescope_utils.autograder_utils.decorators import weight, number
from spell_checker import SpellChecker

class TestSpellChecker(unittest.TestCase):
    def setUp(self):
        self.dictionary = ["apple", "banana", "cherry", "date", "elderberry", "hello"]
        self.spell_checker = SpellChecker(self.dictionary)
    
    # @weight(1)
    # @number("3.1")
    def test_load_dictionary(self):
        self.assertEqual(len(self.spell_checker.dictionary), 6)
        self.assertTrue(all(word in self.spell_checker.dictionary for word in self.dictionary))
    
    # @weight(1)
    # @number("3.2")
    def test_check_correct_word(self):
        self.assertTrue(self.spell_checker.check_word("apple"))
        self.assertTrue(self.spell_checker.check_word("banana"))
    
    # @weight(1)
    # @number("3.3")
    def test_check_incorrect_word(self):
        self.assertFalse(self.spell_checker.check_word("helo"))
        self.assertFalse(self.spell_checker.check_word("wrld"))
    
    # @weight(1)
    # @number("3.4")
    def test_suggest_corrections(self):
        suggestions = self.spell_checker.suggest_corrections("helo")
        self.assertIn("hello", suggestions)
    
    # @weight(1)
    # @number("3.5")
    def test_check_text(self):
        text = "This is a testt of the spellchecker"
        misspelled = self.spell_checker.check_text(text)
        self.assertIn("testt", misspelled)
        self.assertIn("spellchecker", misspelled)
    
    # @weight(1)
    # @number("3.6")
    def test_spell_check_and_suggest(self):
        text = "The quick brown fox jumps over the lazy dog."
        suggestions = self.spell_checker.spell_check_and_suggest(text)
        self.assertNotIn("then", suggestions)
        self.assertIn("jumps", suggestions)