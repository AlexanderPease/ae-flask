from werkzeug.security import check_password_hash, generate_password_hash


def get_password_hash(password):
    """Returns the hash for input password."""
    return generate_password_hash(password)


def check_password_hash(password_hash, password):
    """Checks if a password matches a hash."""
    return check_password_hash(password_hash, password)
