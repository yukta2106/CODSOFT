import tkinter as tk
from tkinter import messagebox

contacts = {}

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contacts[name] = {
            'Phone': phone,
            'Email': email,
            'Address': address
        }
        messagebox.showinfo("Success", f"Contact {name} added successfully!")
        clear_entries()
    else:
        messagebox.showerror("Error", "Name and Phone are required fields.")

def view_contacts():
    contact_list.delete(0, tk.END)
    if contacts:
        for name, details in contacts.items():
            contact_list.insert(tk.END, f"Name: {name}, Phone: {details['Phone']}")
    else:
        messagebox.showinfo("Info", "No contacts available.")

def search_contact():
    name = search_entry.get()
    contact_list.delete(0, tk.END)
    
    if name in contacts:
        details = contacts[name]
        contact_list.insert(tk.END, f"Name: {name}")
        contact_list.insert(tk.END, f"Phone: {details['Phone']}")
        contact_list.insert(tk.END, f"Email: {details['Email']}")
        contact_list.insert(tk.END, f"Address: {details['Address']}")
    else:
        messagebox.showinfo("Info", f"Contact {name} not found.")

def update_contact():
    name = name_entry.get()
    if name in contacts:
        contacts[name]['Phone'] = phone_entry.get()
        contacts[name]['Email'] = email_entry.get()
        contacts[name]['Address'] = address_entry.get()
        messagebox.showinfo("Success", f"Contact {name} updated successfully!")
        clear_entries()
    else:
        messagebox.showerror("Error", f"Contact {name} not found.")

def delete_contact():
    name = name_entry.get()
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Success", f"Contact {name} deleted successfully!")
        clear_entries()
    else:
        messagebox.showerror("Error", f"Contact {name} not found.")

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Contact Book")

# Create and place labels and entry widgets
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Phone").grid(row=1, column=0, padx=10, pady=5)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Email").grid(row=2, column=0, padx=10, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Address").grid(row=3, column=0, padx=10, pady=5)
address_entry = tk.Entry(root)
address_entry.grid(row=3, column=1, padx=10, pady=5)

# Create buttons
add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=4, column=0, padx=10, pady=10)

view_button = tk.Button(root, text="View Contacts", command=view_contacts)
view_button.grid(row=4, column=1, padx=10, pady=10)

search_button = tk.Button(root, text="Search Contact", command=search_contact)
search_button.grid(row=5, column=0, padx=10, pady=10)

update_button = tk.Button(root, text="Update Contact", command=update_contact)
update_button.grid(row=5, column=1, padx=10, pady=10)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.grid(row=6, column=0, padx=10, pady=10)

clear_button = tk.Button(root, text="Clear Entries", command=clear_entries)
clear_button.grid(row=6, column=1, padx=10, pady=10)

# Listbox to display contacts
contact_list = tk.Listbox(root, width=50, height=10)
contact_list.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
