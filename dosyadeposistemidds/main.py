import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
import shutil
import os

# Folder to store uploaded files
UPLOAD_FOLDER = 'uploads'

# Function to upload file
def upload_file():
    file_path = filedialog.askopenfilename()
    
    if file_path:
        project_folder = os.getcwd()  # Current working directory (project folder)
        upload_folder = os.path.join(project_folder, UPLOAD_FOLDER)
        
        # Ensure the 'uploads' directory exists
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        
        # Copy the selected file to the 'uploads' folder
        destination_path = os.path.join(upload_folder, os.path.basename(file_path))
        shutil.copy(file_path, destination_path)
        
        file_label.config(text=f"File uploaded to: {destination_path}")
        progress_bar['value'] = 100
        progress_label.config(text="Upload Complete")

# Function to delete all files in the uploads directory
def delete_all_files():
    upload_folder = os.path.join(os.getcwd(), UPLOAD_FOLDER)
    
    # Check if the directory exists
    if os.path.exists(upload_folder):
        for filename in os.listdir(upload_folder):
            file_path = os.path.join(upload_folder, filename)
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")
        
        file_label.config(text="All files deleted")
        progress_bar['value'] = 0
        progress_label.config(text="Ready to Upload")
    else:
        file_label.config(text="No files to delete")

# Create the main window
root = tk.Tk()
root.title("File Uploader")
root.geometry("400x300")

# Use ttk for modern-looking widgets
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=10)

upload_image = Image.open('upload_icon.png')

# Resize the image
resized_upload = upload_image.resize((50, 50))  # Adjust size as needed

# Convert the resized image to a PhotoImage format that tkinter can use
upload_image_tk = ImageTk.PhotoImage(resized_upload)

# Upload button
upload_button = ttk.Button(root, text="Select File to Upload", image=upload_image_tk, compound="left", command=upload_file)
upload_button.pack(pady=20)

delete_image = Image.open('trash.png')

# Resize the image
resized_delete = delete_image.resize((50, 50))  # Adjust size as needed

# Convert the resized image to a PhotoImage format that tkinter can use
delete_image_tk = ImageTk.PhotoImage(resized_delete)

# Upload button
delete_button = ttk.Button(root, text="Delete All Files", image=delete_image_tk, compound="left", command=delete_all_files)
delete_button.pack(pady=20)

# Label to display the uploaded file path
file_label = tk.Label(root, text="No file uploaded yet", font=("Arial", 10), fg="blue")
file_label.pack(pady=10)

# Progress bar
progress_bar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress_bar.pack(pady=10)

# Progress label
progress_label = tk.Label(root, text="Ready to Upload", font=("Arial", 10))
progress_label.pack(pady=5)

reset_image = Image.open('restart.png')

# Resize the image
resized_reset = reset_image.resize((50, 50))  # Adjust size as needed

# Convert the resized image to a PhotoImage format that tkinter can use
reset_image_tk = ImageTk.PhotoImage(resized_reset)
# Add a reset button to reset progress
reset_button = ttk.Button(root, image=reset_image_tk,  text="Reset", command=lambda: [progress_bar['value'], progress_label.config(text="Ready to Upload")])
reset_button.pack(pady=10)

# Run the application
root.mainloop()
