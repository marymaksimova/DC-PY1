list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_index = 0
max_element = list_numbers[max_index]
last_element = list_numbers[-1]

for i, current_element in enumerate(list_numbers):
    max_element = list_numbers[max_index]
    if current_element > max_element:
        max_index = i
        max_element = list_numbers[max_index]

list_numbers[-1] , list_numbers[max_index] = max_element , last_element

print(list_numbers)
