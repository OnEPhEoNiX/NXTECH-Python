'''
Screenshot Capture

This program captures a screenshot of the current screen using the PyAutoGUI library and saves it to a user-specified location using a tkinter-based GUI.

Requirements:
- PyAutoGUI library
- tkinter library (included in Python standard library)

'''

import pyautogui
import tkinter as tk
from tkinter.filedialog import asksaveasfile

# Create the main window
root = tk.Tk()
root.title("Screenshot Capture")
root.geometry("300x300")

# Create a canvas to hold the GUI elements
canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()

def takeScreenshot():
    '''
    Function to capture the screenshot and save it to a user-specified location.
    '''
    # Capture the screenshot
    myscreenshot = pyautogui.screenshot()

    # Prompt the user to select a save location
    save_path = asksaveasfile(defaultextension='.png')

    # Save the screenshot if a valid save location is selected
    if save_path:
        myscreenshot.save(save_path.name)

# Create a button to trigger the screenshot capture
myButton = tk.Button(text="Take Screenshot", command=takeScreenshot, font=("Arial", 10))
canvas1.create_window(150, 150, window=myButton)

# Start the GUI event loop
root.mainloop()