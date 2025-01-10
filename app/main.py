import sys


def main():
    # Uncomment this block to pass the first stage
    # sys.stdout.write("$ ")
    sys.stdout.write("$ ")

    
    # Wait for user input
    while True:
        command = input()
        # if ans := input().strip():
        if command == "exit 0":
            sys.exit(0)
        elif "type" in command:
            if command[5:] in ['echo', 'type', 'exit']:
                print(f"{command[5:]} is a shell builtin")
                # print(f"{command[5:]} not found")
            else:
                sys.stdout.write(f"{command}: command not found\n")
                sys.stdout.write("$ ")
        elif "echo" in command:
            print(f"{command[5:]}")
            sys.stdout.write("$ ")
        else:
            sys.stdout.write(f"{command}: command not found\n")
            sys.stdout.write("$ ")
if __name__ == "__main__":
    main()
