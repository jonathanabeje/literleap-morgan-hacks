// Sample passages for fallback when API is unavailable
const samplePassages = {
  easy: [
    {
      title: "The Lost Dog",
      passage: "Tom lost his dog in the park. He looked under trees and behind bushes. He called out its name. Then he heard a bark. His dog ran to him from behind a bench. Tom was so happy to see his dog again."
    },
    {
      title: "A Day at the Beach",
      passage: "Sarah went to the beach with her family. The sun was shining and the water was blue. She built a sand castle and found many shells. Later, they had ice cream and watched the waves. It was a perfect day at the beach."
    },
    {
      title: "My Red Bike",
      passage: "I got a new red bike for my birthday. It has black wheels and a silver bell. I ride it to school every day. My friends like my bike too. We race in the park after school. My red bike is very fast!"
    },
    {
      title: "The Big Race",
      passage: "Max was in the big race at school. He ran as fast as he could. His legs were tired, but he kept going. He passed one boy, then another. At the end, Max came in first place! His mom and dad cheered for him."
    },
    {
      title: "The Little Bird",
      passage: "A little bird made a nest in our tree. Every day, I watched it bring small twigs. Soon there were three blue eggs in the nest. I was quiet so I would not scare the bird. After some time, the eggs hatched. Now there are baby birds in the tree!"
    },
    {
      title: "Pizza Day",
      passage: "Friday is pizza day at my school. We all line up to get a slice. I like cheese pizza the best. My friend Jim likes pepperoni. We sit together and eat our pizza. Pizza day is the best day of the week!"
    },
    {
      title: "The Snow Day",
      passage: "I woke up and saw snow outside my window. Mom said school was closed today. I put on my warm coat and boots. My brother and I built a snowman. We gave him a carrot nose and a hat. It was the best snow day ever!"
    },
    {
      title: "The New Puppy",
      passage: "My family got a new puppy. His name is Spot. He is small and has brown spots. Spot likes to play with his ball. He sleeps in a bed next to mine. I love my new puppy very much!"
    }
  ],
  medium: [
    {
      title: "The Mystery of the Old Clock",
      passage: "Hannah found an old clock in her grandmother's attic. It was covered in dust, but still ticking. When she wound it up, strange things began to happen around the house. Lights would flicker, and doors would open on their own. Hannah wondered if the clock had some kind of magic power. She decided to research its history at the local library."
    },
    {
      title: "Journey to the Mountains",
      passage: "After weeks of planning, we finally began our hike up the mountain trail. The path was steep and rocky, but the views were breathtaking. We saw eagles soaring above and deer drinking from a clear stream. By midday, we reached a small cabin where we rested and enjoyed our packed lunch. The mountain air was crisp and refreshing, making every breath feel cleansing."
    },
    {
      title: "The Secret Garden",
      passage: "Behind the old stone wall, Emma discovered a hidden garden that no one had tended for years. Wildflowers grew between cracked pathways, and an ancient fountain stood silent in the center. Emma decided to bring the garden back to life. Each day after school, she pulled weeds and planted new seeds. Slowly, the garden began to transform, becoming a colorful haven where butterflies danced and birds sang their sweet songs."
    },
    {
      title: "The Lighthouse Keeper",
      passage: "Mr. Sullivan had been the lighthouse keeper for forty years. Every night, he climbed the spiral staircase to light the massive lamp that guided ships safely to shore. During terrible storms, he would watch anxiously as fishing boats battled the waves. The townspeople rarely visited him, but Mr. Sullivan didn't mind the solitude. He found peace in the rhythm of the waves and the company of seagulls that nested near his small cottage."
    },
    {
      title: "The Robot Friend",
      passage: "When Jamie's parents gave him a robot kit for his birthday, he spent three days assembling it. The robot, which Jamie named Bolt, could solve math problems and tell jokes. Jamie programmed Bolt to follow him around the house and help with chores. At school, Jamie's science teacher was so impressed with Bolt that she asked him to demonstrate the robot's abilities at the upcoming science fair."
    },
    {
      title: "Lost in the Aquarium",
      passage: "The class field trip to the aquarium took an unexpected turn when Miguel noticed that everyone had moved to the next exhibit without him. He tried to find his group among the crowds of visitors, but he couldn't spot his teacher's bright yellow shirt anywhere. Miguel approached a staff member, who used a walkie-talkie to contact his teacher. Within minutes, Miguel was reunited with his class, who had been searching for him worriedly."
    },
    {
      title: "The Ancient Map",
      passage: "Carlos found an old map tucked between the pages of a dusty book in his grandfather's attic. The yellowed paper crinkled as he carefully unfolded it, revealing what appeared to be directions to a location in the nearby woods. Curious about where the map might lead, Carlos decided to follow it the next day. After several hours of searching, he discovered a small clearing with the remains of what looked like an old cabin."
    },
    {
      title: "The Piano Lesson",
      passage: "Every Saturday morning, Sophia had her piano lesson with Mrs. Chen. Mrs. Chen was strict but kind, and she always noticed when Sophia hadn't practiced during the week. This week, Sophia had practiced her scales and the new melody diligently. When she played the piece without a single mistake, Mrs. Chen smiled and said, 'Now you're ready for something more challenging.' She pulled out a sheet of music that looked complicated, with notes scattered across the page like stars in the night sky."
    }
  ],
  hard: [
    {
      title: "The Quantum Theory Experiment",
      passage: "Professor Richardson's quantum theory experiment challenged everything we thought we knew about physics. By manipulating subatomic particles in a vacuum chamber, she demonstrated that information could indeed travel faster than light under specific conditions. The scientific community initially rejected her findings, claiming they violated Einstein's theory of relativity. However, after several prestigious laboratories replicated her results, physicists worldwide began reconsidering fundamental principles of quantum mechanics."
    },
    {
      title: "The Evolution of Artificial Intelligence",
      passage: "The evolution of artificial intelligence has transformed from simple rule-based systems to sophisticated neural networks capable of learning and adapting. Early AI programs could only follow explicit instructions, but modern systems can recognize patterns in vast datasets and make predictions with remarkable accuracy. Despite these advancements, researchers continue to debate whether machines will ever develop consciousness or true understanding. The philosophical implications of artificial general intelligence remain one of the most fascinating questions in both computer science and philosophy."
    },
    {
      title: "The Anthropocene Dilemma",
      passage: "The concept of the Anthropocene—a proposed geological epoch characterized by significant human impact on Earth's geology and ecosystems—has sparked intense debate among environmental scientists and policymakers. Evidence of humanity's influence appears in atmospheric carbon levels, plastic pollution in remote oceans, and unprecedented rates of species extinction. Critics argue that framing environmental challenges within geological timescales might diminish the urgency of immediate action. Proponents, however, contend that recognizing the Anthropocene necessitates a fundamental reevaluation of humanity's relationship with natural systems and our responsibility toward future generations."
    },
    {
      title: "Neuroplasticity and Cognitive Development",
      passage: "Recent advances in neuroimaging have revolutionized our understanding of neuroplasticity—the brain's remarkable ability to reorganize itself by forming new neural connections throughout life. Contrary to previous beliefs that brain development was largely complete by adulthood, research now indicates that cognitive functions can be enhanced through specific training regimens even in older individuals. These findings have profound implications for educational methodologies, rehabilitation techniques for brain injury patients, and potential interventions for neurodegenerative diseases like Alzheimer's. Scientists are now investigating the molecular mechanisms that regulate neuroplasticity to develop targeted therapies for cognitive enhancement."
    },
    {
      title: "The Economic Implications of Autonomous Vehicles",
      passage: "The impending widespread adoption of autonomous vehicles represents a paradigm shift that extends far beyond transportation. Economists predict massive disruption across multiple sectors, including insurance (as accident rates potentially decline), real estate (as commuting distances become less relevant), and urban planning (as parking requirements diminish). Simultaneously, concerns about job displacement loom large, particularly for the approximately five million Americans employed as professional drivers. The transition period may prove economically tumultuous, requiring proactive policy interventions such as targeted retraining programs and possibly universal basic income initiatives to mitigate socioeconomic disruption."
    },
    {
      title: "Comparative Constitutional Jurisprudence",
      passage: "Contemporary constitutional courts increasingly engage in transnational judicial dialogue, examining foreign legal precedents when adjudicating complex human rights cases. This practice of comparative constitutional jurisprudence has proponents who argue it enriches legal reasoning and promotes universal human rights standards. Critics, however, raise concerns about democratic legitimacy when judges reference foreign legal concepts not explicitly endorsed by domestic legislative processes. The tension between universalist and particularist approaches to constitutional interpretation reflects broader debates about globalization's influence on national sovereignty and cultural distinctiveness in legal traditions."
    },
    {
      title: "Epigenetic Mechanisms and Intergenerational Trauma",
      passage: "Emerging research in epigenetics suggests that environmental stressors can induce chemical modifications to gene expression that may be transmitted to subsequent generations. Studies examining descendants of famine survivors and genocide victims have identified altered stress hormone regulation and metabolic differences that correlate with ancestral trauma exposure. These findings challenge conventional understanding of inheritance by suggesting that acquired characteristics resulting from extreme environmental conditions might indeed influence offspring phenotypes. While the field remains controversial, with questions about methodology and reproducibility, it opens fascinating possibilities for understanding how historical trauma might manifest physiologically across generations."
    },
    {
      title: "Quantum Computing and Cryptographic Security",
      passage: "The theoretical capabilities of quantum computers pose unprecedented challenges to current cryptographic protocols that safeguard digital communications. Algorithms like Shor's would render RSA encryption—the backbone of secure internet transactions—effectively obsolete by efficiently factoring large prime numbers. In response, cryptographers are developing quantum-resistant algorithms based on lattice problems, hash functions, and other mathematical structures believed to remain secure even against quantum attacks. The race between quantum computing development and post-quantum cryptography implementation has significant national security implications, prompting substantial government investment worldwide in both offensive and defensive quantum information science."
    }
  ],
  beginner: [
    {
      title: "The Big Dog",
      passage: "The dog is big. It has brown fur. The dog likes to play in the park."
    },
    {
      title: "My Red Ball",
      passage: "I have a red ball. It is round and bouncy. I like to throw it high."
    },
    {
      title: "The Cat",
      passage: "The cat is soft. It likes to sleep. It drinks milk from a bowl."
    },
    {
      title: "My House",
      passage: "My house is blue. It has four rooms. I like my house."
    },
    {
      title: "The Fish",
      passage: "The fish swims in water. It has a long tail. The fish is orange and white."
    },
    {
      title: "Going to School",
      passage: "I go to school. I learn to read. I play with my friends at school."
    }
  ],
  elementary: [
    {
      title: "The Lost Cat",
      passage: "Tim lost his cat in the yard. He looked under bushes and called its name. Soon he heard a soft meow from the tree. The cat was stuck on a branch. Tim's dad helped get the cat down. The cat was happy to be safe."
    },
    {
      title: "The New Bike",
      passage: "Sara got a new bike for her birthday. It was blue with silver wheels. She rode it around the block twice. Then she showed it to her best friend. They took turns riding the bike at the park. Sara loved her new bike."
    },
    {
      title: "The School Play",
      passage: "Jack was in the school play. He had to be a tree. His mom made him a costume with green leaves. Jack had to stand still on the stage. When his part came, he said his line very loudly. Everyone clapped at the end. Jack felt proud."
    },
    {
      title: "The Camping Trip",
      passage: "We went camping in the woods. Dad set up our tent near the lake. We cooked hot dogs over the fire. At night, we saw many stars in the sky. I heard an owl go 'Hoot! Hoot!' It was the best camping trip ever."
    },
    {
      title: "My Lost Tooth",
      passage: "My tooth was loose for a week. Then it fell out during lunch. I put it under my pillow that night. The tooth fairy came and left me a dollar! I used the money to buy a new book. Now I have another loose tooth!"
    },
    {
      title: "The Big Storm",
      passage: "Dark clouds filled the sky. The wind began to blow very hard. Rain fell in big drops. We heard thunder and saw lightning. Our dog hid under the bed because he was scared. The storm passed after dinner, and we saw a rainbow in the sky."
    }
  ],
  advanced: [
    {
      title: "The Unexpected Discovery",
      passage: "Professor Clark's archaeological excavation revealed an unprecedented artifact that contradicted existing historical theories. The inscriptions suggested a civilization far more advanced than previously believed. Dating methods confirmed the artifact's authenticity, causing scholarly debates across multiple disciplines. The discovery prompted a complete reexamination of the region's ancient technological capabilities and cultural influences. Several prestigious universities formed a collaborative research team to analyze the implications of this paradigm-shifting find."
    },
    {
      title: "Neuroplasticity Research",
      passage: "Recent neuroplasticity research indicates that the brain can reorganize itself by forming new neural connections throughout life. This phenomenon challenges traditional notions of fixed cognitive development. Studies involving participants of various ages demonstrated significant improvements in memory, attention span, and problem-solving abilities following strategic cognitive training. The implications for education and rehabilitation are substantial, suggesting that customized intervention strategies could effectively address various learning disabilities and recovery from brain injuries."
    },
    {
      title: "Sustainable Urban Planning",
      passage: "Contemporary urban planning increasingly incorporates biophilic design principles that integrate natural elements into metropolitan landscapes. Vertical gardens, renewable energy infrastructure, and pedestrian-oriented transportation systems reflect a paradigm shift toward sustainability. Several European municipalities have implemented comprehensive carbon-neutral initiatives, demonstrating the feasibility of reconciling dense urban populations with environmental conservation. These model cities provide valuable case studies for addressing the challenges of rapid urbanization while simultaneously reducing ecological footprints and enhancing residents' quality of life."
    },
    {
      title: "Digital Privacy in Modern Society",
      passage: "The proliferation of interconnected digital systems has fundamentally transformed our conception of privacy in contemporary society. Sophisticated algorithms continuously analyze consumer behavior patterns, creating detailed psychological profiles that influence everything from product recommendations to political messaging. Recent legislative attempts to regulate data collection practices have encountered significant resistance from technology corporations, who argue that such restrictions would impede innovation and economic growth. This ongoing tension between individual privacy rights and technological advancement represents one of the most consequential ethical dilemmas of the digital era."
    },
    {
      title: "Climate Adaptation Strategies",
      passage: "As climate change accelerates, communities worldwide are implementing adaptation strategies that extend beyond mere mitigation efforts. Coastal cities are redesigning infrastructure to accommodate rising sea levels, while agricultural regions are diversifying crop varieties and irrigation techniques. Insurance companies have developed sophisticated predictive models to assess climate-related risks, fundamentally altering property valuation in vulnerable areas. These multifaceted approaches acknowledge the inevitability of certain climate impacts while attempting to reduce socioeconomic vulnerability through proactive planning and resource allocation."
    },
    {
      title: "Behavioral Economics Principles",
      passage: "Behavioral economics has revolutionized traditional economic theory by incorporating psychological insights into models of decision-making. Concepts such as loss aversion, confirmation bias, and hyperbolic discounting explain seemingly irrational consumer choices that contradict classical utility maximization theories. Policy applications of these principles have yielded effective interventions in public health, retirement savings, and environmental conservation through carefully designed choice architecture. Critics, however, raise concerns about the potential for manipulation when behavioral insights are applied without transparent disclosure or meaningful consent."
    }
  ],
  expert: [
    {
      title: "Quantum Computing Breakthrough",
      passage: "The paradigm-shifting quantum computing breakthrough demonstrates the feasibility of maintaining quantum coherence despite environmental decoherence. This development surmounts what was previously considered an insurmountable barrier in quantum information processing. By employing topological qubits that exploit non-Abelian anyons, researchers achieved unprecedented error correction capabilities essential for scalable quantum applications. The implications extend beyond theoretical physics into cryptography, where current encryption protocols may require fundamental reconceptualization. Pharmaceutical companies have already initiated collaborations to leverage these quantum systems for molecular modeling that could revolutionize drug discovery methodologies."
    },
    {
      title: "Socioeconomic Implications",
      passage: "The socioeconomic implications of artificial intelligence proliferation necessitate a comprehensive reevaluation of educational and workforce development policies. Policymakers must address the impending obsolescence of numerous vocational categories while simultaneously preparing workers for emerging roles that emphasize distinctly human cognitive capabilities. Historically, technological revolutions have ultimately generated net employment growth, yet the unprecedented scope and accelerated pace of AI implementation suggest qualitatively different transition dynamics. Proactive governance frameworks incorporating targeted retraining initiatives, universal basic income experiments, and revised educational curricula represent potential strategies for navigating this unprecedented economic transformation."
    },
    {
      title: "Bioethical Considerations in Genetic Engineering",
      passage: "The bioethical considerations surrounding germline genetic modifications have intensified following recent advances in CRISPR-Cas9 technology that substantially mitigate off-target effects. The therapeutic potential for eliminating hereditary diseases must be evaluated against concerns regarding unintended consequences for future generations and socioeconomic equity in access to enhancement technologies. International regulatory frameworks remain fragmented, with significant jurisdictional variations reflecting cultural and philosophical differences regarding human intervention in natural selection processes. Consequently, scientific collaboration has become increasingly complicated as researchers navigate inconsistent ethical guidelines and reporting requirements across global institutional boundaries."
    },
    {
      title: "Theoretical Cosmology Advancements",
      passage: "Contemporary theoretical cosmology grapples with reconciling quantum field theory and general relativity—frameworks that have resisted integration despite their individual explanatory power. String theory postulates additional spatial dimensions and fundamental vibrating strings to resolve these mathematical incompatibilities, while loop quantum gravity proposes quantized spacetime itself. Recent observational evidence from gravitational wave astronomy has eliminated several competing models but remains insufficient to definitively validate either leading theoretical approach. The philosophical implications of these cosmological frameworks extend beyond physics, influencing contemporary discussions about determinism, multiverses, and the epistemological limitations of scientific inquiry itself."
    },
    {
      title: "Comparative Constitutional Interpretations",
      passage: "Comparative constitutional jurisprudence reveals divergent approaches to balancing individual liberties with collective welfare across democratic societies. While the American tradition emphasizes negative rights and constraints on governmental authority, many European frameworks explicitly incorporate positive rights to healthcare, education, and environmental quality. These philosophical distinctions manifest in interpretive methodologies, with textualist approaches contrasting with purposive or living constitutionalist perspectives. Historical context substantially influences these variations, as constitutions drafted following totalitarian regimes often contain extensive explicit protections reflecting specific historical traumas. Contemporary constitutional scholars increasingly emphasize these contextual factors when evaluating the transferability of jurisprudential principles across jurisdictional boundaries."
    },
    {
      title: "Neurophilosophical Perspectives on Consciousness",
      passage: "Neurophilosophical investigations into consciousness navigate the explanatory gap between phenomenological experience and neurobiological mechanisms. Reductionist approaches that equate mental states with neuronal activity confront persistent challenges in accounting for qualia—the subjective character of experience. Alternative frameworks propose emergent properties arising from complex systems that cannot be predicted from constituent elements alone. Advancements in functional neuroimaging have identified neural correlates of consciousness while simultaneously revealing the limitations of equating correlation with causation or explanation. This intersection of empirical neuroscience and philosophical inquiry illustrates the enduring complexity of integrating first-person subjectivity with third-person methodologies in scientific investigation."
    }
  ]
};

// Function to get a random passage based on difficulty
function getRandomFallbackPassage(difficulty = 'medium') {
  console.log("getRandomFallbackPassage called for difficulty:", difficulty);
  
  // Default to medium if invalid difficulty provided
  if (!['beginner', 'easy', 'elementary', 'medium', 'hard', 'advanced', 'expert'].includes(difficulty)) {
    difficulty = 'medium';
  }
  
  const passagesForDifficulty = samplePassages[difficulty];
  const randomIndex = Math.floor(Math.random() * passagesForDifficulty.length);
  return passagesForDifficulty[randomIndex];
}

// Function to get a specific passage by title
function getPassageByTitle(title) {
  console.log("getPassageByTitle called for title:", title);
  
  // Search through all difficulty levels for the passage with matching title
  for (const difficulty in samplePassages) {
    const matchingPassage = samplePassages[difficulty].find(p => p.title === title);
    if (matchingPassage) {
      return matchingPassage;
    }
  }
  
  // If not found, return a random medium passage
  console.log("Passage not found, returning random medium passage");
  return getRandomFallbackPassage('medium');
}

// Function to get all passages for a given level
function getAllPassagesForLevel(level) {
  // Convert numeric level to difficulty
  let difficulty = 'medium';
  
  if (level <= 2) {
    difficulty = 'easy';
  } else if (level <= 5) {
    difficulty = 'medium';
  } else if (level <= 25) {
    difficulty = 'hard';
  } else if (level <= 50) {
    difficulty = 'advanced';
  } else {
    difficulty = 'expert';
  }
  
  return samplePassages[difficulty] || samplePassages.medium;
}

// Expose everything to window for global access
window.samplePassages = samplePassages;
window.getRandomFallbackPassage = getRandomFallbackPassage;
window.getPassageByTitle = getPassageByTitle;
window.getAllPassagesForLevel = getAllPassagesForLevel;

// Log successful loading
console.log("Passages module loaded successfully with " + 
  Object.values(samplePassages).reduce((sum, arr) => sum + arr.length, 0) + 
  " total passages"); 