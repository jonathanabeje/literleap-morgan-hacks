import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def render_progress_charts():
    """
    Render progress charts for the user to visualize their literacy improvement.
    """
    # Generate demo data for charts
    # In a real app, this would come from the database
    reading_data = generate_reading_data()
    writing_data = generate_writing_data()
    
    # Create tabs for different chart types
    tab1, tab2, tab3 = st.tabs(["Reading Progress", "Writing Progress", "Activity Heatmap"])
    
    with tab1:
        st.subheader("Reading Proficiency Growth")
        
        # Reading accuracy chart
        fig = px.line(
            reading_data, 
            x="date", 
            y="accuracy", 
            title="Reading Accuracy Over Time",
            labels={"date": "Date", "accuracy": "Accuracy (%)"},
            markers=True
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
        
        # Reading fluency chart
        col1, col2 = st.columns(2)
        
        with col1:
            fig = px.bar(
                reading_data,
                x="date",
                y="words_per_minute",
                title="Reading Speed (WPM)",
                labels={"date": "Date", "words_per_minute": "Words Per Minute"}
            )
            fig.update_layout(height=300)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            fig = px.line(
                reading_data,
                x="date",
                y="fluency_score",
                title="Reading Fluency Score",
                labels={"date": "Date", "fluency_score": "Fluency Score"},
                markers=True
            )
            fig.update_layout(height=300)
            st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.subheader("Writing Skill Development")
        
        # Writing accuracy chart
        fig = px.line(
            writing_data,
            x="date",
            y="spelling_accuracy",
            title="Spelling Accuracy Over Time",
            labels={"date": "Date", "spelling_accuracy": "Accuracy (%)"},
            markers=True
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
        
        # Common error types
        st.subheader("Common Error Types")
        error_data = pd.DataFrame({
            "error_type": ["Silent Letters", "Double Consonants", "Vowel Combinations", "Homophones", "Suffixes"],
            "count": [8, 5, 12, 7, 3]
        })
        
        fig = px.bar(
            error_data,
            x="error_type",
            y="count",
            title="Common Error Types",
            labels={"error_type": "Error Type", "count": "Frequency"}
        )
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.subheader("Activity Heatmap")
        
        # Generate activity data
        dates = pd.date_range(end=datetime.now().date(), periods=90, freq='D')
        activity = np.zeros(len(dates))
        
        # Simulate some activity patterns
        for i in range(len(dates)):
            # Higher probability of activity on weekdays
            if dates[i].weekday() < 5:
                activity[i] = np.random.choice([0, 1, 2, 3], p=[0.2, 0.3, 0.3, 0.2])
            else:
                activity[i] = np.random.choice([0, 1, 2, 3], p=[0.4, 0.3, 0.2, 0.1])
        
        # Create calendar heatmap
        activity_df = pd.DataFrame({
            'date': dates,
            'activity': activity,
            'weekday': dates.day_name(),
            'weeknum': dates.isocalendar().week
        })
        
        # Create a pivot table for the heatmap
        pivot_table = activity_df.pivot_table(
            index='weekday', 
            columns='weeknum', 
            values='activity',
            aggfunc='sum'
        )
        
        # Reorder days of week
        days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        pivot_table = pivot_table.reindex(days_order)
        
        # Create heatmap
        fig = px.imshow(
            pivot_table,
            labels=dict(x="Week", y="Day", color="Activities"),
            title="Your Activity Calendar (Last 90 Days)"
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
        
        st.info("💡 Tip: Regular practice is key to literacy improvement. Try to complete at least one exercise every day!")

def generate_reading_data():
    """
    Generate demo reading progress data.
    In a real app, this would come from the database.
    """
    # Generate dates for the past 14 days
    dates = [(datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(14, 0, -1)]
    
    # Generate accuracy data with an upward trend and some variation
    base_accuracy = 75
    accuracies = []
    for i in range(14):
        # Trend upward with some random variation
        accuracy = min(98, base_accuracy + (i * 1.5) + np.random.normal(0, 3))
        accuracies.append(accuracy)
    
    # Generate words per minute data
    base_wpm = 80
    wpm_values = []
    for i in range(14):
        # Trend upward with some random variation
        wpm = max(60, min(150, base_wpm + (i * 0.8) + np.random.normal(0, 5)))
        wpm_values.append(wpm)
    
    # Generate fluency scores
    base_fluency = 65
    fluency_values = []
    for i in range(14):
        # Trend upward with some random variation
        fluency = min(95, base_fluency + (i * 2) + np.random.normal(0, 4))
        fluency_values.append(fluency)
    
    # Create DataFrame
    return pd.DataFrame({
        'date': dates,
        'accuracy': accuracies,
        'words_per_minute': wpm_values,
        'fluency_score': fluency_values
    })

def generate_writing_data():
    """
    Generate demo writing progress data.
    In a real app, this would come from the database.
    """
    # Generate dates for the past 14 days
    dates = [(datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(14, 0, -1)]
    
    # Generate spelling accuracy data with an upward trend and some variation
    base_accuracy = 70
    accuracies = []
    for i in range(14):
        # Trend upward with some random variation
        accuracy = min(98, base_accuracy + (i * 1.8) + np.random.normal(0, 4))
        accuracies.append(accuracy)
    
    # Generate grammar scores
    base_grammar = 65
    grammar_values = []
    for i in range(14):
        # Trend upward with some random variation
        grammar = min(95, base_grammar + (i * 1.5) + np.random.normal(0, 3))
        grammar_values.append(grammar)
    
    # Generate vocabulary scores
    base_vocab = 75
    vocab_values = []
    for i in range(14):
        # Trend upward with some random variation
        vocab = min(98, base_vocab + (i * 1.2) + np.random.normal(0, 3))
        vocab_values.append(vocab)
    
    # Create DataFrame
    return pd.DataFrame({
        'date': dates,
        'spelling_accuracy': accuracies,
        'grammar_score': grammar_values,
        'vocabulary_score': vocab_values
    }) 