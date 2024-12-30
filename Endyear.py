from PIL import Image, ImageTk
import tkinter as tk
import time

# Wish message
print("Wishing you a wonderful year end!")

# Assuming you have a GIF file named 'year_end.gif' in the same directory
gif_path = 'year_end.gif'

# Create a simple GUI to display the GIF
root = tk.Tk()
root.title("Happy Year End!")

gif = Image.open(gif_path)
frames = []

try:
    while True:
        frames.append(ImageTk.PhotoImage(gif.copy()))
        gif.seek(len(frames))  # Move to next frame
except EOFError:
    pass

# Function to update the GIF frame
def update(ind):
    frame = frames[ind]
    ind += 1
    if ind >= len(frames):
        ind = 0
    label.configure(image=frame)
    root.after(gif.info['duration'], update, ind)

label = tk.Label(root)
label.pack()
update(0)

root.mainloop()
