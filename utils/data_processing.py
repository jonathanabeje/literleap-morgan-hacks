import logging
import re
from typing import List, Dict, Any

# Set up logging
logger = logging.getLogger(__name__)

def clean_text(text: str) -> str:
    """
    Clean text by removing extra whitespace and special characters.
    
    Args:
        text (str): The text to clean
        
    Returns:
        str: Cleaned text
    """
    # Remove extra whitespace
    cleaned = re.sub(r'\s+', ' ', text).strip()
    
    # Remove special characters except punctuation
    cleaned = re.sub(r'[^\w\s.,!?;:\'"-]', '', cleaned)
    
    return cleaned

def extract_difficult_words(text: str, min_length: int = 7) -> List[str]:
    """
    Extract potentially difficult words from text based on length.
    
    Args:
        text (str): The text to analyze
        min_length (int): Minimum word length to consider difficult
        
    Returns:
        List[str]: List of difficult words
    """
    # Split text into words and remove punctuation
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Filter for words longer than min_length
    difficult_words = [word for word in words if len(word) >= min_length]
    
    # Remove duplicates while preserving order
    unique_words = []
    for word in difficult_words:
        if word not in unique_words:
            unique_words.append(word)
    
    return unique_words

def calculate_reading_stats(text: str) -> Dict[str, Any]:
    """
    Calculate reading statistics for a given text.
    
    Args:
        text (str): The text to analyze
        
    Returns:
        Dict: Reading statistics
    """
    # Count words
    words = re.findall(r'\b\w+\b', text)
    word_count = len(words)
    
    # Count sentences
    sentences = re.split(r'[.!?]+', text)
    sentence_count = len([s for s in sentences if s.strip()])
    
    # Count syllables (very rough approximation)
    syllable_count = 0
    for word in words:
        word = word.lower()
        # Count vowel groups as syllables
        vowel_groups = re.findall(r'[aeiouy]+', word)
        count = len(vowel_groups)
        # Adjust for some common patterns
        if word.endswith('e') and len(word) > 2 and word[-2] not in 'aeiou':
            count -= 1
        if count == 0:
            count = 1
        syllable_count += count
    
    # Calculate averages
    avg_words_per_sentence = word_count / max(1, sentence_count)
    avg_syllables_per_word = syllable_count / max(1, word_count)
    
    # Calculate readability scores (simplified Flesch-Kincaid)
    flesch_reading_ease = 206.835 - (1.015 * avg_words_per_sentence) - (84.6 * avg_syllables_per_word)
    flesch_kincaid_grade = (0.39 * avg_words_per_sentence) + (11.8 * avg_syllables_per_word) - 15.59
    
    # Clamp scores to reasonable ranges
    flesch_reading_ease = max(0, min(100, flesch_reading_ease))
    flesch_kincaid_grade = max(0, min(12, flesch_kincaid_grade))
    
    stats = {
        "word_count": word_count,
        "sentence_count": sentence_count,
        "syllable_count": syllable_count,
        "avg_words_per_sentence": round(avg_words_per_sentence, 1),
        "avg_syllables_per_word": round(avg_syllables_per_word, 2),
        "flesch_reading_ease": round(flesch_reading_ease, 1),
        "flesch_kincaid_grade": round(flesch_kincaid_grade, 1)
    }
    
    return stats

def format_word_for_display(word: str) -> str:
    """
    Format a word for display with syllable breaks.
    
    Args:
        word (str): The word to format
        
    Returns:
        str: Formatted word with syllable breaks
    """
    # This is a simplified approach - a real implementation would use a dictionary
    vowels = 'aeiouy'
    syllables = []
    current = ""
    
    for i, char in enumerate(word):
        current += char
        if char.lower() in vowels and i < len(word) - 1 and word[i+1].lower() not in vowels:
            syllables.append(current)
            current = ""
    
    if current:
        syllables.append(current)
    
    # Join with dots
    return "·".join(syllables) 