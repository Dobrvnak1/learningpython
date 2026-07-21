sentence = input("Введите своё предложение  ")
first_letter = sentence[0]
if first_letter == first_letter.upper():
    print("Первая буква заглавная")
else:
    print("Первая буква не заглавная")
letter_a = sentence.lower().count("а")
print(f"В этом предложении {letter_a} букв 'а'")
word_count = sentence.split()
word_count = len(word_count)
print(f"В этом предложении {word_count} слов")
word_python = "python"
if word_python in sentence.lower():
    print("Тут есть слово Python")
else:
    print("Тут нет слова Python")
