from random import randint

N = 10
a = []
for i in range(N):
    a.append(randint(1, 99))
print(a)

for i in range(N - 1):
    for j in range(N - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)



def binary_search(list1, n):
    low = 0
    high = len(list1) - 1
    mid = 0

    while low - n:
        high = mid - 1

        # If n is smaller, compared to the left of mid
    else:
        return mid

        # element was not present in the list, return -1
    return -1


# Initial list1
list1 = [12, 24, 32, 39, 45, 50, 54]
n = 12

# Function call
result = binary_search(list1, n)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in list1")