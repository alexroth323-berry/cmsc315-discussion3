"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # Validate index bounds to prevent IndexError
    if index < 0 or index > len(lst):
        print(f"Error: Index {index} is out of bounds for insertion.")
        return

    # Python's list.insert(index, value) shifts all elements from the specified
    # index one position to the right to make space for the new item.
    # Performance Note: Inserting at the beginning or middle is O(n) because
    # elements must be shifted in memory. Inserting at the end (lst.append or
    # insert at index == len(lst)) is O(1) amortized since no shifting is required.
    lst.insert(index, value)
    print(f"Inserted '{value}' at index {index}. Updated list: {lst}")


def delete_at(lst, index):
    """
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Index validation is critical to prevent application crashes caused by
    # IndexError exceptions when trying to access non-existent memory slots.
    # Safe deletion ensures boundary conditions are checked prior to mutating data.
    if index < 0 or index >= len(lst):
        print(f"Error: Invalid index {index} for deletion.")
        return None

    # pop(index) removes and returns the element at the given index,
    # shifting subsequent elements left to fill the gap.
    removed_value = lst.pop(index)
    print(f"Deleted '{removed_value}' from index {index}. Updated list: {lst}")
    return removed_value


def search_value(lst, value):
    """
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # This implements a linear search. It scans sequentially from index 0
    # to the end of the list, comparing each element against the target value.
    # Time Complexity: O(n) in the worst case, because every element may need
    # to be inspected if the item is at the end or missing entirely.
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # INSERTION TESTS
    # ===============================
    print("\n=== INSERTION TESTS ===")
    playlist = ["Song A", "Song B", "Song C"]
    print(f"Original Playlist: {playlist}")

    # 1. Insert at the beginning (index 0) - Causes full right-shift (O(n))
    print("\nTesting insertion at the beginning:")
    insert_at(playlist, 0, "Intro Song")

    # 2. Insert at the middle (index 2) - Causes partial right-shift
    print("\nTesting insertion in the middle:")
    insert_at(playlist, 2, "Interlude")

    # 3. Insert at the end (index == len(playlist)) - O(1) append behavior
    print("\nTesting insertion at the end:")
    insert_at(playlist, len(playlist), "Outro Song")

    # ===============================
    # DELETION TESTS
    # ===============================
    print("\n=== DELETION TESTS ===")
    print(f"Current list before deletions: {playlist}")

    # 1. Delete from the beginning (index 0) - Triggers left-shift of all elements
    print("\nTesting deletion from the beginning:")
    delete_at(playlist, 0)

    # 2. Delete from the middle
    print("\nTesting deletion from the middle:")
    delete_at(playlist, 2)

    # 3. Delete from the end
    print("\nTesting deletion from the end:")
    delete_at(playlist, len(playlist) - 1)

    # ===============================
    # SEARCH TESTS
    # ===============================
    print("\n=== SEARCH TESTS ===")
    current_songs = ["Song B", "Interlude", "Song C"]
    print(f"Active List for Searching: {current_songs}")

    # 1. Search for a value that exists
    target = "Interlude"
    result_idx = search_value(current_songs, target)
    if result_idx != -1:
        print(f"Success: Found '{target}' at index {result_idx}.")
    else:
        print(f"'{target}' was not found.")

    # 2. Search for a value that does not exist
    missing_target = "Nonexistent Track"
    result_idx = search_value(current_songs, missing_target)
    if result_idx != -1:
        print(f"Found '{missing_target}' at index {result_idx}.")
    else:
        print(f"Confirmed: '{missing_target}' does not exist in the list (Returned -1).")

    # ===============================
    # EDGE CASES
    # ===============================
    print("\n=== EDGE CASES ===")
    empty_list = []

    # Edge Case 1: Deleting from an empty list with invalid index handling
    print("Edge Case 1: Attempting to delete from an empty list.")
    delete_at(empty_list, 0)

    # Edge Case 2: Inserting out-of-bounds with boundary validation check
    print("\nEdge Case 2: Attempting an out-of-bounds positive index insertion.")
    insert_at(current_songs, 50, "OutOfBounds Song")


if __name__ == "__main__":
    main()