from src.auth.manager import AuthManager

def test_auth():
    auth = AuthManager()
    assert auth.authenticate('user', 'token') == True
