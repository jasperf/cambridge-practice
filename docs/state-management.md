# State Management in Interactive Tests

This document explains how the interactive test sheets track user answers, correctness, and scores in real-time.

---

## State Object Structure

The central state is stored in a JavaScript object at the top of each worksheet HTML file:

```javascript
const state = {
  answers: {},    // { qid: user's selection }
  correct: {},    // { qid: true/false }
  totalMarks: { math: 0, sci: 0 },
  maxMarks:   { math: 23, sci: 22 },
  startTime: Date.now()
};
```

Supporting metadata:

```javascript
const marks = { m1:2, m2:2, m3:1, ... };  // Points per question
const mathQs = ['m1','m2','m3',...];     // Math question IDs
const sciQs  = ['s1','s2','s3',...];     // Science question IDs
```

---

## State Flow

```
User clicks option
    │
    ▼
selectMCQ(qid, val)  →  state.answers[qid] = val
    │
    ▼
User clicks "Check Answer"
    │
    ▼
checkMCQ(qid, correctVal)  →  state.correct[qid] = (userAnswer === correctVal)
    │
    ▼
markResult(qid, isCorrect)  →  updates UI + triggers updateScores()
    │
    ▼
updateScores()  →  loops through mathQs/sciQs, sums marks where state.correct[qid] === true
```

---

## How State is Updated

### Selection Tracking
When a user selects an answer:
- **MCQ:** `state.answers[qid] = selectedOption` (e.g., `'a'`, `'b'`)
- **Multi-select:** `state.answers[qid] = ['a', 'c']` (array of options)
- **Numeric input:** Value is read from input field at check time

### Correctness Tracking
When a user checks an answer:
- `state.correct[qid] = true/false` is set based on comparison with correct answer
- This is the **source of truth** for scoring

---

## How State is Consumed

### Score Calculation
`updateScores()` reads from `state.correct`:
```javascript
mathQs.forEach(qid => {
  if (state.correct[qid] === true) mathScore += marks[qid];
  if (state.correct[qid] !== undefined) totalAnswered++;
});
```

### Progress Tracking
- Progress bar width: `(totalAnswered / allQuestions) * 100%`
- Score pills update whenever `state.correct` changes

---

## Persistence

Final results are saved to `localStorage` when all questions are answered:

```javascript
const key = `week1_${Date.now()}`;
localStorage.setItem(key, JSON.stringify({ 
  date: new Date().toISOString(), 
  pct, 
  math, 
  sci, 
  time: `${mins}m${secs}s` 
}));
```

---

## Key Principle

**Single source of truth:** The `state` object is the central authority. All UI updates, scoring, and persistence derive from it. DOM elements are just visual representations of this state.
