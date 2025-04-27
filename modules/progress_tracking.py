import streamlit as st
import os
import logging
from datetime import datetime, timedelta
import random
from typing import Dict, List, Any

# Set up logging
logger = logging.getLogger(__name__)

class ProgressTracker:
    """
    A class to track and analyze student progress over time.
    """
    
    def __init__(self):
        """
        Initialize the ProgressTracker.
        """
        logger.info("ProgressTracker initialized")
    
    def get_recent_activities(self, days: int = 7) -> List[Dict[str, Any]]:
        """
        Get recent activities for the current user.
        
        Args:
            days (int): Number of days to include
            
        Returns:
            List[Dict]: List of activity records
        """
        # In a real app, this would fetch from the database
        # For the hackathon, we'll generate mock data
        
        activities = []
        today = datetime.now()
        
        # Generate random activities for the past week
        for i in range(days):
            date = today - timedelta(days=i)
            date_str = date.strftime("%b %d, %Y")
            
            # Add some variety to the activities
            if i == 0:
                activities.append({
                    "date": date_str,
                    "description": "Completed reading exercise with 92% accuracy"
                })
            elif i == 1:
                activities.append({
                    "date": date_str,
                    "description": "Mastered 5 challenging spelling words"
                })
            elif i == 2:
                activities.append({
                    "date": date_str,
                    "description": "Improved reading speed to 110 words per minute"
                })
            elif i == 3:
                activities.append({
                    "date": date_str,
                    "description": "Completed grammar exercise with 85% accuracy"
                })
            else:
                activity_type = random.choice(["reading", "writing", "spelling", "grammar"])
                score = random.randint(75, 95)
                activities.append({
                    "date": date_str,
                    "description": f"Practiced {activity_type} skills ({score}% accuracy)"
                })
        
        logger.info(f"Retrieved {len(activities)} recent activities")
        return activities
    
    def get_progress_summary(self) -> Dict[str, Any]:
        """
        Get a summary of the student's overall progress.
        
        Returns:
            Dict: Summary statistics
        """
        # In a real app, this would calculate from stored data
        # For the hackathon, we'll use mock data
        
        # Generate some realistic progress data
        reading_level = "Intermediate"
        exercises_completed = random.randint(35, 50)
        streak_days = st.session_state.streak_count if "streak_count" in st.session_state else 0
        reading_accuracy = random.uniform(85.0, 95.0)
        writing_accuracy = random.uniform(80.0, 90.0)
        
        # Calculate improvement percentage (mock data)
        reading_improvement = random.uniform(5.0, 15.0)
        writing_improvement = random.uniform(8.0, 20.0)
        
        summary = {
            "reading_level": reading_level,
            "exercises_completed": exercises_completed,
            "streak_days": streak_days,
            "reading_accuracy": reading_accuracy,
            "writing_accuracy": writing_accuracy,
            "reading_improvement": reading_improvement,
            "writing_improvement": writing_improvement,
            "focus_areas": [
                "Long word pronunciation",
                "Reading speed consistency",
                "Spelling words with silent letters",
                "Subject-verb agreement"
            ]
        }
        
        logger.info("Retrieved progress summary")
        return summary
    
    def get_reading_progress_data(self, days: int = 14) -> Dict[str, List]:
        """
        Get reading progress data for charts.
        
        Args:
            days (int): Number of days to include
            
        Returns:
            Dict: Data for chart visualization
        """
        # In a real app, this would fetch from the database
        # For the hackathon, we'll generate mock data
        
        today = datetime.now()
        dates = [(today - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(days, 0, -1)]
        
        # Generate accuracy data with an upward trend and some variation
        base_accuracy = 75
        accuracies = []
        for i in range(days):
            # Trend upward with some random variation
            accuracy = min(98, base_accuracy + (i * 1.5) + random.uniform(-3, 3))
            accuracies.append(round(accuracy, 1))
        
        # Generate words per minute data
        base_wpm = 80
        wpm_values = []
        for i in range(days):
            # Trend upward with some random variation
            wpm = max(60, min(150, base_wpm + (i * 0.8) + random.uniform(-5, 5)))
            wpm_values.append(round(wpm, 1))
        
        # Generate fluency scores
        base_fluency = 65
        fluency_values = []
        for i in range(days):
            # Trend upward with some random variation
            fluency = min(95, base_fluency + (i * 2) + random.uniform(-4, 4))
            fluency_values.append(round(fluency, 1))
        
        data = {
            "dates": dates,
            "accuracy": accuracies,
            "words_per_minute": wpm_values,
            "fluency_score": fluency_values
        }
        
        logger.info(f"Generated reading progress data for {days} days")
        return data
    
    def get_writing_progress_data(self, days: int = 14) -> Dict[str, List]:
        """
        Get writing progress data for charts.
        
        Args:
            days (int): Number of days to include
            
        Returns:
            Dict: Data for chart visualization
        """
        # In a real app, this would fetch from the database
        # For the hackathon, we'll generate mock data
        
        today = datetime.now()
        dates = [(today - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(days, 0, -1)]
        
        # Generate spelling accuracy data with an upward trend and some variation
        base_accuracy = 70
        accuracies = []
        for i in range(days):
            # Trend upward with some random variation
            accuracy = min(98, base_accuracy + (i * 1.8) + random.uniform(-4, 4))
            accuracies.append(round(accuracy, 1))
        
        # Generate grammar scores
        base_grammar = 65
        grammar_values = []
        for i in range(days):
            # Trend upward with some random variation
            grammar = min(95, base_grammar + (i * 1.5) + random.uniform(-3, 3))
            grammar_values.append(round(grammar, 1))
        
        # Generate vocabulary scores
        base_vocab = 75
        vocab_values = []
        for i in range(days):
            # Trend upward with some random variation
            vocab = min(98, base_vocab + (i * 1.2) + random.uniform(-3, 3))
            vocab_values.append(round(vocab, 1))
        
        data = {
            "dates": dates,
            "spelling_accuracy": accuracies,
            "grammar_score": grammar_values,
            "vocabulary_score": vocab_values
        }
        
        logger.info(f"Generated writing progress data for {days} days")
        return data
    
    def get_common_error_types(self) -> Dict[str, int]:
        """
        Get frequency of different error types.
        
        Returns:
            Dict: Error types and their counts
        """
        # In a real app, this would analyze stored error data
        # For the hackathon, we'll use mock data
        
        error_types = {
            "Silent Letters": random.randint(5, 10),
            "Double Consonants": random.randint(3, 8),
            "Vowel Combinations": random.randint(8, 15),
            "Homophones": random.randint(4, 9),
            "Suffixes": random.randint(2, 6)
        }
        
        logger.info("Retrieved common error types")
        return error_types
    
    def record_exercise_completion(self, exercise_type: str, score: float) -> bool:
        """
        Record the completion of an exercise.
        
        Args:
            exercise_type (str): Type of exercise (reading, writing, spelling, grammar)
            score (float): Score achieved (0-100)
            
        Returns:
            bool: True if successfully recorded
        """
        # In a real app, this would save to the database
        # For the hackathon, we'll just update session state
        
        # Update streak if this is the first exercise completed today
        if not st.session_state.get("exercise_completed_today", False):
            st.session_state.streak_count = st.session_state.get("streak_count", 0) + 1
            st.session_state.exercise_completed_today = True
            logger.info(f"Updated streak count to {st.session_state.streak_count}")
        
        logger.info(f"Recorded {exercise_type} exercise completion with score {score:.1f}")
        return True
    
    def get_achievements(self) -> List[Dict[str, Any]]:
        """
        Get list of earned achievements.
        
        Returns:
            List[Dict]: List of achievement records
        """
        # In a real app, this would be based on actual progress
        # For the hackathon, we'll base it on the streak count
        
        streak_count = st.session_state.get("streak_count", 0)
        
        achievements = []
        
        # Basic achievements based on streak
        if streak_count >= 1:
            achievements.append({
                "title": "Getting Started",
                "description": "Completed your first exercise",
                "icon": "🏆",
                "date_earned": (datetime.now() - timedelta(days=streak_count)).strftime("%b %d, %Y")
            })
        
        if streak_count >= 3:
            achievements.append({
                "title": "On Fire",
                "description": "Maintained a 3-day streak",
                "icon": "🔥",
                "date_earned": (datetime.now() - timedelta(days=streak_count-3)).strftime("%b %d, %Y")
            })
        
        if streak_count >= 7:
            achievements.append({
                "title": "Weekly Warrior",
                "description": "Practiced every day for a week",
                "icon": "⚔️",
                "date_earned": (datetime.now() - timedelta(days=streak_count-7)).strftime("%b %d, %Y")
            })
        
        # Add some mock skill achievements
        if random.random() < 0.7:
            achievements.append({
                "title": "Spelling Superstar",
                "description": "Achieved 90% accuracy in spelling exercises",
                "icon": "🌟",
                "date_earned": (datetime.now() - timedelta(days=random.randint(1, 7))).strftime("%b %d, %Y")
            })
        
        if random.random() < 0.6:
            achievements.append({
                "title": "Speed Reader",
                "description": "Read at over 100 words per minute",
                "icon": "⚡",
                "date_earned": (datetime.now() - timedelta(days=random.randint(1, 5))).strftime("%b %d, %Y")
            })
        
        logger.info(f"Retrieved {len(achievements)} achievements")
        return achievements 