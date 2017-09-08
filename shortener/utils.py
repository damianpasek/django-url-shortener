import random
import string


def generate_code(max_length=6):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=max_length))
