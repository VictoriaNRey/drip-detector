# drip-detector
detects your vibe based on a few quiz questions :)

## Project Overview

The app asks a series of questions, collects your answers, figures out your vibe, and shows a result with an image and description

The six possible vibes are:

- Soft
- Casual
- Preppy
- Alternative
- Gamer
- Sporty

## Running the App

1. Make sure you're in the project folder
2. Run the main file: 

```bash
drip_detector.py
```

The quiz window should pop up and you're good to go!

## Running Tests

If you want to run the tests

```bash
python -m pytest
``` 

This will run all tests in test_drip_detector.py file and show you what passes/fails

If pytest isn’t installed: pip install pytest

## Components

- **Business logic**
  - `calculate_vibe(answers)` figures out your final vibe based on your answers
  - `questions` holds all the quiz questions, answer choices, and vibe mappings

- **Interface layer**
  - `DripDetectorQuiz` runs the Tkinter GUI
  - Handles displaying questions, collecting answers, moving between screens, and showing results
  - Uses the quiz logic instead of redoing the scoring in the GUI

## Use of AI Tools

AI tools were used in part to help format some functions and organize the question/answer structure. It was also used to brainstorm a few UI ideas

All core logic, debugging, and final implementation decisions were done by the project team, and anything from AI was reviewed and adjusted before being used