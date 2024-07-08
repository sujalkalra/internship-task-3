import tkinter as tk
from tkinter import messagebox
import random
import string


# Function to generate a strong password
def generate_password():
    length = int(length_entry.get())
    if length < 8:
        messagebox.showwarning("Weak Password", "Password length should be at least 8 characters.")
        return

    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_chars) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


# Initialize the main window
root = tk.Tk()
root.title("Strong Password Generator")
root.geometry("400x300")
root.configure(bg="#2c3e50")

# Title Label
title_label = tk.Label(root, text="Strong Password Generator", font=("Helvetica", 18, "bold"), fg="#1cf0f1",
                       bg="#2c3e50")
title_label.pack(pady=20)

# Length Label and Entry
length_label = tk.Label(root, text="Enter Password Length:", font=("Helvetica", 14), fg="#ecf0f1", bg="#2c3e50")
length_label.pack(pady=10)
length_entry = tk.Entry(root, font=("Helvetica", 12), width=15)
length_entry.pack(pady=5)

# Password Entry
password_entry = tk.Entry(root, font=("Helvetica", 12), width=30)
password_entry.pack(pady=20)

# Generate Button
generate_button = tk.Button(root, text="Generate Password", font=("Helvetica", 14), bg="#006633", fg="#ecf0f1",
                            command=generate_password)
generate_button.pack(pady=20)

# Run the GUI event loop
root.mainloop()
