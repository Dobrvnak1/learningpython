year_of_birth = int(input("Укажите ваш год рождения "))
current_year = 2026
age = (current_year - year_of_birth)
if age >= 18:
    print("Ты уже взрослый и наверно самостоятельный человек")
elif age == 17:
    print("Ты ещё школьник")
elif age >= 14:
    print("Ты ещё школьник")
else:
    print("У тебя ещё молоко на губах не обсохло")
print(type(input))
