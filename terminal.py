import os
import shutil
from datetime import datetime

class Terminal:
    def __init__(self):
        self.commands = {
            "help": self.help,
            "ls": self.list_files,
            "cd": self.change_directory,
            "mkdir": self.make_directory,
            "rmdir": self.remove_directory,
            "touch": self.create_file,
            "rm": self.remove_file,
            "pwd": self.print_working_directory,
            "echo": self.echo,
            "cat": self.read_file,
            "cp": self.copy_file,
            "mv": self.move_file,
            "date": self.current_date,
            "time": self.current_time,
            "whoami": self.whoami,
            "exit": self.exit_terminal,
            "clear": self.clear_terminal,
            "rename": self.rename_file,
            "find": self.find_file,
            "size": self.file_size
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
                self.commands[cmd_name](*args)
            except TypeError:
                print(f"Invalid usage of command: {cmd_name}. Try 'help' for more information.")
        else:
            print(f"Command not found: {cmd_name}. Try 'help' for more information.")

    def help(self):
        print("Available commands:")
        for cmd in self.commands:
            print(f" - {cmd}")

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

if __name__ == "__main__":
    terminal = Terminal()
    terminal.run()
