import streamlit as st
import os
import logging
import random
import json
import time
from typing import Dict, List, Any
import google.generativeai as genai
from dotenv import load_dotenv

# Set up logging
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Configure Google Gemini API
try:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    logger.info("Google Gemini API configured successfully for writing exercises")
except Exception as e:
    logger.error(f"Error configuring Gemini API for writing exercises: {e}")
    model = None

class WritingExerciseGenerator:
    """
    A class to generate writing exercises for spelling, grammar, and sentence structure.
    """
    
    def __init__(self):
        """
        Initialize the WritingExerciseGenerator with sample exercises.
        """
        # Define sample exercises for different levels and types
        self.sample_exercises = {
            "spelling": {
                "beginner": [
                    {
                        "instruction": "Listen to the word and type it correctly.",
                        "target_word": "play",
                        "hint": "What you do with toys or games",
                        "audio_url": None
                    },
                    {
                        "instruction": "Listen to the word and type it correctly.",
                        "target_word": "book",
                        "hint": "Something you read",
                        "audio_url": None
                    }
                ],
                "elementary": [
                    {
                        "instruction": "Listen to the word and type it correctly.",
                        "target_word": "because",
                        "hint": "Giving a reason for something",
                        "audio_url": None
                    },
                    {
                        "instruction": "Listen to the word and type it correctly.",
                        "target_word": "weather",
                        "hint": "If it's sunny, rainy, or snowy outside",
                        "audio_url": None
                    }
                ],
                "intermediate": [
                    {
                        "instruction": "Listen to the word and type it correctly.",
                        "target_word": "particularly",
                        "hint": "Especially or specifically",
                        "audio_url": None
                    },
                    {
                        "instruction": "Listen to the word and type it correctly.",
                        "target_word": "necessary",
                        "hint": "Something that must be done or is needed",
                        "audio_url": None
                    }
                ],
                "advanced": [
                    {
                        "instruction": "Listen to the word and type it correctly.",
                        "target_word": "conscientious",
                        "hint": "Being careful and thorough",
                        "audio_url": None
                    },
                    {
                        "instruction": "Listen to the word and type it correctly.",
                        "target_word": "quintessential",
                        "hint": "The perfect example of something",
                        "audio_url": None
                    }
                ],
                "expert": [
                    {
                        "instruction": "Listen to the word and type it correctly.",
                        "target_word": "sesquipedalian",
                        "hint": "Using long words",
                        "audio_url": None
                    },
                    {
                        "instruction": "Listen to the word and type it correctly.",
                        "target_word": "verisimilitude",
                        "hint": "The appearance of being true or real",
                        "audio_url": None
                    }
                ]
            },
            "grammar": {
                "beginner": [
                    {
                        "instruction": "Choose the correct word to complete the sentence: The cat ___ on the bed.",
                        "options": ["is", "are", "am"],
                        "correct_answer": "is",
                        "explanation": "We use 'is' with singular nouns like 'cat'."
                    }
                ],
                "intermediate": [
                    {
                        "instruction": "Choose the correct word to complete the sentence: Neither the students nor the teacher ___ going to the field trip.",
                        "options": ["is", "are", "am"],
                        "correct_answer": "is",
                        "explanation": "In 'neither/nor' constructions, the verb agrees with the noun closest to it (teacher)."
                    }
                ]
            },
            "sentence_structure": {
                "beginner": [
                    {
                        "instruction": "Put these words in the correct order to make a sentence: ball, the, threw, I",
                        "words": ["ball", "the", "threw", "I"],
                        "correct_answer": "I threw the ball",
                        "explanation": "In English, we usually put the subject (I) first, then the verb (threw), then the object (the ball)."
                    }
                ],
                "intermediate": [
                    {
                        "instruction": "Put these words in the correct order to make a sentence: yesterday, to the store, quickly, ran, she",
                        "words": ["yesterday", "to the store", "quickly", "ran", "she"],
                        "correct_answer": "She quickly ran to the store yesterday",
                        "explanation": "In English, we usually put the subject first (she), then adverbs (quickly), then the verb (ran), then the object (to the store), then time expressions (yesterday)."
                    }
                ]
            }
        }
        
        # Define common error patterns for spelling
        self.error_patterns = {
            "silent_letters": ["knight", "listen", "island", "doubt", "calm", "receipt", "subtle"],
            "double_consonants": ["opportunity", "accommodate", "successfully", "recommend", "committee"],
            "ie_ei_words": ["receive", "believe", "ceiling", "perceive", "receipt", "weight", "neighbor"],
            "homophones": [
                {"word": "their", "confusing_pairs": ["there", "they're"]},
                {"word": "wear", "confusing_pairs": ["where", "were"]},
                {"word": "effect", "confusing_pairs": ["affect"]},
                {"word": "principal", "confusing_pairs": ["principle"]},
                {"word": "weather", "confusing_pairs": ["whether"]}
            ]
        }
        
        logger.info("WritingExerciseGenerator initialized with sample exercises")
    
    def generate_exercise(self, exercise_type: str = "spelling", difficulty: str = "intermediate", interests: List[str] = None) -> Dict[str, Any]:
        """
        Generate a writing exercise based on type, difficulty, and interests.
        
        Args:
            exercise_type (str): Type of exercise (spelling, grammar, sentence_structure)
            difficulty (str): Difficulty level (beginner, elementary, intermediate, advanced, expert)
            interests (List[str]): List of user interests to personalize content
            
        Returns:
            Dict: Exercise data
        """
        # Validate exercise type
        if exercise_type not in self.sample_exercises:
            exercise_type = "spelling"
            logger.warning(f"Invalid exercise type. Defaulting to {exercise_type}")
        
        # Validate difficulty
        if difficulty not in ["beginner", "elementary", "intermediate", "advanced", "expert"]:
            difficulty = "intermediate"
            logger.warning(f"Invalid difficulty. Defaulting to {difficulty}")
        
        # If we don't have the specific difficulty for this exercise type, choose the closest one
        available_difficulties = list(self.sample_exercises[exercise_type].keys())
        if difficulty not in available_difficulties:
            if difficulty in ["beginner", "elementary"]:
                difficulty = "beginner" if "beginner" in available_difficulties else "elementary"
            elif difficulty in ["advanced", "expert"]:
                difficulty = "expert" if "expert" in available_difficulties else "advanced"
            else:
                difficulty = "intermediate"
            
            logger.warning(f"Adjusted difficulty to {difficulty} based on available options")
        
        # If no interests or no API key, use sample exercises
        if not interests or not model:
            sample_exercises = self.sample_exercises[exercise_type][difficulty]
            exercise = random.choice(sample_exercises)
            logger.info(f"Generated {exercise_type} exercise from samples")
            return exercise
        
        # Otherwise, generate a customized exercise using the Gemini API
        try:
            # Only use the first interest for simplicity
            interest = interests[0] if interests else None
            
            # Create prompt based on exercise type
            if exercise_type == "spelling":
                prompt = self._create_spelling_prompt(difficulty, interest)
            elif exercise_type == "grammar":
                prompt = self._create_grammar_prompt(difficulty, interest)
            else:  # sentence_structure
                prompt = self._create_sentence_structure_prompt(difficulty, interest)
            
            # Generate response
            response = model.generate_content(prompt)
            
            # Parse the response
            try:
                # Try to extract JSON from the response
                response_text = response.text
                if "```json" in response_text:
                    # Extract JSON from markdown code block
                    json_str = response_text.split("```json")[1].split("```")[0].strip()
                elif "```" in response_text:
                    # Extract JSON from generic code block
                    json_str = response_text.split("```")[1].strip()
                else:
                    # Assume the whole response is JSON
                    json_str = response_text
                
                exercise_data = json.loads(json_str)
                logger.info(f"Successfully generated {exercise_type} exercise using Gemini")
                return exercise_data
            
            except Exception as e:
                # If JSON parsing fails, fall back to sample
                logger.error(f"Error parsing JSON from model response: {e}")
                sample_exercises = self.sample_exercises[exercise_type][difficulty]
                return random.choice(sample_exercises)
        
        except Exception as e:
            logger.error(f"Error generating exercise with Gemini: {e}")
            # Fall back to sample exercises
            sample_exercises = self.sample_exercises[exercise_type][difficulty]
            return random.choice(sample_exercises)
    
    def _create_spelling_prompt(self, difficulty: str, interest: str = None) -> str:
        """Create a prompt for spelling exercise generation."""
        
        difficulty_descriptions = {
            "beginner": "simple words (3-4 letters) for a 1st grade student",
            "elementary": "basic words (4-6 letters) for a 3rd grade student",
            "intermediate": "moderately challenging words (6-9 letters) for a 6th grade student",
            "advanced": "challenging words (8-12 letters) for a 9th grade student",
            "expert": "very challenging words (10+ letters) for a 12th grade student"
        }
        
        interest_text = f" related to {interest}" if interest else ""
        difficulty_desc = difficulty_descriptions[difficulty]
        
        prompt = f"""
        Generate a spelling exercise with {difficulty_desc}{interest_text}.
        
        The exercise should include:
        - A word to spell
        - A short instruction
        - A hint that helps understand the word's meaning
        
        Format the response as a JSON object with these fields:
        - instruction: "Listen to the word and type it correctly."
        - target_word: [the word to spell]
        - hint: [a helpful hint about the word's meaning]
        - audio_url: null
        """
        
        return prompt
    
    def _create_grammar_prompt(self, difficulty: str, interest: str = None) -> str:
        """Create a prompt for grammar exercise generation."""
        
        interest_text = f" related to {interest}" if interest else ""
        
        prompt = f"""
        Generate a grammar exercise for a {difficulty} level student{interest_text}.
        
        The exercise should be a multiple-choice question asking the student to select 
        the grammatically correct option to complete a sentence.
        
        Format the response as a JSON object with these fields:
        - instruction: [the question asking to complete the sentence]
        - options: [array of possible answer choices]
        - correct_answer: [the correct option]
        - explanation: [brief explanation of the grammar rule]
        """
        
        return prompt
    
    def _create_sentence_structure_prompt(self, difficulty: str, interest: str = None) -> str:
        """Create a prompt for sentence structure exercise generation."""
        
        interest_text = f" related to {interest}" if interest else ""
        
        prompt = f"""
        Generate a sentence structure exercise for a {difficulty} level student{interest_text}.
        
        The exercise should give the student a set of words in random order and 
        ask them to arrange them into a grammatically correct sentence.
        
        Format the response as a JSON object with these fields:
        - instruction: [instruction to arrange the words]
        - words: [array of words in random order]
        - correct_answer: [the words arranged in correct order]
        - explanation: [brief explanation of the sentence structure rule]
        """
        
        return prompt
    
    def check_spelling_answer(self, user_answer: str, correct_answer: str) -> Dict[str, Any]:
        """
        Check if the user's spelling answer is correct and provide feedback.
        
        Args:
            user_answer (str): The user's typed answer
            correct_answer (str): The correct spelling
            
        Returns:
            Dict: Results of the check with feedback
        """
        is_correct = user_answer.lower() == correct_answer.lower()
        
        # Prepare character-by-character comparison
        comparison = []
        for i in range(max(len(user_answer), len(correct_answer))):
            if i < len(user_answer) and i < len(correct_answer):
                if user_answer[i].lower() == correct_answer[i].lower():
                    # Correct character
                    comparison.append({"char": correct_answer[i], "status": "correct"})
                else:
                    # Incorrect character
                    comparison.append({"char": correct_answer[i], "status": "incorrect", "user_char": user_answer[i]})
            elif i < len(correct_answer):
                # Missing character
                comparison.append({"char": correct_answer[i], "status": "missing"})
            else:
                # Extra character
                comparison.append({"char": "", "status": "extra", "user_char": user_answer[i]})
        
        # Determine error type and feedback
        feedback = ""
        if not is_correct:
            # Check for common error patterns
            if len(user_answer) < len(correct_answer):
                feedback = "You're missing some letters. Try sounding out the word more carefully."
            elif len(user_answer) > len(correct_answer):
                feedback = "You've added extra letters. Try listening to the word again."
            elif self._has_vowel_errors(user_answer, correct_answer):
                feedback = "Check the vowels in your spelling. Remember the difference between 'a', 'e', 'i', 'o', and 'u'."
            elif self._has_double_letter_errors(user_answer, correct_answer):
                feedback = "Pay attention to double letters. Some words have repeated letters."
            elif correct_answer.lower() in self.error_patterns["ie_ei_words"] and ('ie' in user_answer.lower() or 'ei' in user_answer.lower()):
                feedback = "Remember the rule: 'i' before 'e', except after 'c', or when sounded like 'a' as in 'neighbor' and 'weigh'."
            else:
                feedback = "Try sounding out the word carefully, one syllable at a time."
        
        result = {
            "is_correct": is_correct,
            "comparison": comparison,
            "feedback": feedback
        }
        
        logger.info(f"Spelling check: {'correct' if is_correct else 'incorrect'}")
        return result
    
    def _has_vowel_errors(self, user_answer: str, correct_answer: str) -> bool:
        """Check if the error is related to vowels."""
        vowels = 'aeiou'
        for i in range(min(len(user_answer), len(correct_answer))):
            if user_answer[i].lower() != correct_answer[i].lower():
                if user_answer[i].lower() in vowels or correct_answer[i].lower() in vowels:
                    return True
        return False
    
    def _has_double_letter_errors(self, user_answer: str, correct_answer: str) -> bool:
        """Check if the error is related to double letters."""
        # Look for patterns where a letter is doubled in one but not the other
        for i in range(min(len(user_answer), len(correct_answer)) - 1):
            if correct_answer[i] == correct_answer[i+1] and (i >= len(user_answer) - 1 or user_answer[i] != user_answer[i+1]):
                return True
            if i < len(user_answer) - 1 and user_answer[i] == user_answer[i+1] and correct_answer[i] != correct_answer[i+1]:
                return True
        return False 