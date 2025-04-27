import re
from typing import List, Dict, Tuple, Optional
from datetime import datetime
import random
from models.writing_intervention import (
    WritingProfile, WritingSession, WritingAnalysis,
    WritingStrength, Achievement, WritingPrompt,
    LearningCompanionInteraction, StoryAnimation
)

class WritingAnalysisService:
    def __init__(self):
        self.grammar_patterns = {
            'sentence_fragments': r'[A-Z][^.!?]*(?=[.!?])',
            'run_on_sentences': r'[^.!?]+(?:[,.][^.!?]+){3,}[.!?]',
            'passive_voice': r'\b(?:am|is|are|was|were|be|being|been)\s+\w+ed\b',
        }
        
    def analyze_text(self, content: str) -> WritingAnalysis:
        """Perform comprehensive analysis of writing content"""
        word_count = len(content.split())
        sentences = self._split_into_sentences(content)
        
        # Analyze different aspects
        grammar_score, grammar_issues = self._analyze_grammar(content)
        vocab_score, vocab_analysis = self._analyze_vocabulary(content)
        structure_score = self._analyze_structure(sentences)
        org_score = self._analyze_organization(sentences)
        
        return WritingAnalysis(
            session_id=0,  # This would be set by the caller
            grammar_score=grammar_score,
            vocabulary_score=vocab_score,
            structure_score=structure_score,
            organization_score=org_score,
            suggestions=self._generate_suggestions(grammar_issues, vocab_analysis),
            strengths_identified=self._identify_strengths(
                grammar_score, vocab_score, structure_score, org_score
            ),
            areas_for_improvement=self._identify_improvements(
                grammar_score, vocab_score, structure_score, org_score
            ),
            timestamp=datetime.now()
        )
    
    def _split_into_sentences(self, text: str) -> List[str]:
        """Split text into sentences"""
        return re.split(r'[.!?]+', text)
    
    def _analyze_grammar(self, text: str) -> Tuple[float, List[Dict]]:
        """Analyze grammar patterns and issues"""
        issues = []
        score = 80.0  # Base score
        
        for pattern_name, pattern in self.grammar_patterns.items():
            matches = re.finditer(pattern, text)
            for match in matches:
                issues.append({
                    'type': pattern_name,
                    'text': match.group(),
                    'position': match.span()
                })
                score -= 2  # Deduct points for each issue
        
        return max(0.0, min(100.0, score)), issues
    
    def _analyze_vocabulary(self, text: str) -> Tuple[float, Dict]:
        """Analyze vocabulary usage and diversity"""
        words = text.lower().split()
        unique_words = len(set(words))
        total_words = len(words)
        
        diversity_score = (unique_words / total_words * 100) if total_words > 0 else 0
        
        return diversity_score, {
            'unique_words': unique_words,
            'total_words': total_words,
            'diversity_ratio': diversity_score
        }
    
    def _analyze_structure(self, sentences: List[str]) -> float:
        """Analyze sentence structure variety"""
        lengths = [len(s.split()) for s in sentences if s.strip()]
        if not lengths:
            return 0.0
        
        avg_length = sum(lengths) / len(lengths)
        variety_score = len(set(lengths)) / len(lengths) * 100
        
        return min(100.0, (variety_score + (avg_length / 20 * 100)) / 2)
    
    def _analyze_organization(self, sentences: List[str]) -> float:
        """Analyze text organization"""
        if not sentences:
            return 0.0
        
        # Simple organization analysis based on paragraph breaks and transitions
        score = 80.0  # Base score
        
        # Check for clear beginning and ending
        if len(sentences) >= 3:
            score += 10.0
        
        # Check for transition words
        transition_words = ['however', 'therefore', 'furthermore', 'moreover']
        for word in transition_words:
            if any(word in s.lower() for s in sentences):
                score += 2.5
        
        return min(100.0, score)
    
    def _generate_suggestions(self, grammar_issues: List[Dict], vocab_analysis: Dict) -> List[Dict[str, str]]:
        """Generate improvement suggestions based on analysis"""
        suggestions = []
        
        # Grammar suggestions
        if grammar_issues:
            suggestions.append({
                'type': 'grammar',
                'text': 'Review your sentence structure for potential improvements'
            })
        
        # Vocabulary suggestions
        if vocab_analysis['diversity_ratio'] < 60:
            suggestions.append({
                'type': 'vocabulary',
                'text': 'Try using more varied vocabulary to enhance your writing'
            })
        
        return suggestions
    
    def _identify_strengths(self, grammar: float, vocab: float, structure: float, org: float) -> List[str]:
        """Identify areas of strength based on scores"""
        strengths = []
        if grammar >= 85:
            strengths.append('Strong grammar usage')
        if vocab >= 85:
            strengths.append('Rich vocabulary')
        if structure >= 85:
            strengths.append('Varied sentence structure')
        if org >= 85:
            strengths.append('Well-organized content')
        return strengths
    
    def _identify_improvements(self, grammar: float, vocab: float, structure: float, org: float) -> List[str]:
        """Identify areas needing improvement based on scores"""
        improvements = []
        if grammar < 70:
            improvements.append('Grammar accuracy')
        if vocab < 70:
            improvements.append('Vocabulary variety')
        if structure < 70:
            improvements.append('Sentence structure')
        if org < 70:
            improvements.append('Content organization')
        return improvements

class WritingPromptService:
    def __init__(self):
        self.prompts_by_level = self._initialize_prompts()
    
    def _initialize_prompts(self) -> Dict[int, List[WritingPrompt]]:
        """Initialize writing prompts for different levels"""
        prompts = {}
        for level in range(1, 6):
            prompts[level] = self._create_level_prompts(level)
        return prompts
    
    def _create_level_prompts(self, level: int) -> List[WritingPrompt]:
        """Create prompts for a specific level"""
        base_prompts = {
            1: [
                "Write about your favorite place",
                "Describe your best friend",
                "Tell a story about a happy memory"
            ],
            2: [
                "Compare two different seasons",
                "Explain how to make your favorite food",
                "Write about a time you helped someone"
            ],
            3: [
                "Discuss the pros and cons of social media",
                "Write about a challenge you overcame",
                "Explain why your favorite subject is important"
            ],
            4: [
                "Analyze the impact of technology on education",
                "Argue for or against year-round schooling",
                "Discuss how to solve a community problem"
            ],
            5: [
                "Evaluate the effectiveness of remote learning",
                "Analyze the role of artificial intelligence in society",
                "Propose solutions to environmental challenges"
            ]
        }
        
        return [
            WritingPrompt(
                id=i,
                text=prompt,
                level=level,
                categories=['general'],
                times_used=0,
                average_engagement=0.0,
                created_at=datetime.now()
            )
            for i, prompt in enumerate(base_prompts[level])
        ]
    
    def generate_prompt(self, level: int, interests: List[str]) -> WritingPrompt:
        """Generate a personalized writing prompt"""
        available_prompts = self.prompts_by_level.get(level, self.prompts_by_level[1])
        return random.choice(available_prompts)

class AchievementService:
    def __init__(self):
        self.achievements = self._initialize_achievements()
    
    def _initialize_achievements(self) -> List[Achievement]:
        """Initialize available achievements"""
        return [
            Achievement(
                id=1,
                title="Word Wizard",
                description="Master basic vocabulary and simple sentences",
                requirements={'words_written': 1000},
                unlocked=False,
                unlocked_date=None,
                progress=0
            ),
            Achievement(
                id=2,
                title="Sentence Sculptor",
                description="Create varied sentences with descriptive language",
                requirements={'avg_sentence_score': 80},
                unlocked=False,
                unlocked_date=None,
                progress=0
            ),
            Achievement(
                id=3,
                title="Paragraph Pro",
                description="Develop organized paragraphs with supporting details",
                requirements={'organization_score': 85},
                unlocked=False,
                unlocked_date=None,
                progress=0
            )
        ]
    
    def check_achievements(self, profile: WritingProfile, analysis: WritingAnalysis) -> List[Achievement]:
        """Check for newly unlocked achievements"""
        new_achievements = []
        
        for achievement in self.achievements:
            if not achievement.unlocked:
                if self._check_achievement_requirements(achievement, profile, analysis):
                    achievement.unlocked = True
                    achievement.unlocked_date = datetime.now()
                    new_achievements.append(achievement)
        
        return new_achievements
    
    def _check_achievement_requirements(self, achievement: Achievement, profile: WritingProfile, analysis: WritingAnalysis) -> bool:
        """Check if achievement requirements are met"""
        if 'words_written' in achievement.requirements:
            if profile.total_words_written >= achievement.requirements['words_written']:
                return True
        
        if 'avg_sentence_score' in achievement.requirements:
            if analysis.structure_score >= achievement.requirements['avg_sentence_score']:
                return True
        
        if 'organization_score' in achievement.requirements:
            if analysis.organization_score >= achievement.requirements['organization_score']:
                return True
        
        return False

class StoryAnimationService:
    def __init__(self):
        self.scene_templates = self._initialize_scene_templates()
    
    def _initialize_scene_templates(self) -> Dict[str, Dict]:
        """Initialize animation scene templates"""
        return {
            'character_intro': {
                'duration': 2000,
                'elements': ['character', 'background'],
                'animations': ['fade_in', 'slide_in']
            },
            'action': {
                'duration': 3000,
                'elements': ['character', 'props', 'effects'],
                'animations': ['move', 'scale', 'rotate']
            },
            'transition': {
                'duration': 1000,
                'elements': ['background'],
                'animations': ['fade', 'slide']
            }
        }
    
    def create_animation(self, text: str) -> StoryAnimation:
        """Create animation data for a story"""
        sentences = text.split('.')
        scenes = []
        
        for i, sentence in enumerate(sentences):
            if sentence.strip():
                scene_type = self._determine_scene_type(sentence)
                scenes.append(self._create_scene(scene_type, sentence, i))
        
        return StoryAnimation(
            session_id=0,  # This would be set by the caller
            scene_count=len(scenes),
            animation_data={'scenes': scenes},
            duration=sum(scene['duration'] for scene in scenes),
            user_interactions=0,
            created_at=datetime.now()
        )
    
    def _determine_scene_type(self, sentence: str) -> str:
        """Determine the type of scene based on sentence content"""
        if any(word in sentence.lower() for word in ['then', 'next', 'after']):
            return 'transition'
        if any(word in sentence.lower() for word in ['ran', 'jumped', 'moved']):
            return 'action'
        return 'character_intro'
    
    def _create_scene(self, scene_type: str, sentence: str, index: int) -> Dict:
        """Create a scene based on the template and content"""
        template = self.scene_templates[scene_type]
        return {
            'id': index,
            'type': scene_type,
            'content': sentence.strip(),
            'duration': template['duration'],
            'elements': template['elements'].copy(),
            'animations': template['animations'].copy()
        } 