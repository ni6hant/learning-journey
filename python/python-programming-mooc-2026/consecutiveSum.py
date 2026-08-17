# Write your solution here
limit = int(input("Limit: "))
number = 1
sum = 0
consecutiveSum = "1 "
total = 0

while sum <= limit:
    sum += number
    number += 1
    consecutiveSum += f"+ {number} "
    total += number

print(f"{consecutiveSum} = {total}")