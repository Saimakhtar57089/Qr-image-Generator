import pyqrcode
import tkinter as tk

# Define the data:
data = "https://github.com/"

# Create QR code:
qr = pyqrcode.create(data)

# Save the QR code in PNG format with proper scaling:
qr.png("githubID.png", scale=5)

# Create Tkinter window:
win = tk.Tk()
win.title("QR Code")

# Load and display the QR code image:
img = tk.PhotoImage(file="githubID.png") 
label = tk.Label(win, image=img)
label.pack()

win.mainloop()
