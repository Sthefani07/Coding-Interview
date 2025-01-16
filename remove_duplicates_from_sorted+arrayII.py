def remove_duplicates(nums):
    write = 0  # Position to write the next valid number
    
    for read in range(len(nums)):
        # Check if it's safe to write the current number
        if write < 2 or nums[read] != nums[write - 2]:
            nums[write] = nums[read]
            write += 1
    
    return write

