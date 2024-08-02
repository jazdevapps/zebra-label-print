import customtkinter
import zebra_printer_dm

LABEL_SIZES = [
    {"name": "4x6", "width": 812, "height": 1218}
]

def print_labels():
    global root

    quantity = quantity_entry.get()
    size = label_size_dropdown.get()
    data = label_data_entry.get()
    suffix = suffix_dropdown.get()
    trailing_zeros = 0
    if trailing_zeros_entry.get() != "None" and trailing_zeros_entry.get() != "":
        trailing_zeros = trailing_zeros_entry.get()
        print("Trailing zeros: " + trailing_zeros)
    if starting_number_entry.get() != "None" and starting_number_entry.get() != "":
        starting_number = starting_number_entry.get()
        print("Starting number: " + starting_number)
    else:
        starting_number = 0

    zebra_printer_dm.start(int(quantity),
        size,
        data,
        suffix,
        int(starting_number),
        int(trailing_zeros)
    )

def on_suffix_change(event):
    print("Entered")
    if suffix_dropdown.get() == "Numeric":
        trailing_zeros_label.pack(pady=(12, 2), padx=10)
        trailing_zeros_entry.pack(pady=(2, 12), padx=10)
        starting_number_label.pack(pady=(12, 2), padx=10)
        starting_number_entry.pack(pady=(2, 12), padx=10)
    else:
        trailing_zeros_label.pack_forget()
        trailing_zeros_entry.pack_forget()
        starting_number_label.pack_forget()
        starting_number_entry.pack_forget()

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Zebra Label Print")
root.geometry("400x600")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

suffix_type = customtkinter.StringVar()
suffix_type.trace("w", on_suffix_change)

# Quantity of labels to print input field
quantity_label = customtkinter.CTkLabel(master=frame, text="Quantity of labels to print: ")
quantity_label.pack(pady=(12, 2), padx=10)
quantity_entry = customtkinter.CTkEntry(master=frame, placeholder_text="ex. 10")
quantity_entry.pack(pady=(2, 12), padx=10)

# ComboBox for label size (labels can be 3x2 or 4x6)
label_size_label = customtkinter.CTkLabel(master=frame, text="Label Size: ")
label_size_label.pack(pady=(12, 2), padx=10)
label_size_options = [label["name"] for label in LABEL_SIZES]
label_size_dropdown = customtkinter.CTkComboBox(master=frame, values=label_size_options)
label_size_dropdown.pack(pady=(2, 12), padx=10)

# Label data
label_data_label = customtkinter.CTkLabel(master=frame, text="Label Data: ")
label_data_label.pack(pady=(12, 2), padx=10)
label_data_entry = customtkinter.CTkEntry(master=frame, placeholder_text="ex. 1, 2, 10")
label_data_entry.pack(pady=(2, 12), padx=10)

# Suffix dropdown for selecting alpha or numeric suffix
suffix_label = customtkinter.CTkLabel(master=frame, text="Suffix: ")
suffix_label.pack(pady=(12, 2), padx=10)
suffix_options = ["Alpha", "Numeric", "None"]
suffix_dropdown = customtkinter.CTkComboBox(master=frame, values=suffix_options, command=on_suffix_change)
suffix_dropdown.pack(pady=(2, 12), padx=10)

# If numeric suffix is selected, allow user to input number of trailing zeros
trailing_zeros_label = customtkinter.CTkLabel(master=frame, text="Trailing Zeros: ")
trailing_zeros_label.pack_forget()
trailing_zeros_entry = customtkinter.CTkEntry(master=frame, placeholder_text="ex. 1, 2, 3")
trailing_zeros_entry.pack_forget()

# Starting number for numeric suffix
starting_number_label = customtkinter.CTkLabel(master=frame, text="Starting Number: ")
starting_number_label.pack_forget()
starting_number_entry = customtkinter.CTkEntry(master=frame, placeholder_text="ex. 1, 2, 10, 100")
starting_number_entry.pack_forget()

print_button = customtkinter.CTkButton(master=root, text="Print", command=print_labels)
print_button.pack(pady=(12, 2), padx=10)

root.mainloop()
