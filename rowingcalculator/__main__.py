# This program acts to convert a unit such as mph or km/h into a time/500m split

# Setting variable at the start
input_speed = 0
output_split = 0
converting_from = 0
number_of_options = 0

# Importing text file with conversion options
options_list = 'things.txt'
options_list.close()

# Program
print('################################################')
print('\n\nProgram starting up - please wait\n\n')
print('################################################')

def rowing_conversion():
    try:
        with open(options_list,'r') as fp:
            number_of_options = len(fp.readlines())
            print(number_of_options)
            # print("Please select from the options below [1-",number_of_options,"] what you are converting FROM!")
        with open(options_list, 'r') as file:
            file_content = file.read()
            print(file_content)
    except FileNotFoundError:
        print(f'File '{'options_list'}' not found.')
    except Exception as e:
        print(f'An error occured: {e}')

options_list.close()

rowing_conversion()