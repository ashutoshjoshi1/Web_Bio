import sys


def main():
    # Uncomment this block to pass the first stage
    # sys.stdout.write("$ ")
    sys.stdout.write("$ ")

    
    # Wait for user input
    command = input()
    while command != 'quit':
        print(f"{command}: command not found")
        main()

if __name__ == "__main__":
    main()
