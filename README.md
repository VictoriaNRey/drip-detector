# drip-detector
detects your vibe based on a few quiz questions :)

## Project Overview

The application presents the user with a series of questions, collects their answers, calculates their vibe, and displays their result with an image and description.

The six possible vibes are:

- Soft
- Casual
- Preppy
- Alternative
- Gamer
- Sporty

## Software Architecture

The project is organized so that the quiz logic is separate from the GUI

### components

- **Business logic**
  - `calculate_vibe(answers)` computes the final vibe from a list of answer choices
  - `questions` stores the quiz questions, answer options, and vibe mappings

- **Interface layer**
  - `DripDetectorQuiz` manages the Tkinter GUI
  - The GUI handles rendering questions, collecting input, navigation, result display, and animation
  - The GUI calls the underlying quiz logic rather than duplicating scoring behavior
