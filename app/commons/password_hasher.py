from argon2 import PasswordHasher

hasher = PasswordHasher()


def hash_password(password: str) -> str:
    return hasher.hash(password)


def verify_password(password: str, hased_password: str) -> bool:
    try:
        return hasher.verify(hash=hased_password, password=password)
    except:
        return False
