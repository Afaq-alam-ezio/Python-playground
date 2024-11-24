def optimal(pages, capacity):
    """
    Implement the Optimal Page Replacement algorithm.

    Parameters:
    pages (list): List of page references.
    capacity (int): The number of frames in the memory.

    Returns:
    int: The number of page faults.
    """
    memory = []  # List to represent the frames in memory
    page_faults = 0  # Counter for page faults

    for page in pages:
        if page not in memory:
            if len(memory) < capacity:
                memory.append(page)
            else:
                # Find the page in memory that won't be used for the longest period of time
                farthest_used = -1
                farthest_page = None
                for mem_page in memory:
                    try:
                        farthest_index = pages.index(mem_page, pages.index(page) + 1)
                        if farthest_index > farthest_used:
                            farthest_used = farthest_index
                            farthest_page = mem_page
                    except ValueError:
                        farthest_used = len(pages)
                        farthest_page = mem_page
                        break
                memory.remove(farthest_page)
                memory.append(page)
            page_faults += 1

    return page_faults


# Example usage:
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
capacity = 4
page_faults = optimal(pages, capacity)
print("Number of page faults using Optimal:", page_faults)
