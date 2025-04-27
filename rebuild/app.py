import os
import json
import time
import random
from datetime import datetime, timedelta
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from dotenv import load_dotenv
import logging
import re

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Try to import and configure Google Gemini API, but make it optional
try:
    import google.generativeai as genai
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    logger.info("Google Gemini API configured successfully")
    GEMINI_AVAILABLE = True
except (ImportError, Exception) as e:
    logger.warning(f"Google Gemini API not available: {e}")
    model = None
    GEMINI_AVAILABLE = False

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "literleap-secret-key")

# Sample data
sample_passages = {
    "easy": [
        {
            "title": "The Lost Ball",
            "text": "Tom had a red ball. He liked to play with it every day. One day, he threw the ball too high. It went over the fence. Tom looked for his ball. He could not find it. Then, his friend Sam came. Sam had found the ball! Tom was happy. He said, 'Thank you, Sam!'"
        },
        {
            "title": "My Dog Friend",
            "text": "My dog likes to run in the yard. He chases after balls and sticks. When he gets tired, he lies under the big tree. He is a good friend to me."
        }
    ],
    "medium": [
        {
            "title": "The Ancient Map",
            "text": "Carlos found the old map tucked between the pages of a dusty book in his grandfather's attic. The yellowed paper crinkled as he carefully unfolded it, revealing what appeared to be directions to a location in the nearby woods. Curious about where the map might lead, Carlos decided to follow it the next day. The directions were challenging to follow, with landmarks that had changed over the years. After several hours of searching, Carlos discovered a small clearing with the remains of what looked like an old cabin. Among the ruins, he found a metal box containing photographs and letters from nearly a century ago. Carlos realized he had uncovered a forgotten piece of local history that told the story of the people who had lived in these woods long before his time."
        },
        {
            "title": "The Lost Library",
            "text": "The ancient library contained thousands of forgotten books. Dust covered the shelves and the smell of old paper filled the air. The librarian moved quietly between the towering bookcases, carefully organizing the precious volumes."
        }
    ],
    "hard": [
        {
            "title": "The Quantum Conundrum",
            "text": "Quantum mechanics describes the peculiar behavior of subatomic particles that seemingly defy classical physics. The principle of wave-particle duality suggests that electrons and photons simultaneously possess characteristics of both waves and particles, challenging our intuitive understanding of physical reality."
        },
        {
            "title": "Technology's Societal Impact",
            "text": "The intricate relationship between technological innovation and societal transformation has been extensively documented throughout history. Paradigm shifts in communication methodologies invariably precipitate fundamental changes in how communities organize themselves politically and economically."
        }
    ]
}

AVAILABLE_INTERESTS = [
    "Basketball", "Soccer", "Baseball", "Football", "Swimming",
    "Space", "Animals", "Dinosaurs", "Chemistry", "Physics",
    "Movies", "Music", "Video Games", "Comics", "Animation",
    "Drawing", "Painting", "Crafts", "Photography", "Theater",
    "Ancient Civilizations", "World Wars", "American History", "Famous People",
    "Inventions", "Exploration", "Medieval Times", "Archaeology"
]

# Helper functions
def generate_passage(interests, reading_level="medium"):
    """Generate a reading passage based on interests and level"""
    # Default to sample passages if no model is available or if interests not provided
    if not interests or not GEMINI_AVAILABLE or not model:
        # Normalize difficulty level
        if reading_level not in sample_passages:
            reading_level = "medium"
        
        # Pick a random passage from the appropriate difficulty
        passages = sample_passages[reading_level]
        selected_passage = random.choice(passages)
        return {
            "title": selected_passage["title"],
            "passage": selected_passage["text"]
        }
    
    try:
        interest_text = ", ".join(interests[:3])
        
        prompt = f"""
        Create an engaging reading passage for a {reading_level} level student.
        The passage should be about the following interests: {interest_text}
        Please format the output as a JSON object with two fields:
        - title: A catchy title for the passage
        - passage: The text of the passage
        """
        
        response = model.generate_content(prompt)
        
        try:
            response_text = response.text
            if "```json" in response_text:
                json_str = response_text.split("```json")[1].split("```")[0].strip()
            elif "```" in response_text:
                json_str = response_text.split("```")[1].strip()
            else:
                json_str = response_text
            
            passage_data = json.loads(json_str)
            return passage_data
        except Exception as e:
            logger.error(f"Error parsing response: {e}")
            # Fallback to sample passages
            passages = sample_passages[reading_level]
            selected_passage = random.choice(passages)
            return {
                "title": selected_passage["title"],
                "passage": selected_passage["text"]
            }
            
    except Exception as e:
        logger.error(f"Error generating passage: {e}")
        # Fallback to sample passages
        passages = sample_passages[reading_level]
        selected_passage = random.choice(passages)
        return {
            "title": selected_passage["title"],
            "passage": selected_passage["text"]
        }

def generate_spelling_exercise(difficulty="intermediate"):
    """Generate a spelling exercise"""
    spelling_exercises = {
        "beginner": {
            "instruction": "Listen to the word and type it correctly.",
            "target_word": "play",
            "hint": "What you do with toys or games"
        },
        "intermediate": {
            "instruction": "Listen to the word and type it correctly.",
            "target_word": "particularly",
            "hint": "Especially or specifically"
        }
    }
    
    return spelling_exercises.get(difficulty, spelling_exercises["intermediate"])

def generate_progress_data(days=14):
    """Generate mock progress data for charts"""
    dates = [(datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(days, 0, -1)]
    
    # Generate reading data with upward trend
    base_accuracy = 75
    accuracies = []
    wpm_values = []
    fluency_values = []
    
    for i in range(days):
        accuracy = min(98, base_accuracy + (i * 1.5) + random.uniform(-3, 3))
        wpm = max(60, min(150, 80 + (i * 0.8) + random.uniform(-5, 5)))
        fluency = min(95, 65 + (i * 2) + random.uniform(-4, 4))
        
        accuracies.append(round(accuracy, 1))
        wpm_values.append(round(wpm, 1))
        fluency_values.append(round(fluency, 1))
    
    # Generate writing data
    spelling_accuracy = []
    grammar_scores = []
    
    for i in range(days):
        spell_acc = min(98, 70 + (i * 1.8) + random.uniform(-4, 4))
        grammar = min(95, 65 + (i * 1.5) + random.uniform(-3, 3))
        
        spelling_accuracy.append(round(spell_acc, 1))
        grammar_scores.append(round(grammar, 1))
    
    return {
        "dates": dates,
        "reading": {
            "accuracy": accuracies,
            "words_per_minute": wpm_values,
            "fluency_score": fluency_values
        },
        "writing": {
            "spelling_accuracy": spelling_accuracy,
            "grammar_score": grammar_scores
        }
    }

def get_recent_activities(days=7):
    """Get mock recent activities"""
    activities = []
    today = datetime.now()
    
    for i in range(days):
        date = today - timedelta(days=i)
        date_str = date.strftime("%b %d, %Y")
        
        activity_types = [
            "Completed reading exercise with {} accuracy",
            "Mastered {} challenging spelling words",
            "Improved reading speed to {} words per minute",
            "Completed grammar exercise with {} accuracy"
        ]
        
        if i < 4:
            activity = activity_types[i].format(random.randint(85, 95) if i != 2 else random.randint(100, 130))
        else:
            activity_type = random.choice(["reading", "writing", "spelling", "grammar"])
            score = random.randint(75, 95)
            activity = f"Practiced {activity_type} skills ({score}% accuracy)"
        
        activities.append({
            "date": date_str,
            "description": activity
        })
    
    return activities

# Routes
@app.route('/')
def home():
    """Home page route"""
    streak_count = session.get('streak_count', 0)
    interests = session.get('interests', [])
    return render_template('index.html', streak_count=streak_count, interests=interests)

@app.route('/profile')
def profile():
    """User profile page"""
    interests = session.get('interests', [])
    return render_template('profile.html', 
                          interests=interests,
                          available_interests=AVAILABLE_INTERESTS)

@app.route('/milestones')
def milestones():
    # This route handles the milestones and achievements page
    return render_template('milestones.html')

@app.route('/save_interests', methods=['POST'])
def save_interests():
    """Save user interests"""
    data = request.get_json()
    interests = data.get('interests', [])
    session['interests'] = interests
    return jsonify({"success": True})

@app.route('/reading')
def reading():
    """Reading practice page"""
    try:
        interests = session.get('interests', [])
        reading_level = request.args.get('level', 'medium')
        # Check if a specific passage was requested
        requested_passage = request.args.get('passage', None)
        
        logger.info(f"Rendering reading template with interests={interests}, level={reading_level}, passage={requested_passage}")
        
        return render_template('reading.html', 
                              interests=interests,
                              reading_level=reading_level,
                              requested_passage=requested_passage)
    except Exception as e:
        logger.error(f"Error rendering reading template: {e}")
        return f"Error rendering template: {str(e)}", 500

@app.route('/get_passage', methods=['GET'])
def get_passage():
    """API endpoint to get a reading passage"""
    interests = session.get('interests', [])
    reading_level = request.args.get('level', 'medium')
    requested_title = request.args.get('title', None)
    
    # If a specific title is requested, try to find it in sample passages
    if requested_title:
        for level, passages in sample_passages.items():
            for passage in passages:
                if passage["title"] == requested_title:
                    return jsonify({
                        "title": passage["title"],
                        "passage": passage["text"]
                    })
    
    # If no title found or no title requested, generate a passage as usual
    passage = generate_passage(interests, reading_level)
    return jsonify(passage)

@app.route('/analyze_reading', methods=['POST'])
def analyze_reading():
    """API endpoint to analyze reading with speech recognition"""
    data = request.get_json()
    
    # Get the data from the request
    spoken_text = data.get('spoken_text', '')
    original_text = data.get('original_text', '')
    client_comparison = data.get('comparison', None)
    
    # If client already did the comparison, use that data
    if client_comparison:
        accuracy = client_comparison.get('accuracy', 85.0)
        words_per_minute = client_comparison.get('words_per_minute', 110.0)
        fluency_score = client_comparison.get('fluency_score', 80.0)
        difficult_words = client_comparison.get('difficult_words', [])
    else:
        # Fallback if client comparison isn't provided
        word_count = len(original_text.split())
        accuracy = random.uniform(80.0, 98.0)
        words_per_minute = random.uniform(85.0, 140.0)
        fluency_score = random.uniform(70.0, 95.0)
        
        # Simulate finding difficult words
        difficult_words = []
        words = original_text.split()
        for word in words:
            if len(word) > 8 and random.random() < 0.3:
                difficult_words.append(word)
    
    # Generate appropriate feedback based on accuracy and fluency
    strengths = []
    areas_for_improvement = []
    
    # Strengths feedback
    if accuracy > 90:
        strengths.append("Excellent word accuracy")
    elif accuracy > 80:
        strengths.append("Good word recognition for most of the passage")
    
    if words_per_minute > 120:
        strengths.append("Strong reading speed")
    elif words_per_minute > 100:
        strengths.append("Good reading pace")
    
    if fluency_score > 85:
        strengths.append("Smooth reading flow")
    elif fluency_score > 75:
        strengths.append("Consistent reading rhythm")
    
    # Make sure we have at least two strengths
    if len(strengths) < 2:
        strengths.append("Clear pronunciation of most common words")
    
    # Areas for improvement
    if accuracy < 85:
        areas_for_improvement.append("Focus on pronouncing words more clearly")
    
    if words_per_minute < 90:
        areas_for_improvement.append("Work on increasing your reading speed")
    elif words_per_minute > 140:
        areas_for_improvement.append("Consider slowing down slightly for better clarity")
    
    if fluency_score < 80:
        areas_for_improvement.append("Practice smoother transitions between sentences")
    
    # Add specific difficult words feedback if available
    if difficult_words:
        word_list = ", ".join(difficult_words[:3])
        areas_for_improvement.append(f"Practice pronouncing longer words like: {word_list}")
    
    # Create pronunciation guides for difficult words
    pronunciation_guides = {}
    for word in difficult_words:
        # Create simple phonetic breakdown
        syllables = []
        current = ""
        
        for i, char in enumerate(word):
            current += char
            if char.lower() in 'aeiou' and i < len(word) - 1 and word[i+1].lower() not in 'aeiou':
                syllables.append(current)
                current = ""
        
        if current:
            syllables.append(current)
        
        # Join with dots and create guide
        syllable_text = "·".join(syllables)
        pronunciation_guides[word] = f"{syllable_text} ({word.upper()})"
    
    # Create highlighted passage
    highlighted_passage = original_text
    if difficult_words:
        # Safely create a regex pattern with all difficult words
        # Will highlight all occurrences of difficult words in the passage
        safe_words = [re.escape(word) for word in difficult_words]
        pattern = r'\b(' + '|'.join(safe_words) + r')\b'
        highlighted_passage = re.sub(pattern, r'<span class="highlighted-word">\1</span>', original_text, flags=re.IGNORECASE)
    
    # If not completed an exercise today, update streak
    if not session.get('exercise_completed_today', False):
        session['streak_count'] = session.get('streak_count', 0) + 1
        session['exercise_completed_today'] = True
    
    return jsonify({
        "accuracy": round(accuracy, 1),
        "words_per_minute": round(words_per_minute, 1),
        "fluency_score": round(fluency_score, 1),
        "strengths": strengths,
        "areas_for_improvement": areas_for_improvement,
        "difficult_words": difficult_words,
        "pronunciation_guides": pronunciation_guides,
        "highlighted_passage": highlighted_passage
    })

@app.route('/writing')
def writing():
    """Writing practice page"""
    # Provide an initial word exercise
    difficulty = request.args.get('difficulty', 'intermediate')
    exercise_type = request.args.get('type', 'word')
    
    if exercise_type == 'word':
        exercise = {
            "instruction": "Listen to the word and type it correctly.",
            "target_word": "particularly",
            "hint": "Especially or specifically"
        }
    else:
        exercise = {
            "instruction": "Listen to the phrase and type it exactly as you hear it.",
            "target_text": "The ancient map showed a hidden treasure location.",
            "hint": "About a valuable discovery"
        }
        
    return render_template('writing.html', exercise=exercise)

@app.route('/check_spelling', methods=['POST'])
def check_spelling():
    """API endpoint to check spelling and provide feedback for words and phrases"""
    data = request.get_json()
    user_answer = data.get('answer', '').strip().lower()
    target_text = data.get('target_text', '').strip().lower()
    exercise_type = data.get('exercise_type', 'word')
    
    # Check if answer is correct
    is_correct = user_answer == target_text
    
    # Compare characters for detailed feedback
    comparison = []
    
    if not user_answer:
        comparison = [{'char': c, 'status': 'missing'} for c in target_text]
    else:
        # Use dynamic programming approach for more sophisticated comparison
        # This is a simplified version of the Levenshtein distance algorithm
        
        i, j = 0, 0
        while i < len(target_text) or j < len(user_answer):
            if i < len(target_text) and j < len(user_answer) and target_text[i] == user_answer[j]:
                # Characters match
                comparison.append({'char': target_text[i], 'status': 'correct'})
                i += 1
                j += 1
            elif j < len(user_answer) and (i >= len(target_text) or i < len(target_text) and j < len(user_answer) and target_text[i] != user_answer[j]):
                # Extra character in user answer
                comparison.append({'user_char': user_answer[j], 'status': 'extra'})
                j += 1
            elif i < len(target_text):
                # Missing character in user answer
                comparison.append({'char': target_text[i], 'status': 'missing'})
                i += 1
    
    # Generate appropriate feedback
    feedback = ""
    if not is_correct:
        if exercise_type == 'word':
            # Word-specific feedback
            if len(user_answer) < len(target_text):
                feedback = "You're missing some letters. Try sounding out the word completely."
            elif len(user_answer) > len(target_text):
                feedback = "You've added extra letters. Listen to the word again carefully."
            elif any(c in target_text for c in 'aeiou') and not any(c == user_answer[i] for i, c in enumerate(target_text) if c in 'aeiou' and i < len(user_answer)):
                feedback = "Check the vowels in your spelling. Pay attention to 'a', 'e', 'i', 'o', and 'u'."
            elif any(c+c in target_text for c in 'bcdfghjklmnpqrstvwxyz'):
                feedback = "This word contains double consonants. Listen carefully for repeated sounds."
            elif 'ie' in target_text or 'ei' in target_text:
                feedback = "Remember the rule: 'i' before 'e', except after 'c', or when sounded like 'a'."
            else:
                feedback = "Try sounding out the word syllable by syllable."
        else:
            # Phrase-specific feedback
            words_target = target_text.split()
            words_user = user_answer.split()
            
            if len(words_user) < len(words_target):
                feedback = f"Your answer is missing some words. The phrase has {len(words_target)} words but you typed {len(words_user)}."
            elif len(words_user) > len(words_target):
                feedback = f"You added extra words. The phrase has {len(words_target)} words but you typed {len(words_user)}."
            else:
                # Find the first mismatched word
                for i, (target_word, user_word) in enumerate(zip(words_target, words_user)):
                    if target_word != user_word:
                        feedback = f"Check your spelling of '{user_word}'. The correct word is '{target_word}'."
                        break
                
                if not feedback:
                    feedback = "Check your punctuation and capitalization."
    
    # If not completed an exercise today, update streak
    if is_correct and not session.get('exercise_completed_today', False):
        session['streak_count'] = session.get('streak_count', 0) + 1
        session['exercise_completed_today'] = True
    
    return jsonify({
        "is_correct": is_correct,
        "comparison": comparison,
        "feedback": feedback
    })

@app.route('/progress')
def progress():
    """Progress tracking page"""
    streak_count = session.get('streak_count', 0)
    progress_data = generate_progress_data()
    activities = get_recent_activities()
    
    return render_template('progress.html', 
                          streak_count=streak_count,
                          progress_data=progress_data,
                          activities=activities)

@app.route('/get_progress_data')
def get_progress_data():
    """API endpoint to get progress data for charts"""
    return jsonify(generate_progress_data())

# Writing Intervention System Routes
@app.route('/api/writing/analyze', methods=['POST'])
def analyze_writing():
    """Analyze submitted writing and return detailed feedback"""
    content = request.json.get('content', '')
    
    # Perform writing analysis
    analysis = {
        'grammar': {
            'score': random.randint(60, 100),
            'suggestions': []
        },
        'vocabulary': {
            'score': random.randint(60, 100),
            'suggestions': []
        },
        'structure': {
            'score': random.randint(60, 100),
            'suggestions': []
        },
        'organization': {
            'score': random.randint(60, 100),
            'suggestions': []
        }
    }
    
    return jsonify(analysis)

@app.route('/api/writing/generate-topic', methods=['POST'])
def generate_topic():
    """Generate a personalized writing topic based on user interests"""
    interests = request.json.get('interests', [])
    level = request.json.get('level', 1)
    
    # Sample topics for different levels
    topics = {
        1: [
            "Write about your favorite hobby",
            "Describe your perfect day",
            "Tell a story about a pet or animal"
        ],
        2: [
            "Compare and contrast two different activities you enjoy",
            "Explain how to do something you're good at",
            "Write about a time you learned something new"
        ],
        3: [
            "Analyze the pros and cons of a recent decision",
            "Describe a challenge you overcame",
            "Write about a goal you want to achieve"
        ],
        4: [
            "Argue for or against a position on a topic you care about",
            "Analyze the impact of technology on your life",
            "Write a detailed plan for achieving a personal goal"
        ],
        5: [
            "Create a complex narrative with multiple perspectives",
            "Analyze a significant issue in your community",
            "Write a persuasive essay on a controversial topic"
        ]
    }
    
    # Select a topic based on level
    available_topics = topics.get(level, topics[1])
    selected_topic = random.choice(available_topics)
    
    return jsonify({'topic': selected_topic})

@app.route('/api/writing/save-draft', methods=['POST'])
def save_draft():
    """Save a writing draft"""
    content = request.json.get('content', '')
    title = request.json.get('title', f'Draft - {datetime.now().strftime("%Y-%m-%d %H:%M")}')
    
    # In a real implementation, this would save to a database
    draft = {
        'id': random.randint(1000, 9999),
        'title': title,
        'content': content,
        'timestamp': datetime.now().isoformat()
    }
    
    return jsonify(draft)

@app.route('/api/writing/achievements', methods=['GET'])
def get_achievements():
    """Get user's writing achievements"""
    # Sample achievements data
    achievements = [
        {
            'id': 1,
            'title': 'Word Wizard',
            'description': 'Master basic vocabulary and simple sentences',
            'progress': 75,
            'unlocked': True
        },
        {
            'id': 2,
            'title': 'Sentence Sculptor',
            'description': 'Create varied sentences with descriptive language',
            'progress': 45,
            'unlocked': False
        },
        {
            'id': 3,
            'title': 'Paragraph Pro',
            'description': 'Develop organized paragraphs with supporting details',
            'progress': 20,
            'unlocked': False
        }
    ]
    
    return jsonify(achievements)

@app.route('/api/writing/strength-map', methods=['GET'])
def get_strength_map():
    """Get user's writing strengths"""
    # Sample strength map data
    strengths = [
        {
            'category': 'Vocabulary',
            'level': 3,
            'examples': ['diverse word choice', 'precise language']
        },
        {
            'category': 'Grammar',
            'level': 4,
            'examples': ['correct punctuation', 'proper tense usage']
        },
        {
            'category': 'Structure',
            'level': 2,
            'examples': ['clear paragraphs', 'topic sentences']
        },
        {
            'category': 'Creativity',
            'level': 3,
            'examples': ['unique ideas', 'engaging descriptions']
        }
    ]
    
    return jsonify(strengths)

@app.route('/api/writing/companion-message', methods=['POST'])
def get_companion_message():
    """Get a response from the learning companion"""
    message_type = request.json.get('type', 'feedback')
    analysis = request.json.get('analysis', {})
    
    # Sample companion messages
    messages = {
        'feedback': [
            "Great job! Your writing is showing real improvement.",
            "I notice you're using more complex sentences. Keep it up!",
            "Your vocabulary choices are getting stronger.",
            "Let's work on organizing your ideas more clearly."
        ],
        'encouragement': [
            "You're making excellent progress!",
            "Keep writing - you're developing your own style.",
            "I'm here to help you become an even better writer.",
            "Every word you write helps you grow as an author."
        ],
        'suggestion': [
            "Try adding more descriptive details to your writing.",
            "Consider varying your sentence structure more.",
            "Think about your audience as you write.",
            "Remember to support your main ideas with examples."
        ]
    }
    
    selected_message = random.choice(messages.get(message_type, messages['feedback']))
    
    return jsonify({'message': selected_message})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 