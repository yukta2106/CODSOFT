import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3

# Database setup
def setup_database():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    # Create table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY, task TEXT NOT NULL, completed BOOLEAN NOT NULL DEFAULT 0 CHECK (completed IN (0, 1)))''')
    
    # Check if the 'completed' column exists and add it if it doesn't
    c.execute("PRAGMA table_info(tasks)")
    columns = [column[1] for column in c.fetchall()]
    if 'completed' not in columns:
        c.execute('ALTER TABLE tasks ADD COLUMN completed BOOLEAN NOT NULL DEFAULT 0 CHECK (completed IN (0, 1))')
    
    conn.commit()
    conn.close()

# Add task to database
def add_task_to_db(task):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('INSERT INTO tasks (task, completed) VALUES (?, 0)', (task,))
    conn.commit()
    conn.close()

# Delete task from database
def delete_task_from_db(task_id):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()

# Update task in database
def update_task_in_db(task_id, new_task):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('UPDATE tasks SET task = ? WHERE id = ?', (new_task, task_id))
    conn.commit()
    conn.close()

# Toggle task completion in database
def toggle_task_completion_in_db(task_id, completed):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('UPDATE tasks SET completed = ? WHERE id = ?', (completed, task_id))
    conn.commit()
    conn.close()

# Fetch tasks from database
def fetch_tasks_from_db():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('SELECT * FROM tasks')
    tasks = c.fetchall()
    conn.close()
    return tasks

# Main application
class ToDoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To-Do List")
        self.geometry("450x600")
        self.configure(bg="#e0f7fa")

        # Title Label
        self.title_label = tk.Label(self, text="To-Do List", font=("Helvetica", 20, "bold"), bg="#e0f7fa", fg="#00796b")
        self.title_label.pack(pady=20)

        # Task Listbox
        self.task_frame = tk.Frame(self, bg="#e0f7fa")
        self.task_frame.pack(pady=20)

        self.task_listbox = tk.Listbox(self.task_frame, height=15, width=50, bd=0, font=("Helvetica", 12), selectbackground="#00796b", activestyle="none")
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.task_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        # Task Entry
        self.entry = tk.Entry(self, font=("Helvetica", 12), width=37, bg="#ffffff", fg="#00796b", highlightbackground="#00796b", highlightcolor="#00796b", highlightthickness=1)
        self.entry.pack(pady=10)

        # Buttons Frame
        self.button_frame = tk.Frame(self, bg="#e0f7fa")
        self.button_frame.pack(pady=10)

        self.add_button = tk.Button(self.button_frame, text="Add Task", command=self.add_task, font=("Helvetica", 12), bg="#00796b", fg="#ffffff", padx=10, pady=5)
        self.add_button.grid(row=0, column=0, padx=10)

        self.del_button = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task, font=("Helvetica", 12), bg="#e53935", fg="#ffffff", padx=10, pady=5)
        self.del_button.grid(row=0, column=1, padx=10)

        self.edit_button = tk.Button(self.button_frame, text="Edit Task", command=self.edit_task, font=("Helvetica", 12), bg="#fbc02d", fg="#ffffff", padx=10, pady=5)
        self.edit_button.grid(row=0, column=2, padx=10)

        self.load_tasks()

    def load_tasks(self):
        self.tasks = fetch_tasks_from_db()
        self.task_listbox.delete(0, tk.END)  # Clear the listbox
        for task in self.tasks:
            task_text = f"[{'X' if task[2] else ' '}] {task[1]}"
            self.task_listbox.insert(tk.END, task_text)

    def add_task(self):
        task = self.entry.get()
        if task:
            add_task_to_db(task)
            self.load_tasks()  # Reload tasks to update the listbox and self.tasks
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            selected_task_id = self.tasks[selected_task_index][0]
            delete_task_from_db(selected_task_id)
            self.load_tasks()  # Reload tasks to update the listbox and self.tasks
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def edit_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            selected_task_id = self.tasks[selected_task_index][0]
            new_task = self.entry.get()
            if new_task:
                update_task_in_db(selected_task_id, new_task)
                self.load_tasks()  # Reload tasks to update the listbox and self.tasks
                self.entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a task.")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def toggle_task_completion(self, event):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            selected_task_id = self.tasks[selected_task_index][0]
            current_completion_status = self.tasks[selected_task_index][2]
            new_completion_status = not current_completion_status
            toggle_task_completion_in_db(selected_task_id, new_completion_status)
            self.load_tasks()  # Reload tasks to update the listbox and self.tasks
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    setup_database()
    app = ToDoApp()
    app.task_listbox.bind('<Double-Button-1>', app.toggle_task_completion)
    app.mainloop()
