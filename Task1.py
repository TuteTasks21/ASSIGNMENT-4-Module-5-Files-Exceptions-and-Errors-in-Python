#Task 1: Read a File and Handle Errors 

def read_file():
    try:
        with open('sample.txt', 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Error: The file 'sample.txt' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_file()
