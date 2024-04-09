import tkinter as tk
from tkinter import ttk
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.length_label = ttk.Label(root, text="Password Length:")
        self.length_label.grid(row=0, column=0, padx=10, pady=10)

        self.length_entry = ttk.Entry(root)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        self.complexity_label = ttk.Label(root, text="Complexity Level:")
        self.complexity_label.grid(row=1, column=0, padx=10, pady=10)

        self.complexity_combo = ttk.Combobox(root, values=["Letters Only", "Letters + Numbers", "Letters + Numbers + Special Characters"])
        self.complexity_combo.current(0)
        self.complexity_combo.grid(row=1, column=1, padx=10, pady=10)

        self.generate_button = ttk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=2, columnspan=2, padx=10, pady=10)

        self.password_label = ttk.Label(root, text="Generated Password:")
        self.password_label.grid(row=3, column=0, padx=10, pady=10)

        self.password_display = ttk.Entry(root, state="readonly")
        self.password_display.grid(row=3, column=1, padx=10, pady=10)

    def generate_password(self):
        length = int(self.length_entry.get())
        complexity = self.complexity_combo.current() + 1

        if length <= 0:
            self.password_display.config(state="normal")
            self.password_display.delete(0, tk.END)
            self.password_display.insert(0, "Invalid length")
            self.password_display.config(state="readonly")
        else:
            password = self.generate_random_password(length, complexity)
            self.password_display.config(state="normal")
            self.password_display.delete(0, tk.END)
            self.password_display.insert(0, password)
            self.password_display.config(state="readonly")

    def generate_random_password(self, length, complexity):
        if complexity == 1:
            chars = string.ascii_letters
        elif complexity == 2:
            chars = string.ascii_letters + string.digits
        elif complexity == 3:
            chars = string.ascii_letters + string.digits + string.punctuation
        else:
            return "Invalid complexity level"

        password = ''.join(random.choice(chars) for _ in range(length))
        return password

def main():
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
