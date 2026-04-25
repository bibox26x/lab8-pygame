# lab8-pygame

Small Pygame simulation with 100 colored squares moving around in an 800x600 window.

What it does:
- each square has random size (10 to 50)
- smaller squares move faster, bigger squares move slower
- squares bounce on window edges
- smaller squares flee nearby bigger squares
- movement is time-based (`dt`) so it stays more stable across frame timing changes

## Setup

1. Create/activate a virtual environment (or use the existing `.venv`).
2. Install dependencies from `requirements.txt`.

## Run

Run:

`python main.py`

If your environment uses `.venv`, use that Python interpreter directly.
