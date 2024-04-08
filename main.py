from main_view import MainView
import tkinter as tk

class ToDoApp:
    def __init__(self):
        self.root = tk.Tk()
        self.main_view = MainView(self.root)
        self.main_view.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    app = ToDoApp()
    app.root.mainloop()
