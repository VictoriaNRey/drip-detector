# drip-detector

detects your vibe based on a few quiz questions :)

*drip - very swag and cool; can be used to describe an outfit/accessory, person, song, etc.*

*used in a sentence: "yall like the drip?"*

## Authors

Christine Bui

Victoria Rey

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

1. Install Python 3 if you have not already done so

2. Download project from GitHub by clicking the green Code button and selecting 'Download Zip'

3. Find the downloaded ZIP file on your computer and extract it then open it

4. Inside the folder, open a terminal

- Windows: right-click in the folder and select “Open in Terminal"

- Mac: right-click the folder and select “New Terminal at Folder” or open Terminal and navigate to the folder

5. Install Pillow image package if needed

*Windows*

```bash
pip install pillow
```

*Mac*

```bash
pip3 install pillow
```

6. Run the quiz by typing this in the terminal

*Windows*

```bash 
python drip_detector.py
```

*Mac*

```bash
python3 drip_detector.py
```

The quiz window should pop up and you're good to go!

## Running Tests

1. Make sure you are inside the project folder (the same folder that contains drip_detector.py and test_drip_detector.py)

2. Open a terminal in that folder

- Windows: right-click inside the folder and select “Open in Terminal”

- Mac: right-click the folder and select “New Terminal at Folder” or open Terminal and navigate to the folder

3. Install pytest if you have not already done so

*Windows*

```bash
pip install pytest
```

*Mac*

```bash
pip3 install pytest
```

4. In the same terminal window, run the tests using Python

*Windows*

```bash
python -m pytest
```

*Mac*

```bash
python3 -m pytest
```

5. The terminal will display the results, showing which tests passed or failed

6. If all tests pass, you will see a message indicating that all tests were successful

This will run all tests in test_drip_detector.py and display the results!

## Components

- Business logic
  - `calculate_vibe(answers)` figures out your final vibe based on your answers
  - `questions` holds all the quiz questions, answer choices, and vibe mappings

- Interface layer
  - `DripDetectorQuiz` runs the Tkinter GUI
  - Handles displaying questions, collecting answers, moving between screens, and showing results
  - Uses the quiz logic instead of redoing the scoring in the GUI

## Use of AI Tools

AI tools were used in part to help format some functions and organize the question/answer structure. It was also used to brainstorm a few UI ideas

All core logic, debugging, and final implementation decisions were done by the project team, and anything from AI was reviewed and adjusted before being used
