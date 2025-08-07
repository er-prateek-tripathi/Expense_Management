# login.py - Entry point for authentication screens
from auth import login_screen
from database import cursor, conn


def start_login(root):
    login_screen(root)

