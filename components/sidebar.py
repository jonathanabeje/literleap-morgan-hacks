import streamlit as st
import os
from pathlib import Path

def render_sidebar():
    """
    Render the sidebar navigation for the LiterLeap application.
    """
    with st.sidebar:
        # Logo and title
        st.markdown(
            """
            <div style='text-align: center'>
                <h1 style='color: #4B3AC5'>LiterLeap</h1>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
        st.markdown("---")
        
        # Navigation options
        nav_options = {
            "home": {"label": "Home", "icon": "🏠"},
            "profile": {"label": "Profile & Interests", "icon": "👤"},
            "reading": {"label": "Reading Practice", "icon": "📖"},
            "writing": {"label": "Writing Practice", "icon": "✏️"},
            "progress": {"label": "Progress Tracker", "icon": "📊"}
        }
        
        st.markdown("### Navigation")
        
        for page_id, page_info in nav_options.items():
            button_style = "primary" if st.session_state.current_page == page_id else "secondary"
            if st.button(
                f"{page_info['icon']} {page_info['label']}", 
                key=f"nav_{page_id}",
                use_container_width=True,
                type=button_style
            ):
                st.session_state.current_page = page_id
                st.experimental_rerun()
        
        st.markdown("---")
        
        # User streak information
        st.markdown(
            f"""
            <div style='text-align: center'>
                <h3>Daily Streak</h3>
                <h2>{st.session_state.streak_count} days 🔥</h2>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Tips
        with st.expander("Literacy Tips"):
            tips = [
                "Read aloud to improve pronunciation and fluency.",
                "Keep a journal to practice writing regularly.",
                "Try to learn 5 new words every week.",
                "Re-read passages you find challenging.",
                "Use context clues to guess the meaning of unfamiliar words."
            ]
            
            tip_index = st.session_state.streak_count % len(tips)
            st.info(f"💡 **Tip #{tip_index + 1}**: {tips[tip_index]}")
        
        # Version and credits at the bottom
        st.markdown("---")
        st.markdown(
            """
            <div style='text-align: center; color: #888; font-size: 0.8em;'>
                LiterLeap v1.0<br>
                Created at Morgan Hacks 2025
            </div>
            """,
            unsafe_allow_html=True
        ) 