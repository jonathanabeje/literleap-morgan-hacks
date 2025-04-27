console.log("🎤 SPEECH RECOGNITION MODULE LOADING");

// Speech Recognition Module
// This module handles browser speech recognition and provides feedback on reading performance

// Global variables
let recognition = null;          // Speech recognition instance
let isRecording = false;         // Flag to track recording state
let currentPassage = "";         // The text passage to be read
let transcript = "";             // The recorded speech transcript
let timerInterval = null;        // Timer interval reference
let startTime = null;            // Recording start time
let permissionGranted = false;   // Flag to track microphone permission

// Function to log debug messages
function logDebug(message) {
  const timestamp = new Date().toISOString().substring(11, 19);
  console.log(`[SpeechRecognition ${timestamp}] ${message}`);
}

// Simple test function to verify speech recognition is accessible
window.testSpeechRecognition = function() {
  const supported = 'webkitSpeechRecognition' in window || 'SpeechRecognition' in window;
  console.log("🎤 Speech Recognition Test");
  console.log("- API Available:", supported);
  console.log("- Recognition object:", recognition ? "initialized" : "not initialized");
  console.log("- Current passage length:", currentPassage.length);
  console.log("- Recording state:", isRecording);
  
  // Try to initialize if not already
  if (!recognition && supported) {
    try {
      initSpeechRecognition();
      console.log("- Init result:", recognition ? "SUCCESS" : "FAILED");
    } catch (e) {
      console.error("- Init error:", e.message);
    }
  }
  
  return supported;
};

// Check if browser supports speech recognition
function checkBrowserSupport() {
  return ('webkitSpeechRecognition' in window) || ('SpeechRecognition' in window);
}

// Check for microphone permission
function checkMicrophonePermission() {
  return new Promise((resolve, reject) => {
    navigator.mediaDevices.getUserMedia({ audio: true })
      .then(stream => {
        // Stop the stream immediately - we just wanted to check permission
        stream.getTracks().forEach(track => track.stop());
        permissionGranted = true;
        resolve(true);
      })
      .catch(err => {
        logDebug(`Microphone permission error: ${err.message}`);
        permissionGranted = false;
        resolve(false);
      });
  });
}

// Initialize speech recognition
function initSpeechRecognition() {
  logDebug("Initializing speech recognition");
  
  try {
    // Check if the browser supports the Web Speech API
    if (!checkBrowserSupport()) {
      logDebug("Speech recognition not supported in this browser");
      alert("Speech recognition is not supported in your browser. Please try using Chrome.");
      return false;
    }

    // Create recognition instance
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    recognition = new SpeechRecognition();
    
    // Configure recognition
    recognition.continuous = true;
    recognition.interimResults = true;
    recognition.maxAlternatives = 3;
    recognition.lang = 'en-US';
    
    // Set up event handlers
    setupRecognitionHandlers();
    
    logDebug("Speech recognition initialized successfully");
    return true;
  } catch (error) {
    logDebug(`Error initializing speech recognition: ${error.message}`);
    console.error("Full error details:", error);
    return false;
  }
}

// Set up event handlers for the recognition object
function setupRecognitionHandlers() {
  if (!recognition) {
    logDebug("Cannot setup handlers: recognition object is null");
    return;
  }
  
  // Handler for when recognition starts
  recognition.onstart = function() {
    logDebug("Recognition started");
    isRecording = true;
    
    // Show recording UI elements
    const startButton = document.getElementById('start-recording-btn');
    const stopButton = document.getElementById('stop-recording-btn');
    const recordingIndicator = document.getElementById('recording-indicator');
    
    if (startButton) startButton.classList.add('d-none');
    if (stopButton) stopButton.classList.remove('d-none');
    if (recordingIndicator) recordingIndicator.classList.remove('d-none');
    
    // Reset transcript
    transcript = "";
    const liveTranscription = document.getElementById('live-transcription');
    if (liveTranscription) {
      liveTranscription.textContent = "Listening...";
    }
    
    // Start timer
    startTime = new Date();
    startTimer();
  };
  
  // Handler for recognition results
  recognition.onresult = function(event) {
    logDebug(`Got result event with ${event.results.length} results`);
    // Get the latest result
    let interimTranscript = '';
    let finalTranscript = '';
    
    for (let i = event.resultIndex; i < event.results.length; i++) {
      const result = event.results[i];
      const text = result[0].transcript;
      
      if (result.isFinal) {
        finalTranscript += text;
        logDebug(`Final text: ${text}`);
      } else {
        interimTranscript += text;
        logDebug(`Interim text: ${text}`);
      }
    }
    
    // Update the transcript
    if (finalTranscript) {
      transcript += finalTranscript + ' ';
    }
    
    // Display current transcript
    const liveTranscription = document.getElementById('live-transcription');
    if (liveTranscription) {
      liveTranscription.innerHTML = transcript + 
        (interimTranscript ? `<span class="text-muted">${interimTranscript}</span>` : '');
    }
  };
  
  // Handler for recognition errors
  recognition.onerror = function(event) {
    logDebug(`Recognition error: ${event.error}`);
    console.error("Full error details:", event);
    
    // Display error message based on the error type
    let errorMessage = "An error occurred with speech recognition.";
    
    switch (event.error) {
      case 'no-speech':
        errorMessage = "No speech was detected. Please try again.";
        break;
      case 'aborted':
        errorMessage = "Speech recognition was aborted.";
        break;
      case 'network':
        errorMessage = "Network error occurred. Please check your connection.";
        break;
      case 'not-allowed':
        errorMessage = "Microphone access was denied. Please allow microphone access in your browser settings.";
        permissionGranted = false;
        break;
      case 'service-not-allowed':
        errorMessage = "Speech recognition service is not allowed. Please check your browser settings.";
        break;
      case 'audio-capture':
        errorMessage = "No microphone was found. Please ensure your microphone is connected.";
        break;
    }
    
    // Alert the user for critical errors
    if (event.error !== 'no-speech' && event.error !== 'aborted') {
      alert(errorMessage);
    }
    
    // Stop recording if a critical error occurred
    if (event.error !== 'no-speech') {
      stopRecording();
    }
  };
  
  // Handler for when recognition ends
  recognition.onend = function() {
    logDebug("Recognition ended");
    
    if (isRecording) {
      // If we're still supposed to be recording, restart
      // This handles cases where recognition stops unexpectedly
      logDebug("Restarting recognition as it ended unexpectedly");
      try {
        recognition.start();
      } catch (error) {
        logDebug(`Error restarting recognition: ${error.message}`);
        isRecording = false;
        alert("Could not restart speech recognition. Please try again.");
        
        // Process with what we have
        processResults();
      }
    }
  };
}

// Function to reset the UI elements
function resetUI() {
  const startButton = document.getElementById('start-recording-btn');
  const stopButton = document.getElementById('stop-recording-btn');
  const recordingIndicator = document.getElementById('recording-indicator');
  
  if (startButton) startButton.classList.remove('d-none');
  if (stopButton) stopButton.classList.add('d-none');
  if (recordingIndicator) recordingIndicator.classList.add('d-none');
}

// Function to start recording
async function startRecording() {
  logDebug("startRecording called");
  
  // Don't start if there's no passage to read
  if (!currentPassage || currentPassage.trim().length === 0) {
    logDebug("No passage set for reading");
    alert("Please select a passage to read first.");
    return;
  }
  
  // Don't start if already recording
  if (isRecording) {
    logDebug("Already recording, ignoring start request");
    return;
  }
  
  // Check microphone permission first
  try {
    const hasPermission = await checkMicrophonePermission();
    if (!hasPermission) {
      logDebug("Microphone permission denied");
      alert("Microphone access is required for speech recognition. Please allow microphone access in your browser settings.");
      return;
    }
  } catch (error) {
    logDebug(`Error checking microphone permission: ${error.message}`);
  }
  
  // Initialize recognition if needed
  if (!recognition) {
    logDebug("Recognition not initialized, initializing now");
    if (!initSpeechRecognition()) {
      logDebug("Failed to initialize speech recognition");
      return;
    }
  }
  
  try {
    // Reset transcript
    transcript = "";
    const liveTranscription = document.getElementById('live-transcription');
    if (liveTranscription) {
      liveTranscription.textContent = "Listening...";
    }
    
    // Start recording
    recognition.start();
    logDebug("Started recording successfully");
  } catch (error) {
    logDebug(`Error starting recognition: ${error.message}`);
    
    if (error.message.includes('permission') || error.name === 'NotAllowedError') {
      alert("Microphone permission denied. Please allow microphone access in your browser settings and try again.");
    } else {
      alert("Failed to start speech recognition. Please try again or use Google Chrome browser.");
    }
    
    console.error("Full error details:", error);
  }
}

// Function to stop recording
function stopRecording() {
  logDebug("Stopping recording");
  
  if (!isRecording) {
    logDebug("Not currently recording, nothing to stop");
    return;
  }
  
  // Stop the recognition
  try {
    if (recognition) {
      recognition.stop();
      isRecording = false;
    }
  } catch (error) {
    logDebug(`Error stopping recognition: ${error.message}`);
  }
  
  // Stop the timer
  stopTimer();
  
  // Update UI
  resetUI();
  
  // Process the results
  processResults();
}

// Process the recorded results
function processResults() {
  logDebug("Processing results");
  logDebug(`Current passage length: ${currentPassage.length}, transcript length: ${transcript.length}`);
  
  if (!currentPassage || currentPassage.trim().length === 0) {
    logDebug("No passage set, cannot process results");
    alert("No passage was loaded. Please refresh the page and try again.");
    return;
  }
  
  if (!transcript || transcript.trim().length === 0) {
    logDebug("No speech recorded");
    alert("No speech was detected. Please try again and speak clearly into the microphone.");
    return;
  }
  
  // Compare the spoken text with the original passage
  const results = compareTexts(transcript, currentPassage);
  
  // Update the analysis UI with the results
  updateAnalysisUI(results);
  
  // Make sure the analysis is visible
  setTimeout(() => {
    if (typeof window.showAnalysis === 'function') {
      window.showAnalysis();
    } else {
      // Direct DOM manipulation if function not available
      const analysisContainer = document.getElementById('analysis-container');
      if (analysisContainer) {
        analysisContainer.classList.remove('d-none');
      }
    }
  }, 100);
}

// Compare the spoken text with the original text
function compareTexts(spokenText, originalText) {
  logDebug("Comparing spoken text with original passage");
  
  // Normalize texts for comparison
  const normalizeText = (text) => {
    // Remove extra whitespace, convert to lowercase, and remove punctuation
    return text.trim()
      .toLowerCase()
      .replace(/[.,\/#!$%\^&\*;:{}=\-_`~()]/g, "")
      .replace(/\s+/g, " ");
  };
  
  const normalizedSpoken = normalizeText(spokenText);
  const normalizedOriginal = normalizeText(originalText);
  
  // Split into words
  const spokenWords = normalizedSpoken.split(" ");
  const originalWords = normalizedOriginal.split(" ");
  
  // Track correct, incorrect, and missed words
  const incorrectWords = [];
  const missedWords = [];
  let correctCount = 0;
  
  // Compare word by word (simple approach)
  const commonLength = Math.min(spokenWords.length, originalWords.length);
  
  for (let i = 0; i < commonLength; i++) {
    // Skip empty words
    if (!spokenWords[i] || !originalWords[i]) continue;
    
    // Compare words - if they're similar enough, count as correct
    if (levenshteinDistance(spokenWords[i], originalWords[i]) <= 1) {
      correctCount++;
    } else {
      incorrectWords.push(originalWords[i]);
    }
  }
  
  // Words missed (if original is longer)
  if (originalWords.length > spokenWords.length) {
    for (let i = spokenWords.length; i < originalWords.length; i++) {
      if (originalWords[i] && originalWords[i].length > 3) { // Only consider significant words
        missedWords.push(originalWords[i]);
      }
    }
  }
  
  // Calculate accuracy
  const totalWords = originalWords.filter(word => word.length > 0).length;
  const accuracy = totalWords > 0 ? (correctCount / totalWords) * 100 : 0;
  
  // Find difficult words (incorrect or missed long words)
  const allProblematicWords = [...incorrectWords, ...missedWords];
  const difficultWords = [...new Set(allProblematicWords)]
    .filter(word => word.length > 4) // Only consider longer words as difficult
    .slice(0, 5); // Limit to top 5 difficult words
  
  logDebug(`Accuracy: ${accuracy.toFixed(1)}%, Correct: ${correctCount}, Total: ${totalWords}`);
  logDebug(`Incorrect words: ${incorrectWords.length}, Difficult words: ${difficultWords.length}`);
  
  return {
    accuracy,
    spokenLength: spokenWords.length,
    originalLength: originalWords.length,
    correctCount,
    incorrectWords,
    missedWords,
    difficultWords,
    totalWords
  };
}

// Simple Levenshtein distance implementation to compare word similarity
function levenshteinDistance(a, b) {
  if (a.length === 0) return b.length;
  if (b.length === 0) return a.length;
  
  const matrix = [];
  
  // Initialize matrix
  for (let i = 0; i <= b.length; i++) {
    matrix[i] = [i];
  }
  
  for (let j = 0; j <= a.length; j++) {
    matrix[0][j] = j;
  }
  
  // Fill matrix
  for (let i = 1; i <= b.length; i++) {
    for (let j = 1; j <= a.length; j++) {
      const cost = a[j - 1] === b[i - 1] ? 0 : 1;
      matrix[i][j] = Math.min(
        matrix[i - 1][j] + 1,      // deletion
        matrix[i][j - 1] + 1,      // insertion
        matrix[i - 1][j - 1] + cost  // substitution
      );
    }
  }
  
  return matrix[b.length][a.length];
}

// Update the UI with analysis results
function updateAnalysisUI(results) {
  logDebug("Updating analysis UI");
  
  // Update accuracy meter
  const accuracyMeter = document.getElementById('accuracy-meter');
  const accuracyPercentage = document.getElementById('accuracy-percentage');
  
  if (accuracyMeter) {
    accuracyMeter.value = results.accuracy;
  }
  
  if (accuracyPercentage) {
    accuracyPercentage.textContent = `${Math.round(results.accuracy)}%`;
  }
  
  // Generate feedback for strengths and improvements
  const strengths = generateStrengths(results.accuracy, results.spokenLength, results.originalLength);
  const improvements = generateImprovements(results.accuracy, results.incorrectWords, results.difficultWords);
  
  // Update strengths
  const strengthsContainer = document.getElementById('strengths-container');
  if (strengthsContainer) {
    let strengthsHTML = '';
    strengths.forEach(strength => {
      strengthsHTML += `<li class="list-group-item"><i class="fas fa-check-circle text-success me-2"></i>${strength}</li>`;
    });
    strengthsContainer.innerHTML = strengthsHTML || '<li class="list-group-item">Complete more readings to see your strengths</li>';
  }
  
  // Update improvements
  const improvementsContainer = document.getElementById('improvements-container');
  if (improvementsContainer) {
    let improvementsHTML = '';
    improvements.forEach(improvement => {
      improvementsHTML += `<li class="list-group-item"><i class="fas fa-arrow-alt-circle-up text-primary me-2"></i>${improvement}</li>`;
    });
    improvementsContainer.innerHTML = improvementsHTML || '<li class="list-group-item">Great job! No specific improvements needed</li>';
  }
  
  // Generate pronunciation guides for difficult words
  const pronunciationGuides = generatePronunciationGuides(results.difficultWords);
  
  // Create highlighted version of passage showing difficult words
  const highlightedPassage = createHighlightedPassage(currentPassage, results.incorrectWords);
  
  // Update highlighted passage if function is available
  if (typeof window.updateHighlightedPassage === 'function') {
    window.updateHighlightedPassage(highlightedPassage, results.difficultWords);
  }
  
  // Update pronunciation guide if function is available
  if (typeof window.updatePronunciationGuide === 'function') {
    window.updatePronunciationGuide(results.difficultWords, pronunciationGuides);
  }
}

// Create a highlighted version of the passage with difficult words marked
function createHighlightedPassage(passage, incorrectWords) {
  if (!passage || !incorrectWords || incorrectWords.length === 0) {
    return passage;
  }
  
  let highlightedText = passage;
  
  // Create a case-insensitive regex for each incorrect word
  incorrectWords.forEach(word => {
    if (word && word.length > 0) {
      const regex = new RegExp(`\\b${word}\\b`, 'gi');
      highlightedText = highlightedText.replace(regex, `<span class="highlight-word">$&</span>`);
    }
  });
  
  return highlightedText;
}

// Generate strengths based on the reading performance
function generateStrengths(accuracy, spokenLength, originalLength) {
  const strengths = [];
  
  if (accuracy >= 90) {
    strengths.push("Excellent reading accuracy");
  } else if (accuracy >= 75) {
    strengths.push("Good reading accuracy");
  }
  
  if (spokenLength >= originalLength * 0.95) {
    strengths.push("Complete coverage of the passage");
  }
  
  if (accuracy >= 60) {
    strengths.push("Good comprehension of the content");
  }
  
  if (spokenLength > 0 && accuracy > 40) {
    strengths.push("Consistent reading pace");
  }
  
  // Add general encouragement if few strengths identified
  if (strengths.length < 2 && accuracy > 30) {
    strengths.push("Showing progress in reading skills");
  }
  
  // Always provide at least one positive feedback
  if (strengths.length === 0) {
    strengths.push("Practicing regularly will improve your reading skills");
  }
  
  return strengths;
}

// Generate improvement suggestions based on the performance
function generateImprovements(accuracy, incorrectWords, difficultWords) {
  const improvements = [];
  
  if (accuracy < 70) {
    improvements.push("Focus on pronouncing words more clearly");
  }
  
  if (incorrectWords.length > 5) {
    improvements.push("Practice reading aloud more frequently");
  }
  
  if (difficultWords.length > 0) {
    improvements.push("Work on the challenging words highlighted in the passage");
  }
  
  if (accuracy < 50) {
    improvements.push("Try reading at a slower pace for better pronunciation");
  }
  
  if (difficultWords.length > 3) {
    improvements.push("Review the pronunciation guide for difficult words");
  }
  
  return improvements;
}

// Generate pronunciation guides for difficult words
function generatePronunciationGuides(difficultWords) {
  const guides = {};
  
  // Sample pronunciation guides
  const sampleGuides = {
    "quantum": { 
      pronunciation: "KWAHN-tuhm", 
      example: "The quantum theory revolutionized physics."
    },
    "artificial": { 
      pronunciation: "ahr-tuh-FISH-uhl", 
      example: "Artificial intelligence is changing how we interact with technology."
    },
    "intelligence": { 
      pronunciation: "in-TEL-i-juhns", 
      example: "Her intelligence was evident from an early age."
    },
    "experiment": { 
      pronunciation: "ik-SPER-uh-muhnt", 
      example: "The experiment proved the hypothesis correct."
    },
    "manipulating": { 
      pronunciation: "muh-NIP-yoo-ley-ting", 
      example: "She was manipulating the controls with precision."
    },
    "subatomic": { 
      pronunciation: "sub-uh-TOM-ik", 
      example: "Subatomic particles are smaller than atoms."
    },
    "particles": { 
      pronunciation: "PAHR-ti-kuhls", 
      example: "Dust particles were visible in the sunlight."
    },
    "demonstrated": { 
      pronunciation: "DEM-uhn-strey-tid", 
      example: "He demonstrated how to solve the problem."
    },
    "information": { 
      pronunciation: "in-fer-MEY-shuhn", 
      example: "The book contains valuable information."
    },
    "scientific": { 
      pronunciation: "sahy-uhn-TIF-ik", 
      example: "The scientific method requires careful observation."
    },
    "community": { 
      pronunciation: "kuh-MYOO-ni-tee", 
      example: "The local community supported the school project."
    },
    "rejected": { 
      pronunciation: "ri-JEK-tid", 
      example: "They rejected the initial proposal."
    },
    "prestigious": { 
      pronunciation: "pre-STI-juhs", 
      example: "She attended a prestigious university."
    },
    "laboratories": { 
      pronunciation: "LAB-ruh-tawr-eez", 
      example: "The research was conducted in several laboratories."
    },
    "physicists": { 
      pronunciation: "FIZ-uh-sists", 
      example: "Physicists study the fundamental forces of nature."
    },
    "fundamental": { 
      pronunciation: "fuhn-duh-MEN-tl", 
      example: "These are the fundamental principles of the theory."
    },
    "principles": { 
      pronunciation: "PRIN-suh-puhls", 
      example: "The principles of mathematics are universal."
    },
    "evolution": { 
      pronunciation: "ev-uh-LOO-shuhn", 
      example: "The evolution of species occurs over many generations."
    },
    "transformed": { 
      pronunciation: "trans-FAWRMD", 
      example: "The city transformed over the decades."
    },
    "sophisticated": { 
      pronunciation: "suh-FIS-ti-key-tid", 
      example: "They used sophisticated equipment for the analysis."
    },
    "capable": { 
      pronunciation: "KEY-puh-buhl", 
      example: "She is capable of solving complex problems."
    },
    "adapting": { 
      pronunciation: "uh-DAP-ting", 
      example: "Animals are constantly adapting to their environment."
    },
    "explicit": { 
      pronunciation: "ik-SPLIS-it", 
      example: "He gave explicit instructions for the task."
    },
    "instructions": { 
      pronunciation: "in-STRUHK-shuhnz", 
      example: "Follow the instructions carefully to assemble the furniture."
    },
    "recognize": { 
      pronunciation: "REK-uhg-nahyz", 
      example: "I didn't recognize him with his new haircut."
    },
    "accuracy": { 
      pronunciation: "AK-yuh-ruh-see", 
      example: "The test measures the accuracy of the instrument."
    },
    "advancements": { 
      pronunciation: "ad-VANS-muhnts", 
      example: "Technological advancements have improved our lives."
    },
    "researchers": { 
      pronunciation: "ri-SUR-cherz", 
      example: "Researchers are studying the effects of climate change."
    },
    "continue": { 
      pronunciation: "kuhn-TIN-yoo", 
      example: "They will continue the discussion tomorrow."
    },
    "consciousness": { 
      pronunciation: "KON-shuhs-nis", 
      example: "The question of consciousness remains a mystery."
    },
    "understanding": { 
      pronunciation: "uhn-der-STAN-ding", 
      example: "Understanding complex topics takes time."
    },
    "philosophical": { 
      pronunciation: "fil-uh-SOF-i-kuhl", 
      example: "They discussed philosophical questions late into the night."
    },
    "implications": { 
      pronunciation: "im-pli-KEY-shuhnz", 
      example: "The implications of this decision are far-reaching."
    },
    "fascinating": { 
      pronunciation: "FAS-uh-ney-ting", 
      example: "It was a fascinating documentary about deep sea creatures."
    },
    "computer": { 
      pronunciation: "kuhm-PYOO-ter", 
      example: "She uses her computer for work and entertainment."
    },
    "philosophy": { 
      pronunciation: "fi-LOS-uh-fee", 
      example: "She studied philosophy at university."
    }
  };
  
  // Generate guides for each difficult word
  difficultWords.forEach(word => {
    // Look up in sample guides or generate a simple phonetic guide
    if (sampleGuides[word.toLowerCase()]) {
      guides[word] = sampleGuides[word.toLowerCase()];
    } else {
      guides[word] = {
        pronunciation: generateSimplePhonetic(word),
        example: `Practice saying "${word}" clearly.`
      };
    }
  });
  
  return guides;
}

// Generate a simple phonetic representation
function generateSimplePhonetic(word) {
  // Very basic phonetic representation
  return word.toUpperCase();
}

// Start timer for recording duration
function startTimer() {
  const timerElement = document.getElementById('recording-timer');
  if (!timerElement) return;
  
  // Update timer display immediately
  updateTimerDisplay(timerElement);
  
  // Set up interval to update timer every second
  timerInterval = setInterval(() => {
    updateTimerDisplay(timerElement);
  }, 1000);
}

// Stop timer
function stopTimer() {
  if (timerInterval) {
    clearInterval(timerInterval);
    timerInterval = null;
  }
}

// Update timer display
function updateTimerDisplay(timerElement) {
  if (!startTime || !timerElement) return;
  
  const now = new Date();
  const diffInSeconds = Math.floor((now - startTime) / 1000);
  const minutes = Math.floor(diffInSeconds / 60);
  const seconds = diffInSeconds % 60;
  
  timerElement.textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
}

// Set the current passage for comparison
function setCurrentPassage(passage) {
  logDebug(`Setting current passage (${passage.length} chars)`);
  currentPassage = passage;
}

// Immediately initialize on load
let speechRecoInitialized = false;
try {
  speechRecoInitialized = initSpeechRecognition();
  logDebug(`Speech recognition initialized on load: ${speechRecoInitialized}`);
} catch (error) {
  logDebug(`Error during initial initialization: ${error.message}`);
}

// Expose API to window
window.initSpeechRecognition = initSpeechRecognition;
window.startRecording = startRecording;
window.stopRecording = stopRecording;
window.setCurrentPassage = setCurrentPassage;

// Log module load
console.log("Speech recognition module loaded successfully. Ready:", speechRecoInitialized);