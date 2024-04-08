import tkinter as tk
from add_task_view import AddTaskView
from todo import Task

class MainView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master

        self.tasks = []

        self.tasks_frame = tk.Frame(self)
        self.tasks_frame.pack(pady=10)

        self.add_button = tk.Button(self, text="Add Task", command=self.open_add_task)
        self.add_button.pack(pady=10)

    def open_add_task(self):
        add_task_view = AddTaskView(self.master, self.add_task_callback)

    def add_task_callback(self, task):
        self.tasks.append(task)
        self.refresh_tasks()

    def refresh_tasks(self):
        # Logic to refresh the main view with the updated task list
        pass  # Replace with actual implementation
