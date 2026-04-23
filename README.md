# drip-detector
detects your vibe based on a few quiz questions :)

## Project Overview

The app asks a series of questions, collects your answers, figures out your vibe, and shows a result with an image and description.

The six possible vibes are:

- Soft
- Casual
- Preppy
- Alternative
- Gamer
- Sporty

## Running the App

1. Make sure you're in the project folder
2. Run the main file: drip_detector.py

The quiz window should pop up and you're good to go.

## Running Tests

If you want to run the tests, use pytest

This will run everything in the tests/ folder and show you what passes/fails.

If pytest isn’t installed: pip install pytest

### components

- **Business logic**
  - `calculate_vibe(answers)` computes the final vibe from a list of answer choices
  - `questions` stores the quiz questions, answer options, and vibe mappings

- **Interface layer**
  - `DripDetectorQuiz` manages the Tkinter GUI
  - The GUI handles rendering questions, collecting input, navigation, result display, and animation
  - The GUI calls the underlying quiz logic rather than duplicating scoring behavior

## Use of AI Tools

AI tools (e.g., ChatGPT) were used to assist with formatting reusable function structures and organizing question/answer templates. AI was also used for brainstorming minor UI enhancements.

All algorithm development, integration, debugging, and final code decisions were completed by the project team.

