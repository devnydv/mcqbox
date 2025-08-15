
const allQuestions = [
    {
        question: "What is the largest planet in our solar system?",
        options: ["Earth", "Jupiter", "Saturn", "Neptune"],
        correct: 1,
        explanation: "Jupiter is the largest planet in our solar system, with a mass greater than all other planets combined. It's a gas giant with a diameter of about 88,695 miles (142,800 km).",
        category: "science"
    },
    {
        question: "Which programming language was created by Guido van Rossum?",
        options: ["Java", "C++", "Python", "JavaScript"],
        correct: 2,
        explanation: "Python was created by Guido van Rossum and first released in 1991. It's known for its simple, readable syntax and is widely used in web development, data science, and artificial intelligence.",
        category: "technology"
    },
    {
        question: "What is the chemical symbol for Gold?",
        options: ["Go", "Gd", "Au", "Ag"],
        correct: 2,
        explanation: "The chemical symbol for Gold is Au, which comes from the Latin word 'aurum' meaning gold. Gold is a precious metal with atomic number 79.",
        category: "science"
    },
    {
        question: "In which year did World War II end?",
        options: ["1944", "1945", "1946", "1947"],
        correct: 1,
        explanation: "World War II ended in 1945. The war in Europe ended on May 8, 1945 (VE Day), and the war with Japan ended on September 2, 1945 (VJ Day) after the atomic bombings and Soviet invasion.",
        category: "history"
    },
    {
        question: "What is the capital of Australia?",
        options: ["Sydney", "Melbourne", "Canberra", "Perth"],
        correct: 2,
        explanation: "Canberra is the capital of Australia. While Sydney and Melbourne are larger cities, Canberra was specifically planned and built as the national capital, established in 1913.",
        category: "geography"
    },
    {
        question: "Which organ in the human body produces insulin?",
        options: ["Liver", "Kidney", "Pancreas", "Heart"],
        correct: 2,
        explanation: "The pancreas produces insulin, a hormone that regulates blood sugar levels. Beta cells in the pancreas release insulin to help cells absorb glucose from the bloodstream.",
        category: "biology"
    },
    {
        question: "What is the fastest land animal?",
        options: ["Lion", "Cheetah", "Leopard", "Gazelle"],
        correct: 1,
        explanation: "The cheetah is the fastest land animal, capable of reaching speeds up to 70 mph (112 km/h) in short bursts. They can accelerate from 0 to 60 mph in just 3 seconds.",
        category: "biology"
    },
    {
        question: "Which scientist developed the theory of relativity?",
        options: ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Stephen Hawking"],
        correct: 1,
        explanation: "Albert Einstein developed both the special theory of relativity (1905) and general theory of relativity (1915), revolutionizing our understanding of space, time, and gravity.",
        category: "science"
    },
    {
        question: "What is the smallest unit of matter?",
        options: ["Molecule", "Atom", "Electron", "Proton"],
        correct: 1,
        explanation: "An atom is the smallest unit of matter that retains the properties of an element. Atoms consist of protons, neutrons, and electrons, and combine to form molecules.",
        category: "science"
    },
    {
        question: "Which ocean is the largest?",
        options: ["Atlantic", "Indian", "Arctic", "Pacific"],
        correct: 3,
        explanation: "The Pacific Ocean is the largest ocean, covering about 63 million square miles (165 million square kilometers) and containing more than half of the world's free water.",
        category: "geography"
    },
    {
        question: "What is the hardest natural substance on Earth?",
        options: ["Gold", "Iron", "Diamond", "Platinum"],
        correct: 2,
        explanation: "Diamond is the hardest natural substance on Earth with a hardness of 10 on the Mohs scale. Its crystal structure makes it extremely resistant to scratching.",
        category: "science"
    },
    {
        question: "Which planet is known as the Red Planet?",
        options: ["Venus", "Mars", "Mercury", "Jupiter"],
        correct: 1,
        explanation: "Mars is known as the Red Planet due to iron oxide (rust) on its surface, which gives it a reddish appearance. It's the fourth planet from the Sun.",
        category: "science"
    },
    {
        question: "Who painted the Mona Lisa?",
        options: ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo"],
        correct: 2,
        explanation: "Leonardo da Vinci painted the Mona Lisa between 1503-1519. It's one of the most famous paintings in the world and is housed in the Louvre Museum.",
        category: "arts"
    },
    {
        question: "What is the most abundant gas in Earth's atmosphere?",
        options: ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        correct: 2,
        explanation: "Nitrogen makes up about 78% of Earth's atmosphere, while oxygen comprises about 21%. The remaining 1% consists of argon, carbon dioxide, and other gases.",
        category: "science"
    },
    {
        question: "Which country invented tea?",
        options: ["India", "China", "Japan", "Sri Lanka"],
        correct: 1,
        explanation: "Tea was first discovered in China around 2737 BCE according to legend. China has been cultivating and consuming tea for thousands of years before it spread to other countries.",
        category: "history"
    },
    {
        question: "What is the speed of light in vacuum?",
        options: ["300,000 km/s", "299,792,458 m/s", "186,000 miles/s", "All of the above"],
        correct: 3,
        explanation: "The speed of light in vacuum is exactly 299,792,458 meters per second, which is approximately 300,000 km/s or 186,000 miles per second.",
        category: "science"
    },
    {
        question: "Which is the longest river in the world?",
        options: ["Amazon", "Nile", "Yangtze", "Mississippi"],
        correct: 1,
        explanation: "The Nile River is generally considered the longest river in the world at approximately 6,650 km (4,130 miles), flowing through northeastern Africa.",
        category: "geography"
    },
    {
        question: "What does 'www' stand for?",
        options: ["World Wide Web", "World Wide Website", "Web World Wide", "Wide World Web"],
        correct: 0,
        explanation: "WWW stands for World Wide Web, the information system that enables documents to be connected to other documents by hypertext links, accessible via the Internet.",
        category: "technology"
    },
    {
        question: "Which blood type is known as the universal donor?",
        options: ["A+", "B+", "AB+", "O-"],
        correct: 3,
        explanation: "O- (O negative) is known as the universal donor because it can be given to patients with any blood type in emergency situations, as it has no A, B, or Rh antigens.",
        category: "biology"
    },
    {
        question: "What is the largest mammal in the world?",
        options: ["African Elephant", "Blue Whale", "Giraffe", "Polar Bear"],
        correct: 1,
        explanation: "The Blue Whale is the largest mammal and the largest animal ever known to have lived on Earth, reaching lengths up to 100 feet and weights up to 200 tons.",
        category: "biology"
    }
];

let questions = allQuestions.slice(0, 10);
let questionsLoaded = 10;
let currentTopic = 'all';
let currentQuestion = 0;
let score = 0;
let userAnswers = [];
let quizCompleted = false;

function selectTopic(topic) {
    currentQuestion = 0;
    score = 0;
    userAnswers = [];
    quizCompleted = false;
    currentTopic = topic;

    document.querySelectorAll('.topic-chip').forEach(chip => {
        chip.classList.remove('active');
    });
    document.querySelector(`[data-topic="${topic}"]`).classList.add('active');

    let filteredQuestions;
    if (topic === 'all') {
        filteredQuestions = allQuestions;
    } else {
        filteredQuestions = allQuestions.filter(q => q.category === topic);
    }

    const questionsToLoad = Math.min(10, filteredQuestions.length);
    questions = filteredQuestions.slice(0, questionsToLoad);
    questionsLoaded = questionsToLoad;

    updateDisplay();
    updateProgress();
    updateScore();
    updateLoadMoreButton();

    const completed = document.querySelector('.quiz-completed');
    if (completed) {
        completed.remove();
    }

    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function getFilteredQuestions() {
    if (currentTopic === 'all') {
        return allQuestions;
    }
    return allQuestions.filter(q => q.category === currentTopic);
}

function renderQuestion(index) {
    const question = questions[index];
    const isAnswered = userAnswers[index] !== undefined;

    return `
                <div class="question-card" data-question-index="${index}">
                    <div class="question-number">Question ${index + 1} of ${questions.length}</div>
                    <div class="question-text">${question.question}</div>
                    <div class="options">
                        ${question.options.map((option, optIndex) => `
                            <div class="option ${isAnswered ? (optIndex === userAnswers[index] ? 'selected' : '') : ''} ${isAnswered ? (optIndex === question.correct ? 'correct' : (optIndex === userAnswers[index] && optIndex !== question.correct ? 'incorrect' : '')) : ''}" 
                                 onclick="${isAnswered ? '' : `selectOption(${index}, ${optIndex})`}">
                                ${String.fromCharCode(65 + optIndex)}. ${option}
                            </div>
                        `).join('')}
                    </div>
                    <div class="button-group">
                        
                        <button class="btn btn-secondary" onclick="toggleExplanation(${index})">
                            Show Explanation
                        </button>
                    </div>
                    <div class="explanation" id="explanation-${index}">
                        <h4>💡 Explanation:</h4>
                        <p>${question.explanation}</p>
                        <p><strong>Correct Answer: ${String.fromCharCode(65 + question.correct)}. ${question.options[question.correct]}</strong></p>
                    </div>
                </div>
            `;
}

function selectOption(questionIndex, optionIndex) {
    if (userAnswers[questionIndex] !== undefined) return;

    userAnswers[questionIndex] = optionIndex;
    updateDisplay();
}

function submitAnswer(questionIndex) {
    if (userAnswers[questionIndex] === undefined) return;

    const question = questions[questionIndex];
    if (userAnswers[questionIndex] === question.correct) {
        score++;
    }

    updateDisplay();
    updateProgress();
    updateScore();

    if (Object.keys(userAnswers).length === questions.length) {
        setTimeout(() => {
            showQuizCompleted();
        }, 1000);
    }
}

function toggleExplanation(questionIndex) {
    const explanation = document.getElementById(`explanation-${questionIndex}`);
    explanation.classList.toggle('show');
}

function updateDisplay() {
    const container = document.getElementById('quizContainer');
    container.innerHTML = questions.map((_, index) => renderQuestion(index)).join('');
}

function updateProgress() {
    const answered = Object.keys(userAnswers).length;
    const progress = (answered / questions.length) * 100;
    document.getElementById('progressBar').style.width = progress + '%';
}

function updateScore() {
    // Score display removed - function kept for compatibility
}

function showQuizCompleted() {
    const percentage = Math.round((score / questions.length) * 100);
    let message = '';
    let emoji = '';

    if (percentage >= 90) {
        message = 'Outstanding! You\'re a quiz master!';
        emoji = '🏆';
    } else if (percentage >= 70) {
        message = 'Great job! You did really well!';
        emoji = '🎉';
    } else if (percentage >= 50) {
        message = 'Good effort! Keep learning!';
        emoji = '👍';
    } else {
        message = 'Keep studying and try again!';
        emoji = '📚';
    }

    const completedDiv = document.createElement('div');
    completedDiv.className = 'quiz-completed';
    completedDiv.innerHTML = `
                <h2>${emoji} Quiz Completed!</h2>
                <p>Your final score: <strong>${score}/${questions.length} (${percentage}%)</strong></p>
                <p>${message}</p>
                <button class="btn btn-primary" onclick="restartQuiz()" style="margin-top: 20px;">Take Quiz Again</button>
            `;

    document.getElementById('quizContainer').appendChild(completedDiv);
    quizCompleted = true;
}

function restartQuiz() {
    selectTopic(currentTopic);
}

function loadMoreQuestions() {
    const filteredQuestions = getFilteredQuestions();
    const remainingQuestions = filteredQuestions.length - questionsLoaded;
    if (remainingQuestions <= 0) return;

    const questionsToLoad = Math.min(5, remainingQuestions);
    const newQuestions = filteredQuestions.slice(questionsLoaded, questionsLoaded + questionsToLoad);

    questions = questions.concat(newQuestions);
    questionsLoaded += questionsToLoad;

    updateDisplay();
    updateProgress();
    updateScore();
    updateLoadMoreButton();

    setTimeout(() => {
        const firstNewQuestion = document.querySelector(`[data-question-index="${questions.length - questionsToLoad}"]`);
        if (firstNewQuestion) {
            firstNewQuestion.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
    }, 100);
}

function updateLoadMoreButton() {
    const loadMoreBtn = document.getElementById('loadMoreBtn');
    const filteredQuestions = getFilteredQuestions();
    const remainingQuestions = filteredQuestions.length - questionsLoaded;

    if (remainingQuestions <= 0) {
        loadMoreBtn.textContent = '✅ All Questions Loaded';
        loadMoreBtn.disabled = true;
    } else {
        loadMoreBtn.textContent = `🔥 Load More Questions (${remainingQuestions} remaining)`;
        loadMoreBtn.disabled = false;
    }
}

// Initialize the quiz
updateDisplay();
updateProgress();
updateScore();
updateLoadMoreButton();
