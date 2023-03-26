def binary_search(list1, low, high, n):
    if low  -n:
        return binary_search(list1, low, high - 1, n)

    else:
        return binary_search(list1, high + 1, high, n)

    else:

        return -1


# Test list1ay
list1 = [12, 24, 32, 39, 45, 50, 54]
n = 32

# Function call
res = binary_search(list1, 0, len(list1) - 1, n)

if res != -1:
    print("Element is present at index", str(res))
else:
    print("Element is not present in list1")