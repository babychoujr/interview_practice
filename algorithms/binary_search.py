

"""
Time Complexity: O(log n)
Space Complexity: O(1)

Assumptions
-----------
- sorted array
"""
def binary_search(input_array, target):

    input_array.sort()

    found = False

    left = 0
    right = len(input_array) - 1

    while left <= right:

        mid = left + (right - left) // 2

        if input_array[mid] == target:
            found = True
            return found

        if input_array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return found

def recursive_bs(input_array, left, right, target):

    if left <= right:

        mid = left + (right - left) // 2

        if input_array[mid] == target:
            return True
        
        if input_array[mid] > target:
            return recursive_bs(input_array, left, mid - 1, target)
        else:
            return recursive_bs(input_array, mid + 1, right, target)
        
    return False



if __name__ == "__main__":
    

    l = [6, 2, 3, 4, 5]
    l.sort()
    print(binary_search(l, 3))

    print(recursive_bs(l, 0, len(l) -1, 7))