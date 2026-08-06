import random
import string


def generate_short_code(length: int = 7) -> str:
    alphabet = string.ascii_letters + string.digits

    return "".join(random.choices(alphabet, k=length))