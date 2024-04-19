from utils import take_screenshot, copy_images_with_date
import tkinter as tk
from tkinter import messagebox
import sys
import os

def main():

    # Retrieve the dashboard image
    url1 = 'url1'
    element_id = '#componentContentArea'
    output_filename1 = 'dashboard.png'
    take_screenshot(url1, element_id, output_filename1)

    # Retrieve the image for Report1
    url2 = 'url2'
    element_class1 = '.reportOutput'
    output_filename2 = 'report1.png'
    take_screenshot(url2, element_class1, output_filename2)

    # Retrieve the image for Report2
    url3 = 'url3'
    element_class2 = '.reportOutput'
    output_filename3 = 'report2.png'
    take_screenshot(url3, element_class2, output_filename3)

    # Get the path of the executed script or executable file
    executable_path = sys.argv[0]

    # Convert the path to an absolute path
    absolute_path = os.path.abspath(executable_path)

    # Get the path of the folder containing the executable file
    current_folder = os.path.dirname(absolute_path)

    # Get the username
    username = os.getlogin()

    # Specify the paths for the original folder and the new folder
    source_folder = current_folder
    destination_folder = f"C:\\Users\\{username}\\Box"

    # Retrieve the list of image files
    image_files = [
        "dashboard.png",
        "report1.png",
        "report2.png"
    ]

    # Move the image files
    copy_images_with_date(source_folder, destination_folder, image_files)

    # Action when OK button is clicked
    def on_ok_click():
        root.quit()

    # Create the main window
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Show a popup
    messagebox.showinfo("Completed")

    # Set the action when the OK button is clicked
    root.after(0, on_ok_click)

    # Start the main loop
    root.mainloop()

if __name__ == "__main__":
    main()
