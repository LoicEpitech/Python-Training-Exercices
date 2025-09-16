# Task 2.2
17**24

# Task 3.1
a = 42
b = 4
virgule = a / b
a = a // b
reste = a % b
print(virgule)
print(a)
print(reste)
# 10.5
# 10
# 2

# Task 3.2
a = int(input())
if (a % 2) == 0:
    print("pair")
else:
    print("impair")

# Task 3.3 & 3.4 & 3.5
list = [1, 2, 3, 4, 3, 4, 5, 6, 5]
list2 = [3, 4, 5, 5, 6, 7, 4, 2, 6]
list3 = [4, 4, 4, 9, 0, 3, 2, 0, 0, 9, 7]
sum = 0
for i in list:
    sum = sum + i
print(sum)
numbers = [12.24, 424242.8412]
integer_parts = [int(num) for num in numbers]
print(integer_parts)
numbers = [12.24, 424242.8412]
decimal_parts = [num - int(num) for num in numbers]
print(decimal_parts)

# Task 4.1
π = 0
impaire = 1
signe = 1
i = 100000
while i != 0:
    π += signe * (1 / impaire)
    signe *= -1
    impaire += 2
    i -= 1
π *= 4
print(π)

# Task 4.2
epsilon = 5e-7
N = 1
pi_prec = 0
max_N = 1000
while N < max_N:
    val = 2
    for k in range(N, 0, -1):
        n = 2 * k - 1
        val = n**2 / (6 + val)
    pi = 3 + val
    if abs(pi - pi_prec) < epsilon:
        break
    pi_prec = pi
    N += 1
print(pi)
