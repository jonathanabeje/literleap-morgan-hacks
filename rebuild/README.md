# LiterLeap - Flask Implementation

A robust implementation of the LiterLeap literacy intervention platform using Flask, modern JavaScript, and interactive charts.

## Features

- **Modern Web Interface**: Bootstrap 5-based responsive UI
- **Interactive Reading Exercises**: Real-time audio processing and feedback
- **Spelling Practice**: Character-by-character feedback with pronunciation guides
- **Interactive Progress Tracking**: Visual charts and heatmaps using Plotly
- **Interest-Based Content**: Personalized content generation

## Technology Stack

- **Backend**: Flask with Python 3.9+
- **Frontend**: HTML5, CSS3, JavaScript with Bootstrap 5
- **Charts**: Plotly.js for interactive visualizations
- **AI Integration**: Google Gemini API for content generation
- **Data Visualization**: Interactive charts and heatmaps

## Installation

1. Clone the repository
```bash
git clone <repository-url>
cd literleap/rebuild
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables
Create a `.env` file with the following variables:
```
GOOGLE_API_KEY=your_gemini_api_key
SECRET_KEY=your_secret_key
```

5. Run the application
```bash
flask run
```

6. Access the application at http://localhost:5000

## Directory Structure

```
rebuild/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── static/                 # Static assets
│   ├── css/                # Custom CSS
│   ├── js/                 # Custom JavaScript
│   └── images/             # Images and icons
└── templates/              # HTML templates
    ├── layout.html         # Base template
    ├── index.html          # Home page
    ├── profile.html        # User profile page
    ├── reading.html        # Reading exercise page
    ├── writing.html        # Writing exercise page
    └── progress.html       # Progress tracking page
```

## Key Improvements Over Streamlit Version

1. **Performance**: Faster page loads and interactive elements
2. **Modularity**: Clean separation of concerns with MVC pattern
3. **Interactivity**: Smoother user experience with client-side processing
4. **Animation**: Subtle animations enhance user engagement
5. **Responsive Design**: Optimized for mobile and desktop experiences
6. **Real-time Feedback**: Immediate user feedback with AJAX
7. **Browser Features**: Utilizes modern browser capabilities like SpeechSynthesis
8. **Customizability**: Easier to extend and customize the UI

## Future Enhancements

- User authentication system
- Offline mode with service workers
- Native audio processing
- Teacher/parent dashboard
- Content library expansion
- Mobile app with WebView 