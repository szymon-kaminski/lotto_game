import random


def draw_lotto_numbers():
    return sorted(random.sample(range(1, 50), 6))


def get_user_numbers():
    numbers = []
    print("Enter your 6 numbers from 1 to 49:")
    while len(numbers) < 6:
        try:
            num = int(input(f"Enter number {len(numbers) + 1}:"))
            if 1 <= num <= 49 and not in numbers:
                numbers.append(num)
            else:
                print("Number must be between 1 to 49 and cannot be repeated.")
        except ValueError:
            print("Please enter a valid number.")
    return sorted(numbers)    