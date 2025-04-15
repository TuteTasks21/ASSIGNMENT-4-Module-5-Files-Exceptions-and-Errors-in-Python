#Task 2: Write and Append Data to a File

def write_and_append_to_file():
    user_input = input("Enter some text to write to the file: ")
    with open('output.txt', 'w') as file:
        file.write(user_input + '\n')
    additional_data = input("Enter some additional text to append to the file: ")
    
    with open('output.txt', 'a') as file:
        file.write(additional_data + '\n')
    print("\nFinal content of the file:")
    with open('output.txt', 'r') as file:
        content = file.read()
        print(content)

write_and_append_to_file()

