from drip_detector import calculate_vibe


def test_soft_result():
    answers = ["A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A"]
    assert calculate_vibe(answers) == "Soft"


def test_casual_result():
    answers = ["A", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B"]
    assert calculate_vibe(answers) == "Casual"


def test_preppy_result():
    answers = ["A", "C", "C", "C", "C", "A", "C", "C", "C", "C", "C"]
    assert calculate_vibe(answers) == "Preppy"


def test_gamer_result():
    answers = ["A", "D", "D", "D", "D", "B", "D", "D", "D", "D", "D"]
    assert calculate_vibe(answers) == "Gamer"


def test_sporty_result():
    answers = ["A", "E", "E", "E", "E", "C", "E", "E", "E", "E", "E"]
    assert calculate_vibe(answers) == "Sporty"


def test_alternative_result():
    answers = ["A", "F", "F", "F", "F", "D", "F", "F", "F", "F", "F"]
    assert calculate_vibe(answers) == "Alternative"


def test_tie_breaker_returns_soft_first():
    answers = ["A", "A", "B", "A", "B", "A", "B", "A", "B", "A", "B"]
    assert calculate_vibe(answers) == "Soft"


def test_no_scoring_answers_defaults_to_casual():
    answers = ["A"]
    assert calculate_vibe(answers) == "Casual"