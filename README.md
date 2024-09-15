# Priority Queue and Heapsort Implementation

## Project Overview

This project consists of two core components: Heapsort and a Priority Queue implementation using a max-heap. Both algorithms are implemented in Python and use a binary heap represented as a list (or array). The Heapsort algorithm is used to sort an array in-place by first building a max-heap, and the priority queue is designed to manage tasks based on their priorities using a max-heap structure.

### Heapsort Implementation

The Heapsort algorithm begins by building a max-heap from the input array, then repeatedly extracts the maximum element (the root of the heap), placing it at the end of the array. The heap property is restored after each extraction by re-heapifying the remaining elements.

#### Key Operations:
- **Heapify:** Ensures the max-heap property is maintained for a subtree.
- **Heapsort:** Builds the max-heap and sorts the array.

### Priority Queue Implementation

The priority queue is implemented using a binary max-heap, where tasks are stored along with their priority values. The queue supports the insertion of new tasks, extracting the task with the highest priority, and checking if the queue is empty.

#### Key Operations:
- **Insert:** Adds a new task to the priority queue while maintaining the heap property.
- **Extract Max:** Removes and returns the task with the highest priority.
- **Is Empty:** Checks if the priority queue is empty.

---

## How to Run the Code

### Heapsort
1. Clone the repository.
2. Navigate to the project directory.
3. Run the Heapsort implementation by calling the `heapsort()` function with any array of numbers:
    ```python
    arr = [12, 11, 13, 5, 6, 7]
    heapsort(arr)
    print("Sorted array:", arr)
    ```

### Priority Queue
1. Instantiate the `PriorityQueue` class.
2. Insert tasks with a task ID and priority.
3. Extract tasks in the order of their priority using `extract_max()`:
    ```python
    pq = PriorityQueue()
    pq.insert(Task("Task1", 2))
    pq.insert(Task("Task2", 5))
    print(pq.extract_max())
    ```

## File Structure

- **heapsort.py:** Contains the implementation of the Heapsort algorithm.
- **priority_queue.py:** Contains the implementation of the Priority Queue with insert and extract operations.
- **README.md:** This file.

---

## Time Complexity Analysis

- **Heapsort:**
  - Worst-case, Best-case, and Average-case time complexity: O(n log n)
  - Space complexity: O(1)
  
- **Priority Queue Operations:**
  - Insertion and Extraction: O(log n)
  - Space complexity: O(n)

---

## License

This project is licensed under the MIT License.
