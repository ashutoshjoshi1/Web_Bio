import sys


def main():
    # Uncomment this block to pass the first stage
    # sys.stdout.write("$ ")
    sys.stdout.write("$ ")

    
    # Wait for user input
    while True:
        command = input()
        if command == 'exit':
            return 0
        else:
            sys.stdout.write(f"{command}: command not found\n")
            sys.stdout.write("$ ")
            sys.stdout.flush()
if __name__ == "__main__":
    main()
