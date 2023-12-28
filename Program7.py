# WRITE A PYTHON FUNCITON THAT TAKES A LIST AND RETURNS A NEW LIST WITH DISTINCT ELEMENTS FROM THE FIRST LIST.
# Sample list i/p: [1,2,3,3,3,3,4,5]
# Unique list i/p: [1,2,3,4,5]


def remove_duplicates(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

# Example usage:
sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
result_list = remove_duplicates(sample_list)
print(f"Original list: {sample_list}")
print(f"List with distinct elements: {result_list}")
