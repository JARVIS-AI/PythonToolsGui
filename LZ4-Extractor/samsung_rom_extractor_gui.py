import tkinter as tk
from tkinter import filedialog, messagebox
import lz4.block
import os

def extract_lz4(file_path, output_path):
    with open(file_path, 'rb') as lz4_file:
        compressed_data = lz4_file.read()
    decompressed_data = lz4.block.decompress(compressed_data)
    with open(output_path, 'wb') as output_file:
        output_file.write(decompressed_data)

def on_browse_rom():
    rom_path = filedialog.askdirectory(title="Select Samsung ROM Directory")
    rom_path_var.set(rom_path)

def on_extract():
    rom_path = rom_path_var.get()
    if not rom_path:
        messagebox.showerror("Error", "Please select a ROM directory.")
        return
    
    if not os.path.exists(rom_path):
        messagebox.showerror("Error", "The selected directory does not exist.")
        return

    files_to_extract = []
    if system_var.get():
        files_to_extract.append("system.img.lz4")
    if recovery_var.get():
        files_to_extract.append("recovery.img.lz4")
    if boot_var.get():
        files_to_extract.append("boot.img.lz4")

    if not files_to_extract:
        messagebox.showerror("Error", "Please select at least one image to extract.")
        return

    for file_name in files_to_extract:
        file_path = os.path.join(rom_path, file_name)
        if not os.path.exists(file_path):
            messagebox.showerror("Error", f"{file_name} not found in the selected directory.")
            continue

        output_path = os.path.join(rom_path, file_name.replace(".lz4", ".img"))
        
        try:
            extract_lz4(file_path, output_path)
            messagebox.showinfo("Success", f"Extraction complete: {output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during extraction: {e}")

def show_about():
    messagebox.showinfo("About", "lz4 Extractor by JARVIS-AI\nVersion 1.0.6\n\nThis application allows you to extract .img.lz4 files from Samsung ROM files")

root = tk.Tk()
root.title("lz4 Extractor by JARVIS-AI")
root.resizable(False, False)

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=show_about)
menu_bar.add_cascade(label="Help", menu=help_menu)

rom_path_var = tk.StringVar()
system_var = tk.BooleanVar()
recovery_var = tk.BooleanVar()
boot_var = tk.BooleanVar()

frame = tk.Frame(root)
frame.pack(padx=4, pady=4)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)

browse_button = tk.Button(frame, text="Open File", command=on_browse_rom)
browse_button.grid(row=0, column=0, sticky="w", padx=1, pady=1)
rom_dir_entry = tk.Entry(frame, textvariable=rom_path_var)
rom_dir_entry.grid(row=0, column=1, columnspan=2, sticky="we", padx=1, pady=1)

system_check = tk.Checkbutton(frame, text="system.img.lz4", variable=system_var)
system_check.grid(row=1, column=0, sticky="w", padx=1, pady=1)
recovery_check = tk.Checkbutton(frame, text="recovery.img.lz4", variable=recovery_var)
recovery_check.grid(row=1, column=1, sticky="w", padx=1, pady=1)
boot_check = tk.Checkbutton(frame, text="boot.img.lz4", variable=boot_var)
boot_check.grid(row=1, column=2, sticky="w", padx=1, pady=1)

extract_button = tk.Button(frame, text="Extract", command=on_extract)
extract_button.grid(row=2, column=0, columnspan=4, pady=10)

root.mainloop()
