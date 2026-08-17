# Write your solution here
# Model Solution
# def greatest_number(a, b, c):
#     if a >= b and a >= c:
#         return a
#     elif b >= c:
#         return b
#     else:
#         return c


def max(a, b):
    if a > b:
        return a
    else:
        return b

def greatest_number(a,b,c):
    return max(max(max(a,b),max(b,c)),max(c,a))


# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)