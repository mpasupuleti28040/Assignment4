class Task:
    def __init__(self, task_id, priority):
        self.task_id = task_id
        self.priority = priority

    def __repr__(self):
        return f"Task(ID={self.task_id}, Priority={self.priority})"

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, task):
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move last element to root
        self._heapify_down(0)
        return root

    def increase_key(self, task_id, new_priority):
        # Find the task with task_id
        for i, task in enumerate(self.heap):
            if task.task_id == task_id and new_priority > task.priority:
                task.priority = new_priority
                self._heapify_up(i)
                return task
        return None

    def decrease_key(self, task_id, new_priority):
        # Find the task with task_id
        for i, task in enumerate(self.heap):
            if task.task_id == task_id and new_priority < task.priority:
                task.priority = new_priority
                self._heapify_down(i)
                return task
        return None

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index].priority > self.heap[parent].priority:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if left < len(self.heap) and self.heap[left].priority > self.heap[largest].priority:
            largest = left
        if right < len(self.heap) and self.heap[right].priority > self.heap[largest].priority:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def is_empty(self):
        return len(self.heap) == 0

# Example Usage
pq = PriorityQueue()
pq.insert(Task("Task1", 3))
pq.insert(Task("Task2", 7))
pq.insert(Task("Task3", 1))

# Increase priority of Task1
pq.increase_key("Task1", 8)

print("Max priority task extracted:", pq.extract_max())

# Decrease priority of Task2
pq.decrease_key("Task2", 2)

print("Max priority task extracted:", pq.extract_max())
