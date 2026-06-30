def authenticate(username, password):
    """
    Simple demo authentication (FREE VERSION)
    In production this would be replaced with a real user system.
    """
    return username == "admin" and password == "admin"
