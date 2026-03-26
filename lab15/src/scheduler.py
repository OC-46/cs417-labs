"""
Lab 15: Task Scheduler — A priority queue in action

Task 3: Build a TaskScheduler class using heapq.
"""

import heapq


class TaskScheduler:
    """A priority-based task scheduler.

    Tasks are added with a priority (lower number = more urgent).
    Tasks with the same priority are processed in FIFO order.
    """

    def __init__(self):
        """Initialize the scheduler."""
        # TODO: Set up your internal data structures
        self.heap = []
        self._counter = 0
        self._len = 0


    def add_task(self, priority, description):
        """Add a task to the scheduler.

        Args:
            priority: An integer priority (lower = more urgent).
            description: A string describing the task.
        """
        # TODO: Push onto the heap with a tiebreaker
        heapq.heappush(self.heap, (priority, self._counter, description))
        self._counter += 1
        self._len += 1

    def next_task(self):
        """Remove and return the highest-priority task's description.

        Returns:
            The description string, or None if empty.
        """
        # TODO: Pop from the heap, return the description
        if self.is_empty():
            return None
        else:
            self._len -= 1
            return heapq.heappop(self.heap)[2]

    def peek(self):
        """Return the highest-priority task's description without removing it.

        Returns:
            The description string, or None if empty.
        """
        # TODO: Look at h[0] without popping
        if self.is_empty():
            return None
        else:
            return self.heap[0][2]
        


    def __len__(self):
        """Return the number of pending tasks."""
        # TODO: Return the length of the heap
        return self._len

    def is_empty(self):
        """Return True if there are no pending tasks."""
        # TODO
        return self._len == 0
    
