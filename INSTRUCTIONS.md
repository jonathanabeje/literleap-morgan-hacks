# LiterLeap - Setup & Demo Instructions

## Overview

LiterLeap is an AI-powered literacy intervention platform designed to help middle school students improve their reading and writing skills through personalized exercises. The application leverages the Google Gemini API to generate custom content based on student interests and provide targeted feedback.

## Features Implemented

- **Interest-based content generation**: Personalized reading passages based on student interests
- **Reading analysis**: Simulated voice recording and analysis of reading performance
- **Writing exercises**: Spelling, grammar, and sentence structure exercises with feedback
- **Progress tracking**: Visualization of improvement over time
- **Engagement features**: Streaks, achievements, and gamification elements

## Prerequisites

- Python 3.9 or higher
- Git
- A Google Cloud API key for the Gemini API (optional for full functionality)

## Quick Start

1. **Clone the repository**
   ```
   git clone <repository-url>
   cd literleap
   ```

2. **Setup environment variables**
   Create a `.env` file by copying the example:
   ```
   cp .env.example .env
   ```
   
   Edit the `.env` file to add your API keys if available.

3. **Run the application**
   ```
   ./run.sh
   ```
   
   This script will:
   - Create a virtual environment
   - Install dependencies
   - Start the Streamlit application

   Alternatively, you can run these steps manually:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   streamlit run app.py
   ```

4. **Access the application**
   Open your browser and go to http://localhost:8501

## Demo Flow

For the best demo experience, follow these steps:

1. **Home Page**: Start by exploring the home page and streak features
2. **Profile**: Go to the profile page and select some interests
3. **Reading Practice**: Try the reading exercise with the simulated recording
4. **Writing Practice**: Complete a spelling exercise
5. **Progress Tracker**: View your progress over time

## Docker Deployment (Optional)

To run the application in a Docker container:

```
docker build -t literleap .
docker run -p 8501:8501 literleap
```

## Key Files

- `app.py`: Main application entry point
- `modules/`: Core functionality for each feature
- `components/`: UI components
- `services/`: External API integrations
- `assets/`: Static files

## Technologies Used

- Streamlit for the UI
- Google Gemini API for content generation
- Plotly for data visualization
- Python's standard libraries for simulations and processing

## Important Notes

- The voice recording functionality is simulated for the hackathon
- Sample data is provided for demonstration purposes when API keys are not available
- Progress data is generated with realistic trends but does not persist between sessions 