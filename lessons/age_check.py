age = int(input("Укажите ваш год рождения "))
current_year = 2026
age = (current_year - age)
print(age)
if age >= 18:
    print("Ты уже взрослый и наверно самостоятельный человек")
elif age <= 18:
    print("Ты ещё школьник")
else:
    print("У тебя ещё молоко на губах не обсохло")
