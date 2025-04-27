import unittest
import sys
import os

# Add parent directory to path so we can import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.data_processing import (
    clean_text,
    extract_difficult_words,
    calculate_reading_stats,
    format_word_for_display
)


class TestDataProcessing(unittest.TestCase):
    """Test cases for data processing utilities."""
    
    def test_clean_text(self):
        """Test the clean_text function."""
        # Test removing extra whitespace
        self.assertEqual(clean_text("  Hello   world!  "), "Hello world!")
        
        # Test removing special characters
        self.assertEqual(clean_text("Hello @#$% world!"), "Hello  world!")
        
        # Test preserving punctuation
        self.assertEqual(clean_text("Hello, world!"), "Hello, world!")
    
    def test_extract_difficult_words(self):
        """Test the extract_difficult_words function."""
        text = "The hippopotamus is a large, mostly herbivorous, semiaquatic mammal."
        
        # Default minimum length (7)
        difficult_words = extract_difficult_words(text)
        self.assertIn("hippopotamus", difficult_words)
        self.assertIn("herbivorous", difficult_words)
        self.assertIn("semiaquatic", difficult_words)
        self.assertNotIn("large", difficult_words)
        self.assertNotIn("mammal", difficult_words)
        
        # Custom minimum length
        difficult_words = extract_difficult_words(text, min_length=5)
        self.assertIn("large", difficult_words)
        self.assertIn("mammal", difficult_words)
        self.assertNotIn("is", difficult_words)
        self.assertNotIn("a", difficult_words)
    
    def test_calculate_reading_stats(self):
        """Test the calculate_reading_stats function."""
        text = "The cat sat on the mat. It was very comfortable."
        
        stats = calculate_reading_stats(text)
        
        self.assertEqual(stats["word_count"], 9)
        self.assertEqual(stats["sentence_count"], 2)
        self.assertEqual(stats["avg_words_per_sentence"], 4.5)
        
        # Check that all expected keys are present
        expected_keys = [
            "word_count", "sentence_count", "syllable_count",
            "avg_words_per_sentence", "avg_syllables_per_word",
            "flesch_reading_ease", "flesch_kincaid_grade"
        ]
        for key in expected_keys:
            self.assertIn(key, stats)
    
    def test_format_word_for_display(self):
        """Test the format_word_for_display function."""
        # Test simple words
        self.assertEqual(format_word_for_display("cat"), "cat")
        
        # Test multi-syllable words
        formatted = format_word_for_display("reading")
        self.assertTrue("·" in formatted)
        
        # Test specific examples
        self.assertEqual(format_word_for_display("hippopotamus"), "hi·ppo·po·ta·mus")


if __name__ == "__main__":
    unittest.main() 