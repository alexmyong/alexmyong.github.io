def file_to_list(filename):
    with open(filename,'r') as file:
        numbers = [line.strip() for line in file.readlines()]
    return license

filename = 'numbers.txt'
numbers = file_to_list(filename)

print(numbers)