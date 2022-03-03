def list_sum_recursive(input_list):
    if not input_list:
        return 0

    head = input_list[0]
    smaller_list = input_list[1:]
    return head + list_sum_recursive(smaller_list)

print(list_sum_recursive([1, 2, 3]))

# 6