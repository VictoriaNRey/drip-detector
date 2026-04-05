# Vibe Detector Quiz
# Vibes: Soft, Casual, Preppy, Alternative, Gamer, Sporty
# Authors: Christine Bui, Victoria Rey

import tkinter as tk
from tkinter import ttk
from collections import defaultdict  # Used to store vibe scores


# ============= QUIZ DATA AND LOGIC =============

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


# ============= GUI CODE =============

class DripDetectorQuiz:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Drip Detector - What's Your Vibe?")
        self.root.geometry("600x550")
        self.root.resizable(False, False)

        # Set color scheme
        self.bg_color = "#f5f0eb"
        self.primary_color = "#8b5e3c"
        self.secondary_color = "#d4c4b0"
        self.accent_color = "#a67c52"
        self.text_color = "#3a2a22"

        self.root.configure(bg=self.bg_color)

        # Store answers
        self.answers: list[str] = []
        self.current_question_index: int = 0
        self.answer_var: tk.StringVar | None = None

        # Create frames
        self.setup_frames()

        # Start the quiz
        self.show_question()

    def setup_frames(self) -> None:
        # Title/Header Frame
        self.header_frame = tk.Frame(self.root, bg=self.primary_color, height=80)
        self.header_frame.pack(fill=tk.X, pady=(0, 20))
        self.header_frame.pack_propagate(False)

        title_label = tk.Label(
            self.header_frame,
            text="💧 DRIP DETECTOR 💧",
            font=("Helvetica", 24, "bold"),
            bg=self.primary_color,
            fg="white",
        )
        title_label.pack(expand=True)

        subtitle_label = tk.Label(
            self.header_frame,
            text="Discover Your Vibe",
            font=("Helvetica", 12),
            bg=self.primary_color,
            fg="#f0e6d8",
        )
        subtitle_label.pack()

        # Main content frame
        self.content_frame = tk.Frame(self.root, bg=self.bg_color)
        self.content_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)

        # Progress frame
        self.progress_frame = tk.Frame(self.content_frame, bg=self.bg_color)
        self.progress_frame.pack(fill=tk.X, pady=(0, 20))

        self.progress_label = tk.Label(
            self.progress_frame,
            text="",
            font=("Helvetica", 10),
            bg=self.bg_color,
            fg=self.text_color,
        )
        self.progress_label.pack()

        self.progress_bar = ttk.Progressbar(
            self.progress_frame,
            length=400,
            mode="determinate",
            style="TProgressbar",
        )
        self.progress_bar.pack(pady=5)

        # Question frame
        self.question_frame = tk.Frame(self.content_frame, bg=self.bg_color)
        self.question_frame.pack(fill=tk.BOTH, expand=True)

        # Navigation buttons frame
        self.nav_frame = tk.Frame(self.content_frame, bg=self.bg_color)
        self.nav_frame.pack(fill=tk.X, pady=(20, 0))

        self.prev_button = tk.Button(
            self.nav_frame,
            text="← Previous",
            font=("Helvetica", 10),
            bg=self.secondary_color,
            fg=self.text_color,
            command=self.prev_question,
            state=tk.DISABLED,
        )
        self.prev_button.pack(side=tk.LEFT, padx=5)

        self.next_button = tk.Button(
            self.nav_frame,
            text="Next →",
            font=("Helvetica", 10, "bold"),
            bg=self.accent_color,
            fg="white",
            command=self.next_question,
        )
        self.next_button.pack(side=tk.RIGHT, padx=5)

    def show_question(self) -> None:
        # Clear previous content
        for widget in self.question_frame.winfo_children():
            widget.destroy()

        # Get current question
        question_data = questions[self.current_question_index]
        question_text = question_data["question"]

        # Update progress
        total = len(questions)
        current = self.current_question_index + 1
        self.progress_label.config(text=f"Question {current} of {total}")
        self.progress_bar["value"] = (current / total) * 100

        # Question label
        question_label = tk.Label(
            self.question_frame,
            text=question_text,
            font=("Helvetica", 14, "bold"),
            bg=self.bg_color,
            fg=self.text_color,
            wraplength=500,
            justify=tk.LEFT,
        )
        question_label.pack(pady=(0, 20), anchor=tk.W)

        # Create variable to store answer
        self.answer_var = tk.StringVar()

        # If we already have an answer for this question, preselect it
        if len(self.answers) > self.current_question_index:
            self.answer_var.set(self.answers[self.current_question_index])

        # Create option buttons
        options = question_data["options"]
        for key, value in options.items():
            option_text = value["text"]

            # Create frame for each option
            option_frame = tk.Frame(self.question_frame, bg=self.bg_color)
            option_frame.pack(fill=tk.X, pady=5)

            radio = tk.Radiobutton(
                option_frame,
                text=f"{key}. {option_text}",
                variable=self.answer_var,
                value=key,
                font=("Helvetica", 11),
                bg=self.bg_color,
                fg=self.text_color,
                selectcolor=self.bg_color,
                activebackground=self.bg_color,
                command=self.on_answer_selected,
                wraplength=520,
                justify=tk.LEFT,
            )
            radio.pack(anchor=tk.W, padx=20)

            # Hover effect
            def on_enter(e: tk.Event, btn: tk.Radiobutton = radio) -> None:
                btn.config(cursor="hand2")

            def on_leave(e: tk.Event, btn: tk.Radiobutton = radio) -> None:
                btn.config(cursor="")

            radio.bind("<Enter>", on_enter)
            radio.bind("<Leave>", on_leave)

        # Update next button text on last question
        if self.current_question_index == len(questions) - 1:
            self.next_button.config(text="Submit Quiz →")
        else:
            self.next_button.config(text="Next →")

        # Enable/disable prev button
        if self.current_question_index > 0:
            self.prev_button.config(state=tk.NORMAL)
        else:
            self.prev_button.config(state=tk.DISABLED)

        # Disable next button initially if no answer selected
        if not self.answer_var.get():
            self.next_button.config(state=tk.DISABLED)
        else:
            self.next_button.config(state=tk.NORMAL)

    def on_answer_selected(self) -> None:
        # Enable next button when an answer is selected
        self.next_button.config(state=tk.NORMAL)

    def next_question(self) -> None:
        # Save current answer
        if not self.answer_var or not self.answer_var.get():
            return

        # Update answers list
        if len(self.answers) > self.current_question_index:
            self.answers[self.current_question_index] = self.answer_var.get()
        else:
            self.answers.append(self.answer_var.get())

        # Check if this was the last question
        if self.current_question_index == len(questions) - 1:
            self.show_results()
        else:
            self.current_question_index += 1
            self.show_question()

    def prev_question(self) -> None:
        # Save current answer
        if self.answer_var and self.answer_var.get():
            if len(self.answers) > self.current_question_index:
                self.answers[self.current_question_index] = self.answer_var.get()
            else:
                self.answers.append(self.answer_var.get())

        # Go to previous question
        self.current_question_index -= 1
        self.show_question()

    def show_results(self) -> None:
        # Calculate vibe
        vibe = calculate_vibe(self.answers)

        # Vibe descriptions and emojis
        vibe_info = {
            "Soft": {
                "emoji": "🌸",
                "color": "#f5c6d0",
                "description": "You're gentle, romantic, and love all things cute and cozy! Your aesthetic is dreamy and soft.",
            },
            "Casual": {
                "emoji": "👕",
                "color": "#a8b2b8",
                "description": "You're laid-back, easygoing, and keep things simple but stylish. Comfort is key for you!",
            },
            "Preppy": {
                "emoji": "🎩",
                "color": "#8b9dc3",
                "description": "You're polished, put-together, and have classic taste. Always looking sharp and sophisticated!",
            },
            "Alternative": {
                "emoji": "🎸",
                "color": "#7b6c8c",
                "description": "You're unique, creative, and march to the beat of your own drum. Your style is edgy and expressive!",
            },
            "Gamer": {
                "emoji": "🎮",
                "color": "#6b8c6b",
                "description": "You're tech-savvy, love gaming culture, and prioritize comfort for those long gaming sessions!",
            },
            "Sporty": {
                "emoji": "⚡",
                "color": "#c4a35a",
                "description": "You're active, energetic, and always ready to move. Athletic wear is your everyday style!",
            },
        }

        info = vibe_info.get(vibe, vibe_info["Casual"])

        # Clear the content frame
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        # Results display
        results_frame = tk.Frame(self.content_frame, bg=self.bg_color)
        results_frame.pack(fill=tk.BOTH, expand=True)

        # Vibe emoji and title
        emoji_label = tk.Label(
            results_frame,
            text=info["emoji"],
            font=("Helvetica", 72),
            bg=self.bg_color,
        )
        emoji_label.pack(pady=(20, 10))

        result_label = tk.Label(
            results_frame,
            text="Your Vibe Is:",
            font=("Helvetica", 18, "bold"),
            bg=self.bg_color,
            fg=self.text_color,
        )
        result_label.pack()

        vibe_label = tk.Label(
            results_frame,
            text=vibe,
            font=("Helvetica", 36, "bold"),
            bg=self.bg_color,
            fg=self.primary_color,
        )
        vibe_label.pack(pady=10)

        # Description
        desc_label = tk.Label(
            results_frame,
            text=info["description"],
            font=("Helvetica", 12),
            bg=self.bg_color,
            fg=self.text_color,
            wraplength=450,
            justify=tk.CENTER,
        )
        desc_label.pack(pady=20)

        # Color bar
        color_bar = tk.Frame(results_frame, bg=info["color"], height=10)
        color_bar.pack(fill=tk.X, pady=20)

        # Button frame
        button_frame = tk.Frame(results_frame, bg=self.bg_color)
        button_frame.pack(pady=20)

        restart_button = tk.Button(
            button_frame,
            text="Take Quiz Again",
            font=("Helvetica", 12, "bold"),
            bg=self.accent_color,
            fg="white",
            command=self.restart_quiz,
            padx=20,
            pady=10,
        )
        restart_button.pack(side=tk.LEFT, padx=10)

        quit_button = tk.Button(
            button_frame,
            text="Quit",
            font=("Helvetica", 12),
            bg=self.secondary_color,
            fg=self.text_color,
            command=self.root.quit,
            padx=20,
            pady=10,
        )
        quit_button.pack(side=tk.LEFT, padx=10)

        # Hover effects for buttons
        def on_enter(e: tk.Event, btn: tk.Button, color: str) -> None:
            btn.config(bg=color)

        def on_leave(e: tk.Event, btn: tk.Button, color: str) -> None:
            btn.config(bg=color)

        restart_button.bind("<Enter>", lambda e: on_enter(e, restart_button, "#8b6b42"))
        restart_button.bind("<Leave>", lambda e: on_leave(e, restart_button, self.accent_color))
        quit_button.bind("<Enter>", lambda e: on_enter(e, quit_button, "#b4a490"))
        quit_button.bind("<Leave>", lambda e: on_leave(e, quit_button, self.secondary_color))

    def restart_quiz(self) -> None:
        # Reset quiz state
        self.answers = []
        self.current_question_index = 0

        # Rebuild the content frame
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        # Recreate frames
        self.setup_frames_in_content()

        # Start over
        self.show_question()

    def setup_frames_in_content(self) -> None:
        # Recreate progress frame
        self.progress_frame = tk.Frame(self.content_frame, bg=self.bg_color)
        self.progress_frame.pack(fill=tk.X, pady=(0, 20))

        self.progress_label = tk.Label(
            self.progress_frame,
            text="",
            font=("Helvetica", 10),
            bg=self.bg_color,
            fg=self.text_color,
        )
        self.progress_label.pack()

        self.progress_bar = ttk.Progressbar(
            self.progress_frame,
            length=400,
            mode="determinate",
            style="TProgressbar",
        )
        self.progress_bar.pack(pady=5)

        # Recreate question frame
        self.question_frame = tk.Frame(self.content_frame, bg=self.bg_color)
        self.question_frame.pack(fill=tk.BOTH, expand=True)

        # Recreate navigation frame
        self.nav_frame = tk.Frame(self.content_frame, bg=self.bg_color)
        self.nav_frame.pack(fill=tk.X, pady=(20, 0))

        self.prev_button = tk.Button(
            self.nav_frame,
            text="← Previous",
            font=("Helvetica", 10),
            bg=self.secondary_color,
            fg=self.text_color,
            command=self.prev_question,
            state=tk.DISABLED,
        )
        self.prev_button.pack(side=tk.LEFT, padx=5)

        self.next_button = tk.Button(
            self.nav_frame,
            text="Next →",
            font=("Helvetica", 10, "bold"),
            bg=self.accent_color,
            fg="white",
            command=self.next_question,
        )
        self.next_button.pack(side=tk.RIGHT, padx=5)


def main() -> None:
    root = tk.Tk()

    # Configure ttk styles
    style = ttk.Style()
    style.theme_use("clam")
    style.configure(
        "TProgressbar",
        background="#a67c52",
        troughcolor="#d4c4b0",
        thickness=10,
    )

    DripDetectorQuiz(root)
    root.mainloop()


if __name__ == "__main__":
    main()
