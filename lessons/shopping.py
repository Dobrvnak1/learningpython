products = ["молоко", "куриная грудка", "рис"]
count = 0
print(f"У вас в корзине {len(products)} товара, такие как: ")
for product in products:
    count += 1
    print(f"{count}.{product}")
while True:
    shopping_basket = input("Что вы ещё хотите добавить в корзину?  ")
    shopping_basket = " ".join(shopping_basket.lower().split())
    if shopping_basket == "ничего":
        break
    if shopping_basket == "":
        continue
    if shopping_basket in products:
        print("У вас уже есть такой товар :) ")
    else:
        products.append(shopping_basket)
products.sort()
count = 0
print(f"У вас {len(products)} товара, такие как: ")
for product in products:
    count += 1
    print(f"{count}.{product}")
