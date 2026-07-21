word = input("Напишите слово: ")
word = word.lower().replace(" ", "")
if word == "":
    print("Пустая строка не считается '_' ")
elif word[::-1] == word:
    print(f"Слово {word} является палиндромом")
else:
    print("Это не палиндром")
