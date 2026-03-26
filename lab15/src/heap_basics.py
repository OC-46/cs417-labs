"""
Lab 15: Heap Basics — Getting comfortable with heapq

Tasks 1 and 2: Explore the heapq API and work with tuple priorities.
"""

import heapq


# ── Task 1: Heap Basics ─────────────────────────────────────────────


def push_and_pop(values):
    """Push all values onto a heap, then pop them all off.

    Args:
        values: A list of numbers.

    Returns:
        A list of the same numbers in ascending order.
    """
    # TODO: Create a heap, push each value, pop them all off
    list = []
    for i in values:
        heapq.heappush(list, i)
    sorted_list = []
    for i in range(len(list)):
        sorted_list.append(heapq.heappop(list))
    return sorted_list



def heapify_and_peek(values):
    """Turn a list into a heap and return the smallest value.

    Args:
        values: A list of numbers.

    Returns:
        The smallest value (without removing it from the heap).
    """
    # TODO: Use heapq.heapify(), then peek with h[0]
    heapq.heapify(values)
    return values[0]



def top_k_smallest(values, k):
    """Return the k smallest values in ascending order.

    Args:
        values: A list of numbers.
        k: How many smallest values to return.

    Returns:
        A list of the k smallest values, sorted ascending.
    """
    # TODO: Use heapq to find the k smallest values
    heapq.nsmallest(k, values)
    return heapq.nsmallest(k, values)


# ── Task 2: Tuple Priorities ────────────────────────────────────────


def sort_by_priority(tasks):
    """Sort tasks by priority, maintaining FIFO order for equal priorities.

    Args:
        tasks: A list of (priority, description) tuples.

    Returns:
        A list of description strings in priority order.
        Same-priority tasks appear in their original order.
    """
    # TODO: Use a heap with a sequence counter as tiebreaker
    heap = []
    for i, task in enumerate(tasks):
        heapq.heappush(heap, (task[0], i, task[1]))
    
    sorted_tasks = []
    for i in range(len(heap)):
        sorted_tasks.append(heapq.heappop(heap)[2])
    return sorted_tasks




