import random


def draw_lotto_numbers():
    return sorted(random.sample(range(1, 50), 6))