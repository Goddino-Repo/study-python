# Simple program that checks if the water is boiling

temperature_boil = 100
temperature_now = int(input("What is the water temperature now? "))
if temperature_now < temperature_boil:
    output = "Not boiling"
else:
    output = "Boiling"
print(output)
