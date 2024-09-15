def heapify(arr, n, i):
    largest = i  # Assume i is the largest
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # Check if the left child is larger than the current largest
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if the right child is larger than the current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest is not the current node, swap and heapify again
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    if len(arr) == 0:  # Edge case for empty array
        return arr
    elif len(arr) == 1:  # Edge case for single element
        return arr
    
    n = len(arr)

    # Build the max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)  # Heapify the reduced heap

# Example usage
arr = [19, 2, 31, 45, 6, 11, 121, 27]
heapsort(arr)
print("Sorted array is:", arr)
