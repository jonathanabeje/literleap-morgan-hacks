from datetime import datetime
from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class WritingStrength:
    category: str
    level: int
    examples: List[str]
    last_updated: datetime

@dataclass
class Achievement:
    id: int
    title: str
    description: str
    requirements: Dict[str, int]
    unlocked: bool
    unlocked_date: Optional[datetime]
    progress: int

@dataclass
class WritingDraft:
    id: int
    title: str
    content: str
    created_at: datetime
    last_modified: datetime
    word_count: int
    analysis_scores: Dict[str, float]

@dataclass
class WritingProfile:
    user_id: int
    current_level: int
    total_words_written: int
    average_scores: Dict[str, float]
    strengths: List[WritingStrength]
    achievements: List[Achievement]
    interests: List[str]
    drafts: List[WritingDraft]
    last_activity: datetime

@dataclass
class WritingPrompt:
    id: int
    text: str
    level: int
    categories: List[str]
    times_used: int
    average_engagement: float
    created_at: datetime

@dataclass
class WritingSession:
    id: int
    user_id: int
    prompt_id: int
    content: str
    start_time: datetime
    end_time: Optional[datetime]
    word_count: int
    analysis_results: Dict[str, float]
    feedback_given: List[str]
    achievements_earned: List[int]

@dataclass
class LearningCompanionInteraction:
    id: int
    user_id: int
    session_id: int
    interaction_type: str
    message: str
    timestamp: datetime
    user_response: Optional[str]
    effectiveness_rating: Optional[int]

@dataclass
class WritingAnalysis:
    session_id: int
    grammar_score: float
    vocabulary_score: float
    structure_score: float
    organization_score: float
    suggestions: List[Dict[str, str]]
    strengths_identified: List[str]
    areas_for_improvement: List[str]
    timestamp: datetime

@dataclass
class StoryAnimation:
    session_id: int
    scene_count: int
    animation_data: Dict[str, any]
    duration: int
    user_interactions: int
    created_at: datetime

# Sample data generation functions
def create_sample_writing_profile(user_id: int) -> WritingProfile:
    """Create a sample writing profile for testing"""
    return WritingProfile(
        user_id=user_id,
        current_level=2,
        total_words_written=1500,
        average_scores={
            'grammar': 85.0,
            'vocabulary': 78.5,
            'structure': 82.0,
            'organization': 76.0
        },
        strengths=[
            WritingStrength(
                category='Vocabulary',
                level=3,
                examples=['diverse word choice', 'precise language'],
                last_updated=datetime.now()
            ),
            WritingStrength(
                category='Grammar',
                level=4,
                examples=['correct punctuation', 'proper tense usage'],
                last_updated=datetime.now()
            )
        ],
        achievements=[
            Achievement(
                id=1,
                title='Word Wizard',
                description='Master basic vocabulary',
                requirements={'words_written': 1000},
                unlocked=True,
                unlocked_date=datetime.now(),
                progress=100
            )
        ],
        interests=['science', 'technology', 'art'],
        drafts=[],
        last_activity=datetime.now()
    )

def create_sample_writing_session(user_id: int, prompt_id: int) -> WritingSession:
    """Create a sample writing session for testing"""
    return WritingSession(
        id=1,
        user_id=user_id,
        prompt_id=prompt_id,
        content="Sample writing content...",
        start_time=datetime.now(),
        end_time=None,
        word_count=0,
        analysis_results={},
        feedback_given=[],
        achievements_earned=[]
    )

def create_sample_writing_analysis(session_id: int) -> WritingAnalysis:
    """Create a sample writing analysis for testing"""
    return WritingAnalysis(
        session_id=session_id,
        grammar_score=85.0,
        vocabulary_score=78.5,
        structure_score=82.0,
        organization_score=76.0,
        suggestions=[
            {
                'type': 'grammar',
                'text': 'Consider using more varied sentence structures'
            }
        ],
        strengths_identified=[
            'Strong vocabulary usage',
            'Clear paragraph organization'
        ],
        areas_for_improvement=[
            'Sentence variety',
            'Transition words'
        ],
        timestamp=datetime.now()
    ) 