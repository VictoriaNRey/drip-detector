# Vibe Detector Quiz
# Vibes: Soft, Casual, Preppy, Alternative, Gamer, Sporty
# Authors: Christine Bui, Victoria Rey

from collections import defaultdict  # Used to store vibe scores

# Each question has answer choices that map to one or more vibes
# The algorithm will count points for each vibe based on answers

questions = [
    {
        "question": "What is your gender?",
        "options": {
            "A": {"text": "Girl", "vibes": []},  # Does not affect scoring
            "B": {"text": "Boy", "vibes": []},
            "C": {"text": "Other / Prefer not to say", "vibes": []},
        },
    },
    {
        "question": "Favorite hobbies?",
        "options": {
            "A": {"text": "Reading, journaling, or relaxing", "vibes": ["Soft"]},
            "B": {"text": "Hanging out with friends, watching shows", "vibes": ["Casual"]},
            "C": {"text": "Golf, studying, or structured activities", "vibes": ["Preppy"]},
            "D": {"text": "Gaming or being online", "vibes": ["Gamer"]},
            "E": {"text": "Working out or playing sports", "vibes": ["Sporty"]},
            "F": {"text": "Art, music, or creative expression", "vibes": ["Alternative"]},
        },
    },
    {
        "question": "Where do you like to go?",
        "options": {
            "A": {"text": "Cute cafes or bookstores", "vibes": ["Soft"]},
            "B": {"text": "Mall, Target, or casual spots", "vibes": ["Casual"]},
            "C": {"text": "Brunch, nice areas, or events", "vibes": ["Preppy"]},
            "D": {"text": "Stay home or gaming setups", "vibes": ["Gamer"]},
            "E": {"text": "Gym, park, or outdoors", "vibes": ["Sporty"]},
            "F": {"text": "Concerts or thrift stores", "vibes": ["Alternative"]},
        },
    },
    {
        "question": "What colors do you usually wear?",
        "options": {
            "A": {"text": "Pastels and light colors", "vibes": ["Soft"]},
            "B": {"text": "Neutrals like black, white, gray", "vibes": ["Casual"]},
            "C": {"text": "Classic tones like navy and beige", "vibes": ["Preppy"]},
            "D": {"text": "Dark and bold colors", "vibes": ["Alternative"]},
            "E": {"text": "Bright or athletic colors", "vibes": ["Sporty"]},
            "F": {"text": "Whatever is comfortable", "vibes": ["Gamer"]},
        },
    },
    {
        "question": "Personality? Worst trait?",
        "options": {
            "A": {"text": "Too emotional or sensitive", "vibes": ["Soft"]},
            "B": {"text": "Lazy or unmotivated", "vibes": ["Casual"]},
            "C": {"text": "Too perfectionist", "vibes": ["Preppy"]},
            "D": {"text": "Too chaotic or unpredictable", "vibes": ["Alternative"]},
            "E": {"text": "Too competitive", "vibes": ["Sporty"]},
            "F": {"text": "Too online or distracted", "vibes": ["Gamer"]},
        },
    },
    {
        "question": "How much effort do you put into getting ready?",
        "options": {
            "A": {"text": "A lot, I love looking cute", "vibes": ["Soft", "Preppy"]},
            "B": {"text": "Just enough", "vibes": ["Casual"]},
            "C": {"text": "Very little effort", "vibes": ["Gamer"]},
            "D": {"text": "Depends, but I like standing out", "vibes": ["Alternative"]},
            "E": {"text": "Quick and practical", "vibes": ["Sporty"]},
        },
    },
    {
        "question": "What kind of shoes do you usually wear?",
        "options": {
            "A": {"text": "Cute flats or sandals", "vibes": ["Soft"]},
            "B": {"text": "Basic sneakers", "vibes": ["Casual"]},
            "C": {"text": "Loafers or polished shoes", "vibes": ["Preppy"]},
            "D": {"text": "Boots or statement shoes", "vibes": ["Alternative"]},
            "E": {"text": "Running shoes", "vibes": ["Sporty"]},
            "F": {"text": "Slides or whatever is closest", "vibes": ["Gamer"]},
        },
    },
    {
        "question": "What kind of music do you usually listen to?",
        "options": {
            "A": {"text": "Soft pop or indie", "vibes": ["Soft"]},
            "B": {"text": "Popular music", "vibes": ["Casual"]},
            "C": {"text": "Classy or polished playlists", "vibes": ["Preppy"]},
            "D": {"text": "Rock or alternative", "vibes": ["Alternative"]},
            "E": {"text": "Workout or hype music", "vibes": ["Sporty"]},
            "F": {"text": "Game soundtracks or lo-fi", "vibes": ["Gamer"]},
        },
    },
    {
        "question": "What’s your favorite drink?",
        "options": {
            "A": {"text": "Matcha or something cute", "vibes": ["Soft"]},
            "B": {"text": "Iced coffee", "vibes": ["Casual"]},
            "C": {"text": "Latte or something classy", "vibes": ["Preppy"]},
            "D": {"text": "Energy drink", "vibes": ["Alternative", "Gamer"]},
            "E": {"text": "Protein shake or water", "vibes": ["Sporty"]},
        },
    },
    {
        "question": "Where do you usually shop?",
        "options": {
            "A": {"text": "Boutiques or aesthetic stores", "vibes": ["Soft"]},
            "B": {"text": "Target or basic stores", "vibes": ["Casual"]},
            "C": {"text": "Classic clothing stores", "vibes": ["Preppy"]},
            "D": {"text": "Thrift or alt stores", "vibes": ["Alternative"]},
            "E": {"text": "Athletic stores", "vibes": ["Sporty"]},
            "F": {"text": "Online only", "vibes": ["Gamer"]},
        },
    },
    {
        "question": "What accessories do you usually wear?",
        "options": {
            "A": {"text": "Dainty jewelry or bows", "vibes": ["Soft"]},
            "B": {"text": "None or minimal", "vibes": ["Casual"]},
            "C": {"text": "Watch or polished jewelry", "vibes": ["Preppy"]},
            "D": {"text": "Chains or statement pieces", "vibes": ["Alternative"]},
            "E": {"text": "Cap or fitness watch", "vibes": ["Sporty"]},
            "F": {"text": "Headset counts", "vibes": ["Gamer"]},
        },
    },
]

# Takes list of answers and returns final vibe
def calculate_vibe(answers: list[str]) -> str:
    scores: defaultdict[str, int] = defaultdict(int)

    for question, answer in zip(questions, answers):
        answer = answer.upper()
        if answer in question["options"]:
            for vibe in question["options"][answer]["vibes"]:
                scores[vibe] += 1

    if not scores:
        return "Casual"

    max_score = max(scores.values())
    top_vibes = [v for v, s in scores.items() if s == max_score]

    vibe_order = ["Soft", "Casual", "Preppy", "Alternative", "Gamer", "Sporty"]
    for vibe in vibe_order:
        if vibe in top_vibes:
            return vibe

    return "Casual"
