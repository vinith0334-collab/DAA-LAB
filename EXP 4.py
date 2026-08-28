import random

comparison_count = 0  # Global counter


# Divide and Conquer
def min_max_dc(arr, low, high):
    global comparison_count

    # Base case: one element
    if low == high:
        return arr[low], arr[low]

    # Base case: two elements
    if high == low + 1:
        comparison_count += 1
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    # Divide
    mid = (low + high) // 2

    lmin, lmax = min_max_dc(arr, low, mid)
    rmin, rmax = min_max_dc(arr, mid + 1, high)

    # Combine
    comparison_count += 1
    overall_min = lmin if lmin < rmin else rmin

    comparison_count += 1
    overall_max = lmax if lmax > rmax else rmax

    return overall_min, overall_max


# Naive Method
def min_max_naive(arr):
    mn = arr[0]
    mx = arr[0]
    comps = 0

    for x in arr[1:]:
        comps += 1
        if x < mn:
            mn = x

        comps += 1
        if x > mx:
            mx = x

    return mn, mx, comps


# ---------------- Small Example ----------------
arr = [3, 1, 7, 4, 9, 2, 8, 5, 6, 0]

comparison_count = 0

mn, mx = min_max_dc(arr, 0, len(arr) - 1)
dc_comps = comparison_count

_, _, naive_comps = min_max_naive(arr)

print("Array:", arr)
print("Minimum:", mn)
print("Maximum:", mx)
print("D&C Comparisons:", dc_comps)
print("Naive Comparisons:", naive_comps)


# ---------------- Performance Analysis ----------------
print("\n{:>8} {:>12} {:>14} {:>16}".format(
    "Size", "DC Comps", "Naive Comps", "Formula"
))
print("-" * 56)

for size in [10, 100, 1000, 10000]:
    arr = [random.randint(1, 10000) for _ in range(size)]

    comparison_count = 0

    mn, mx = min_max_dc(arr, 0, len(arr) - 1)
    dc = comparison_count

    _, _, naive = min_max_naive(arr)

    formula = (3 * size) // 2 - 2

    print("{:>8} {:>12} {:>14} {:>16}".format(
        size, dc, naive, formula
    ))

OUTPUT:
Array: [3, 1, 7, 4, 9, 2, 8, 5, 6, 0]
Minimum: 0
Maximum: 9
D&C Comparisons: 14
Naive Comparisons: 18

    Size     DC Comps    Naive Comps          Formula
--------------------------------------------------------
      10           14             18               13
     100          162            198              148
    1000         1510           1998             1498
   10000        15902          19998            14998
