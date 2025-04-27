import streamlit as st
import os
import logging
import time
import random
from typing import Dict, List, Tuple, Any
import json
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
    logger.info("Google Gemini API configured successfully")
except Exception as e:
    logger.error(f"Error configuring Gemini API: {e}")
    model = None

class ReadingAnalyzer:
    """
    A class to handle reading passage generation and analysis.
    """
    
    def __init__(self):
        """
        Initialize the ReadingAnalyzer with sample passages for different levels.
        """
        # Define sample passages for different reading levels
        # In a real application, these would be dynamically generated
        self.sample_passages = {
            "beginner": [
                {
                    "title": "The Lost Ball",
                    "text": "Tom had a red ball. He liked to play with it every day. One day, he threw the ball too high. It went over the fence. Tom looked for his ball. He could not find it. Then, his friend Sam came. Sam had found the ball! Tom was happy. He said, 'Thank you, Sam!'"
                },
                {
                    "title": "My Pet Dog",
                    "text": "I have a pet dog. His name is Max. Max is brown and white. He likes to run and play. He chases his tail and barks at birds. Max sleeps in a big bed. I feed Max every morning. I love my dog Max very much."
                }
            ],
            "elementary": [
                {
                    "title": "The Mysterious Garden",
                    "text": "Behind Jenny's house was an old garden. No one had taken care of it for years. Weeds grew tall, and vines covered the fence. One sunny Saturday, Jenny decided to explore the garden. She pushed through the rusty gate and gasped. Hidden among the weeds were beautiful flowers of every color. There was also a small pond with tiny fish swimming in it. Jenny spent the whole day cleaning up the garden. She pulled weeds and trimmed branches. By evening, she had discovered a magical place that would become her special hideaway."
                },
                {
                    "title": "The Science Fair Project",
                    "text": "Miguel was excited about the science fair. He wanted to create something amazing that would impress everyone. After thinking for days, he decided to build a small robot that could sort colored blocks. His dad helped him get the parts, but Miguel did all the work himself. It wasn't easy. The robot kept dropping blocks or putting them in the wrong places. Miguel had to fix it many times. Finally, on the day of the science fair, his robot worked perfectly. Miguel won first prize, but he was most proud that he hadn't given up when things got difficult."
                }
            ],
            "intermediate": [
                {
                    "title": "The Ancient Map",
                    "text": "Carlos found the old map tucked between the pages of a dusty book in his grandfather's attic. The yellowed paper crinkled as he carefully unfolded it, revealing what appeared to be directions to a location in the nearby woods. Curious about where the map might lead, Carlos decided to follow it the next day. The directions were challenging to follow, with landmarks that had changed over the years. After several hours of searching, Carlos discovered a small clearing with the remains of what looked like an old cabin. Among the ruins, he found a metal box containing photographs and letters from nearly a century ago. Carlos realized he had uncovered a forgotten piece of local history that told the story of the people who had lived in these woods long before his time."
                },
                {
                    "title": "The Robot Competition",
                    "text": "Aisha had been working on her robot for six months, carefully programming it to navigate complex obstacles and solve puzzles. The STEM competition was only two weeks away, and she was making final adjustments when disaster struck. During a test run, the robot's main circuit board short-circuited, sending a small puff of smoke into the air. Aisha's heart sank as she realized the extent of the damage. With the competition approaching rapidly, she would need to rebuild the central processing unit from scratch. Working late into the night, Aisha redesigned the circuit with a more efficient layout. Her determination paid off when, on the day of the competition, her robot not only functioned flawlessly but performed better than her original design. The setback had forced her to innovate, ultimately leading to her first-place victory."
                }
            ],
            "advanced": [
                {
                    "title": "The Quantum Physics Experiment",
                    "text": "Dr. Eliza Chen meticulously reviewed the data from her quantum entanglement experiment, her eyes scanning the columns of numbers for patterns that might explain the anomalous results she had observed during the last three trials. The particles were behaving in ways that contradicted established theories, maintaining their connection across distances that should have made such interactions impossible. If her findings could be replicated, they would challenge fundamental principles of physics and potentially revolutionize our understanding of the universe's underlying structure. However, Eliza was cautious about jumping to conclusions; scientific history was littered with promising discoveries that failed under rigorous examination. She would need to eliminate all possible sources of experimental error before presenting her findings to the international physics community, where skepticism would be the default response to such extraordinary claims."
                },
                {
                    "title": "The Economic Impact of Climate Change",
                    "text": "The relationship between climate change and global economic systems reveals complex interdependencies that challenge traditional models of sustainable development. As extreme weather events increase in frequency and severity, industries from agriculture to insurance face unprecedented disruptions to their operational stability. Coastal economies particularly face existential threats from rising sea levels, with some projections suggesting that major urban centers could experience trillions of dollars in infrastructure damage by mid-century if current warming trends continue. Adaptation strategies require substantial initial investments but may ultimately prove more economically viable than the massive costs associated with disaster recovery and population displacement. Policymakers now confront difficult decisions about allocating limited resources between mitigation efforts, which address root causes, and adaptation measures, which respond to already inevitable changes to regional climates."
                }
            ],
            "expert": [
                {
                    "title": "Neuroplasticity and Cognitive Development",
                    "text": "The paradigm shift in our understanding of neuroplasticity—the brain's remarkable capacity to reorganize itself by forming new neural connections—has profound implications for educational theory and cognitive development models. Contrary to earlier deterministic perspectives that emphasized critical periods beyond which certain types of learning became virtually impossible, contemporary neuroscience research demonstrates that structural and functional plasticity persists throughout the lifespan, albeit with different characteristics and constraints at different developmental stages. This evolving comprehension of neural malleability has catalyzed innovative therapeutic interventions for individuals with traumatic brain injuries, neurodevelopmental disorders, and age-related cognitive decline. Moreover, it has substantiated the efficacy of enriched environmental stimulation and targeted cognitive exercises in enhancing intellectual capabilities across diverse populations. Educational methodologies that strategically leverage these neurobiological principles can potentially optimize learning outcomes by synchronizing instructional approaches with the mechanistic underpinnings of knowledge acquisition and memory consolidation."
                },
                {
                    "title": "Theoretical Implications of Quantum Computing",
                    "text": "The potential realization of fault-tolerant quantum computing systems represents a paradigmatic disruption in computational theory and applied mathematics. Unlike classical computers, which manipulate deterministic bits in boolean logic operations, quantum computers utilize qubits that exist in superposition states and exhibit entanglement—properties that fundamentally alter the landscape of algorithmic possibility. The implications extend beyond mere computational efficiency; certain previously intractable problems become theoretically solvable, necessitating reconsideration of cryptographic protocols that underpin contemporary digital security infrastructure. Shor's algorithm exemplifies this transformative potential, offering exponential speedup for integer factorization compared to the best-known classical algorithms. However, significant theoretical and engineering challenges persist in the transition from conceptual quantum advantage to practical quantum supremacy. Error correction, qubit coherence maintenance, and scaling issues remain formidable obstacles. The interdisciplinary nature of these challenges has fostered unprecedented collaboration between theoretical physicists, computer scientists, materials engineers, and mathematicians—a convergence that itself accelerates innovation across multiple scientific domains."
                }
            ]
        }
        
        logger.info("ReadingAnalyzer initialized with sample passages for 5 reading levels")
    
    def generate_passage(self, interests: List[str] = None, reading_level: str = "intermediate") -> Dict[str, Any]:
        """
        Generate a reading passage based on user interests and reading level.
        
        Args:
            interests (List[str]): List of user interests
            reading_level (str): The reading level (beginner, elementary, intermediate, advanced, expert)
            
        Returns:
            Dict: A dictionary containing the title and text of the passage
        """
        # Validate reading level
        if reading_level not in self.sample_passages:
            reading_level = "intermediate"
            logger.warning(f"Invalid reading level provided. Defaulting to {reading_level}")
        
        # If no interests provided, use sample passages
        if not interests or not model:
            sample_for_level = self.sample_passages[reading_level]
            return random.choice(sample_for_level)
        
        # Otherwise, generate a passage using Google Gemini API
        try:
            # Create prompt for the model
            interest_text = ", ".join(interests[:3])  # Use up to 3 interests
            
            reading_level_descriptions = {
                "beginner": "for a 1st grade student (age 6-7). Use simple sentences and common words.",
                "elementary": "for a 3rd grade student (age 8-9). Use simple paragraphs and include some challenging vocabulary.",
                "intermediate": "for a 6th grade student (age 11-12). Use several paragraphs with varied sentence structure.",
                "advanced": "for a 9th grade student (age 14-15). Use complex sentences and academic vocabulary.",
                "expert": "for a 12th grade student (age 17-18). Use sophisticated language and complex concepts."
            }
            
            level_description = reading_level_descriptions[reading_level]
            
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
            logger.error(f"Error generating passage: {e}")
            # Fall back to sample passages
            sample_for_level = self.sample_passages[reading_level]
            return random.choice(sample_for_level)
    
    def analyze_reading(self, audio_data: bytes, expected_text: str) -> Dict[str, Any]:
        """
        Analyze a reading sample against the expected text.
        
        Args:
            audio_data (bytes): The recorded audio data
            expected_text (str): The text that was supposed to be read
            
        Returns:
            Dict: Analysis results including accuracy, fluency, etc.
        """
        # In a real application, this would use speech recognition and analysis
        # For the hackathon, we'll simulate the analysis
        
        # Simulate processing time
        time.sleep(2)
        
        # Generate mock analysis results
        word_count = len(expected_text.split())
        
        # Calculate mock metrics
        accuracy = random.uniform(80.0, 98.0)
        words_per_minute = random.uniform(85.0, 140.0)
        fluency_score = random.uniform(70.0, 95.0)
        
        # Generate mock error words (words that were difficult to pronounce)
        words = expected_text.split()
        error_words = []
        for word in words:
            if len(word) > 8 and random.random() < 0.3:  # 30% chance for long words
                error_words.append(word)
            elif word.endswith('ing') and random.random() < 0.2:  # 20% chance for -ing words
                error_words.append(word)
        
        # Limit to 3 error words
        error_words = error_words[:3]
        
        analysis_results = {
            "accuracy": accuracy,
            "words_per_minute": words_per_minute,
            "fluency_score": fluency_score,
            "error_words": error_words,
            "total_words": word_count,
            "strengths": [
                "Good pacing throughout most of the passage",
                "Clear pronunciation of most words",
                "Appropriate expression for the content"
            ],
            "areas_for_improvement": [
                f"Some difficulty with longer words like '{', '.join(error_words)}'",
                "Occasional hesitation between sentences",
                "Could improve reading speed consistency"
            ]
        }
        
        logger.info(f"Reading analysis completed with accuracy: {accuracy:.1f}%")
        return analysis_results
    
    def get_pronunciation_guide(self, word: str) -> str:
        """
        Get a pronunciation guide for a difficult word.
        
        Args:
            word (str): The word to get pronunciation for
            
        Returns:
            str: Pronunciation guide
        """
        # In a real application, this would use a pronunciation API
        # For the hackathon, we'll use some mock data
        
        pronunciation_guides = {
            "particularly": "par·tic·u·lar·ly (par-TIK-yuh-ler-lee)",
            "thoroughly": "thor·ough·ly (THUR-oh-lee)",
            "phenomenon": "phe·nom·e·non (fih-NOM-uh-non)",
            "necessary": "nec·es·sar·y (NESS-eh-sair-ee)",
            "specifically": "spe·cif·i·cal·ly (spih-SIF-ik-lee)",
            "interesting": "in·ter·est·ing (IN-ter-es-ting)",
            "temperature": "tem·per·a·ture (TEM-per-uh-chur)",
            "environment": "en·vi·ron·ment (en-VY-ern-ment)",
            "scientific": "sci·en·tif·ic (sy-en-TIF-ik)",
            "government": "gov·ern·ment (GUV-ern-ment)"
        }
        
        # If we have a guide for the word, return it
        if word.lower() in pronunciation_guides:
            return pronunciation_guides[word.lower()]
        
        # Otherwise, make a simple syllable breakdown
        syllables = []
        current = ""
        
        for i, char in enumerate(word):
            current += char
            if char.lower() in 'aeiou' and i < len(word) - 1 and word[i+1].lower() not in 'aeiou':
                syllables.append(current)
                current = ""
        
        if current:
            syllables.append(current)
        
        # Join with dots
        syllable_text = "·".join(syllables)
        
        return f"{syllable_text} ({word.upper()})" 