# LiterLeap: AI-Powered Literacy Intervention Platform

LiterLeap is an innovative web application designed to improve literacy skills for middle school students. The platform uses AI to provide personalized reading and writing exercises, speech recognition for pronunciation feedback, and progress tracking to keep students engaged and motivated.

## Features

- **Reading Practice**: Interactive reading exercises with text-to-speech and speech recognition technology
- **Personalized Passages**: Content tailored to student interests and reading level
- **Real-time Feedback**: Immediate analysis of reading accuracy and fluency
- **Progress Tracking**: Level-based progression system with achievements
- **Responsive Design**: Works across desktop and mobile devices

## Technology Stack

- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Backend**: Flask (Python)
- **Natural Language Processing**: Google Generative AI (with fallback mechanisms)
- **Speech Recognition**: Web Speech API
- **Data Visualization**: Plotly for progress charts

## Project Structure

The project consists of two main components:

1. `app.py` - The original Streamlit application (legacy)
2. `rebuild/` - The Flask-based application (current version)

## Setup and Installation

### Prerequisites
- Python 3.11+
- pip (Python package manager)

### Installation Steps

1. Clone the repository:
   ```
   git clone https://github.com/jonathanabeje/morgan-hacks.git
   cd morgan-hacks
   ```

2. Set up a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables (optional for enhanced features):
   - Create a `.env` file based on `.env.example`
   - Add your Google API key for AI-generated content

5. Run the application:
   ```
   cd rebuild
   ./run.sh  # On Windows: run.bat
   ```

6. Access the application:
   - Open your browser and navigate to `http://127.0.0.1:5000`

## Feature Highlights

### Reading Practice
- Multiple difficulty levels from beginner to expert
- Real-time speech recognition and analysis
- Detailed feedback on accuracy, fluency, and pronunciation

### User Progress
- Level-based progression system
- Achievement unlocks for milestones
- Visual progress tracking

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Created during Morgan State University Hackathon 2025
- Special thanks to all contributors and mentors 