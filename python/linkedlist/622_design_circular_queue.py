
class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None] * k  # Initialize queue with fixed size
        self.max_size = k  # Store the max size of the queue
        self.front = -1  # Initialize front pointer
        self.rear = -1  # Initialize rear pointer

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = 0  # First element to be enqueued
        self.rear = (self.rear + 1) % self.max_size  # Move rear pointer
        self.queue[self.rear] = value
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        if self.front == self.rear:
            # Only one element was in the queue, now it's empty
            self.front = -1
            self.rear = -1
        else:
            # Move the front pointer to the next element
            self.front = (self.front + 1) % self.max_size
        return True
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.front]
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.rear]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.front == -1
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return (self.rear + 1) % self.max_size == self.front