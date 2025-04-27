import streamlit as st
import os
import logging
from typing import List

# Set up logging
logger = logging.getLogger(__name__)

class InterestProfiler:
    """
    A class to handle user interest profiling for personalized content generation.
    """
    
    def __init__(self):
        """
        Initialize the InterestProfiler with predefined interest categories.
        """
        # Define interest categories and specific interests
        self.interest_categories = {
            "Sports": [
                "Basketball", "Soccer", "Baseball", "Football", "Swimming",
                "Running", "Gymnastics", "Dance", "Martial Arts", "Cycling"
            ],
            "Science": [
                "Space", "Animals", "Dinosaurs", "Chemistry", "Physics",
                "Biology", "Environment", "Technology", "Robotics", "Experiments"
            ],
            "Entertainment": [
                "Movies", "Music", "Video Games", "Comics", "Animation",
                "Superheroes", "Fantasy", "Science Fiction", "Comedy", "Adventure"
            ],
            "Arts": [
                "Drawing", "Painting", "Crafts", "Photography", "Theater",
                "Sculpture", "Fashion", "Design", "Music Creation", "Writing"
            ],
            "History": [
                "Ancient Civilizations", "World Wars", "American History", "Famous People",
                "Inventions", "Exploration", "Medieval Times", "Archaeology", "Mythology", "Culture"
            ]
        }
        
        # Flatten all interests for easy access
        self.all_interests = []
        for category, interests in self.interest_categories.items():
            self.all_interests.extend(interests)
        
        logger.info("InterestProfiler initialized with %d interest categories", len(self.interest_categories))
    
    def get_available_interests(self) -> List[str]:
        """
        Get a list of all available interests.
        
        Returns:
            List[str]: A list of all available interests
        """
        return sorted(self.all_interests)
    
    def get_interests_by_category(self) -> dict:
        """
        Get all interests organized by category.
        
        Returns:
            dict: Dictionary of interests by category
        """
        return self.interest_categories
    
    def get_recommended_interests(self, user_interests: List[str]) -> List[str]:
        """
        Get recommended interests based on user's current interests.
        
        Args:
            user_interests (List[str]): The user's current interests
            
        Returns:
            List[str]: A list of recommended interests
        """
        if not user_interests:
            # If no interests selected, recommend popular ones
            return ["Basketball", "Space", "Superheroes", "Drawing", "Ancient Civilizations"]
        
        # Find which categories the user is interested in
        category_counts = {}
        for category, interests in self.interest_categories.items():
            count = sum(1 for interest in user_interests if interest in interests)
            if count > 0:
                category_counts[category] = count
        
        # Find the most liked category
        favorite_category = max(category_counts.items(), key=lambda x: x[1])[0] if category_counts else "Science"
        
        # Recommend other interests from the favorite category
        recommendations = []
        for interest in self.interest_categories[favorite_category]:
            if interest not in user_interests:
                recommendations.append(interest)
        
        # Take top 5 or all if less than 5
        return recommendations[:5]
    
    def save_user_interests(self, user_id: str, interests: List[str]) -> bool:
        """
        Save the user's interests to the database.
        
        Args:
            user_id (str): The user's ID
            interests (List[str]): The user's selected interests
            
        Returns:
            bool: True if successful, False otherwise
        """
        # In a real application, this would save to a database
        # For the hackathon, we'll just log and pretend it worked
        logger.info("Saving interests for user %s: %s", user_id, interests)
        return True
    
    def get_user_interests(self, user_id: str) -> List[str]:
        """
        Get the user's saved interests from the database.
        
        Args:
            user_id (str): The user's ID
            
        Returns:
            List[str]: The user's interests
        """
        # In a real application, this would retrieve from a database
        # For the hackathon, we'll just return what's in the session state
        interests = st.session_state.interests if "interests" in st.session_state else []
        logger.info("Retrieved interests for user %s: %s", user_id, interests)
        return interests 