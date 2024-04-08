import tkinter as tk
from todo import Task

class EditTaskView(tk.Toplevel):
    def __init__(self, master, task):
        super().__init__(master)

        self.task = task

        self.title("Edit Task")
        self.geometry("400x300")

        self.title_label = tk.Label(self, text="Title:")
        self.title_label.pack()

        self.title_entry = tk.Entry(self, textvariable=tk.StringVar(value=task.title))
        self.title_entry.pack()

        self.description_label = tk.Label(self, text="Description:")
        self.description_label.pack()

        self.description_entry = tk.Entry(self, textvariable=tk.StringVar(value=task.description))
        self.description_entry.pack()

        # Add more widgets for editing priority, due date, category, etc.

        self.save_button = tk.Button(self, text="Save")
        self.save_button.pack()
