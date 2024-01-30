import tkinter as tk


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")

        # Set Window Size
        self.root.geometry("300x300")

        # Entry for Task Input
        self.task_entry = tk.Entry(self.root)
        self.task_entry.grid(row=0, column=0, pady=10)

        # Button to add a Task
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=1, column=0, pady=5)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(self.root)
        self.task_listbox.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        # Listbox to display finished tasks
        self.task_finished_listbox = tk.Listbox(self.root)
        self.task_finished_listbox.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        # Button to delete selected task
        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=1, column=1, pady=5)

        # Button to mark task as finished
        self.finish_button = tk.Button(self.root, text="Finish Task", command=self.finish_task)
        self.finish_button.grid(row=3, column=1, pady=5)

        self.load_tasks_from_file()

    def add_task(self):
        task_text = self.task_entry.get()
        if task_text:
            self.task_listbox.insert(tk.END, task_text)
            self.task_entry.delete(0, tk.END)

            self.save_tasks_to_file()

    def delete_task(self):
        # Deletes from task_listbox
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.task_listbox.delete(selected_task_index)

        # Deletes from finished_listbox
        selected_task_index = self.task_finished_listbox.curselection()
        if selected_task_index:
            self.task_finished_listbox.delete(selected_task_index)

        self.save_tasks_to_file()

    def finish_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_text = self.task_listbox.get(selected_task_index)
            self.task_finished_listbox.insert(tk.END, "✓ " + task_text)
            self.task_listbox.delete(selected_task_index)

        self.save_tasks_to_file()

    def save_tasks_to_file(self):
        with open("tasks.txt", "w", encoding="utf-8") as file:
            for task in self.task_listbox.get(0, tk.END):
                file.write(task + "\n")

            for finished_task in self.task_finished_listbox.get(0, tk.END):
                file.write(finished_task + "\n")

    def load_tasks_from_file(self):
        try:
            with open("tasks.txt", "r", encoding="utf-8") as file:
                tasks = [line.strip() for line in file.readlines()]
                self.task_listbox.delete(0, tk.END)
                self.task_finished_listbox.delete(0, tk.END)

                for task in tasks:
                    if task.startswith("✓ "):
                        self.task_finished_listbox.insert(tk.END, task)
                    else:
                        self.task_listbox.insert(tk.END, task)

        except FileNotFoundError:
            pass  # Ignore if the file doesn't exist on first run


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
