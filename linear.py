def linear_search(arr, target):
    """
    Performs linear search on an array.
    
    Args:
        arr: List to search in
        target: Element to search for
    
    Returns:
        Index of target if found, otherwise -1
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Example usage
if __name__ == "__main__":
    numbers = [10, 25, 30, 45, 50, 70]
    target = 45
    
    result = linear_search(numbers, target)
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found")