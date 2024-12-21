from tkinter import Tk, Label, StringVar, OptionMenu, Button, Toplevel, Entry, Frame, PhotoImage, messagebox

# Main window setup remains the same
window = Tk()
window.geometry("1000x600")
window.title("OS CPU")

# Set window icon
icon = PhotoImage(file="image.png")
window.iconphoto(True, icon)

# Add title label
Label(window, text="CPU Scheduling Algorithms", font=("Verdana", 35)).pack(pady=20)

# Dropdown menu
selected_option = StringVar()
selected_option.set("Select an Algorithm")  # Default value

options = [
    "First Come First Served (FCFS)",
    "Non-Preemptive Shortest Job First (SJF)",
    "Preemptive Shortest Job First (SJF)",
    "Round Robin (RR)",
    "Preemptive Priority Scheduling",
    "Non-Preemptive Priority Scheduling"
]

dropdown = OptionMenu(window, selected_option, *options)
dropdown.pack(pady=20)

# Header frame
header_frame = Frame(window)
header_frame.pack()

# Header labels - Centered text with consistent width
Label(header_frame, text="Process", width=10, font=("Verdana", 10), anchor="w").grid(row=0, column=0, padx=5)
Label(header_frame, text="Burst Time", width=15, font=("Verdana", 10), anchor="center").grid(row=0, column=1, padx=5)
Label(header_frame, text="Arrival Time", width=15, font=("Verdana", 10), anchor="w").grid(row=0, column=2, padx=5)
priority_label = Label(header_frame, text="Priority", width=15, font=("Verdana", 10), anchor="w")

# Container for process rows
process_frame = Frame(window)
process_frame.pack(pady=10)

# Track process rows
process_rows = []

def create_entry():
    """Create a standardized Entry widget"""
    entry = Entry(process_frame, width=15, justify='center')
    return entry

def create_hidden_button():
    """Create a truly invisible button that maintains spacing but can't be interacted with"""
    button = Label(process_frame, width=4)  # Using Label instead of Button
    button.grid_remove()  # Initially hidden
    return button

def update_process_labels():
    """Update process labels to ensure they're in numerical order"""
    for i, row in enumerate(process_rows):
        row[0].config(text=f"P{i + 1}")

def update_rows():
    is_priority = "Priority" in selected_option.get()

    # Show or hide the Priority header
    if is_priority:
        priority_label.grid(row=0, column=3, padx=5)
    else:
        priority_label.grid_forget()

    # Update existing rows
    for row_index, row in enumerate(process_rows):
        if is_priority and (len(row) == 5 or len(row) == 4):
            priority_entry = create_entry()
            priority_entry.grid(row=row_index + 1, column=3, padx=5, pady=5)
            
            button_index = -2 if len(row) == 5 else -1
            row.insert(3, priority_entry)
            
            row[button_index].grid(row=row_index + 1, column=4, padx=5, pady=5)
            if len(row) > 5:
                row[-1].grid(row=row_index + 1, column=5, padx=5, pady=5)
                
        elif not is_priority and (len(row) == 7 or len(row) == 6):
            row[3].grid_forget()
            row.pop(3)
            
            button_index = -2 if len(row) == 5 else -1
            row[button_index].grid(row=row_index + 1, column=3, padx=5, pady=5)
            if len(row) > 4:
                row[-1].grid(row=row_index + 1, column=4, padx=5, pady=5)

def remove_process_row(row):
    for widget in row:
        widget.grid_forget()
    process_rows.remove(row)

    # Re-align remaining rows
    is_priority = "Priority" in selected_option.get()
    for row_index, row in enumerate(process_rows):
        for col_index, widget in enumerate(row):
            widget.grid(row=row_index + 1, column=col_index, padx=5, pady=5)
    
    update_process_labels()

def add_process_row():
    process_index = len(process_rows) + 1
    is_priority = "Priority" in selected_option.get()

    # Process label - Centered text
    process_label = Label(process_frame, text=f"P{process_index}", width=15, font=("Verdana", 12), anchor="center")
    process_label.grid(row=process_index, column=0, padx=5, pady=5)

    # Entry fields with centered text
    burst_entry = create_entry()
    burst_entry.grid(row=process_index, column=1, padx=5, pady=5)

    arrival_entry = create_entry()
    arrival_entry.grid(row=process_index, column=2, padx=5, pady=5)

    row = [process_label, burst_entry, arrival_entry]
    
    next_column = 3
    if is_priority:
        priority_entry = create_entry()
        priority_entry.grid(row=process_index, column=next_column, padx=5, pady=5)
        row.append(priority_entry)
        next_column += 1

    # Add and remove buttons with consistent width
    add_button = Button(process_frame, text="+", width=3)
    add_button.configure(command=add_process_row)
    add_button.grid(row=process_index, column=next_column, padx=5, pady=5)
    row.append(add_button)

    if process_index > 1:
        remove_button = Button(process_frame, text="-", width=3)
        remove_button.configure(command=lambda: remove_process_row(row))
        remove_button.grid(row=process_index, column=next_column + 1, padx=5, pady=5)
        row.append(remove_button)
    else:
        # Add hidden button for the first row to maintain spacing
        hidden_button = create_hidden_button()
        hidden_button.grid(row=process_index, column=next_column + 1, padx=5, pady=5)
        row.append(hidden_button)

    process_rows.append(row)

def validate_inputs():
    if selected_option.get() == "Select an Algorithm":
        messagebox.showerror("Error", "Please select an algorithm first!")
        return False
    
    is_priority = "Priority" in selected_option.get()
    for row in process_rows:
        if not row[1].get() or not row[2].get():
            messagebox.showerror("Error", "Please fill all Burst Time and Arrival Time fields!")
            return False
        if is_priority and len(row) >= 4 and not row[3].get():
            messagebox.showerror("Error", "Please fill all Priority fields!")
            return False
        
        try:
            float(row[1].get())
            float(row[2].get())
            if is_priority and len(row) >= 4:
                float(row[3].get())
        except ValueError:
            messagebox.showerror("Error", "All input fields must be numbers!")
            return False

    return True

def create_window():
    if validate_inputs():
        new_window = Toplevel(window)
        new_window.geometry("600x400")
        new_window.title("New Window")
        Label(new_window, text="Selected Algorithm:", font=("Verdana", 20)).pack(pady=20)
        Label(new_window, text=selected_option.get(), font=("Verdana", 18)).pack(pady=10)

# Add the first process row
add_process_row()

# Bind dropdown changes to update rows
selected_option.trace_add("write", lambda *args: update_rows())

# Add Next button
btn = Button(window, text="Next", command=create_window)
btn.pack(pady=20)

# Run the application
window.mainloop()
