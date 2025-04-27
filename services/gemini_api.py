import os
import logging
import json
from typing import Dict, Any, Optional, List
import google.generativeai as genai
from dotenv import load_dotenv

# Set up logging
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

class GeminiService:
    """
    Service class for interacting with the Google Gemini API.
    """
    
    def __init__(self):
        """
        Initialize the Gemini API service.
        """
        try:
            # Get API key from environment
            self.api_key = os.getenv("GOOGLE_API_KEY")
            
            if not self.api_key:
                logger.warning("Google API key not found in environment variables")
                self.model = None
                return
            
            # Configure the API
            genai.configure(api_key=self.api_key)
            
            # Initialize the model
            self.model = genai.GenerativeModel('gemini-pro')
            logger.info("Gemini API service initialized successfully")
            
        except Exception as e:
            logger.error(f"Error initializing Gemini API service: {e}")
            self.model = None
    
    def is_available(self) -> bool:
        """
        Check if the Gemini API service is available.
        
        Returns:
            bool: True if the service is available, False otherwise
        """
        return self.model is not None
    
    def generate_reading_passage(self, interests: List[str], reading_level: str) -> Dict[str, Any]:
        """
        Generate a reading passage based on user interests and reading level.
        
        Args:
            interests (List[str]): User interests
            reading_level (str): Reading level
            
        Returns:
            Dict: Generated passage with title and text
        """
        if not self.is_available():
            logger.warning("Gemini API not available for generating reading passage")
            return {"title": "Sample Passage", "text": "This is a sample passage. The Gemini API is not available."}
        
        try:
            # Format interests as a comma-separated string
            interest_text = ", ".join(interests[:3])  # Use up to 3 interests
            
            # Define reading level descriptions
            reading_level_descriptions = {
                "beginner": "for a 1st grade student (age 6-7). Use simple sentences and common words.",
                "elementary": "for a 3rd grade student (age 8-9). Use simple paragraphs and include some challenging vocabulary.",
                "intermediate": "for a 6th grade student (age 11-12). Use several paragraphs with varied sentence structure.",
                "advanced": "for a 9th grade student (age 14-15). Use complex sentences and academic vocabulary.",
                "expert": "for a 12th grade student (age 17-18). Use sophisticated language and complex concepts."
            }
            
            level_description = reading_level_descriptions.get(
                reading_level, reading_level_descriptions["intermediate"]
            )
            
            # Create prompt
            prompt = f"""
            Create an engaging reading passage {level_description}
            
            The passage should be about the following interests: {interest_text}
            
            The passage should be approximately:
            - beginner: 50-100 words
            - elementary: 150-250 words
            - intermediate: 300-400 words
            - advanced: 400-500 words
            - expert: 500-600 words
            
            Please format the output as a JSON object with two fields:
            - title: A catchy title for the passage
            - text: The text of the passage
            
            Make the passage interesting, informative, and appropriate for a school-age reader.
            """
            
            # Generate response
            response = self.model.generate_content(prompt)
            
            # Try to extract JSON from the response
            try:
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
                
                passage_data = json.loads(json_str)
                logger.info(f"Successfully generated passage about {interest_text}")
                return passage_data
                
            except Exception as e:
                # If JSON parsing fails, create a structured passage from the text
                logger.error(f"Error parsing JSON from model response: {e}")
                fallback_text = response.text.replace("```json", "").replace("```", "")
                
                if "Title:" in fallback_text and "Text:" in fallback_text:
                    title = fallback_text.split("Title:")[1].split("Text:")[0].strip()
                    text = fallback_text.split("Text:")[1].strip()
                else:
                    # If we can't parse it properly, make a best guess
                    parts = fallback_text.split("\n\n", 1)
                    title = parts[0].strip() if len(parts) > 1 else "Interesting Facts"
                    text = parts[1] if len(parts) > 1 else fallback_text
                
                return {"title": title, "text": text}
        
        except Exception as e:
            logger.error(f"Error generating passage with Gemini API: {e}")
            return {"title": "Error", "text": "An error occurred while generating the passage."}
    
    def generate_writing_exercise(self, exercise_type: str, difficulty: str, interest: Optional[str] = None) -> Dict[str, Any]:
        """
        Generate a writing exercise.
        
        Args:
            exercise_type (str): Type of exercise (spelling, grammar, sentence_structure)
            difficulty (str): Difficulty level
            interest (str, optional): User interest
            
        Returns:
            Dict: Generated exercise data
        """
        if not self.is_available():
            logger.warning("Gemini API not available for generating writing exercise")
            return {
                "instruction": "Sample exercise",
                "target_word": "sample",
                "hint": "This is a sample exercise"
            }
        
        try:
            # Create prompt based on exercise type
            if exercise_type == "spelling":
                prompt = self._create_spelling_prompt(difficulty, interest)
            elif exercise_type == "grammar":
                prompt = self._create_grammar_prompt(difficulty, interest)
            else:  # sentence_structure
                prompt = self._create_sentence_structure_prompt(difficulty, interest)
            
            # Generate response
            response = self.model.generate_content(prompt)
            
            # Try to extract JSON from the response
            try:
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
                logger.error(f"Error parsing JSON from model response: {e}")
                return {
                    "instruction": "Listen to the word and type it correctly.",
                    "target_word": "generate",
                    "hint": "To create or produce something"
                }
        
        except Exception as e:
            logger.error(f"Error generating exercise with Gemini API: {e}")
            return {
                "instruction": "Error generating exercise",
                "target_word": "error",
                "hint": "Something went wrong"
            }
    
    def _create_spelling_prompt(self, difficulty: str, interest: Optional[str] = None) -> str:
        """Create a prompt for spelling exercise generation."""
        
        difficulty_descriptions = {
            "beginner": "simple words (3-4 letters) for a 1st grade student",
            "elementary": "basic words (4-6 letters) for a 3rd grade student",
            "intermediate": "moderately challenging words (6-9 letters) for a 6th grade student",
            "advanced": "challenging words (8-12 letters) for a 9th grade student",
            "expert": "very challenging words (10+ letters) for a 12th grade student"
        }
        
        interest_text = f" related to {interest}" if interest else ""
        difficulty_desc = difficulty_descriptions.get(difficulty, difficulty_descriptions["intermediate"])
        
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
    
    def _create_grammar_prompt(self, difficulty: str, interest: Optional[str] = None) -> str:
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
    
    def _create_sentence_structure_prompt(self, difficulty: str, interest: Optional[str] = None) -> str:
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