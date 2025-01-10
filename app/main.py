import sys
import os


def main():
    # Uncomment this block to pass the first stage
    # sys.stdout.write("$ ")
    sys.stdout.write("$ ")
    builtin_cmds = ["echo", "exit", "type"]
    PATH = os.environ.get("PATH")
    # Wait for user input
    while True:
        command = input()
        # if ans := input().strip():
        if command == "exit 0":
            sys.exit(0)
        elif command.startswith("type"):
            cmd = command.split(" ")[1]
            cmd_path = None
            paths = PATH.split(":")
            for path in paths:
                if os.path.isfile(f"{path}/{cmd}"):
                    cmd_path = f"{path}/{cmd}"
            if cmd in builtin_cmds:
                sys.stdout.write(f"{cmd} is a shell builtin\n")
                sys.stdout.write("$ ")
            elif cmd_path:
                sys.stdout.write(f"{cmd} is {cmd_path}\n")
                sys.stdout.write("$ ")
            else:
                sys.stdout.write(f"{cmd} not found\n")
                sys.stdout.write("$ ")
            sys.stdout.flush()
        elif "echo" in command:
            print(f"{command[5:]}")
            sys.stdout.write("$ ")
        else:
            if os.path.isfile(command.split(" ")[0]):
                os.system(command)
            else:
                sys.stdout.write(f"{command}: command not found\n")
                sys.stdout.write("$ ")
                sys.stdout.flush()
if __name__ == "__main__":
    main()
