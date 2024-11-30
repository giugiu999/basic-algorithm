def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # The element to be inserted
        j = i - 1
        # Move elements of the sorted portion that are greater than the key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        # Insert the key at the correct position
        arr[j + 1] = key
    return arr

# testing
if __name__ == "__main__":
    data = [12, 11, 13, 5, 6]
    print("Original array:", data)
    sorted_data = insertion_sort(data)
    print("Sorted array:", sorted_data)
