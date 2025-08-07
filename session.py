# session.py
current_user_id = None
current_username = None

def set_user(user_id, username):
    global current_user_id, current_username
    current_user_id = user_id
    current_username = username

def clear_user():
    set_user(None, None)
