# 📘 TextAnalyzer Learning Web - Complete Documentation

## 📋 Table of Contents

1. [Project Overview](#project-overview)
2. [Core Concept](#core-concept)
3. [System Architecture](#system-architecture)
4. [Scoring Algorithm](#scoring-algorithm)
5. [Application Flow](#application-flow)
6. [Technical Implementation](#technical-implementation)
7. [Data Flow Diagram](#data-flow-diagram)
8. [Scoring Issues & Solutions](#scoring-issues--solutions)
9. [Future Improvements](#future-improvements)

---

## 🎯 Project Overview

### What is TextAnalyzer?

**TextAnalyzer Learning Web** is an educational web application designed to help children aged 6-10 years old learn polite and effective communication skills through interactive scenarios.

### Target Users
- **Primary**: Children (6-10 years old)
- **Secondary**: Teachers, Parents (creating scenarios)

### Learning Goals
- Practice polite communication
- Develop empathy and emotional intelligence
- Learn situation-appropriate responses
- Build confidence in social interactions

---

## 💡 Core Concept

### Educational Philosophy

The application uses a **"Learn by Doing"** approach:

```
Present Scenario → Student Responds → Analyze Response → Give Feedback → Practice Again
```

### Four Communication Goals

1. **Giving Feedback** (`giving_feedback`)
   - Teaching constructive criticism
   - Focusing on solutions, not problems
   - Using gentle language

2. **Polite Refusal** (`polite_refusal`)
   - Saying "no" without hurting feelings
   - Providing reasons
   - Offering alternatives

3. **Apologizing** (`apologizing`)
   - Taking responsibility
   - Showing empathy
   - Promising improvement

4. **Asking for Help** (`asking_for_help`)
   - Being polite and clear
   - Explaining the need
   - Expressing gratitude

---

## 🏗️ System Architecture

### Technology Stack

```
Frontend:
├── HTML5 (Semantic markup)
├── CSS3 (Custom properties, Flexbox, Grid)
└── Vanilla JavaScript (Form validation, interactions)

Backend:
├── Python 3.8+
├── Flask (Web framework)
├── ANTLR 4 (Lexical analysis)
└── OpenAI API (AI-powered feedback)

Analysis Engine:
├── ANTLR Grammar (Token classification)
├── Context-Aware Analyzer (Semantic analysis)
└── Scoring Engine (Multi-criteria evaluation)
```

### Project Structure

```
TextAnalyzer_Learning_Web/
│
├── analysis/                    # ANTLR & Analysis modules
│   ├── grammar/
│   │   ├── SentenceLexer.g4    # Token definitions
│   │   └── SentenceParser.g4   # Grammar rules
│   ├── generated/              # ANTLR-generated files
│   ├── analyzer.py             # Context-aware analyzer
│   └── parser_runner.py        # ANTLR runner
│
├── logic/                       # Business logic
│   ├── evaluator.py            # Response evaluation
│   ├── hint_engine.py          # Hint generation
│   └── lesson_engine.py        # Lesson creation
│
├── routes/                      # Flask routes
│   ├── home.py                 # Homepage
│   ├── scenario.py             # Scenario display
│   ├── answer.py               # Answer submission
│   ├── feedback.py             # Feedback display
│   └── admin.py                # Admin functions
│
├── templates/                   # HTML templates
│   ├── index.html
│   ├── scenario.html
│   ├── feedback.html
│   └── admin_create.html
│
├── static/                      # Static assets
│   └── css/
│       ├── main.css            # Global styles
│       ├── home.css            # Home page styles
│       ├── scenario.css        # Scenario page styles
│       └── feedback.css        # Feedback page styles
│
├── scenarios/                   # Scenario data
│   ├── default_scenarios.json
│   └── custom_scenarios.json
│
├── app.py                       # Flask application
├── config.py                    # Configuration
└── .env                         # Environment variables
```

---

## 📊 Scoring Algorithm

### Current Scoring System (Improved Version)

The scoring system evaluates responses across **5 main criteria**:

#### 1. Politeness Score (0-30 points)

```python
Base Score: 0

+ Has greeting (hi, hello)                → +5
+ Has thank you                           → +5
+ Uses "please"                           → +5
+ Has softening words (maybe, I think)    → +8
+ Has polite verbs (could, would, may)    → +7

Maximum: 30 points
```

**Example:**
```
"Hi! Could you please help me? Thank you!"
→ Greeting(5) + Please(5) + Polite verb(7) + Thank you(5) = 22/30
```

#### 2. Emotion Score (0-25 points)

```python
Base Score: 15 (neutral)

If positive emotion detected                → +10
If negative emotion detected                → -10
If shows empathy (understand, feel, know)   → +5

Constrained to: 0-25 points
```

**Example:**
```
"I understand you're upset. I'm sorry."
→ Base(15) + Empathy(5) = 20/25
```

#### 3. Structure Score (0-20 points)

```python
Base Score: 10

+ Each polite structure (up to 10 pts)     → +3 each
- Each harsh structure                      → -5 each

Examples of polite structures:
- "Could you..."
- "Would you mind..."
- "I think..."

Examples of harsh structures:
- "You must..."
- "You always..."
- "Why don't you..."

Constrained to: 0-20 points
```

**Example:**
```
"You must help me now!" 
→ Base(10) - Harsh structure(5) = 5/20
```

#### 4. Goal Alignment Score (0-25 points)

Evaluates if the response fits the communication goal:

```python
Base Score: 100 (then scaled to 25)

For each REQUIRED element missing     → -20
For each RECOMMENDED element missing  → -10
For each element to AVOID present     → -15

Final score = (adjusted_score / 4)  # Scale 100 → 25
```

**Goal Requirements Example (Apologizing):**

```python
{
    'required': ['APOLOGY_WORD'],              # Must have
    'recommended': ['EMPATHY_WORD', 'SOFT_WORD'], # Should have
    'avoid': ['STRONG_WORD', 'COMMAND_WORD']   # Shouldn't have
}
```

**Calculation Example:**
```
"I'm really sorry. I understand how you feel."

Required:
✓ Has APOLOGY_WORD ("sorry") → No penalty

Recommended:
✓ Has EMPATHY_WORD ("understand") → No penalty
✓ Has implicit softening → No penalty

Avoid:
✓ No STRONG_WORD → No penalty
✓ No COMMAND_WORD → No penalty

Score: 100 / 4 = 25/25
```

#### 5. Penalty System

```python
Penalties (deducted from total):

- Has strong/harsh words (stupid, bad, wrong)  → -10
- Has command words (must, have to)            → -8
- Shows negative emotion                       → -5

Total penalties are subtracted from combined score
```

### Final Score Calculation

```python
overall_score = (
    politeness_score +      # 0-30
    emotion_score +         # 0-25
    structure_score +       # 0-20
    goal_alignment_score -  # 0-25
    penalties               # variable
)

# Constrain to 0-100
overall_score = max(0, min(100, overall_score))
```

### Score Interpretation

```
85-100: Excellent! Very polite and thoughtful
70-84:  Good! Polite with minor improvements needed
55-69:  Okay. Can be improved with more polite elements
40-54:  Needs work. Missing key polite elements
0-39:   Requires significant improvement
```

---

## 🔄 Application Flow

### Complete User Journey

```
┌─────────────────────────────────────────────────────────┐
│                    1. HOMEPAGE                          │
│  User sees available scenarios                          │
│  ↓ Clicks "Start Practice"                             │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│                 2. SCENARIO PAGE                         │
│  ┌──────────────────────────────────────────┐          │
│  │  Story: "Your friend borrowed your       │          │
│  │  pencil and broke it..."                 │          │
│  └──────────────────────────────────────────┘          │
│  ┌──────────────────────────────────────────┐          │
│  │  Question: "What would you say?"         │          │
│  └──────────────────────────────────────────┘          │
│  ┌──────────────────────────────────────────┐          │
│  │  [Text Area for User Answer]             │          │
│  │  "Hi Alex! It's okay, accidents happen.  │          │
│  │   Maybe we can fix it together?"         │          │
│  └──────────────────────────────────────────┘          │
│  ↓ Clicks "Submit"                                      │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│              3. BACKEND PROCESSING                       │
│                                                          │
│  Step 3.1: Parse with ANTLR                             │
│  ┌──────────────────────────────────────────┐          │
│  │ Tokens: [GREETING, PRONOUN, SOFT_WORD,   │          │
│  │         POSITIVE_ADJ, QUESTION_WORD]      │          │
│  └──────────────────────────────────────────┘          │
│                    ↓                                     │
│  Step 3.2: Context Analysis                             │
│  ┌──────────────────────────────────────────┐          │
│  │ • Sentiment: Positive                     │          │
│  │ • Structure: Polite                       │          │
│  │ • Goal fit: 85% match                     │          │
│  └──────────────────────────────────────────┘          │
│                    ↓                                     │
│  Step 3.3: Calculate Score                              │
│  ┌──────────────────────────────────────────┐          │
│  │ Politeness:        22/30                  │          │
│  │ Emotion:           23/25                  │          │
│  │ Structure:         18/20                  │          │
│  │ Goal Alignment:    21/25                  │          │
│  │ Penalties:         -0                     │          │
│  │ ───────────────────────                   │          │
│  │ TOTAL:             84/100 ✓               │          │
│  └──────────────────────────────────────────┘          │
│                    ↓                                     │
│  Step 3.4: Generate Feedback                            │
│  ┌──────────────────────────────────────────┐          │
│  │ AI creates improvement example            │          │
│  │ Template selects appropriate hints        │          │
│  │ Lesson engine creates personalized lesson │          │
│  └──────────────────────────────────────────┘          │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│                4. FEEDBACK PAGE                          │
│                                                          │
│  ┌────────────────────────────────────────┐            │
│  │         🎉 Great Job!                   │            │
│  │            84/100                        │            │
│  │        Style: Very Polite                │            │
│  └────────────────────────────────────────┘            │
│                                                          │
│  ┌────────────────────────────────────────┐            │
│  │  Your Answer (with highlights):         │            │
│  │  [Hi] [It's okay] [Maybe] we can fix it │            │
│  │   Green   Green    Green                 │            │
│  └────────────────────────────────────────┘            │
│                                                          │
│  ✅ What You Did Well:                                  │
│  • Used a friendly greeting                             │
│  • Showed understanding                                 │
│  • Offered a solution                                   │
│                                                          │
│  💡 You Can Improve:                                    │
│  • Try adding "thank you" at the end                   │
│                                                          │
│  📚 Today's Lesson:                                     │
│  Good communication focuses on solutions...             │
│                                                          │
│  [Try Again] [Go Home]                                  │
└─────────────────────────────────────────────────────────┘
```

---

## 🔧 Technical Implementation

### Step-by-Step Processing

#### Step 1: Token Extraction (ANTLR)

**Input:** `"Hi! Could you please help me?"`

**ANTLR Processing:**
```python
# SentenceLexer.g4 tokenizes
tokens = [
    'GREETING',      # "Hi"
    'POLITE_VERB',   # "Could"
    'PRONOUN',       # "you"
    'SOFT_WORD',     # "please"
    'REQUEST_WORD',  # "help"
    'PRONOUN',       # "me"
    'PUNCT'          # "?"
]
```

#### Step 2: Sentiment Analysis

```python
def _analyze_sentiment(text):
    patterns = {
        'positive': [r'\b(love|like|happy|glad|wonderful)\b'],
        'negative': [r'\b(hate|sad|angry|upset|terrible)\b'],
        'apologetic': [r'\b(sorry|apologize|forgive)\b'],
        'empathetic': [r'\b(understand|feel|know how)\b']
    }
    
    # Count matches
    scores = {
        'positive': 2,    # "love", "happy"
        'negative': 0,
        'apologetic': 1,  # "sorry"
        'empathetic': 0
    }
    
    # Determine dominant
    return {
        'dominant': 'positive',
        'is_balanced': False
    }
```

#### Step 3: Structure Analysis

```python
def _analyze_structure(text):
    polite_count = 0
    harsh_count = 0
    
    # Check polite patterns
    for pattern in [r'\b(could you|would you)\b', r'\b(please)\b']:
        polite_count += len(re.findall(pattern, text))
    
    # Check harsh patterns
    for pattern in [r'\b(you must|you should)\b']:
        harsh_count += len(re.findall(pattern, text))
    
    return {
        'polite_count': polite_count,
        'harsh_count': harsh_count,
        'tone': 'polite' if polite_count > harsh_count else 'harsh'
    }
```

#### Step 4: Goal Alignment Check

```python
def _check_goal_alignment(tokens, goal):
    requirements = {
        'asking_for_help': {
            'required': ['POLITE_VERB', 'REQUEST_WORD'],
            'recommended': ['THANK_YOU', 'SOFT_WORD'],
            'avoid': ['COMMAND_WORD', 'STRONG_WORD']
        }
    }
    
    reqs = requirements[goal]
    score = 100
    missing = []
    
    # Check required
    for req in reqs['required']:
        if req not in tokens:
            score -= 20
            missing.append(req)
    
    # Check recommended
    for rec in reqs['recommended']:
        if rec not in tokens:
            score -= 10
    
    # Check avoid
    for avoid in reqs['avoid']:
        if avoid in tokens:
            score -= 15
    
    return {
        'score': max(0, score),
        'missing_elements': missing,
        'aligned': score >= 60
    }
```

#### Step 5: Score Calculation

```python
def _calculate_detailed_scores(features, sentiment, structure, goal_alignment):
    # 1. Politeness (0-30)
    politeness = 0
    if features["has_greeting"]: politeness += 5
    if features["has_thank_you"]: politeness += 5
    if features["has_please"]: politeness += 5
    if features["has_softening"]: politeness += 8
    if features["has_polite_verb"]: politeness += 7
    
    # 2. Emotion (0-25)
    emotion = 15  # base
    if sentiment['dominant'] == 'positive': emotion += 10
    if features["has_empathy"]: emotion += 5
    emotion = max(0, min(25, emotion))
    
    # 3. Structure (0-20)
    structure_score = 10  # base
    structure_score += min(10, structure['polite_count'] * 3)
    structure_score -= structure['harsh_count'] * 5
    structure_score = max(0, min(20, structure_score))
    
    # 4. Goal (0-25)
    goal_score = goal_alignment['score'] / 4  # scale 100→25
    
    # 5. Penalties
    penalty = 0
    if features["has_strong"]: penalty += 10
    if features["has_command"]: penalty += 8
    if features["has_negative_emotion"]: penalty += 5
    
    # Total
    overall = politeness + emotion + structure_score + goal_score - penalty
    overall = max(0, min(100, int(overall)))
    
    return {
        'politeness': politeness,
        'emotion': emotion,
        'structure': structure_score,
        'goal_alignment': goal_score,
        'penalty': penalty,
        'overall': overall
    }
```

---

## 📈 Data Flow Diagram

### Complete System Flow

```
┌──────────────┐
│    USER      │
│  (Student)   │
└──────┬───────┘
       │
       │ 1. Selects scenario
       ↓
┌──────────────────┐
│   HOME PAGE      │ ← scenarios/default_scenarios.json
│   (index.html)   │
└──────┬───────────┘
       │
       │ 2. Views scenario + Writes answer
       ↓
┌───────────────────┐
│  SCENARIO PAGE    │
│  (scenario.html)  │
└──────┬────────────┘
       │
       │ 3. POST /answer/<id>
       ↓
┌────────────────────────────┐
│   ANSWER ROUTE             │
│   (routes/answer.py)       │
│                            │
│ • Save to session          │
│ • Track attempts           │
│ • Redirect to feedback     │
└────────────┬───────────────┘
             │
             │ 4. GET /feedback/<id>
             ↓
┌──────────────────────────────────────────────────┐
│           FEEDBACK ROUTE                         │
│           (routes/feedback.py)                   │
│                                                  │
│  ┌─────────────────────────────────────┐       │
│  │  Step 1: Call Evaluator              │       │
│  │  logic/evaluator.py                  │       │
│  │                                       │       │
│  │  ┌────────────────────────────────┐ │       │
│  │  │  ANTLR Analysis                 │ │       │
│  │  │  analysis/analyzer.py           │ │       │
│  │  │                                 │ │       │
│  │  │  • Parse with ANTLR             │ │       │
│  │  │  • Extract tokens               │ │       │
│  │  │  • Analyze sentiment            │ │       │
│  │  │  • Check structure              │ │       │
│  │  │  • Verify goal alignment        │ │       │
│  │  │  • Calculate scores             │ │       │
│  │  └────────────────────────────────┘ │       │
│  └─────────────┬───────────────────────┘       │
│                │                                 │
│                │ evaluation_result               │
│                ↓                                 │
│  ┌─────────────────────────────────────┐       │
│  │  Step 2: Generate Lesson             │       │
│  │  logic/lesson_engine.py              │       │
│  │                                       │       │
│  │  • Determine lesson type             │       │
│  │  • Create personalized content       │       │
│  │  • Add practice tips                 │       │
│  └─────────────┬───────────────────────┘       │
│                │                                 │
│                │ lesson_data                     │
│                ↓                                 │
│  ┌─────────────────────────────────────┐       │
│  │  Step 3: Generate Hints              │       │
│  │  logic/hint_engine.py                │       │
│  │                                       │       │
│  │  • Select from templates             │       │
│  │  • Create example (AI if needed)     │       │
│  │  • Get useful phrases                │       │
│  └─────────────┬───────────────────────┘       │
│                │                                 │
│                │ hint_data                       │
│                ↓                                 │
│  ┌─────────────────────────────────────┐       │
│  │  Step 4: Render Template             │       │
│  │  templates/feedback.html             │       │
│  │                                       │       │
│  │  • Display score                     │       │
│  │  • Highlight words                   │       │
│  │  • Show analysis                     │       │
│  │  • Present suggestions               │       │
│  │  • Display lesson                    │       │
│  └─────────────────────────────────────┘       │
└──────────────────┬───────────────────────────────┘
                   │
                   │ 5. HTML response
                   ↓
            ┌──────────────┐
            │  FEEDBACK    │
            │  PAGE        │
            │              │
            │ User sees    │
            │ results      │
            └──────────────┘
```

---

## ⚠️ Scoring Issues & Solutions

### Issue 1: Score Too Low for Good Responses

**Problem:**
```
Input: "Hi! I'm sorry. I know you're upset."
Expected: 75+
Actual: 47
```

**Root Cause:**
- Old system only counted presence of tokens
- Didn't consider context
- No bonus for combined elements

**Solution:**
```python
# OLD (Bad)
score = 50
if has_greeting: score += 10
if has_apology: score += 10
# Result: 70

# NEW (Good)
score = 0
score += politeness_score   # Up to 30
score += emotion_score      # Up to 25
score += structure_score    # Up to 20
score += goal_score         # Up to 25
# Result: 84
```

### Issue 2: Goal Alignment Not Considered

**Problem:**
```
Scenario Goal: "Asking for Help"
Answer: "I'm very happy today!"
Score: 65 (Too high!)
```

**Root Cause:**
- Answer is polite but doesn't match goal
- System rewards politeness regardless of relevance

**Solution:**
```python
# Check goal alignment
goal_alignment = check_goal_alignment(tokens, scenario_goal)

if goal_alignment['score'] < 60:
    # Apply penalty for not matching goal
    final_score -= 15
```

### Issue 3: No Penalty for Negative Elements

**Problem:**
```
Answer: "You're stupid! But please help me."
Score: 70 (Has "please", so high score)
```

**Root Cause:**
- System only adds points, never subtracts
- Strong words not penalized enough

**Solution:**
```python
# Apply penalties
penalty = 0
if has_strong_words: penalty += 10
if has_command_tone: penalty += 8
if negative_emotion: penalty += 5

final_score = base_score - penalty
```

### Issue 4: Context Ignored

**Problem:**
```
"sorry sorry sorry sorry sorry"
Score: 100 (Each "sorry" adds points)
```

**Root Cause:**
- Counting tokens, not understanding meaning
- No semantic analysis

**Solution:**
```python
# Analyze sentiment and context
sentiment = analyze_sentiment(text)
structure = analyze_structure(text)

# Check if genuinely apologetic or just repetitive
if sentiment['is_genuine'] and structure['is_coherent']:
    score += bonus
else:
    score -= penalty_for_spam
```

---

## 🚀 Future Improvements

### Short-term (1-2 months)

1. **Better AI Integration**
   ```python
   # Use AI to evaluate tone and intent
   ai_score = evaluate_with_ai(answer, context)
   final_score = (antlr_score * 0.7) + (ai_score * 0.3)
   ```

2. **Progress Tracking**
   ```python
   # Store user progress in database
   user_progress = {
       'scenarios_completed': [],
       'average_score': 75,
       'strengths': ['politeness', 'empathy'],
       'needs_work': ['goal_alignment']
   }
   ```

3. **Adaptive Difficulty**
   ```python
   # Adjust scenario difficulty based on performance
   if average_score > 80:
       recommend_advanced_scenarios()
   else:
       recommend_practice_scenarios()
   ```

### Medium-term (3-6 months)

4. **Multi-language Support**
   - Vietnamese scenarios
   - Thai scenarios
   - Localized feedback

5. **Voice Input**
   - Record spoken responses
   - Analyze tone and emotion
   - Provide pronunciation feedback

6. **Gamification**
   - Badges and achievements
   - Leaderboards
   - Daily challenges

### Long-term (6-12 months)

7. **AI-Generated Scenarios**
   ```python
   # Generate personalized scenarios
   scenario = ai_generate_scenario(
       user_level=student.level,
       interests=student.interests,
       needs_work=student.weak_areas
   )
   ```

8. **Peer Learning**
   - Students review each other
   - Collaborative scenarios
   - Group challenges

9. **Teacher Dashboard**
   - Class progress overview
   - Individual student analytics
   - Custom lesson plans

---

## 📊 Scoring Formula Summary

### Quick Reference

```
TOTAL SCORE = P + E + S + G - PENALTIES

Where:
P = Politeness (0-30)
    = Greeting(5) + ThankYou(5) + Please(5) + Softening(8) + PoliteVerb(7)

E = Emotion (0-25)
    = Base(15) + Positive(10) OR Negative(-10) + Empathy(5)

S = Structure (0-20)
    = Base(10) + PoliteStructures(3 each, max 10) - HarshStructures(5 each)

G = Goal Alignment (0-25)
    = (100 - Missing_Required(20 each) - Missing_Recommended(10 each) 
       - Has_Avoid(15 each)) / 4

PENALTIES = StrongWords(10) + Commands(8) + NegativeEmotion(5)

FINAL = max(0, min(100, TOTAL))
```

### Example Calculations

#### Example 1: Excellent Response
```
Input: "Hi! I'm sorry for breaking your pencil. I understand you're upset. 
        Could we fix it together? Thank you for understanding!"

Goal: Apologizing

Breakdown:
✓ Greeting (Hi)                    → +5
✓ Apology (sorry)                  → In empathy
✓ Empathy (understand)             → +5
✓ Polite verb (Could)              → +7
✓ Thank you                        → +5
✓ Softening (together)             → +8
✓ Positive tone                    → +10
✓ Polite structure ("Could we")    → +3

Politeness: 5 + 5 + 7 + 8 = 25/30
Emotion: 15 + 10 + 5 = 25/25 (capped)
Structure: 10 + 3 = 13/20
Goal: (100 - 0) / 4 = 25/25
Penalties: 0

TOTAL: 25 + 25 + 13 + 25 - 0 = 88/100 ✓
```

#### Example 2: Poor Response
```
Input: "You're stupid! Give me my pencil back now!"

Goal: Apologizing

Breakdown:
✗ No greeting                      → 0
✗ No apology                       → Missing required (-20)
✗ Strong word (stupid)             → -10 penalty
✗ Command (Give me, now)           → -8 penalty
✗ Harsh structure ("Give me")      → -5

Politeness: 0/30
Emotion: 15 - 10 (negative) = 5/25
Structure: 10 - 5 = 5/20
Goal: (100 - 20 - 30) / 4 = 12.5/25
Penalties: 10 + 8 = 18

TOTAL: 0 + 5 + 5 + 12.5 - 18 = 4.5 ≈ 5/100 ✗
```

#### Example 3: Average Response
```
Input: "Sorry, I didn't mean to break it."

Goal: Apologizing

Breakdown:
✗ No greeting                      → 0
✓ Apology (Sorry)                  → In empathy
✓ Some explanation                 → +3 structure
✗ No thank you                     → 0
✗ No polite verb                   → 0
✗ No empathy shown                 → 0

Politeness: 0/30
Emotion: 15 + 0 = 15/25
Structure: 10 + 3 = 13/20
Goal: (100 - 0 - 10) / 4 = 22.5/25
Penalties: 0

TOTAL: 0 + 15 + 13 + 22.5 - 0 = 50.5 ≈ 51/100 ~
```

---

##