import subprocess

class Kernel:
    def __init__(self):
        print("Loaded Tux Plus Kernel")
        self.running = False

    def start(self):
        self.running = True
        print("Kernel started.")
        self.load_terminal()

    def load_terminal(self):
        print("Loading terminal...")
        subprocess.run(["python", "terminal.py"])

if __name__ == "__main__":
    kernel = Kernel()
    kernel.start()


