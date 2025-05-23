def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Find middle
        left = arr[:mid]     # Dividing the array into two halves
        right = arr[mid:]

        merge_sort(left)     # Sorting the first half
        merge_sort(right)    # Sorting the second half

        # Merging two halves
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # If anything left in left array
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # If anything left in right array
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Example usage
arr = [12, 11, 13, 5, 6, 7]
print("Original array:", arr)

merge_sort(arr)

print("Sorted array:", arr)
