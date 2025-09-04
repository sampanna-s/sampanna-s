# KBC Quiz Game

This repository contains a simple implementation of the KBC (Kaun Banega Crorepati) quiz game in Python.

## Features

- 15 progressive questions with increasing difficulty
- 3 lifelines: 50-50, Audience Poll, Phone a Friend
- Prize money progression from ₹1,000 to ₹1 Crore
- Interactive command-line interface
- Quit option to leave with current winnings

## How to Play

1. **Clone or download the repository**
2. **Run the game:**
   ```bash
   python3 kbc_game.py
   ```
3. **Follow the on-screen instructions:**
   - Answer questions by typing A, B, C, or D
   - Type 'lifeline' to use available lifelines
   - Type 'quit' to leave with current winnings

## Game Rules

- Answer 15 questions correctly to win ₹1 Crore
- Each question has 4 multiple choice options
- You have 3 lifelines that can be used once each:
  - **50-50**: Eliminates 2 wrong answers
  - **Audience Poll**: Shows simulated audience voting percentages
  - **Phone a Friend**: Get help from a simulated friend
- Wrong answer ends the game (you keep your current winnings)

## Requirements

- Python 3.6 or higher
- No additional packages required (uses only standard library)

## Example Gameplay

```
🎯 WELCOME TO KBC - KAUN BANEGA CROREPATI 🎯

💡 QUESTION 1 FOR ₹1,000
What is the capital of India?
   A) Mumbai
   B) Delhi
   C) Kolkata
   D) Chennai

🆘 Available Lifelines: 50-50, audience_poll, phone_friend

Your answer (A/B/C/D), 'lifeline', or 'quit': B

🎉 CORRECT! You've won ₹1,000
```

## About

This is a learning project created as part of Python programming practice. The game simulates the famous Indian quiz show "Kaun Banega Crorepati" with a simple command-line interface.

---

👋 Hi, I'm @sampanna-s  
👀 I'm interested in coding  
🌱 I'm currently learning python  
💞️ I'm looking to collaborate on project