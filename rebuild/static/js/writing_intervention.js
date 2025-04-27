// Writing Intervention System Core Module

import StoryAnimator from './story-animator.js';

class WritingInterventionSystem {
    constructor() {
        this.currentLevel = 1;
        this.achievements = new AchievementSystem();
        this.animator = null; // Will be initialized after DOMContentLoaded
        this.companion = new LearningCompanion();
        this.topicGenerator = new PersonalizedTopicGenerator();
        this.assessmentEngine = new WritingAssessmentEngine();
    }

    async initialize() {
        await this.loadUserProfile();
        this.setupEventListeners();
        this.companion.initialize();
        this.updateDashboard();
        // Initialize SVG-based StoryAnimator
        this.animator = new StoryAnimator('story-animator-svg');
        await this.animator.loadSprites();
    }

    async loadUserProfile() {
        // Load user's writing profile, preferences, and progress
        this.userProfile = {
            level: 1,
            strengths: [],
            interests: [],
            achievements: [],
            writingHistory: []
        };
    }

    setupEventListeners() {
        document.getElementById('writing-submit').addEventListener('click', () => this.submitWriting());
        document.getElementById('topic-generate').addEventListener('click', () => this.generateNewTopic());
    }

    async submitWriting() {
        const writingContent = document.getElementById('writing-input').value.toLowerCase();
        const analysis = await this.assessmentEngine.analyzeWriting(writingContent);
        this.updateFeedback(analysis);
        // Hard-coded emoji/ASCII animation for certain prompts
        const animatorDiv = document.getElementById('story-animator-svg').parentElement;
        let output = '';
        if (writingContent.includes('dance')) {
            output = '💃🕺✨';
        } else if (writingContent.includes('run')) {
            output = '🏃💨';
        } else if (writingContent.includes('sad')) {
            output = '😢';
        } else if (writingContent.includes('happy')) {
            output = '😃✨';
        } else if (writingContent.includes('tree')) {
            output = '🌳';
        } else if (writingContent.includes('house')) {
            output = '🏠';
        } else if (writingContent.includes('ball')) {
            output = '🏀';
        } else if (writingContent.includes('book')) {
            output = '📚';
        } else {
            output = '✨'; // Default sparkle
        }
        animatorDiv.innerHTML = '<h4>Story Animator</h4><div style="font-size: 4rem; text-align: center;">' + output + '</div>';
        // Trigger celebration on every submit
        this.companion.celebrateAchievements([{}]);
        this.checkAchievements(analysis);
    }

    async generateNewTopic() {
        const topic = await this.topicGenerator.generateTopic(this.userProfile);
        document.getElementById('writing-prompt').textContent = topic;
    }

    updateFeedback(analysis) {
        // Update UI with writing analysis feedback
        const feedback = {
            grammar: analysis.grammarScore,
            vocabulary: analysis.vocabularyScore,
            structure: analysis.structureScore,
            organization: analysis.organizationScore
        };
        
        this.companion.provideFeedback(feedback);
    }

    checkAchievements(analysis) {
        const newAchievements = this.achievements.checkForNewAchievements(analysis);
        if (newAchievements.length > 0) {
            this.companion.celebrateAchievements(newAchievements);
        }
    }

    updateDashboard() {
        // Update writing progress visualization
        this.updateStrengthMap();
        this.updateProgressChart();
        this.updateRecentAchievements();
    }

    updateStrengthMap() {
        const strengthMap = document.getElementById('strength-map');
        // Sample strengths data (replace with real API call if available)
        const strengths = [
            { category: 'Vocabulary', icon: '📝', color: '#1976d2', examples: ['I used the word "astonishing" in my story.'] },
            { category: 'Grammar', icon: '🔤', color: '#43a047', examples: ['I always use capital letters at the start of sentences.'] },
            { category: 'Structure', icon: '📐', color: '#fbc02d', examples: ['My paragraph starts with a topic sentence.'] },
            { category: 'Creativity', icon: '🌟', color: '#8e24aa', examples: ['I described the dragon as "shimmering like a rainbow".'] }
        ];
        strengthMap.innerHTML = '';
        strengths.forEach(strength => {
            const item = document.createElement('div');
            item.className = 'strength-item';
            item.style.borderColor = strength.color;
            item.innerHTML = `
                <div class="strength-icon" style="color:${strength.color}">${strength.icon}</div>
                <div><span class="strength-star">★</span> <b>${strength.category}</b></div>
                <div class="strength-example">${strength.examples[0]}</div>
            `;
            strengthMap.appendChild(item);
        });
    }

    updateProgressChart() {
        const progressChart = document.getElementById('progress-chart');
        // Sample progress data (replace with real API call if available)
        const progress = [
            { label: 'Grammar', icon: '🔤', color: '#1976d2', percent: 82 },
            { label: 'Vocabulary', icon: '📝', color: '#43a047', percent: 76 },
            { label: 'Structure', icon: '📐', color: '#fbc02d', percent: 68 },
            { label: 'Organization', icon: '🗂️', color: '#8e24aa', percent: 74 }
        ];
        progressChart.innerHTML = '';
        progress.forEach(skill => {
            const barContainer = document.createElement('div');
            barContainer.style.marginBottom = '18px';
            barContainer.innerHTML = `
                <div style="display:flex;align-items:center;margin-bottom:4px;">
                    <span style="font-size:1.3rem;margin-right:8px;">${skill.icon}</span>
                    <span style="font-weight:600;color:${skill.color};">${skill.label}</span>
                    <span style="margin-left:auto;font-weight:600;">${skill.percent}%</span>
                </div>
                <div class="progress" style="height:18px;background:#e3e3e3;border-radius:9px;overflow:hidden;">
                    <div class="progress-bar" style="width:0%;background:linear-gradient(90deg,${skill.color} 60%,#ffd600 100%);transition:width 1s;"></div>
                </div>
            `;
            progressChart.appendChild(barContainer);
            // Animate the bar width
            setTimeout(() => {
                const bar = barContainer.querySelector('.progress-bar');
                if (bar) bar.style.width = skill.percent + '%';
            }, 100);
        });
    }

    updateRecentAchievements() {
        const achievementsContainer = document.getElementById('recent-achievements');
        // Update achievements display
    }
}

class AchievementSystem {
    constructor() {
        this.levels = {
            1: "Word Wizard",
            2: "Sentence Sculptor",
            3: "Paragraph Pro",
            4: "Purpose Pioneer",
            5: "Expression Expert"
        };
        this.badges = [];
    }

    checkForNewAchievements(analysis) {
        // Check writing analysis against achievement criteria
        return [];
    }

    awardBadge(badgeType) {
        // Award new badge and trigger celebration
    }
}

class StoryAnimator {
    constructor(canvasId) {
        this.canvas = document.getElementById(canvasId);
        this.ctx = this.canvas.getContext('2d');
        this.sprites = {};
    }

    async loadSprites() {
        // Load character and object sprites
    }

    async animateStory(content) {
        const sentences = content.split('.');
        for (const sentence of sentences) {
            await this.animateSentence(sentence);
        }
    }

    async animateSentence(sentence) {
        // Create animation for single sentence
    }

    reset() {
        // Reset the story animator
    }

    addScene(scene) {
        // Add a new scene to the story animator
    }

    async play() {
        // Play the story animation
    }
}

class LearningCompanion {
    constructor() {
        this.personality = "encouraging";
        this.avatar = null;
        this.recognition = null;
        this.isListening = false;
    }

    initialize() {
        this.loadAvatar();
        this.setupVoiceRecognition();
        // Set up button event
        const voiceBtn = document.getElementById('companion-voice');
        if (voiceBtn) {
            voiceBtn.addEventListener('click', () => this.toggleVoiceRecognition());
        }
    }

    setupVoiceRecognition() {
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        if (!SpeechRecognition) return;
        this.recognition = new SpeechRecognition();
        this.recognition.lang = 'en-US';
        this.recognition.continuous = false;
        this.recognition.interimResults = false;
        this.recognition.onstart = () => {
            this.isListening = true;
            const btn = document.getElementById('companion-voice');
            if (btn) btn.classList.add('listening');
            document.getElementById('companion-message').textContent = 'Listening...';
        };
        this.recognition.onend = () => {
            this.isListening = false;
            const btn = document.getElementById('companion-voice');
            if (btn) btn.classList.remove('listening');
        };
        this.recognition.onresult = (event) => {
            const transcript = event.results[0][0].transcript;
            document.getElementById('companion-message').textContent = `You said: "${transcript}"`;
            this.processVoiceCommand(transcript);
        };
    }

    toggleVoiceRecognition() {
        if (!this.recognition) return;
        if (this.isListening) {
            this.recognition.stop();
        } else {
            this.recognition.start();
        }
    }

    async processVoiceCommand(command) {
        // For demo: respond to simple commands
        const msg = document.getElementById('companion-message');
        if (!msg) return;
        if (command.toLowerCase().includes('help')) {
            msg.textContent = 'How can I help you with your writing?';
        } else if (command.toLowerCase().includes('idea')) {
            msg.textContent = "Here's a writing idea: Write about your favorite adventure!";
        } else if (command.toLowerCase().includes('encourage')) {
            msg.textContent = "You're doing great! Keep going!";
        } else {
            msg.textContent = `I heard: "${command}"`;
        }
    }

    provideFeedback(analysis) {
        // Generate personalized feedback
    }

    celebrateAchievements(achievements) {
        // Trigger celebration animations
        // Confetti
        const container = document.body;
        for (let i = 0; i < 30; i++) {
            const confetti = document.createElement('div');
            confetti.className = 'confetti-piece';
            confetti.style.left = Math.random() * 100 + 'vw';
            confetti.style.background = `hsl(${Math.random()*360},90%,60%)`;
            confetti.style.top = '-20px';
            confetti.style.zIndex = 9999;
            container.appendChild(confetti);
            setTimeout(() => confetti.remove(), 1300);
        }
        // Bounce the achievement cards
        const achievementItems = document.querySelectorAll('.achievement-item');
        achievementItems.forEach(item => item.classList.add('celebration'));
        setTimeout(() => achievementItems.forEach(item => item.classList.remove('celebration')), 800);
        // Animate the companion avatar
        const avatar = document.getElementById('companion-avatar');
        if (avatar) {
            avatar.classList.add('celebration');
            setTimeout(() => avatar.classList.remove('celebration'), 800);
        }
        // Show a message
        const msg = document.getElementById('companion-message');
        if (msg) msg.textContent = 'Congratulations! You earned a new achievement!';
    }

    loadAvatar() {
        // Load and initialize companion avatar
    }
}

class PersonalizedTopicGenerator {
    constructor() {
        this.topics = [];
        this.interestCategories = [];
    }

    async generateTopic(userProfile) {
        // Generate personalized writing prompt
        return "";
    }

    async updateTopicLibrary() {
        // Update available topics
    }

    assessInterests(responses) {
        // Analyze interest inventory responses
    }
}

class WritingAssessmentEngine {
    constructor() {
        this.grammarRules = [];
        this.vocabularyDatabase = {};
    }

    async analyzeWriting(content) {
        return {
            grammarScore: 0,
            vocabularyScore: 0,
            structureScore: 0,
            organizationScore: 0,
            suggestions: []
        };
    }

    assessGrammar(text) {
        // Analyze grammar patterns
    }

    assessVocabulary(text) {
        // Evaluate vocabulary usage
    }

    assessStructure(text) {
        // Analyze sentence structure
    }

    assessOrganization(text) {
        // Evaluate text organization
    }
}

// Initialize the system
const writingSystem = new WritingInterventionSystem();
document.addEventListener('DOMContentLoaded', () => writingSystem.initialize());

// Add a test button for celebration
if (typeof window !== 'undefined') {
    window.testCelebrate = function() {
        const companion = new LearningCompanion();
        companion.celebrateAchievements([{}]);
    };
} 