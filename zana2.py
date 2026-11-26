"""One-click launcher for Hormuz Run. Run this Python file to open the game."""

from pathlib import Path
import webbrowser


game_page = Path(__file__).with_name("play.html")
if not game_page.is_file():
    raise FileNotFoundError(f"Game page not found: {game_page}")

webbrowser.open(game_page.resolve().as_uri())
