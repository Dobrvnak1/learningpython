hidden_number = 7
attempts = 0
input_number = int(input("Угадай число от 1 до 10: "))
attempts = attempts + 1
if input_number == hidden_number:
    print(f"Поздравляю ты угадал число {hidden_number} с первой попытки")
else:
    while input_number != hidden_number:
        print("Try again")
        attempts = attempts + 1
        input_number = int(input("Угадай число от 1 до 10: "))
    print(f"Поздравляю ты угадал число {hidden_number} за {attempts} раз")