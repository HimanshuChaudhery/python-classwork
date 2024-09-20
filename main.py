""" Design a file Oraganizer GUI app """

import tkinter as tk

import move

"""
def orga():
    directory = entry.get()
    res = move.organize_files(directory)
    print(res)
"""

root = tk.Tk()
root.title("File Oraganizer")
root.geometry("400x250")

label = tk.Label(root, text="Enter Address:")
label.pack(pady=10)

entry = tk.Entry(root, width=100)
entry.pack(pady=5)

button = tk.Button(root, text="Submit")
button.pack(pady=5)

root.mainloop()