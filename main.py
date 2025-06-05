import random

lotto_numbers = random.sample(range(1,50), 6)
print("Wylosowane liczby lotto to: ", lotto_numbers)

user_input = input("Podaj sześć różnych liczb z zakresu 1-49, oddzielając je spacją: ")
user_numbers = [int(num) for num in user_input.split()]