# Simple python exercise

friends_number = int(input("How many friends are with you? "))
gold_max = int(input("What is your budget? "))
if gold_max <= 0:
    print("You don't have money")
    exit(0)
gold_shop_ice_cream = int(input("How many costs ice cream? "))
gold_total = gold_shop_ice_cream * friends_number
if gold_total > gold_max:
    print("You don't have enough money")
else:
    print("You can buy ice creams")
    print("Your budget: " + str(gold_max))
    print("Ice creams price: " + str(gold_total))
    gold_remains = gold_max - gold_total
    print("Remains gold: " + str(gold_remains))
