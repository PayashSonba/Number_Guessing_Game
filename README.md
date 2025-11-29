# Number Guessing Game 🎯

A console-based Python game where players guess a random number between 1 and 100. Features smart hints ("Very close!", "Too high/low"), 10-attempt limits, input validation, and unlimited replays. Built as an internship project demonstrating core Python concepts.

## Description

This project implements a complete number guessing game using only Python's standard library. Players receive progressive hints based on guess proximity, with a maximum of 10 attempts per round. The modular design separates game logic (`play_round()`) from the main loop, making it easy to extend with difficulty levels or persistence. Perfect for practicing loops, conditionals, exception handling, and user experience design in console applications.

## Features

- 🎲 Random number generation (1-100 range)
- 🧠 Proximity hints ("Very close!" within ±5)
- ⏳ 10-attempt limit with win/loss feedback
- ✅ Input validation (skips invalid entries)
- 🔄 Unlimited replay functionality
- 🧩 Clean, modular code structure

## Demo

Guess a number between 1 and 100 (max 10 attempts)!
Attempt 1: 50
Too high!
Attempt 2: 30
Very close! Try a bit higher or lower.
Attempt 3: 35
Correct! You won in 3/10 attempts.

Play again? (y/n): y



## Learning Outcomes

- 🔄 Control flow with loops and conditionals
- 🛡️ Exception handling for user input
- ⚙️ Modular function design
- 🎮 Console user experience best practices

## Future Improvements

- 🎚️ Difficulty modes (easy/medium/hard)
- 📂 High score persistence with JSON
- 🌈 Colored terminal output using `colorama`
- 🌐 Web interface with Flask

## Author

Built by Payash Sonbarsa for internship portfolio preparation.

