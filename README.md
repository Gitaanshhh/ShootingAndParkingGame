# ShootingAndParkingGame

This project consists of two Python-based games: a shooting game and a driving/parking game. The primary focus of this project was to implement various features rather than front-end design. It leverages several modules, including `pygame`, `os`, `time`, and `random`, and also includes a leaderboard that tracks the scores and performance of all players.

## Overview

Upon launching the program, the user is greeted with a start screen, where they can press any key to proceed. The next screen prompts the user to either sign up or log in by entering a username. Once the username is entered and confirmed, the main menu appears, offering several options, including different game maps and access to the leaderboard.

### Game 1: Shooting Game

- **Controls**: The player can move using the arrow keys and shoot up to three bullets at a time using the right control button.
- **Gameplay**: A bot respawns randomly on the screen after being shot, adding an element of challenge and unpredictability.

### Game 2: Driving/Parking Game

- **Objective**: The player must park a car within a rectangular box displayed on the screen, using the shortest possible path.
- **Timer**: The game starts a timer when the start button is clicked, and the player's time is recorded upon completion.
- **Leaderboard Integration**: The recorded time is saved along with the username in a text file. The leaderboard is updated every time it is accessed, arranging players in ascending order based on their recorded times.

## Leaderboard

The leaderboard is dynamically updated by organizing player data in increasing order of their completion times. This process occurs every time the leaderboard is accessed, ensuring that the latest data is always displayed.

## Learning Experience

This project was an incredible learning journey. While the focus wasn't on front-end design, I concentrated on integrating as many features as possible to enhance the overall gameplay experience. I thoroughly enjoyed exploring various aspects of game development through this project.
