def find_combinations(target, items):
    def find_combinations_helper(target, current_combination, start_index):
        if target == 0:
            # Base case: Combination found, print it
            print(current_combination)
            return
        if target < 0:
            # Base case: Target exceeded, no valid combination
            return

        for i in range(start_index, len(items)):
            # Explore each possibility
            new_combination = current_combination + [items[i]]
            find_combinations_helper(target - items[i], new_combination, i)

    find_combinations_helper(target, [], 0)

# Test the find_combinations function
target_value = 10
item_list = [2, 3, 5]
print(f"Combinations that sum up to {target_value}:")
find_combinations(target_value, item_list)
