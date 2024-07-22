import os
import subprocess

def show_system_info():
    try:
        result = subprocess.run(['neofetch'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")

def check_kernel_status():
    try:
        if os.path.exists("kernel.py"):
            result = subprocess.run(['ps', '-aux'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            kernel_info = [line for line in result.stdout.splitlines() if 'kernel.py' in line]
            if kernel_info:
                print("Kernel Status: Running")
                for line in kernel_info:
                    print(line)
            else:
                print("Kernel Status: Not Running")
        else:
            print("kernel.py file does not exist.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")

def show_help():
    help_text = """
Available commands:
- neofetch: Show information about the system.
- check --kernel: Check the status of kernel.py.
- help: Show this help message.
- exit: Exit the terminal.
- Any .py file: Execute the Python file.
- Any other command: Execute as a shell command.
"""
    print(help_text)

def basic_terminal():
    print("Welcome to the basic Python terminal. Type 'help' for available commands, and 'exit' to quit.")
    
    while True:
        command = input(">> ")
        
        if command.lower() == 'exit':
            break
        elif command.lower() == 'neofetch':
            show_system_info()
        elif command.lower() == 'check --kernel':
            check_kernel_status()
        elif command.lower() == 'help':
            show_help()
        elif command.endswith(".py"):
            try:
                result = subprocess.run(['python', command], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                print(result.stdout)
            except subprocess.CalledProcessError as e:
                print(f"Error: {e.stderr}")
        else:
            try:
                result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                print(result.stdout)
            except subprocess.CalledProcessError as e:
                print(f"Error: {e.stderr}")

if __name__ == "__main__":
    basic_terminal()
