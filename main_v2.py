import random


def draw_lotto_numbers():
    return sorted(random.sample(range(1, 50), 6))


def get_user_numbers():
    numbers = []
    print("Enter your 6 numbers from 1 to 49:")
    while len(numbers) < 6:
        try:
            num = int(input(f"Enter number {len(numbers) + 1}:"))
            if 1 <= num <= 49 and num not in numbers:
                numbers.append(num)
            else:
                print("Number must be between 1 to 49 and cannot be repeated.")
        except ValueError:
            print("Please enter a valid number.")
    return sorted(numbers)    


def compare_numbers(drawn, user):
    return len(frozenset(drawn) & frozenset(user)), set(drawn) & set(user)


def main():
    drawn_numbers = draw_lotto_numbers()
    user_numbers = get_user_numbers()
    matches, matched_numbers = compare_numbers(drawn_numbers, user_numbers)

    print(f"Drawn numbers: {drawn_numbers}")
    print(f"User numbers: {user_numbers}")
    print(f"You matched: {matches} number(s): {matched_numbers}" if matches > 0 else "You did not match any numbers.")


if __name__ == "__main__":
    main()