# Vibe Detector Quiz
# Vibes: Soft, Casual, Preppy, Alternative, Gamer, Sporty
# Authors: Christine Bui, Victoria Rey

import os
import random
import tkinter as tk
from collections import defaultdict
from tkinter import ttk

from PIL import Image, ImageTk


questions = [
    {
        "question": "What gender do you identify with?",
        "options": {
            "A": {"text": "Female", "vibes": []},
            "B": {"text": "Male", "vibes": []},
        },
    },
    {
        "question": "What are you doing on your day off?",
        "options": {
            "A": {"text": "Baking sweet treats", "vibes": ["Soft"]},
            "B": {"text": "A casual shopping trip with friends", "vibes": ["Casual"]},
            "C": {"text": "Reading a classic literature book", "vibes": ["Preppy"]},
            "D": {"text": "Playing video games", "vibes": ["Gamer"]},
            "E": {"text": "Running, hiking, or cycling outdoors", "vibes": ["Sporty"]},
            "F": {
                "text": "Playing an instrument or listening to music all day",
                "vibes": ["Alternative"],
            },
        },
    },
    {
        "question": "Where are you most likely spotted?",
        "options": {
            "A": {"text": "A farmer’s market on a sunny morning", "vibes": ["Soft"]},
            "B": {"text": "My best friend’s house", "vibes": ["Casual"]},
            "C": {
                "text": "A local bookstore or the school library",
                "vibes": ["Preppy"],
            },
            "D": {"text": "On Discord", "vibes": ["Gamer"]},
            "E": {"text": "A sports bar during game season", "vibes": ["Sporty"]},
            "F": {"text": "Thrift stores or vintage shops", "vibes": ["Alternative"]},
        },
    },
    {
        "question": "What are your favorite colors?",
        "options": {
            "A": {"text": "Pastel & light (baby blue, lavender)", "vibes": ["Soft"]},
            "B": {"text": "Neutrals (black, white, beige)", "vibes": ["Casual"]},
            "C": {"text": "Elegant & timeless (navy blue, burgundy)", "vibes": ["Preppy"]},
            "D": {"text": "Neon & hot (hot pink, neon green)", "vibes": ["Gamer"]},
            "E": {"text": "Bright & bold (bright red, neon yellow)", "vibes": ["Sporty"]},
            "F": {"text": "Dark (black, charcoal gray, deep purple)", "vibes": ["Alternative"]},
        },
    },
    {
        "question": "What would your closest friends say is your biggest flaw?",
        "options": {
            "A": {"text": "I am too sensitive", "vibes": ["Soft"]},
            "B": {"text": "I procrastinate everything", "vibes": ["Casual"]},
            "C": {"text": "I am a perfectionist", "vibes": ["Preppy"]},
            "D": {"text": "I am lazy", "vibes": ["Gamer"]},
            "E": {"text": "I compare myself to others often", "vibes": ["Sporty"]},
            "F": {"text": "I am too chaotic / unpredictable", "vibes": ["Alternative"]},
        },
    },
    {
        "question": "How much effort do you put into getting ready?",
        "options": {
            "A": {"text": "A lot! I love looking cute", "vibes": ["Soft", "Preppy"]},
            "B": {"text": "Just enough / very little effort", "vibes": ["Casual", "Gamer"]},
            "C": {"text": "Quick & practical", "vibes": ["Sporty"]},
            "D": {"text": "Depends, I like to stand out", "vibes": ["Alternative"]},
        },
    },
    {
        "question": "What are your favorite shoes to wear?",
        "options": {
            "A": {"text": "Mary Janes with little socks", "vibes": ["Soft"]},
            "B": {"text": "Basic white sneakers", "vibes": ["Casual"]},
            "C": {"text": "Leather loafers", "vibes": ["Preppy"]},
            "D": {"text": "Slides or crocs", "vibes": ["Gamer"]},
            "E": {"text": "Running shoes or shoes with support", "vibes": ["Sporty"]},
            "F": {"text": "Combat or platform boots", "vibes": ["Alternative"]},
        },
    },
    {
        "question": "What accessories do you usually wear?",
        "options": {
            "A": {"text": "Dainty necklaces or initial pendants", "vibes": ["Soft"]},
            "B": {"text": "A simple watch or bracelet", "vibes": ["Casual"]},
            "C": {"text": "Polished jewelry", "vibes": ["Preppy"]},
            "D": {"text": "Lanyards or charms of your favorite character", "vibes": ["Gamer"]},
            "E": {"text": "Fitness tracker & a water bottle", "vibes": ["Sporty"]},
            "F": {"text": "Rings on every finger & multiple piercings", "vibes": ["Alternative"]},
        },
    },
    {
        "question": "What would you order at a coffee shop?",
        "options": {
            "A": {"text": "An iced strawberry matcha latte", "vibes": ["Soft"]},
            "B": {"text": "An iced coffee", "vibes": ["Casual"]},
            "C": {"text": "A flat white (with latte art)", "vibes": ["Preppy"]},
            "D": {"text": "A double espresso", "vibes": ["Gamer"]},
            "E": {"text": "A black cold brew", "vibes": ["Sporty"]},
            "F": {"text": "An iced chai latte", "vibes": ["Alternative"]},
        },
    },
    {
        "question": "What is your most played music genre?",
        "options": {
            "A": {"text": "Indie pop", "vibes": ["Soft"]},
            "B": {"text": "Pop", "vibes": ["Casual"]},
            "C": {"text": "Lo-fi", "vibes": ["Preppy"]},
            "D": {"text": "Electronic dance music", "vibes": ["Gamer"]},
            "E": {"text": "Hip hop & rap", "vibes": ["Sporty"]},
            "F": {"text": "Rock & punk", "vibes": ["Alternative"]},
        },
    },
    {
        "question": "Which emoji combo resembles you?",
        "options": {
            "A": {"text": "🥺💖✨☁️🫶🧸", "vibes": ["Soft"]},
            "B": {"text": "😭💀👍🤷‍♀️✨😌", "vibes": ["Casual"]},
            "C": {"text": "☕📚🎾👜🛍️💳", "vibes": ["Preppy"]},
            "D": {"text": "🎮😤💻🕹️👾🔥", "vibes": ["Gamer"]},
            "E": {"text": "💪🏀⚡💧🏆🥇", "vibes": ["Sporty"]},
            "F": {"text": "🖤🎸🥀😈🌙🦉", "vibes": ["Alternative"]},
        },
    },
]


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


def get_shuffled_options(options: dict[str, dict]) -> list[tuple[str, dict]]:
    option_items = list(options.items())
    random.shuffle(option_items)
    return option_items


def get_next_button_text(
    question_index: int,
    total_questions: int,
    has_answer: bool,
) -> str:
    if not has_answer:
        return "Select an answer"
    if question_index == total_questions - 1:
        return "Submit Quiz →"
    return "Next →"


def get_next_button_state(has_answer: bool) -> str:
    if has_answer:
        return tk.NORMAL
    return tk.DISABLED


class DripDetectorQuiz:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Drip Detector - What's Your Vibe?")
        self.root.geometry("980x820")
        self.root.minsize(850, 700)
        self.root.resizable(True, True)

        self.bg_color = "#eaf4ff"
        self.card_color = "#ffffff"
        self.primary_color = "#173b7a"
        self.secondary_color = "#bcdcff"
        self.accent_color = "#6ea8fe"
        self.dark_accent = "#2f5fb3"
        self.text_color = "#16325c"
        self.option_border = "#9dc7ff"
        self.option_selected = "#cfe6ff"

        self.root.configure(bg=self.bg_color)

        self.answers: list[str] = []
        self.current_question_index: int = 0
        self.answer_var: tk.StringVar | None = None
        self.result_photo: ImageTk.PhotoImage | None = None
        self.option_buttons: list[tk.Radiobutton] = []
        self.confetti_canvas: tk.Canvas | None = None
        self.confetti_pieces: list[dict] = []
        self.confetti_running = False

        self.setup_frames()
        self.show_question()

    def setup_frames(self) -> None:
        self.header_frame = tk.Frame(self.root, bg=self.primary_color, height=90)
        self.header_frame.pack(fill=tk.X, pady=(0, 14))
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
            font=("Helvetica", 12, "bold"),
            bg=self.primary_color,
            fg="#dcecff",
        )
        subtitle_label.pack(pady=(0, 10))

        self.content_frame = tk.Frame(self.root, bg=self.bg_color)
        self.content_frame.pack(fill=tk.BOTH, expand=True, padx=24, pady=(0, 18))

        self.setup_frames_in_content()

    def setup_frames_in_content(self) -> None:
        self.progress_frame = tk.Frame(self.content_frame, bg=self.bg_color)
        self.progress_frame.pack(fill=tk.X, pady=(0, 10))

        self.progress_label = tk.Label(
            self.progress_frame,
            text="",
            font=("Helvetica", 11, "bold"),
            bg=self.bg_color,
            fg=self.text_color,
        )
        self.progress_label.pack()

        self.progress_bar = ttk.Progressbar(
            self.progress_frame,
            length=450,
            mode="determinate",
            style="TProgressbar",
        )
        self.progress_bar.pack(pady=6)

        self.quiz_area = tk.Frame(self.content_frame, bg=self.bg_color)
        self.quiz_area.pack(expand=True)

        self.question_frame = tk.Frame(self.quiz_area, bg=self.bg_color)
        self.question_frame.pack(pady=(0, 6))

        self.nav_frame = tk.Frame(self.quiz_area, bg=self.bg_color)
        self.nav_frame.pack(pady=(6, 0))

        self.prev_button = tk.Button(
            self.nav_frame,
            text="← Previous",
            font=("Helvetica", 11, "bold"),
            bg=self.secondary_color,
            fg=self.text_color,
            activebackground="#a9d0ff",
            activeforeground=self.text_color,
            relief="flat",
            bd=0,
            width=14,
            height=1,
            cursor="hand2",
            command=self.prev_question,
            state=tk.DISABLED,
        )
        self.prev_button.pack(side=tk.LEFT, padx=8)

        self.next_button = tk.Button(
            self.nav_frame,
            text="Select an answer",
            font=("Helvetica", 11, "bold"),
            bg="#d9d9d9",
            fg="#666666",
            activeforeground="white",
            activebackground=self.primary_color,
            disabledforeground="#666666",
            relief="flat",
            bd=0,
            highlightthickness=0,
            width=18,
            height=1,
            cursor="hand2",
            command=self.next_question,
            state=tk.DISABLED,
        )
        self.next_button.pack(side=tk.LEFT, padx=8)

    def clear_question_frame(self) -> None:
        for widget in self.question_frame.winfo_children():
            widget.destroy()
        self.option_buttons = []

    def show_question(self) -> None:
        self.stop_confetti()
        self.clear_question_frame()

        question_data = questions[self.current_question_index]
        question_text = question_data["question"]
        is_emoji_question = self.current_question_index == len(questions) - 1
        option_fg = "black" if is_emoji_question else self.text_color

        total = len(questions)
        current = self.current_question_index + 1
        self.progress_label.config(text=f"Question {current} of {total}")
        self.progress_bar["value"] = (current / total) * 100

        question_card = tk.Frame(
            self.question_frame,
            bg=self.card_color,
            highlightbackground="#d0e6ff",
            highlightthickness=2,
            bd=0,
            width=700,
            height=75,
        )
        question_card.pack(pady=(0, 8))
        question_card.pack_propagate(False)

        question_label = tk.Label(
            question_card,
            text=question_text,
            font=("Helvetica", 15, "bold"),
            bg=self.card_color,
            fg=self.primary_color,
            wraplength=640,
            justify=tk.CENTER,
            padx=16,
            pady=10,
        )
        question_label.pack(fill=tk.BOTH, expand=True)

        self.answer_var = tk.StringVar()

        if len(self.answers) > self.current_question_index:
            self.answer_var.set(self.answers[self.current_question_index])

        options = get_shuffled_options(question_data["options"])

        for key, value in options:
            option_text = value["text"]

            radio = tk.Radiobutton(
                self.question_frame,
                text=option_text,
                variable=self.answer_var,
                value=key,
                indicatoron=0,
                font=("Helvetica", 11),
                bg=self.card_color,
                fg=option_fg,
                activebackground=self.option_selected,
                activeforeground=option_fg,
                selectcolor=self.option_selected,
                relief="solid",
                bd=1,
                highlightthickness=2,
                highlightbackground=self.option_border,
                highlightcolor=self.dark_accent,
                padx=16,
                pady=8,
                anchor="w",
                justify=tk.LEFT,
                wraplength=560,
                width=58,
                cursor="hand2",
                command=self.on_answer_selected,
            )
            radio.pack(pady=3)
            self.option_buttons.append(radio)

        self.update_option_styles()

        if self.current_question_index > 0:
            self.prev_button.config(state=tk.NORMAL)
        else:
            self.prev_button.config(state=tk.DISABLED)

        self.update_next_button()

    def update_next_button(self) -> None:
        has_answer = bool(self.answer_var and self.answer_var.get())

        button_text = get_next_button_text(
            self.current_question_index,
            len(questions),
            has_answer,
        )

        button_state = get_next_button_state(has_answer)
        if has_answer:
            self.next_button.config(
                state=button_state,
                text=button_text,
                bg=self.dark_accent,
                fg="white",
                disabledforeground="white",
                cursor="hand2",
            )
        else:
            self.next_button.config(
                state=button_state,
                text=button_text,
                bg="#d9d9d9",
                fg="#666666",
                disabledforeground="#666666",
                cursor="arrow",
            )
            
    def update_option_styles(self) -> None:
        if not self.answer_var:
            return

        selected = self.answer_var.get()
        is_emoji_question = self.current_question_index == len(questions) - 1
        default_fg = "black" if is_emoji_question else self.text_color

        for button in self.option_buttons:
            if button.cget("value") == selected:
                button.config(
                    bg=self.option_selected,
                    fg=default_fg,
                    activeforeground=default_fg,
                    font=("Helvetica", 12, "bold"),
                    relief="solid",
                    highlightbackground=self.dark_accent,
                    bd=2,
                )
            else:
                button.config(
                    bg=self.card_color,
                    fg=default_fg,
                    activeforeground=default_fg,
                    font=("Helvetica", 12),
                    relief="solid",
                    highlightbackground=self.option_border,
                    bd=1,
                )

    def on_answer_selected(self) -> None:
        self.update_next_button()
        self.update_option_styles()

    def next_question(self) -> None:
        if not self.answer_var or not self.answer_var.get():
            return

        if len(self.answers) > self.current_question_index:
            self.answers[self.current_question_index] = self.answer_var.get()
        else:
            self.answers.append(self.answer_var.get())

        if self.current_question_index == len(questions) - 1:
            self.show_results()
        else:
            self.current_question_index += 1
            self.show_question()

    def prev_question(self) -> None:
        if self.answer_var and self.answer_var.get():
            if len(self.answers) > self.current_question_index:
                self.answers[self.current_question_index] = self.answer_var.get()
            else:
                self.answers.append(self.answer_var.get())

        if self.current_question_index > 0:
            self.current_question_index -= 1
            self.show_question()

    def show_results(self) -> None:
        self.stop_confetti()

        vibe = calculate_vibe(self.answers)

        vibe_info = {
            "Soft": {
                "emoji": "🌸",
                "color": "#f7cfe3",
                "girl": "you’re the sweetest cutie patootie that anyone would go to war for, the girl next door with a heart of gold. you believe in hope, soulmates, and that everything happens for a reason. you probably own more colors than anyone you know and your camera roll is full of sunset and floral pictures. you’re the epitome of sunshine, flowers blooming, the color pink, and finding magic in the little things.",
                "boy": "you’re a fan of feminist literature and your go-to order at a local coffee shop is an iced matcha latte. you probably have a playlist full of indie artists nobody’s heard of yet and you secretly love keeping up with trends. you’re emotionally intelligent, probably cried during a movie this month, and you’re not afraid to admit it. you’re the epitome of a great jean jacket, a cozy book, and warm lighting in a quiet room.",
            },
            "Casual": {
                "emoji": "👕",
                "color": "#d9e7f7",
                "girl": "you’re down-to-earth and can make friends with literally anyone. a human golden retriever in the best way. you have an emotional support sweater that’s seen better days but you’ll never get rid of it. you’re possibly an ambivert who enjoys both chaotic nights out and peaceful nights in. you’re the epitome of uggs, roasted marshmallows around a campfire, a night with good friends, and never overcomplicating a good thing.",
                "boy": "you’re the polished, put-together guy who always has his life organized in a color-coded calendar. always 3 steps ahead of your classmates. you probably own more polo shirts than t-shirts and you’ve never shown up late to anything. your friends come to you for advice because you actually have your act together. you’re the epitome of a navy blazer, fresh haircuts, and knowing exactly what you want out of life.",
            },
            "Preppy": {
                "emoji": "🎩",
                "color": "#bfd7ff",
                "girl": "you’re polished, ambitious, and always have your life together (or at least it looks like it). you thrive on structure, goals, and a clean aesthetic. your vibe is timeless and effortlessly put-together. you’re the epitome of planners, early mornings, and always being the most prepared person in the room.",
                "boy": "you’re sharp, driven, and always thinking ahead. you probably have a plan for the next five years and a backup plan just in case. you value discipline, presentation, and success. you’re the epitome of crisp outfits, structured routines, and quiet confidence.",
            },
            "Alternative": {
                "emoji": "🎸",
                "color": "#d8d2f0",
                "girl": "you’re the mysterious, creative soul who marches to the beat of her own drum. you probably have a playlist that would make your grandma concerned and a wardrobe that’s mostly black with a splash of chaos. you don’t follow trends, you start them (or reject them entirely). you’re the epitome of thrifted leather jackets, scribbling poetry in a notebook at 2am, and being unapologetically unique.",
                "boy": "you’re the artsy, unpredictable guy who probably knows more about underground bands than anyone you’ve ever met. you don’t fit in a box, and you wouldn’t want to anyway. you probably have strong opinions about coffee shops, vinyl records, and why skinny jeans never die. you’re the epitome of band tees from hot topic, late nights making playlists, and the kind of cool that can’t be bought.",
            },
            "Gamer": {
                "emoji": "🎮",
                "color": "#ffd2f4",
                "girl": "you’re the queen of late night gaming sessions and the person your squad wants on their team. you probably have a headset that’s seen more action than your regular shoes, and you know exactly how to carry a losing match. you’re competitive when it counts but also the first to laugh at a silly glitch. you’re the epitome of rgb lighting, hot pink lighting, and destroying the “girls don’t game” stereotype.",
                "boy": "you’re the dedicated, strategic guy who treats every game like it’s a world championship and your reflexes are terrifying. you probably have a setup that costs more than a used car and definitely yelled “one more game!” at least 7 times in a row. you’re loyal to your squad and you know every easter egg, secret level, and glitch in your favorite games. you’re the epitome of mechanical keyboards, climbing ranked ladders, and the satisfaction of a perfect headshot.",
            },
            "Sporty": {
                "emoji": "⚡",
                "color": "#ffe7a8",
                "girl": "you’re the energetic, competitive force that pushes everyone around you to be better (whether they asked for it or not). you probably have more workout clothes than regular clothes and your water bottle is basically an extension of your arm. you’re the first one to suggest a pickup game and the last one to leave the field. you’re the epitome of ponytails, matcha tea, and that post-workout endorphin rush that keeps you going.",
                "boy": "you’re the athletic, driven guy who treats every workout like it’s training for the big game. you probably have a gym bag that lives in your car and you’ve definitely used “but it’s protein!” as an excuse for a questionable snack choice. you’re competitive but in a way that makes everyone want to be on your team. you’re the epitome of the smell of a freshly mowed field, protein shakes, and the feeling of winning when nobody thought you would.",
            },
        }

        info = vibe_info.get(vibe, vibe_info["Casual"])

        gender_answer = self.answers[0] if self.answers else "A"
        gender = "girl" if gender_answer == "A" else "boy"

        vibe_file_map = {
            "Soft": "soft",
            "Casual": "casual",
            "Preppy": "preppy",
            "Alternative": "alt",
            "Gamer": "gamer",
            "Sporty": "sporty",
        }

        display_vibe = "Softie" if vibe == "Soft" else vibe

        base_dir = os.path.dirname(os.path.abspath(__file__))
        image_filename = os.path.join(
            base_dir,
            "images",
            f"{vibe_file_map[vibe]}{gender}.jpg",
        )

        for widget in self.content_frame.winfo_children():
            widget.destroy()

        results_container = tk.Frame(self.content_frame, bg=self.bg_color)
        results_container.pack(fill=tk.BOTH, expand=True)

        self.confetti_canvas = tk.Canvas(
            results_container,
            bg=self.bg_color,
            highlightthickness=0,
            bd=0,
        )
        self.confetti_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

        results_outer = tk.Frame(results_container, bg=self.bg_color)
        results_outer.pack(fill=tk.BOTH, expand=True)

        results_frame = tk.Frame(results_outer, bg=self.card_color, width=950, height=540)
        results_frame.place(relx=0.5, rely=0.5, anchor="center")
        results_frame.pack_propagate(False)

        main_result_frame = tk.Frame(results_frame, bg=self.card_color)
        main_result_frame.pack(fill=tk.BOTH, expand=True, padx=32, pady=28)

        left_panel = tk.Frame(main_result_frame, bg=self.card_color, width=390)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, padx=(0, 30))
        left_panel.pack_propagate(False)

        right_panel = tk.Frame(main_result_frame, bg=self.card_color)
        right_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        try:
            img = Image.open(image_filename)
            img.thumbnail((360, 360))
            self.result_photo = ImageTk.PhotoImage(img)

            image_label = tk.Label(
                left_panel,
                image=self.result_photo,
                bg=self.card_color,
            )
            image_label.pack(pady=(18, 10), anchor="center")

        except FileNotFoundError:
            error_label = tk.Label(
                left_panel,
                text=f"Image not found:\n{image_filename}",
                font=("Helvetica", 11),
                bg=self.card_color,
                fg="red",
                justify=tk.CENTER,
                wraplength=320,
            )
            error_label.pack(pady=10)

        description = info[gender]

        vibe_title = tk.Label(
            right_panel,
            text=f"{display_vibe} {info['emoji']}",
            font=("Segoe UI Emoji", 28, "bold"),
            bg=self.card_color,
            fg=self.primary_color,
            anchor="w",
            justify=tk.LEFT,
        )
        vibe_title.pack(anchor="w", fill=tk.X, pady=(24, 14))

        desc_label = tk.Label(
            right_panel,
            text=description,
            font=("Helvetica", 12),
            bg=self.card_color,
            fg=self.text_color,
            wraplength=470,
            justify=tk.LEFT,
            anchor="nw",
        )
        desc_label.pack(fill=tk.BOTH, expand=True, anchor="nw")

        color_bar = tk.Frame(results_frame, bg=info["color"], height=12)
        color_bar.pack(fill=tk.X, pady=12, padx=24)

        button_frame = tk.Frame(results_frame, bg=self.card_color)
        button_frame.pack(pady=20)

        restart_button = tk.Button(
            button_frame,
            text="Take Quiz Again",
            font=("Helvetica", 12, "bold"),
            bg=self.dark_accent,
            fg="white",
            activebackground=self.primary_color,
            activeforeground="white",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.restart_quiz,
            padx=22,
            pady=12,
            width=16,
        )
        restart_button.pack(side=tk.LEFT, padx=10)

        quit_button = tk.Button(
            button_frame,
            text="Quit",
            font=("Helvetica", 12, "bold"),
            bg=self.secondary_color,
            fg=self.text_color,
            activebackground="#a9d0ff",
            activeforeground=self.text_color,
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.root.quit,
            padx=22,
            pady=12,
            width=10,
        )
        quit_button.pack(side=tk.LEFT, padx=10)

        self.root.update_idletasks()
        self.start_confetti()

    def start_confetti(self) -> None:
        if not self.confetti_canvas:
            return

        self.confetti_canvas.delete("all")
        self.confetti_pieces = []
        self.confetti_running = True

        width = max(self.confetti_canvas.winfo_width(), 700)
        height = max(self.confetti_canvas.winfo_height(), 600)

        colors = [
            "#ff8fab",
            "#ffd166",
            "#7bdff2",
            "#b8f2e6",
            "#cdb4db",
            "#a0c4ff",
            "#ffc6ff",
            "#f1c0e8",
        ]

        for _ in range(90):
            x = random.randint(0, width)
            y = random.randint(-height, 0)
            size = random.randint(6, 12)
            dx = random.uniform(-1.5, 1.5)
            dy = random.uniform(2.0, 5.0)
            color = random.choice(colors)

            shape_type = random.choice(["oval", "rect"])
            if shape_type == "oval":
                item = self.confetti_canvas.create_oval(
                    x,
                    y,
                    x + size,
                    y + size,
                    fill=color,
                    outline="",
                )
            else:
                item = self.confetti_canvas.create_rectangle(
                    x,
                    y,
                    x + size,
                    y + size,
                    fill=color,
                    outline="",
                )

            self.confetti_pieces.append(
                {
                    "id": item,
                    "dx": dx,
                    "dy": dy,
                    "size": size,
                },
            )

        self.animate_confetti()

    def animate_confetti(self) -> None:
        if not self.confetti_running or not self.confetti_canvas:
            return

        width = max(self.confetti_canvas.winfo_width(), 700)
        height = max(self.confetti_canvas.winfo_height(), 600)

        for piece in self.confetti_pieces:
            self.confetti_canvas.move(piece["id"], piece["dx"], piece["dy"])
            coords = self.confetti_canvas.coords(piece["id"])

            if coords and coords[1] > height:
                new_x = random.randint(0, width)
                new_y = random.randint(-120, -20)
                size = piece["size"]

                self.confetti_canvas.coords(
                    piece["id"],
                    new_x,
                    new_y,
                    new_x + size,
                    new_y + size,
                )

        self.root.after(35, self.animate_confetti)

    def stop_confetti(self) -> None:
        self.confetti_running = False
        self.confetti_pieces = []
        if self.confetti_canvas:
            self.confetti_canvas.delete("all")

    def restart_quiz(self) -> None:
        self.stop_confetti()
        self.answers = []
        self.current_question_index = 0
        self.result_photo = None
        self.answer_var = None
        self.option_buttons = []
        self.confetti_canvas = None

        for widget in self.content_frame.winfo_children():
            widget.destroy()

        self.setup_frames_in_content()
        self.show_question()

def main() -> None:
    root = tk.Tk()

    style = ttk.Style()
    style.theme_use("clam")
    style.configure(
        "TProgressbar",
        background="#6ea8fe",
        troughcolor="#cfe6ff",
        thickness=12,
        borderwidth=0,
    )

    DripDetectorQuiz(root)
    root.mainloop()


if __name__ == "__main__":
    main()