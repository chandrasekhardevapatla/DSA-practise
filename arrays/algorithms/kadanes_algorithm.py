def maximun_sub_array(arr: list) -> list:
    """
    Find the maximum sub array sum and print the array

    """
    if len(arr) < 1:
        return
    
    current_sum = maximum_sum = arr[0]
    start = end = temp_start = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[i] + current_sum:
            current_sum = arr[i]
            temp_start = i
        else:
            current_sum += arr[i]

        if current_sum > maximum_sum:
            maximum_sum = current_sum
            start = temp_start
            end = i
    print(f'Maximum sub array: {arr[start:end+1]}')
    return maximum_sum

