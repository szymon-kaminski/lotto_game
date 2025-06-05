import random

lotto_numbers = random.sample(range(1,50), 6)

user_input = input("Podaj sześć różnych liczb z zakresu 1-49, oddzielając je spacją: ")
user_numbers = [int(num) for num in user_input.split()]

matches = [num for num in user_numbers if num in lotto_numbers]

print(f"\nTwoje liczby: {user_numbers}")
print(f"Wylosowane liczby: {lotto_numbers}")
print(f"Trafione liczby: {matches}")
print(f"Liczba trafień: {len(matches)}")
