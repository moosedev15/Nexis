import os
import shutil
from datetime import datetime

class Terminal:
    def __init__(self):
        self.commands = {
            "help": {"func": self.help, "description": "Displays this help message.", "usage": "help"},
            "ls": {"func": self.list_files, "description": "Lists files in the current directory.", "usage": "ls"},
            "cd": {"func": self.change_directory, "description": "Changes the current directory.", "usage": "cd <path>"},
            "mkdir": {"func": self.make_directory, "description": "Creates a new directory.", "usage": "mkdir <dirname>"},
            "rmdir": {"func": self.remove_directory, "description": "Removes a directory.", "usage": "rmdir <dirname>"},
            "touch": {"func": self.create_file, "description": "Creates an empty file.", "usage": "touch <filename>"},
            "rm": {"func": self.remove_file, "description": "Removes a file.", "usage": "rm <filename>"},
            "pwd": {"func": self.print_working_directory, "description": "Prints the current working directory.", "usage": "pwd"},
            "echo": {"func": self.echo, "description": "Prints the provided text.", "usage": "echo <text>"},
            "cat": {"func": self.read_file, "description": "Displays the contents of a file.", "usage": "cat <filename>"},
            "cp": {"func": self.copy_file, "description": "Copies a file.", "usage": "cp <src> <dst>"},
            "mv": {"func": self.move_file, "description": "Moves or renames a file.", "usage": "mv <src> <dst>"},
            "date": {"func": self.current_date, "description": "Displays the current date.", "usage": "date"},
            "time": {"func": self.current_time, "description": "Displays the current time.", "usage": "time"},
            "whoami": {"func": self.whoami, "description": "Displays the current user.", "usage": "whoami"},
            "exit": {"func": self.exit_terminal, "description": "Exits the terminal.", "usage": "exit"},
            "clear": {"func": self.clear_terminal, "description": "Clears the terminal screen.", "usage": "clear"},
            "rename": {"func": self.rename_file, "description": "Renames a file.", "usage": "rename <src> <dst>"},
            "find": {"func": self.find_file, "description": "Finds a file in the current directory and subdirectories.", "usage": "find <filename>"},
            "size": {"func": self.file_size, "description": "Displays the size of a file.", "usage": "size <filename>"},
            "edit": {"func": self.edit_file, "description": "Edits the content of a file.", "usage": "edit <filename>"}
        }
        self.running = True

    def run(self):
        while self.running:
            command = input(">>> ").strip().split()
            if command:
                cmd_name = command[0]
                args = command[1:]
                self.execute_command(cmd_name, args)

    def execute_command(self, cmd_name, args):
        if cmd_name in self.commands:
            try:
                self.commands[cmd_name]["func"](*args)
            except TypeError:
                print(f"Invalid usage of command: {cmd_name}. Usage: {self.commands[cmd_name]['usage']}")
        else:
            print(f"Command not found: {cmd_name}. Try 'help' for more information.")

    def help(self):
        print("Available commands:")
        for cmd, details in self.commands.items():
            print(f" - {cmd}: {details['description']}\n   Usage: {details['usage']}")

    def list_files(self):
        for item in os.listdir():
            print(item)

    def change_directory(self, path):
        try:
            os.chdir(path)
        except FileNotFoundError:
            print(f"No such directory: {path}")

    def make_directory(self, dirname):
        try:
            os.mkdir(dirname)
        except FileExistsError:
            print(f"Directory already exists: {dirname}")

    def remove_directory(self, dirname):
        try:
            os.rmdir(dirname)
        except FileNotFoundError:
            print(f"No such directory: {dirname}")
        except OSError:
            print(f"Directory not empty: {dirname}")

    def create_file(self, filename):
        open(filename, 'a').close()

    def remove_file(self, filename):
        try:
            os.remove(filename)
        except FileNotFoundError:
            print(f"No such file: {filename}")

    def print_working_directory(self):
        print(os.getcwd())

    def echo(self, *args):
        print(' '.join(args))

    def read_file(self, filename):
        try:
            with open(filename, 'r') as f:
                print(f.read())
        except FileNotFoundError:
            print(f"No such file: {filename}")

    def copy_file(self, src, dst):
        try:
            shutil.copy(src, dst)
        except FileNotFoundError:
            print(f"No such file: {src}")

    def move_file(self, src, dst):
        try:
            shutil.move(src, dst)
        except FileNotFoundError:
            print(f"No such file or directory: {src}")

    def current_date(self):
        print(datetime.now().strftime("%Y-%m-%d"))

    def current_time(self):
        print(datetime.now().strftime("%H:%M:%S"))

    def whoami(self):
        print(os.getlogin())

    def exit_terminal(self):
        self.running = False
        print("Exiting terminal...")

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def rename_file(self, src, dst):
        try:
            os.rename(src, dst)
        except FileNotFoundError:
            print(f"No such file or directory: {src}")

    def find_file(self, filename):
        for root, dirs, files in os.walk('.'):
            if filename in files:
                print(os.path.join(root, filename))

    def file_size(self, filename):
        try:
            size = os.path.getsize(filename)
            print(f"Size of {filename}: {size} bytes")
        except FileNotFoundError:
            print(f"No such file: {filename}")

    def edit_file(self, filename):
        try:
            with open(filename, 'r') as file:
                print(f"Current content of {filename}:")
                print(file.read())
            
            print("\nEnter new content for the file. Type 'SAVE' on a new line to save and exit.")
            lines = []
            while True:
                line = input()
                if line == 'SAVE':
                    break
                lines.append(line)
            
            with open(filename, 'w') as file:
                file.write("\n".join(lines))
            print(f"{filename} has been updated.")

        except FileNotFoundError:
            print(f"No such file: {filename}")

if __name__ == "__main__":
    terminal = Terminal()
    terminal.run()

