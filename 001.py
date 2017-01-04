
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

sum = 0
for i in range(1000//3 + 1):
    sum += i * 3
    multiply_5 = i * 5
    if i < 200 and (i * 5) % 3 != 0:
        sum += i * 5

print(sum)
