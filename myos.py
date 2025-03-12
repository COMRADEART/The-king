import os
import time

#sim file system (using dictionary)
filesystem = {"file.txt": "Hello, this is a test file!"}

def shell():
    print("welcome to myphyos v0.1")
    while True:
        command = input("MyOS> ").strip().lower()
        parts = command.split() # split command into parts
        cmd = parts[0] if parts else ""

        if cmd == "exit":
            print("Shuttin down...")
            break
        elif cmd == "list":  # list file in current direction
            print("Files:", list(filesystem.keys()))
        elif cmd == "read" and len(parts) > 1:
            filename = parts[1]
            if filename in filesystem:
                print(filesystem[filename])
            else:
                print(f"Files '{filename}' not found.")
        elif cmd == "create" and len(parts) > 1:
            filename = parts[1]
            if filename in filesystem:
                print(f"File '{filename}' already exits.")
            else:
                filesystem[filename] = "New file content"
                print(f"Created '{filename}'.")
        elif cmd == "time":
            print("Current time:", time.ctime())
        elif cmd == "clear": # clear terminal
            os.system("clear")
        elif cmd == "":
            continue
        else:
            print(f"command '{cmd}' not recognized ")

if __name__ == "__main__":
    shell()


