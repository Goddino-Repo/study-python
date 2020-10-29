# you have a to choice either $1.000.000 or $0.01 doubled every day for 30 days
# Do your choice using the exponential

now = 1000000
day = 0.01
result = day*(2**29)
if result > now:
    output = "i choose 0.01"
else:
    output = "i choose 1.000.000"

print(output)
