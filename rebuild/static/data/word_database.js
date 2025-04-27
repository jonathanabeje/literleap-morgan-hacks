// Word database for spelling exercises
const wordDatabase = {
  // Beginner level (grades 1-2)
  beginner: {
    animals: [
      { word: "cat", hint: "A small furry pet that meows" },
      { word: "dog", hint: "A loyal pet that barks" },
      { word: "fish", hint: "It swims in water" },
      { word: "bird", hint: "It has wings and can fly" },
      { word: "frog", hint: "A green animal that jumps and lives near water" }
    ],
    food: [
      { word: "milk", hint: "White drink that comes from cows" },
      { word: "cake", hint: "Sweet food you eat on birthdays" },
      { word: "rice", hint: "Small white grains you eat" },
      { word: "egg", hint: "You crack it to cook it" },
      { word: "bread", hint: "You use it to make a sandwich" }
    ],
    colors: [
      { word: "red", hint: "The color of a stop sign" },
      { word: "blue", hint: "The color of the sky" },
      { word: "green", hint: "The color of grass" },
      { word: "black", hint: "The darkest color" },
      { word: "pink", hint: "A light reddish color" }
    ],
    school: [
      { word: "book", hint: "You read it to learn things" },
      { word: "desk", hint: "You sit at it in class" },
      { word: "pen", hint: "You write with it" },
      { word: "bell", hint: "It rings when class is over" },
      { word: "math", hint: "Subject with numbers" }
    ],
    home: [
      { word: "bed", hint: "You sleep on it" },
      { word: "door", hint: "You open it to enter a room" },
      { word: "chair", hint: "You sit on it" },
      { word: "lamp", hint: "It gives light" },
      { word: "clock", hint: "It tells you the time" }
    ]
  },
  
  // Elementary level (grades 3-4)
  elementary: {
    animals: [
      { word: "giraffe", hint: "Tall animal with a long neck" },
      { word: "elephant", hint: "Large gray animal with a trunk" },
      { word: "penguin", hint: "Black and white bird that cannot fly" },
      { word: "dolphin", hint: "Smart sea mammal that makes clicking sounds" },
      { word: "turtle", hint: "Slow-moving animal with a shell" }
    ],
    food: [
      { word: "pizza", hint: "Round food with cheese and toppings" },
      { word: "banana", hint: "Yellow fruit with a peel" },
      { word: "cheese", hint: "Dairy food often used on sandwiches" },
      { word: "chicken", hint: "Meat from a bird" },
      { word: "orange", hint: "Citrus fruit that shares name with a color" }
    ],
    science: [
      { word: "planet", hint: "Earth is one of these" },
      { word: "weather", hint: "If it's sunny, rainy, or snowy outside" },
      { word: "plant", hint: "Living thing that grows from soil" },
      { word: "water", hint: "Liquid you drink" },
      { word: "fossil", hint: "Remains of ancient creatures in rock" }
    ],
    sports: [
      { word: "basketball", hint: "Game where you shoot a ball through a hoop" },
      { word: "soccer", hint: "Game where you kick a ball into a goal" },
      { word: "swimming", hint: "Moving through water" },
      { word: "baseball", hint: "Sport with a bat and ball" },
      { word: "tennis", hint: "Sport played with rackets" }
    ],
    school: [
      { word: "library", hint: "Place with many books to borrow" },
      { word: "science", hint: "Subject about how things work" },
      { word: "teacher", hint: "Person who helps you learn" },
      { word: "recess", hint: "Break time during school" },
      { word: "homework", hint: "School work you do at home" }
    ]
  },
  
  // Intermediate level (grades 5-6)
  intermediate: {
    animals: [
      { word: "rhinoceros", hint: "Large animal with one or two horns" },
      { word: "chameleon", hint: "Lizard that can change colors" },
      { word: "octopus", hint: "Sea creature with eight arms" },
      { word: "kangaroo", hint: "Australian animal that hops and has a pouch" },
      { word: "porcupine", hint: "Animal covered with sharp spines" }
    ],
    science: [
      { word: "gravity", hint: "Force that pulls things toward Earth" },
      { word: "atmosphere", hint: "Layer of gases surrounding Earth" },
      { word: "dinosaur", hint: "Extinct reptile from millions of years ago" },
      { word: "chemical", hint: "Substance formed by combining elements" },
      { word: "molecule", hint: "Tiny particles that make up matter" }
    ],
    geography: [
      { word: "continent", hint: "Large landmass like Africa or Asia" },
      { word: "mountain", hint: "Very high landform with a peak" },
      { word: "village", hint: "Small community smaller than a town" },
      { word: "desert", hint: "Dry area with little rain" },
      { word: "canyon", hint: "Deep valley with steep sides" }
    ],
    literature: [
      { word: "character", hint: "Person in a story" },
      { word: "paragraph", hint: "Section of text with related sentences" },
      { word: "author", hint: "Person who writes books" },
      { word: "chapter", hint: "Main division of a book" },
      { word: "library", hint: "Building with books to borrow" }
    ],
    technology: [
      { word: "computer", hint: "Electronic device for processing information" },
      { word: "internet", hint: "Global network connecting computers" },
      { word: "keyboard", hint: "Device with keys for typing" },
      { word: "software", hint: "Programs that run on a computer" },
      { word: "download", hint: "Getting data from the internet to your device" }
    ]
  },
  
  // Advanced level (grades 7-9)
  advanced: {
    science: [
      { word: "photosynthesis", hint: "Process plants use to make food from sunlight" },
      { word: "constellation", hint: "Group of stars forming a pattern" },
      { word: "precipitation", hint: "Rain, snow, or hail falling from clouds" },
      { word: "microscopic", hint: "Too small to see without magnification" },
      { word: "thermometer", hint: "Tool for measuring temperature" }
    ],
    literature: [
      { word: "metaphor", hint: "Comparison that doesn't use 'like' or 'as'" },
      { word: "protagonist", hint: "Main character in a story" },
      { word: "narrative", hint: "A spoken or written account of events" },
      { word: "descriptive", hint: "Writing that provides details about how something looks or feels" },
      { word: "vocabulary", hint: "All the words known and used by a person" }
    ],
    history: [
      { word: "archaeological", hint: "Related to studying human history through artifacts" },
      { word: "civilization", hint: "Advanced state of human society" },
      { word: "democracy", hint: "Government system where people vote" },
      { word: "revolution", hint: "Overthrow of a government or social order" },
      { word: "monument", hint: "Structure created to commemorate a person or event" }
    ],
    language: [
      { word: "pronunciation", hint: "Way a word is spoken" },
      { word: "syllable", hint: "Unit of spoken language containing one vowel sound" },
      { word: "punctuation", hint: "Marks used in writing to separate sentences and clarify meaning" },
      { word: "grammar", hint: "Rules about how words are used in a language" },
      { word: "synonym", hint: "Word having the same or nearly the same meaning as another" }
    ],
    math: [
      { word: "equation", hint: "Mathematical statement showing equality" },
      { word: "fraction", hint: "Part of a whole number" },
      { word: "geometry", hint: "Branch of math dealing with shapes" },
      { word: "quotient", hint: "Result obtained by division" },
      { word: "variable", hint: "Symbol representing an unknown value" }
    ]
  },
  
  // Expert level (grades 10-12)
  expert: {
    science: [
      { word: "bioluminescence", hint: "Production of light by living organisms" },
      { word: "metamorphosis", hint: "Process of transformation, like a caterpillar to butterfly" },
      { word: "biodiversity", hint: "Variety of life in a particular habitat" },
      { word: "exothermic", hint: "Chemical reaction that releases heat" },
      { word: "mitochondria", hint: "Energy-producing structures in cells" }
    ],
    literature: [
      { word: "juxtaposition", hint: "Placing contrasting elements side by side" },
      { word: "onomatopoeia", hint: "Word that phonetically imitates the sound it describes" },
      { word: "soliloquy", hint: "Act of speaking one's thoughts aloud when alone" },
      { word: "foreshadowing", hint: "Literary device suggesting future events in a story" },
      { word: "denouement", hint: "Final resolution of the intricacies of a plot" }
    ],
    vocabulary: [
      { word: "ostentatious", hint: "Characterized by pretentious display" },
      { word: "quintessential", hint: "Representing the most perfect example of something" },
      { word: "serendipity", hint: "Finding something good without looking for it" },
      { word: "ubiquitous", hint: "Present, appearing, or found everywhere" },
      { word: "mellifluous", hint: "Sweet or musical; pleasant to hear" }
    ],
    social_studies: [
      { word: "anthropomorphic", hint: "Attributing human characteristics to non-human things" },
      { word: "extraterritorial", hint: "Beyond the territorial jurisdiction" },
      { word: "globalization", hint: "Process of international integration" },
      { word: "totalitarianism", hint: "Political system where the state holds total authority" },
      { word: "socioeconomic", hint: "Relating to social and economic factors" }
    ],
    psychology: [
      { word: "unconscious", hint: "Part of mind containing memories and impulses not in awareness" },
      { word: "cognition", hint: "Mental action of acquiring knowledge through thought and senses" },
      { word: "neuroscience", hint: "Scientific study of the nervous system" },
      { word: "behaviorism", hint: "Theory that behavior can be measured and changed" },
      { word: "introspection", hint: "Examination of one's own thoughts and feelings" }
    ]
  },
  
  // Common spelling challenges
  challenges: {
    silent_letters: [
      { word: "knight", hint: "Medieval warrior who fought on horseback", note: "The 'k' is silent" },
      { word: "gnome", hint: "Small mythical being who guards treasures", note: "The 'g' is silent" },
      { word: "psychology", hint: "Study of the mind and behavior", note: "The 'p' is silent" },
      { word: "autumn", hint: "Season between summer and winter", note: "The 'n' is silent" },
      { word: "doubt", hint: "Feeling of uncertainty", note: "The 'b' is silent" }
    ],
    double_consonants: [
      { word: "misspell", hint: "To spell incorrectly", note: "Double 's' and double 'l'" },
      { word: "accommodate", hint: "To provide lodging or space for", note: "Double 'c' and double 'm'" },
      { word: "committee", hint: "Group of people appointed for a specific function", note: "Double 'm' and double 't'" },
      { word: "occurrence", hint: "An incident or event", note: "Double 'c' and double 'r'" },
      { word: "accidentally", hint: "By chance or unintentionally", note: "Double 'c' and double 'l'" }
    ],
    ie_ei_words: [
      { word: "receive", hint: "To get or accept something", note: "'i' before 'e', except after 'c'" },
      { word: "ceiling", hint: "Upper interior surface of a room", note: "'e' before 'i' after 'c'" },
      { word: "deceive", hint: "To cause someone to believe something that is not true", note: "'e' before 'i' after 'c'" },
      { word: "weird", hint: "Suggesting something supernatural", note: "'e' before 'i' as exception" },
      { word: "believe", hint: "To accept something as true", note: "'i' before 'e', except after 'c'" }
    ],
    homophones: [
      { word: "their", hint: "Belonging to them", wrong: ["there", "they're"] },
      { word: "too", hint: "Also or excessively", wrong: ["to", "two"] },
      { word: "weather", hint: "Atmospheric conditions", wrong: ["whether"] },
      { word: "principal", hint: "Head of a school", wrong: ["principle"] },
      { word: "accept", hint: "To receive willingly", wrong: ["except"] }
    ]
  }
};

// Phrases database for dictation exercises
const phraseDatabase = {
  beginner: [
    { text: "The red ball bounced high.", hint: "Something that bounces" },
    { text: "My cat likes to play.", hint: "About a pet's activity" },
    { text: "We went to the park.", hint: "A place to visit" },
    { text: "I like to eat apples.", hint: "About food preference" },
    { text: "The bus is yellow.", hint: "About transportation" }
  ],
  elementary: [
    { text: "The children played games after school.", hint: "Activity after classes end" },
    { text: "My favorite food is pizza with cheese.", hint: "About a meal preference" },
    { text: "The museum has dinosaur bones.", hint: "About an educational place" },
    { text: "We planted flowers in the garden.", hint: "Outdoor activity" },
    { text: "The teacher gave us homework today.", hint: "About school assignments" }
  ],
  intermediate: [
    { text: "The ancient map showed a hidden treasure location.", hint: "About a valuable discovery" },
    { text: "Scientists discovered a new species of butterfly.", hint: "About a scientific finding" },
    { text: "The temperature dropped quickly during the storm.", hint: "About weather changes" },
    { text: "Our basketball team won the championship game.", hint: "About a sports achievement" },
    { text: "The library has books about different countries.", hint: "About educational resources" }
  ],
  advanced: [
    { text: "The constellation appears in the northern hemisphere during winter.", hint: "About astronomy" },
    { text: "Archaeologists uncovered artifacts from an ancient civilization.", hint: "About historical discovery" },
    { text: "Environmental conservation is crucial for protecting endangered species.", hint: "About nature protection" },
    { text: "The technology revolution transformed how we communicate globally.", hint: "About communication changes" },
    { text: "Photosynthesis allows plants to convert sunlight into energy.", hint: "About plant biology" }
  ],
  expert: [
    { text: "The quantum physics experiment demonstrated wave-particle duality.", hint: "About physics concepts" },
    { text: "Socioeconomic factors significantly influence educational outcomes in urban areas.", hint: "About social studies" },
    { text: "The meticulously restored Renaissance painting revealed previously hidden details.", hint: "About art history" },
    { text: "Neuroscientists identified the brain regions associated with language acquisition.", hint: "About brain science" },
    { text: "The committee unanimously approved the constitutional amendment proposal.", hint: "About governmental procedures" }
  ]
};

// Get a random word from the database based on level and category
function getRandomWord(level, category = null) {
  // Select level
  const levelWords = wordDatabase[level] || wordDatabase.intermediate;
  
  // If category is specified and exists, use it
  if (category && levelWords[category]) {
    const categoryWords = levelWords[category];
    return categoryWords[Math.floor(Math.random() * categoryWords.length)];
  }
  
  // Otherwise pick random category
  const categories = Object.keys(levelWords);
  const randomCategory = categories[Math.floor(Math.random() * categories.length)];
  const categoryWords = levelWords[randomCategory];
  
  return categoryWords[Math.floor(Math.random() * categoryWords.length)];
}

// Get a random phrase from the database based on difficulty level
function getRandomPhrase(level) {
  const levelPhrases = phraseDatabase[level] || phraseDatabase.intermediate;
  return levelPhrases[Math.floor(Math.random() * levelPhrases.length)];
}

// Get a word with specific spelling challenge
function getChallengeWord(challengeType) {
  if (!wordDatabase.challenges[challengeType]) {
    // Default to silent letters if challenge type doesn't exist
    challengeType = 'silent_letters';
  }
  
  const challenges = wordDatabase.challenges[challengeType];
  return challenges[Math.floor(Math.random() * challenges.length)];
}

// Get all available categories for a level
function getCategoriesForLevel(level) {
  const levelWords = wordDatabase[level] || wordDatabase.intermediate;
  return Object.keys(levelWords);
}

// Get all available challenge types
function getChallengeTypes() {
  return Object.keys(wordDatabase.challenges);
} 