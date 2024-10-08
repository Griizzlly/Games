import tkinter as tk

# Function to save information to a file
def save_info():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    birth_date = entry_birth_date.get()
    gender = entry_gender.get()
    phone_number = entry_phone_number.get()
    programming_languages = entry_programming_languages.get()

    info = f"First Name: {first_name}\nLast Name: {last_name}\nBirth Date: {birth_date}\nGender: {gender}\nPhone Number: {phone_number}\nProgramming Languages: {programming_languages}\n\n"
    
    file = open("info.txt", "w", encoding="utf-8")  # Open the file
    file.write(info)  # Write information to the file
    file.close()  # Close the file

    label_status.config(text="Information saved!")

# Create the main window
root = tk.Tk()
root.title("Information Form")

# Labels and entries
tk.Label(root, text="First Name:").grid(row=0, column=0)
entry_first_name = tk.Entry(root)
entry_first_name.grid(row=0, column=1)

tk.Label(root, text="Last Name:").grid(row=1, column=0)
entry_last_name = tk.Entry(root)
entry_last_name.grid(row=1, column=1)

tk.Label(root, text="Birth Date:").grid(row=2, column=0)
entry_birth_date = tk.Entry(root)
entry_birth_date.grid(row=2, column=1)

tk.Label(root, text="Gender:").grid(row=3, column=0)
entry_gender = tk.Entry(root)
entry_gender.grid(row=3, column=1)

tk.Label(root, text="Phone Number:").grid(row=4, column=0)
entry_phone_number = tk.Entry(root)
entry_phone_number.grid(row=4, column=1)

tk.Label(root, text="Programming Languages:").grid(row=5, column=0)
entry_programming_languages = tk.Entry(root)
entry_programming_languages.grid(row=5, column=1)

# Button to save information
button_save = tk.Button(root, text="Save", command=save_info)
button_save.grid(row=6, column=1)

# Status label to display the result
label_status = tk.Label(root, text="")
label_status.grid(row=7, column=1)

# Run the window
root.mainloop()
