# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 13:02:24 2023

@author: user
"""

import tkinter as tk
import random
import string
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        
        # Define and initialize variables
        self.password_var = tk.StringVar()
        self.length_var = tk.StringVar()
        self.include_lowercase_var = tk.IntVar()
        self.include_uppercase_var = tk.IntVar()
        self.include_digits_var = tk.IntVar()
        self.include_special_chars_var = tk.IntVar()
        
        # Create GUI components
        self.create_widgets()
    
    def create_widgets(self):
        # Labels
        tk.Label(self.root, text="Password Length:").pack()
        
        # Entry for password length
        length_entry = tk.Entry(self.root, textvariable=self.length_var)
        length_entry.pack()
        self.length_var.set(12)
        
        # Checkboxes for character types
        tk.Checkbutton(self.root, text="Lowercase", variable=self.include_lowercase_var).pack()
        tk.Checkbutton(self.root, text="Uppercase", variable=self.include_uppercase_var).pack()
        tk.Checkbutton(self.root, text="Digits", variable=self.include_digits_var).pack()
        tk.Checkbutton(self.root, text="Special Characters", variable=self.include_special_chars_var).pack()
        
        # Generate Password Button
        generate_button = tk.Button(self.root, text="Generate Password", command=self.generate_password)
        generate_button.pack()
        
        # Password display label
        password_label = tk.Label(self.root, textvariable=self.password_var)
        password_label.pack()
        
        # Copy to Clipboard Button
        copy_button = tk.Button(self.root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        copy_button.pack()
    
    def generate_password(self):
        length = int(self.length_var.get())
        include_lowercase = bool(self.include_lowercase_var.get())
        include_uppercase = bool(self.include_uppercase_var.get())
        include_digits = bool(self.include_digits_var.get())
        include_special_chars = bool(self.include_special_chars_var.get())
        
        characters = ""
        
        if include_lowercase:
            characters += string.ascii_lowercase
        if include_uppercase:
            characters += string.ascii_uppercase
        if include_digits:
            characters += string.digits
        if include_special_chars:
            characters += string.punctuation
        
        if not characters:
            self.password_var.set("Select at least one character type.")
        else:
            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_var.set(password)
    
    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            pyperclip.copy(password)
            print("Password copied to clipboard!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

