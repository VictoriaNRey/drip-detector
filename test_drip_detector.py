from drip_detector import (
    calculate_vibe,
    get_next_button_text,
    get_next_button_state,
    get_shuffled_options,
)


def test_soft_result():
    answers = ["A"] * 11
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


def test_next_button_text_no_answer():
    text = get_next_button_text(0, 11, False)
    assert text == "Select an answer"


def test_next_button_text_mid_quiz():
    text = get_next_button_text(3, 11, True)
    assert text == "Next →"


def test_next_button_text_last_question():
    text = get_next_button_text(10, 11, True)
    assert text == "Submit Quiz →"


def test_next_button_state_disabled():
    state = get_next_button_state(False)
    assert state == "disabled"


def test_next_button_state_enabled():
    state = get_next_button_state(True)
    assert state == "normal"


def test_shuffled_options_keeps_same_keys():
    options = {
        "A": {"text": "Option A", "vibes": ["Soft"]},
        "B": {"text": "Option B", "vibes": ["Casual"]},
        "C": {"text": "Option C", "vibes": ["Gamer"]},
    }

    shuffled = get_shuffled_options(options)

    original_keys = sorted(options.keys())
    shuffled_keys = sorted([key for key, _ in shuffled])

    assert original_keys == shuffled_keys


def test_shuffled_options_not_same_order_most_of_time():
    options = {
        "A": {"text": "Option A", "vibes": ["Soft"]},
        "B": {"text": "Option B", "vibes": ["Casual"]},
        "C": {"text": "Option C", "vibes": ["Gamer"]},
    }

    orders = []
    for _ in range(10):
        shuffled = get_shuffled_options(options)
        orders.append([key for key, _ in shuffled])

    assert any(order != ["A", "B", "C"] for order in orders)