import streamlit as st
import os
from dotenv import load_dotenv
import logging
from pathlib import Path

# Import components
from components.sidebar import render_sidebar
from components.progress_charts import render_progress_charts
from components.exercise_modules import render_module_selector

# Import modules
from modules.interest_profiling import InterestProfiler
from modules.reading_analysis import ReadingAnalyzer
from modules.writing_exercises import WritingExerciseGenerator
from modules.progress_tracking import ProgressTracker

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=getattr(logging, os.getenv("LOG_LEVEL", "INFO")),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Page configuration
st.set_page_config(
    page_title="LiterLeap - Literacy Intervention Platform",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Initialize session state if not already done
if "initialized" not in st.session_state:
    st.session_state.initialized = True
    st.session_state.current_page = "home"
    st.session_state.user = None
    st.session_state.interests = []
    st.session_state.reading_level = "intermediate"
    st.session_state.streak_count = 0
    st.session_state.exercise_completed_today = False
    logger.info("Session state initialized")

def main():
    """
    Main function to render the LiterLeap application.
    """
    # Hide the default Streamlit menu
    hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .stApp {
            background-color: #f9f8f7;
        }
        </style>
    """
    st.markdown(hide_menu_style, unsafe_allow_html=True)

    # Sidebar navigation
    render_sidebar()

    # Main content based on current page
    if st.session_state.current_page == "home":
        render_home_page()
    elif st.session_state.current_page == "profile":
        render_profile_page()
    elif st.session_state.current_page == "reading":
        render_reading_page()
    elif st.session_state.current_page == "writing":
        render_writing_page()
    elif st.session_state.current_page == "progress":
        render_progress_page()
    else:
        render_home_page()

def render_home_page():
    """
    Render the home page with welcome message and app description.
    """
    st.title("Welcome to LiterLeap! 📚")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ## Boost Your Reading & Writing Skills!
        
        LiterLeap is an AI-powered platform designed to help middle school students 
        improve their literacy skills through personalized exercises tailored to your interests.
        
        **How it works:**
        1. Tell us what topics you're interested in
        2. Complete daily reading and writing exercises
        3. Track your progress and watch your skills grow!
        
        Ready to get started? Click on the **Reading** or **Writing** tab in the sidebar!
        """)
        
        # Call to action buttons
        col_a, col_b, _ = st.columns([1, 1, 1])
        with col_a:
            if st.button("Start Reading Exercise", use_container_width=True):
                st.session_state.current_page = "reading"
                st.experimental_rerun()
        with col_b:
            if st.button("Start Writing Exercise", use_container_width=True):
                st.session_state.current_page = "writing"
                st.experimental_rerun()
    
    with col2:
        # Show streak and achievements
        st.markdown("### Your Progress")
        st.metric("Daily Streak", f"{st.session_state.streak_count} days")
        
        # Mock achievement display
        st.markdown("#### Recent Achievements")
        if st.session_state.streak_count > 0:
            st.success("🏆 Getting Started - Completed your first exercise")
        if st.session_state.streak_count >= 3:
            st.success("🔥 On Fire - 3 day streak")
        
        # Show a tip of the day
        st.info("💡 **Tip of the day:** Reading just 20 minutes a day exposes you to 1.8 million words per year!")

def render_profile_page():
    """
    Render the user profile page with interest selection.
    """
    st.title("Your Profile")
    
    # User profile information
    st.subheader("Personal Information")
    
    # Mock user data
    user_name = "Student"
    user_grade = "7th Grade"
    
    col1, col2 = st.columns(2)
    with col1:
        st.text_input("Name", value=user_name, disabled=True)
    with col2:
        st.text_input("Grade", value=user_grade, disabled=True)
    
    # Interest profiling
    st.subheader("Your Interests")
    st.markdown("Select topics you're interested in to receive personalized content:")
    
    interest_profiler = InterestProfiler()
    interests = interest_profiler.get_available_interests()
    
    # Create interest selection columns
    col1, col2, col3 = st.columns(3)
    columns = [col1, col2, col3]
    
    # Distribute interests across columns
    for i, interest in enumerate(interests):
        with columns[i % 3]:
            selected = st.checkbox(
                interest, 
                value=interest in st.session_state.interests
            )
            if selected and interest not in st.session_state.interests:
                st.session_state.interests.append(interest)
            elif not selected and interest in st.session_state.interests:
                st.session_state.interests.remove(interest)
    
    # Save button
    if st.button("Save Preferences"):
        st.success("Your preferences have been saved!")
        # Here we would normally update the database

def render_reading_page():
    """
    Render the reading exercise page.
    """
    st.title("Reading Practice")
    
    reading_analyzer = ReadingAnalyzer()
    
    # Generate content based on interests if needed
    if "current_reading_passage" not in st.session_state:
        st.session_state.current_reading_passage = reading_analyzer.generate_passage(
            interests=st.session_state.interests,
            reading_level=st.session_state.reading_level
        )
    
    # Display reading passage
    st.subheader("Read the passage below")
    with st.expander("Reading Passage", expanded=True):
        st.markdown(st.session_state.current_reading_passage["text"])
    
    # Audio recording for reading analysis
    st.subheader("Practice reading aloud")
    st.markdown("Click the button below to record yourself reading the passage above.")
    
    # Since we can't implement real audio recording in this example, we'll simulate it
    if st.button("Start Recording"):
        with st.spinner("Recording your reading..."):
            # Simulate recording delay
            import time
            time.sleep(2)
        st.success("Recording completed!")
        
        # Simulate analysis
        with st.spinner("Analyzing your reading..."):
            time.sleep(3)
        
        # Display feedback
        st.subheader("Your Reading Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Strengths")
            st.markdown("✅ Good pacing throughout most of the passage")
            st.markdown("✅ Clear pronunciation of most words")
            
        with col2:
            st.markdown("### Areas for Improvement")
            st.markdown("❗ Hesitation on longer words")
            st.markdown("❗ Some difficulty with the word 'particularly'")
        
        # Show the passage with highlighted areas for improvement
        st.subheader("Guided Feedback")
        modified_text = st.session_state.current_reading_passage["text"].replace(
            "particularly", 
            "<span style='background-color: #FFCCCB'>particularly</span>"
        )
        st.markdown(modified_text, unsafe_allow_html=True)
        
        # Pronunciation guide
        st.subheader("Pronunciation Guide")
        st.markdown("particularly → par·tic·u·lar·ly (par-TIK-yuh-ler-lee)")
        
        # Next steps
        st.success("Great job! Try practicing the highlighted words and record again.")
    
    # New passage button
    if st.button("Get New Passage"):
        st.session_state.pop("current_reading_passage", None)
        st.experimental_rerun()

def render_writing_page():
    """
    Render the writing exercise page.
    """
    st.title("Writing Practice")
    
    writing_generator = WritingExerciseGenerator()
    
    # Generate exercise if needed
    if "current_writing_exercise" not in st.session_state:
        st.session_state.current_writing_exercise = writing_generator.generate_exercise(
            exercise_type="spelling",
            difficulty=st.session_state.reading_level,
            interests=st.session_state.interests
        )
        st.session_state.user_answer = ""
        st.session_state.exercise_submitted = False
    
    # Exercise type selector
    exercise_type = st.selectbox(
        "Select exercise type:",
        ["Spelling", "Grammar", "Sentence Structure"],
        index=0
    )
    
    # Display exercise instructions
    st.subheader(st.session_state.current_writing_exercise["instruction"])
    
    # Play audio button (simulated)
    if st.button("🔊 Listen to Word"):
        st.audio("https://example.com/audio.mp3", format="audio/mp3")
        st.info(f"The word is: {st.session_state.current_writing_exercise['target_word']}")
    
    # User answer input
    user_answer = st.text_input(
        "Your answer:", 
        value=st.session_state.user_answer if "user_answer" in st.session_state else ""
    )
    st.session_state.user_answer = user_answer
    
    # Submit button
    if st.button("Submit Answer") or st.session_state.get("exercise_submitted", False):
        st.session_state.exercise_submitted = True
        
        correct_answer = st.session_state.current_writing_exercise["target_word"]
        
        if user_answer.lower() == correct_answer.lower():
            st.success("Correct! Great job! 🎉")
            # Update progress
            if not st.session_state.exercise_completed_today:
                st.session_state.streak_count += 1
                st.session_state.exercise_completed_today = True
        else:
            st.error(f"Not quite. The correct spelling is: {correct_answer}")
            # Show character-by-character comparison
            st.markdown("### Character Analysis")
            
            comparison = ""
            for i in range(max(len(user_answer), len(correct_answer))):
                if i < len(user_answer) and i < len(correct_answer):
                    if user_answer[i].lower() == correct_answer[i].lower():
                        comparison += f"<span style='color:green'>{correct_answer[i]}</span>"
                    else:
                        comparison += f"<span style='color:red'>{correct_answer[i]}</span>"
                elif i < len(correct_answer):
                    comparison += f"<span style='color:red'>{correct_answer[i]}</span>"
            
            st.markdown(f"Correct spelling: {comparison}", unsafe_allow_html=True)
            
            # Provide a hint or rule
            st.info("💡 Remember: 'i' before 'e', except after 'c'.")
        
        # Next exercise button
        if st.button("Next Exercise"):
            st.session_state.pop("current_writing_exercise", None)
            st.session_state.pop("exercise_submitted", None)
            st.experimental_rerun()

def render_progress_page():
    """
    Render the progress tracking page.
    """
    st.title("Your Progress")
    
    progress_tracker = ProgressTracker()
    
    # Summary metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Reading Level", "Intermediate")
    with col2:
        st.metric("Daily Streak", f"{st.session_state.streak_count} days")
    with col3:
        st.metric("Exercises Completed", "42")
    
    # Progress charts
    st.subheader("Progress Over Time")
    render_progress_charts()
    
    # Recent activities
    st.subheader("Recent Activities")
    activities = progress_tracker.get_recent_activities()
    
    for activity in activities:
        st.markdown(f"**{activity['date']}**: {activity['description']}")
    
    # Areas of improvement
    st.subheader("Focus Areas")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Reading")
        st.markdown("- Long word pronunciation")
        st.markdown("- Reading speed consistency")
    
    with col2:
        st.markdown("### Writing")
        st.markdown("- Spelling words with silent letters")
        st.markdown("- Subject-verb agreement")

if __name__ == "__main__":
    main() 