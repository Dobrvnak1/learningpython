hidden_number = 7
attempts = 0
while True:
    input_number = (input("Угадай число от 1 до 10: "))
    if input_number == "":
        print("Пустая строка не считается '_' ")
        continue
    input_number = int(input_number)
    attempts = attempts + 1
    if  input_number == hidden_number:
        print(f"Поздравляю ты угадал число {hidden_number} за {attempts} раз")
        break
    if attempts == 5:
        print("Попытки кончились, ты проиграл")
        break
    print("Попробуй ещё раз")
