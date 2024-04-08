import tkinter as tk
from todo import Task

class AddTaskView(tk.Toplevel):
    def __init__(self, master, add_task_callback):
        super().__init__(master)

        self.add_task_callback = add_task_callback

        self.title("Add Task")
        self.geometry("400x300")

        self.title_label = tk.Label(self, text="Title:")
        self.title_label.pack()

        self.title_entry = tk.Entry(self)
        self.title_entry.pack()

        self.description_label = tk.Label(self, text="Description:")
        self.description_label.pack()

        self.description_entry = tk.Entry(self)
        self.description_entry.pack()

        self.add_button = tk.Button(self, text="Add", command=self.add_task)
        self.add_button.pack()

    def add_task(self):
        title = self.title_entry.get()
        description = self.description_entry.get()
        priority = None  # For simplicity, assume priority is None
        due_date = None  # For simplicity, assume due_date is None
        category = None  # For simplicity, assume category is None

        new_task = Task(title, description, priority, due_date, category)
        self.add_task_callback(new_task)
        self.destroy()
