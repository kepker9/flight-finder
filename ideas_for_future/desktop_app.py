import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("My Flight Finder")
root.geometry("500x400")  # Width x Height

# Add a label
label = tk.Label(root, text="Welcome to Flight Finder!", font=("Arial", 18), fg="white")
label.pack(pady=20)

# Add a text area
text_area = tk.Text(root, height=10, width=50)
text_area.pack(pady=10)
text_area.insert(tk.END, "Enter your flight details here...\n")

# Button functions
def show_message():
    messagebox.showinfo("Info", "Button clicked!")

def clear_text():
    text_area.delete("1.0", tk.END)

# Add buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

btn1 = tk.Button(button_frame, text="Submit", command=show_message, bg="green", fg="white")
btn1.grid(row=0, column=0, padx=10)

btn2 = tk.Button(button_frame, text="Clear Text", command=clear_text, bg="red", fg="white")
btn2.grid(row=0, column=1, padx=10)

# Start the Tkinter event loop
root.mainloop()

