import tkinter as tk
import random
import time
import threading
import pygame
import os

root = tk.Tk()
root.title("For You ❤️")

WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()

BG = "#000000"
TEXT = "#FFFFFF"
STAR_COUNT = 90
TYPING_SPEED = 0.055

MUSIC_FILE = r"C:\Users\ASUS\OneDrive\Documents\GitHub\Random Stuff\Love.mp3"

root.attributes("-fullscreen", True)
root.configure(bg=BG)
root.resizable(False, False)

canvas = tk.Canvas(
    root,
    width=WIDTH,
    height=HEIGHT,
    bg=BG,
    highlightthickness=0
)
canvas.pack(fill="both", expand=True)

stars = []

for _ in range(STAR_COUNT):
    stars.append({
        "x": random.randint(0, WIDTH),
        "y": random.randint(0, HEIGHT),
        "speed": random.uniform(2, 6),
        "symbol": random.choice(["♥", "❤️", "❄️", "*"])
    })


def animate_stars():
    canvas.delete("star")

    for star in stars:
        star["y"] += star["speed"]

        if star["y"] > HEIGHT:
            star["y"] = 0
            star["x"] = random.randint(0, WIDTH)

        canvas.create_text(
            star["x"],
            star["y"],
            text=star["symbol"],
            fill=TEXT,
            font=("Consolas", random.randint(8, 13)),
            tags="star"
        )

    root.after(40, animate_stars)

current_text = None


def clear_message():
    global current_text

    if current_text:
        canvas.delete(current_text)

    current_text = None


def type_message(message, speed=TYPING_SPEED):
    global current_text

    clear_message()

    current_text = canvas.create_text(
        WIDTH // 2,
        HEIGHT // 2,
        text="",
        fill=TEXT,
        font=("Consolas", 18),
        anchor="center"
    )

    text = ""

    for char in message:
        text += char
        canvas.itemconfig(current_text, text=text)
        root.update()
        time.sleep(speed)


def show_message(message, wait=0.2, speed=TYPING_SPEED):
    type_message(message, speed)
    time.sleep(wait)

def play_music():
    try:
        if not os.path.exists(MUSIC_FILE):
            print("❌ SONG NOT FOUND")
            print(MUSIC_FILE)
            return

        pygame.mixer.init()
        pygame.mixer.music.load(MUSIC_FILE)
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play()

        print("▶ MUSIC PLAYING")

    except Exception as e:
        print("Music error:", e)

def lyrics():

    threading.Thread(
        target=play_music,
        daemon=True
    ).start()

    time.sleep(1)

    show_message(
        "I like you",
        wait=0.8,
        speed=0.10
    )

    clear_message()
    time.sleep(2.2)

    show_message(
        "I'm in love",
        wait=0.8,
        speed=0.14
    )

    show_message(
        "With those honest eyes.",
        wait=0.8,
        speed=0.06
    )

    show_message(
        "Like the heart of a young boy.",
        wait=0,
        speed=0.04
    )

    time.sleep(5)
    clear_message()

    message = canvas.create_text(
        WIDTH // 2,
        HEIGHT // 2 - 40,
        text="For My One and Only ❤️",
        fill=TEXT,
        font=("Consolas", 64, "bold")
    )

    time.sleep(5)
    canvas.delete(message)

    message = canvas.create_text(
        WIDTH // 2,
        HEIGHT // 2 - 40,
        text="Here's to more memories together.",
        fill=TEXT,
        font=("Consolas", 52, "bold")
    )

    time.sleep(5)
    canvas.delete(message)

    canvas.create_text(
        WIDTH // 2,
        HEIGHT // 2,
        text="           I  love  you  ❤️",
        fill=TEXT,
        font=("Edwardian Script ITC", 100, "bold")
    )

    canvas.create_text(
        WIDTH // 2,
        HEIGHT // 2 + 120,
        text="To the moon and back.",
        fill="#AAAAAA",
        font=("Edwardian Script ITC", 40)
    )

    time.sleep(5)

def close_program(event=None):
    try:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
    except:
        pass

    root.destroy()

root.bind("<Escape>", close_program)
root.protocol("WM_DELETE_WINDOW", close_program)

animate_stars()

threading.Thread(
    target=lyrics,
    daemon=True
).start()

root.mainloop()