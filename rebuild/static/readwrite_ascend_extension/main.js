// ReadWrite Ascend Extension Main JS

document.addEventListener('DOMContentLoaded', function() {
    const navLinks = document.querySelectorAll('.rw-ascend-link');
    const main = document.getElementById('rw-ascend-main');

    // Section templates
    const sections = {
        assessment: getAssessmentSection,
        strengths: getStrengthMapSection,
        topics: getTopicsSection,
        achievements: getAchievementsSection,
        'story-animator': getStoryAnimatorSection,
        'parent-portal': getParentPortalSection
    };

    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            navLinks.forEach(l => l.classList.remove('active'));
            this.classList.add('active');
            const section = this.getAttribute('href').replace('#', '');
            if (typeof sections[section] === 'function') {
                main.innerHTML = sections[section]();
                if (section === 'assessment') initializeAssessmentFeature();
                if (section === 'strengths') initializeStrengthMapFeature();
                if (section === 'topics') initializeTopicsFeature();
                if (section === 'achievements') initializeAchievementsFeature();
                if (section === 'story-animator') initializeStoryAnimatorFeature();
                if (section === 'parent-portal') initializeParentPortalFeature();
            } else {
                main.innerHTML = sections[section];
            }
        });
    });

    // If user reloads on a hash, show the correct section
    if (window.location.hash) {
        const section = window.location.hash.replace('#', '');
        const link = document.querySelector(`.rw-ascend-link[href='#${section}']`);
        if (link) link.click();
    }

    // Add the interactive guide character to the page
    addGuideCharacter();
});

function getAssessmentSection() {
    return `
    <section class="rw-ascend-section" id="rw-assessment-section">
        <h2 class="text-2xl font-bold mb-4 flex items-center gap-2">✍️ Writing Skills Assessment</h2>
        <form id="rw-assessment-form" class="space-y-6">
            <div>
                <label for="rw-writing-input" class="block text-lg font-medium mb-2">Paste or write your paragraph below:</label>
                <textarea id="rw-writing-input" class="w-full p-4 rounded-lg border border-gray-200 focus:ring-2 focus:ring-primary-400 min-h-[120px]" placeholder="Start writing here..."></textarea>
            </div>
            <div class="flex justify-end">
                <button type="submit" class="rw-ascend-btn">Analyze Writing</button>
            </div>
        </form>
        <div id="rw-assessment-results" class="mt-8 hidden">
            <h3 class="text-xl font-semibold mb-4">Results</h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div>
                    <div class="mb-4">
                        <div class="flex items-center gap-2 mb-1"><span class="font-semibold">Grammar</span> <span id="rw-grammar-score" class="ml-auto font-bold">0%</span></div>
                        <div class="w-full h-3 bg-gray-100 rounded-full"><div id="rw-grammar-bar" class="h-3 bg-primary-500 rounded-full transition-all" style="width:0%"></div></div>
                    </div>
                    <div class="mb-4">
                        <div class="flex items-center gap-2 mb-1"><span class="font-semibold">Vocabulary</span> <span id="rw-vocab-score" class="ml-auto font-bold">0%</span></div>
                        <div class="w-full h-3 bg-gray-100 rounded-full"><div id="rw-vocab-bar" class="h-3 bg-secondary-500 rounded-full transition-all" style="width:0%"></div></div>
                    </div>
                    <div class="mb-4">
                        <div class="flex items-center gap-2 mb-1"><span class="font-semibold">Sentence Structure</span> <span id="rw-structure-score" class="ml-auto font-bold">0%</span></div>
                        <div class="w-full h-3 bg-gray-100 rounded-full"><div id="rw-structure-bar" class="h-3 bg-green-400 rounded-full transition-all" style="width:0%"></div></div>
                    </div>
                    <div class="mb-4">
                        <div class="flex items-center gap-2 mb-1"><span class="font-semibold">Organization</span> <span id="rw-organization-score" class="ml-auto font-bold">0%</span></div>
                        <div class="w-full h-3 bg-gray-100 rounded-full"><div id="rw-organization-bar" class="h-3 bg-yellow-400 rounded-full transition-all" style="width:0%"></div></div>
                    </div>
                </div>
                <div>
                    <div class="mb-4">
                        <h4 class="font-semibold mb-2">Feedback & Suggestions</h4>
                        <ul id="rw-feedback-list" class="list-disc pl-5 text-gray-700 space-y-2"></ul>
                    </div>
                </div>
            </div>
        </div>
    </section>
    `;
}

function initializeAssessmentFeature() {
    const form = document.getElementById('rw-assessment-form');
    const input = document.getElementById('rw-writing-input');
    const results = document.getElementById('rw-assessment-results');
    const grammarScore = document.getElementById('rw-grammar-score');
    const vocabScore = document.getElementById('rw-vocab-score');
    const structureScore = document.getElementById('rw-structure-score');
    const organizationScore = document.getElementById('rw-organization-score');
    const grammarBar = document.getElementById('rw-grammar-bar');
    const vocabBar = document.getElementById('rw-vocab-bar');
    const structureBar = document.getElementById('rw-structure-bar');
    const organizationBar = document.getElementById('rw-organization-bar');
    const feedbackList = document.getElementById('rw-feedback-list');

    if (!form) return;
    form.onsubmit = function(e) {
        e.preventDefault();
        const text = input.value.trim();
        if (!text) return;
        // Simulate analysis (replace with real NLP/AI later)
        const analysis = analyzeWriting(text);
        // Show results
        results.classList.remove('hidden');
        grammarScore.textContent = analysis.grammar + '%';
        vocabScore.textContent = analysis.vocab + '%';
        structureScore.textContent = analysis.structure + '%';
        organizationScore.textContent = analysis.organization + '%';
        grammarBar.style.width = analysis.grammar + '%';
        vocabBar.style.width = analysis.vocab + '%';
        structureBar.style.width = analysis.structure + '%';
        organizationBar.style.width = analysis.organization + '%';
        // Feedback
        feedbackList.innerHTML = '';
        analysis.feedback.forEach(item => {
            const li = document.createElement('li');
            li.textContent = item;
            feedbackList.appendChild(li);
        });
    };
}

function analyzeWriting(text) {
    // Simple mock analysis for demo; replace with real logic/AI
    const wordCount = text.split(/\s+/).length;
    const sentenceCount = text.split(/[.!?]+/).filter(s => s.trim()).length;
    const avgWordLength = text.replace(/\s+/g, '').length / wordCount;
    // Scores
    let grammar = Math.min(100, 60 + wordCount / 2);
    let vocab = Math.min(100, 50 + avgWordLength * 10);
    let structure = Math.min(100, 40 + sentenceCount * 5);
    let organization = Math.min(100, 50 + (sentenceCount > 1 ? 20 : 0));
    // Feedback
    const feedback = [];
    if (grammar < 80) feedback.push('Review grammar rules and check for common errors.');
    if (vocab < 80) feedback.push('Try to use more varied and descriptive vocabulary.');
    if (structure < 80) feedback.push('Work on sentence variety and complexity.');
    if (organization < 80) feedback.push('Focus on logical flow and clear structure.');
    if (grammar >= 80 && vocab >= 80 && structure >= 80 && organization >= 80) feedback.push('Excellent writing! Keep it up!');
    return { grammar: Math.round(grammar), vocab: Math.round(vocab), structure: Math.round(structure), organization: Math.round(organization), feedback };
}

function getStrengthMapSection() {
    // Mock data for strengths
    const strengths = [
        {
            category: 'Word Choice',
            icon: '📝',
            stars: 4,
            example: '"The shimmering lake reflected the golden sunrise."'
        },
        {
            category: 'Sentence Structure',
            icon: '🔗',
            stars: 3,
            example: '"Although it was raining, she decided to go for a run, enjoying the cool drops on her face."'
        },
        {
            category: 'Creativity',
            icon: '🌟',
            stars: 5,
            example: '"The dragon wore sunglasses and danced at the summer festival."'
        }
    ];
    // Mock data for grade-level benchmarking
    const gradeLevel = 4;
    const benchmark = 3.5; // e.g., average for grade 4 is 3.5
    const userLevel = 4.2; // user's estimated level
    const badge = userLevel >= benchmark ? '🏅 Above Grade Level' : '🎯 On Track';
    const feedback = userLevel >= benchmark
        ? 'You are writing above grade level! Keep challenging yourself with more advanced prompts.'
        : 'You are on track for your grade. Focus on expanding your vocabulary and sentence variety.';
    return `
    <section class="rw-ascend-section" id="rw-strength-map-section">
        <h2 class="text-2xl font-bold mb-4 flex items-center gap-2">💪 Writing Strength Map</h2>
        <div class="mb-8">
            <div class="bg-gradient-to-r from-primary-500 to-secondary-500 rounded-xl p-6 flex flex-col md:flex-row items-center justify-between shadow mb-4">
                <div class="flex-1">
                    <div class="text-lg font-semibold text-white mb-2">Grade-Level Benchmarking</div>
                    <div class="flex items-center gap-4 mb-2">
                        <span class="text-2xl font-bold text-white">${badge}</span>
                        <span class="bg-white text-primary-600 rounded-full px-3 py-1 text-sm font-semibold ml-2">Your Level: ${userLevel.toFixed(1)}</span>
                        <span class="bg-white text-secondary-600 rounded-full px-3 py-1 text-sm font-semibold ml-2">Grade ${gradeLevel} Benchmark: ${benchmark.toFixed(1)}</span>
                    </div>
                    <div class="w-full h-3 bg-white bg-opacity-30 rounded-full mb-2">
                        <div style="width: ${(userLevel/5)*100}%" class="h-3 bg-green-400 rounded-full transition-all"></div>
                    </div>
                    <div class="text-white text-sm">${feedback}</div>
                </div>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            ${strengths.map(str => `
                <div class="bg-white rounded-xl shadow p-6 flex flex-col items-center">
                    <div class="text-4xl mb-2">${str.icon}</div>
                    <div class="font-semibold text-lg mb-1">${str.category}</div>
                    <div class="flex mb-2">
                        ${'<span class="text-yellow-400 text-xl">★</span>'.repeat(str.stars)}
                        ${'<span class="text-gray-300 text-xl">★</span>'.repeat(5-str.stars)}
                    </div>
                    <div class="text-gray-600 text-center text-sm italic">${str.example}</div>
                </div>
            `).join('')}
        </div>
        <div class="mt-8 text-center text-gray-500 text-sm">These strengths are based on your recent writing. Keep practicing to unlock more stars!</div>
    </section>
    `;
}

function initializeStrengthMapFeature() {
    // In the future, fetch real data and update the UI
}

function getTopicsSection() {
    return `
    <section class="rw-ascend-section" id="rw-topics-section">
        <div class="flex flex-col md:flex-row md:items-center md:justify-between mb-6 gap-4">
            <h2 class="text-2xl font-bold flex items-center gap-2">📚 Personalized Topics</h2>
            <button class="rw-ascend-btn" id="rwOpenInventoryBtn">Update Interests</button>
        </div>
        <div class="rw-prompt-generator">
            <div class="flex flex-col md:flex-row md:items-center gap-4 w-full">
                <select id="rwPromptCategory" class="rw-topic-filter">
                    <option value="all">All Categories</option>
                    <option value="sports">Sports</option>
                    <option value="adventure">Adventure</option>
                    <option value="animals">Animals</option>
                    <option value="fantasy">Fantasy</option>
                    <option value="science">Science</option>
                </select>
                <select id="rwPromptDifficulty" class="rw-topic-filter">
                    <option value="beginner">Beginner</option>
                    <option value="intermediate">Intermediate</option>
                    <option value="advanced">Advanced</option>
                </select>
                <button class="rw-prompt-btn" id="rwGeneratePromptBtn">Generate Personalized Prompt</button>
            </div>
            <div class="rw-prompt-output" id="rwPromptOutput"></div>
        </div>
        <div class="rw-topic-filters">
            <button class="rw-topic-filter active" data-category="all">All</button>
            <button class="rw-topic-filter" data-category="sports">Sports</button>
            <button class="rw-topic-filter" data-category="adventure">Adventure</button>
            <button class="rw-topic-filter" data-category="animals">Animals</button>
            <button class="rw-topic-filter" data-category="fantasy">Fantasy</button>
            <button class="rw-topic-filter" data-category="science">Science</button>
        </div>
        <input type="text" id="rwTopicSearch" class="input-field mb-4" placeholder="Search topics...">
        <div class="rw-topic-cards" id="rwTopicCards"></div>
        <div id="rwInventoryModal" class="rw-inventory-modal" style="display:none;">
            <div class="rw-inventory-content">
                <button class="rw-inventory-close" id="rwCloseInventoryBtn">&times;</button>
                <h2>Tell us about your interests!</h2>
                <label for="rwInterestSubjects">Favorite Subjects</label>
                <input id="rwInterestSubjects" placeholder="e.g. Space, Soccer, Dinosaurs">
                <label for="rwInterestHobbies">Hobbies</label>
                <input id="rwInterestHobbies" placeholder="e.g. Drawing, Reading, Coding">
                <label for="rwInterestCharacters">Favorite Characters</label>
                <input id="rwInterestCharacters" placeholder="e.g. Harry Potter, Pikachu">
                <button class="rw-ascend-btn" id="rwSaveInventoryBtn">Save Interests</button>
            </div>
        </div>
    </section>
    `;
}

function initializeTopicsFeature() {
    // Mock topic data
    const topics = [
        { title: 'The Big Game', category: 'sports', difficulty: 'beginner', desc: 'Write about your favorite sport and why you love it.' },
        { title: 'Lost in the Jungle', category: 'adventure', difficulty: 'intermediate', desc: 'Describe an adventure where you get lost and find your way home.' },
        { title: 'My Pet Dragon', category: 'fantasy', difficulty: 'beginner', desc: 'Imagine you have a pet dragon. What is it like?' },
        { title: 'The Science Fair', category: 'science', difficulty: 'intermediate', desc: 'Write about a cool science experiment you would like to try.' },
        { title: 'Animal Rescue', category: 'animals', difficulty: 'advanced', desc: 'Tell a story about rescuing an animal in need.' },
        { title: 'Space Explorer', category: 'science', difficulty: 'advanced', desc: 'Imagine you are an astronaut exploring a new planet.' },
        { title: 'The Magical Forest', category: 'fantasy', difficulty: 'intermediate', desc: 'Describe a walk through a magical forest.' },
        { title: 'Soccer Star', category: 'sports', difficulty: 'advanced', desc: 'Write about training to become a professional soccer player.' },
        { title: 'The Secret Club', category: 'adventure', difficulty: 'beginner', desc: 'Invent a secret club and describe its rules and members.' },
        { title: 'My Favorite Animal', category: 'animals', difficulty: 'beginner', desc: 'Describe your favorite animal and what makes it special.' }
    ];
    let filteredCategory = 'all';
    let searchQuery = '';

    // Render topic cards
    function renderTopics() {
        const cards = document.getElementById('rwTopicCards');
        let filtered = topics.filter(t =>
            (filteredCategory === 'all' || t.category === filteredCategory) &&
            (searchQuery === '' || t.title.toLowerCase().includes(searchQuery) || t.desc.toLowerCase().includes(searchQuery))
        );
        cards.innerHTML = filtered.map(t => `
            <div class="rw-topic-card">
                <div class="rw-topic-title">${t.title}</div>
                <div class="rw-topic-category">${capitalize(t.category)}</div>
                <div class="rw-topic-difficulty">${capitalize(t.difficulty)}</div>
                <div class="rw-topic-desc">${t.desc}</div>
                <button class="rw-topic-btn">Start Writing</button>
            </div>
        `).join('') || '<div class="text-gray-400">No topics found.</div>';
    }

    // Filter buttons
    document.querySelectorAll('.rw-topic-filter').forEach(btn => {
        btn.addEventListener('click', function() {
            document.querySelectorAll('.rw-topic-filter').forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            filteredCategory = this.dataset.category;
            renderTopics();
        });
    });

    // Search
    document.getElementById('rwTopicSearch').addEventListener('input', function() {
        searchQuery = this.value.toLowerCase();
        renderTopics();
    });

    // Prompt generator
    document.getElementById('rwGeneratePromptBtn').addEventListener('click', function() {
        const cat = document.getElementById('rwPromptCategory').value;
        const diff = document.getElementById('rwPromptDifficulty').value;
        const interests = getSavedInterests();
        const prompt = generatePersonalizedPrompt(cat, diff, interests);
        document.getElementById('rwPromptOutput').textContent = prompt;
    });

    // Interest inventory modal
    document.getElementById('rwOpenInventoryBtn').addEventListener('click', function() {
        document.getElementById('rwInventoryModal').style.display = 'flex';
        loadInventoryFields();
    });
    document.getElementById('rwCloseInventoryBtn').addEventListener('click', function() {
        document.getElementById('rwInventoryModal').style.display = 'none';
    });
    document.getElementById('rwSaveInventoryBtn').addEventListener('click', function() {
        const subjects = document.getElementById('rwInterestSubjects').value;
        const hobbies = document.getElementById('rwInterestHobbies').value;
        const characters = document.getElementById('rwInterestCharacters').value;
        localStorage.setItem('rwInterests', JSON.stringify({ subjects, hobbies, characters }));
        document.getElementById('rwInventoryModal').style.display = 'none';
    });

    function loadInventoryFields() {
        const interests = getSavedInterests();
        document.getElementById('rwInterestSubjects').value = interests.subjects || '';
        document.getElementById('rwInterestHobbies').value = interests.hobbies || '';
        document.getElementById('rwInterestCharacters').value = interests.characters || '';
    }
    function getSavedInterests() {
        return JSON.parse(localStorage.getItem('rwInterests') || '{}');
    }
    function generatePersonalizedPrompt(category, difficulty, interests) {
        // Simple mock logic for demo
        let base = 'Write a ' + difficulty + ' story';
        if (category !== 'all') base += ' about ' + category;
        if (interests.subjects) base += ' that includes ' + interests.subjects.split(',')[0].trim();
        if (interests.hobbies) base += ' and your hobby: ' + interests.hobbies.split(',')[0].trim();
        if (interests.characters) base += '. Try to mention ' + interests.characters.split(',')[0].trim() + ' in your story!';
        return base + '.';
    }
    function capitalize(str) { return str.charAt(0).toUpperCase() + str.slice(1); }
    renderTopics();
}

function getAchievementsSection() {
    return `
    <section class="rw-ascend-section" id="rw-achievements-section">
        <h2 class="text-2xl font-bold flex items-center gap-2 mb-6">🏆 Achievements & Progress</h2>
        <div id="rwMilestoneCelebration"></div>
        <div class="rw-achievement-dashboard">
            <!-- Core Levels -->
        </div>
        <div class="rw-badge-grid" id="rwBadgeGrid"></div>
    </section>
    `;
}

function initializeAchievementsFeature() {
    // Mock data for levels and badges
    const levels = [
        { title: 'Word Wizard', badge: '🔤', progress: 100, completed: true, status: 'Level Complete!' },
        { title: 'Sentence Sculptor', badge: '✍️', progress: 80, completed: false, status: 'Almost there!' },
        { title: 'Paragraph Pro', badge: '📄', progress: 60, completed: false, status: 'Keep going!' },
        { title: 'Purpose Pioneer', badge: '🎯', progress: 30, completed: false, status: 'Getting started!' },
        { title: 'Expression Expert', badge: '🌟', progress: 0, completed: false, status: 'Locked' }
    ];
    const badges = [
        { title: 'Vocabulary Explorer', icon: '📚', desc: 'Mastered 50 new words', unlocked: true },
        { title: 'Grammar Guardian', icon: '🛡️', desc: 'Scored 90%+ on grammar', unlocked: true },
        { title: 'Creative Spark', icon: '💡', desc: 'Wrote a story with a twist', unlocked: false },
        { title: 'Interest Star', icon: '⭐', desc: 'Excelled in a favorite topic', unlocked: true },
        { title: 'Milestone Maker', icon: '🏅', desc: 'Completed 5 assessments', unlocked: false }
    ];
    // Render levels
    const dash = document.querySelector('.rw-achievement-dashboard');
    dash.innerHTML = levels.map(lvl => `
        <div class="rw-level-card${lvl.completed ? ' completed' : ''}">
            <div class="rw-level-badge">${lvl.badge}</div>
            <div class="rw-level-title">${lvl.title}</div>
            <div class="rw-level-progress"><div class="rw-level-progress-bar" style="width:${lvl.progress}%"></div></div>
            <div class="rw-level-status">${lvl.status}</div>
        </div>
    `).join('');
    // Render badges
    const badgeGrid = document.getElementById('rwBadgeGrid');
    badgeGrid.innerHTML = badges.map(b => `
        <div class="rw-badge${b.unlocked ? ' unlocked' : ' locked'}">
            <div class="rw-badge-icon">${b.icon}</div>
            <div class="rw-badge-title">${b.title}</div>
            <div class="rw-badge-desc">${b.desc}</div>
        </div>
    `).join('');
    // Milestone celebration
    if (levels[0].completed && !localStorage.getItem('rwMilestoneCelebrated')) {
        showMilestoneCelebration('Congratulations! You completed your first level: Word Wizard! 🎉');
        localStorage.setItem('rwMilestoneCelebrated', '1');
    }
}

function showMilestoneCelebration(message) {
    const el = document.getElementById('rwMilestoneCelebration');
    el.innerHTML = `<div class="rw-milestone-celebration">${message}</div>`;
    setTimeout(() => { el.innerHTML = ''; }, 4000);
}

function addGuideCharacter() {
    // Only add once
    if (document.querySelector('.rw-guide-container')) return;
    const guide = document.createElement('div');
    guide.className = 'rw-guide-container';
    guide.innerHTML = `
        <div class="rw-guide-speech" id="rwGuideSpeech">Hi! I'm Ollie the Owl, your writing buddy. Ready to soar to new heights? 🦉</div>
        <div class="rw-guide-avatar" id="rwGuideAvatar" title="Click me for tips!">🦉</div>
    `;
    document.body.appendChild(guide);

    // Tips/messages for the guide
    const tips = [
        "Remember: Great writers revise! Don't be afraid to edit your work.",
        "Try using a new word today. The more words you know, the more you can say!",
        "Break big ideas into smaller sentences for clarity.",
        "Celebrate your progress—every word counts!",
        "Ask me for help anytime. I'm here to guide you! 🦉"
    ];
    let tipIndex = 0;
    const speech = document.getElementById('rwGuideSpeech');
    const avatar = document.getElementById('rwGuideAvatar');
    avatar.addEventListener('click', function() {
        tipIndex = (tipIndex + 1) % tips.length;
        speech.textContent = tips[tipIndex];
    });
}

function getStoryAnimatorSection() {
    return `
    <section class="rw-ascend-section" id="rw-story-animator-section">
        <h2 class="text-2xl font-bold flex items-center gap-2 mb-6">🎬 Instant Story Animator</h2>
        <div class="rw-story-animator-card">
            <div class="flex items-center gap-4 mb-2">
                <div class="rw-story-scene-emoji">🦉</div>
                <div class="font-semibold text-lg">Ollie the Owl will animate your story as you write!</div>
            </div>
            <textarea id="rwStoryInput" class="rw-story-input" placeholder="Write your story here, one sentence at a time..."></textarea>
            <div class="rw-story-btns">
                <button class="rw-story-btn" id="rwAnimateBtn">Animate Story</button>
                <button class="rw-story-btn" id="rwClearStoryBtn">Clear Story</button>
            </div>
            <div class="rw-story-scenes" id="rwStoryScenes"></div>
        </div>
    </section>
    `;
}

function initializeStoryAnimatorFeature() {
    const input = document.getElementById('rwStoryInput');
    const animateBtn = document.getElementById('rwAnimateBtn');
    const clearBtn = document.getElementById('rwClearStoryBtn');
    const scenes = document.getElementById('rwStoryScenes');

    function renderScenes() {
        scenes.innerHTML = '';
        const text = input.value.trim();
        if (!text) return;
        const sentences = text.match(/[^.!?]+[.!?]+/g) || [text];
        sentences.forEach(sentence => {
            const emoji = pickEmojiForSentence(sentence);
            const scene = document.createElement('div');
            scene.className = 'rw-story-scene';
            scene.innerHTML = `<span class="rw-story-scene-emoji">${emoji}</span> <span>${sentence.trim()}</span>`;
            scenes.appendChild(scene);
        });
    }
    function pickEmojiForSentence(sentence) {
        // Simple keyword-based emoji mapping (mock logic)
        const s = sentence.toLowerCase();
        if (s.includes('dragon')) return '🐉';
        if (s.includes('forest')) return '🌳';
        if (s.includes('space') || s.includes('planet')) return '🪐';
        if (s.includes('soccer') || s.includes('game')) return '⚽';
        if (s.includes('science') || s.includes('experiment')) return '🔬';
        if (s.includes('animal') || s.includes('pet')) return '🐾';
        if (s.includes('rain')) return '🌧️';
        if (s.includes('sun')) return '☀️';
        if (s.includes('magic') || s.includes('magical')) return '✨';
        if (s.includes('club')) return '🏫';
        if (s.includes('run')) return '🏃';
        if (s.includes('owl')) return '🦉';
        return '🎬';
    }
    animateBtn.addEventListener('click', renderScenes);
    input.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            renderScenes();
        }
    });
    clearBtn.addEventListener('click', function() {
        input.value = '';
        scenes.innerHTML = '';
    });
}

function getParentPortalSection() {
    return `
    <section class="rw-ascend-section" id="rw-parent-portal-section">
        <h2 class="text-2xl font-bold flex items-center gap-2 mb-6">👨‍👩‍👧‍👦 Parent Portal</h2>
        <div class="rw-child-switcher">
            <div class="rw-child-avatar">A</div>
            <span class="rw-child-name">Alex</span>
            <button class="rw-parent-tab active">Alex</button>
            <button class="rw-parent-tab">Jamie</button>
            <button class="rw-parent-tab">+ Add Child</button>
        </div>
        <div class="rw-parent-dashboard">
            <div class="rw-parent-card">
                <div class="rw-parent-card-title">Writing Progress</div>
                <div class="rw-parent-card-value">Level 2</div>
                <div class="rw-level-progress"><div class="rw-level-progress-bar" style="width:60%"></div></div>
                <div class="rw-level-status">Sentence Sculptor</div>
            </div>
            <div class="rw-parent-card">
                <div class="rw-parent-card-title">Weekly Highlight</div>
                <div class="rw-parent-card-value">"The dragon wore sunglasses and danced at the festival."</div>
                <div class="rw-level-status">Best Writing Piece</div>
            </div>
            <div class="rw-parent-card">
                <div class="rw-parent-card-title">Effort Tracker</div>
                <div class="rw-progress-chart">
                    <div class="rw-progress-bar" style="height: 80%"></div>
                    <div class="rw-progress-bar" style="height: 60%"></div>
                    <div class="rw-progress-bar" style="height: 100%"></div>
                    <div class="rw-progress-bar" style="height: 40%"></div>
                    <div class="rw-progress-bar" style="height: 70%"></div>
                </div>
                <div class="rw-progress-bar-label">Mon Tue Wed Thu Fri</div>
            </div>
            <div class="rw-parent-card">
                <div class="rw-parent-card-title">Next Skills Preview</div>
                <ul class="rw-support-list">
                    <li>Paragraph Organization</li>
                    <li>Descriptive Language</li>
                    <li>Persuasive Writing</li>
                </ul>
            </div>
        </div>
        <div class="rw-activity-feed">
            <div class="rw-activity-item">
                <span class="rw-activity-icon">✍️</span>
                <div class="rw-activity-content">
                    <div class="rw-activity-title">Completed: Narrative Writing</div>
                    <div class="rw-activity-time">2 hours ago</div>
                </div>
            </div>
            <div class="rw-activity-item">
                <span class="rw-activity-icon">🏆</span>
                <div class="rw-activity-content">
                    <div class="rw-activity-title">Unlocked: Grammar Guardian Badge</div>
                    <div class="rw-activity-time">Yesterday</div>
                </div>
            </div>
            <div class="rw-activity-item">
                <span class="rw-activity-icon">📚</span>
                <div class="rw-activity-content">
                    <div class="rw-activity-title">Feedback: "Great use of descriptive words!"</div>
                    <div class="rw-activity-time">2 days ago</div>
                </div>
            </div>
        </div>
        <div class="rw-support-tools">
            <div class="rw-support-title">At-Home Support Tools</div>
            <ul class="rw-support-list">
                <li>5-Minute Activity: Write a silly sentence using three new words.</li>
                <li>Conversation Card: Ask your child what their favorite writing topic is this week.</li>
                <li>Strength Spotlight: Praise your child for using dialogue in their story.</li>
                <li>Writing Roadblock: If your child is stuck, suggest drawing a picture of their story first.</li>
            </ul>
        </div>
    </section>
    `;
}

function initializeParentPortalFeature() {
    // In the future, add logic for switching children, loading real data, etc.
} 