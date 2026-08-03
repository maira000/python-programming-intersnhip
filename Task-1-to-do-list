import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        # Tasks list
        self.tasks = []

        # Create UI components
        self.task_entry = tk.Entry(root, width=40)
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10)
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)

        # Place UI components on the grid
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.delete_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Bind double click on listbox to task completion
        self.task_listbox.bind("<Double-Button-1>", self.toggle_task_completion)

        # Load tasks from file
        self.load_tasks()

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            self.tasks.append(task_text)
            self.task_listbox.insert(tk.END, task_text)
            self.save_tasks()
            self.task_entry.delete(0, tk.END)  # Clear the entry field
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            deleted_task = self.tasks.pop(index)
            self.task_listbox.delete(index)
            self.save_tasks()
            messagebox.showinfo("Task Deleted", f"Task '{deleted_task}' deleted successfully.")
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def toggle_task_completion(self, event):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            task = self.tasks[index]
            if task.startswith("✓ "):
                self.tasks[index] = task[2:]
            else:
                self.tasks[index] = "✓ " + task
            self.save_tasks()
            self.load_tasks()

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def load_tasks(self):
        self.task_listbox.delete(0, tk.END)
        try:
            with open("tasks.txt", "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
                for task in self.tasks:
                    self.task_listbox.insert(tk.END, task)
        except FileNotFoundError:
            pass  # File doesn't exist yet

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
