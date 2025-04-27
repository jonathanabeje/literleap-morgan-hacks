import streamlit as st

def render_module_selector():
    """
    Render a component for selecting between different exercise modules.
    """
    st.subheader("Choose Your Exercise")
    
    col1, col2 = st.columns(2)
    
    with col1:
        reading_card = """
        <div style="padding: 20px; border-radius: 10px; border: 1px solid #4B3AC5; text-align: center;">
            <h3 style="color: #4B3AC5;">📖 Reading Practice</h3>
            <p>Improve your reading fluency, pronunciation, and comprehension with personalized passages.</p>
            <p><strong>Focus areas:</strong> Fluency, pronunciation, comprehension</p>
        </div>
        """
        st.markdown(reading_card, unsafe_allow_html=True)
        
        if st.button("Start Reading Exercise", key="start_reading", use_container_width=True):
            st.session_state.current_page = "reading"
            st.experimental_rerun()
    
    with col2:
        writing_card = """
        <div style="padding: 20px; border-radius: 10px; border: 1px solid #4B3AC5; text-align: center;">
            <h3 style="color: #4B3AC5;">✏️ Writing Practice</h3>
            <p>Enhance your spelling, grammar, and sentence structure with interactive exercises.</p>
            <p><strong>Focus areas:</strong> Spelling, grammar, sentence formation</p>
        </div>
        """
        st.markdown(writing_card, unsafe_allow_html=True)
        
        if st.button("Start Writing Exercise", key="start_writing", use_container_width=True):
            st.session_state.current_page = "writing"
            st.experimental_rerun()
    
    st.markdown("---")
    
    # Exercise difficulty selector
    st.subheader("Exercise Difficulty")
    
    difficulty = st.select_slider(
        "Select your preferred difficulty level:",
        options=["Beginner", "Elementary", "Intermediate", "Advanced", "Expert"],
        value="Intermediate"
    )
    
    # Map the difficulty to the reading level in session state
    difficulty_mapping = {
        "Beginner": "beginner",
        "Elementary": "elementary",
        "Intermediate": "intermediate",
        "Advanced": "advanced",
        "Expert": "expert"
    }
    
    st.session_state.reading_level = difficulty_mapping[difficulty]
    
    # Daily challenge card
    st.markdown("---")
    st.subheader("Daily Challenge")
    
    challenge_card = """
    <div style="padding: 20px; border-radius: 10px; border: 1px solid #FFA500; background-color: #FFF8E1; text-align: center;">
        <h3 style="color: #FFA500;">🏆 Today's Challenge</h3>
        <p>Complete both a reading and writing exercise to maintain your streak!</p>
        <div style="margin-top: 10px; height: 10px; background-color: #EEEEEE; border-radius: 5px;">
            <div style="width: 50%; height: 100%; background-color: #FFA500; border-radius: 5px;"></div>
        </div>
        <p>1/2 completed</p>
    </div>
    """
    
    st.markdown(challenge_card, unsafe_allow_html=True) 