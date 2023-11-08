import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

# Function to open a file dialog and get the image file
def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
    if file_path:
        img = Image.open(file_path)
        watermark_image(img)

# Function to add a watermark to the image
def watermark_image(img):
    watermark_text = watermark_text_entry.get()
    position = watermark_position_var.get()
    transparency = watermark_transparency_scale.get()
    font_size = float(watermark_size_scale.get())

    img_width, img_height = img.size
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font="arial.ttf",size=font_size)

    text_width = font.getlength(watermark_text)
    text_height = font_size
    if position == "Top Left":
        xy = (10, 10)
    elif position == "Top Right":
        xy = (img_width - text_width - 10, 10)
    elif position == "Bottom Left":
        xy = (10, img_height - text_height - 10)
    else:  # Bottom Right
        xy = (img_width - text_width - 10, img_height - text_height - 10)

    draw.text(xy, watermark_text, fill=(255, 255, 255, int(255 * transparency)), font=font)
    img.show()


# Create the main window
root = tk.Tk()
root.title("Image Watermarking App")

# Create and configure the watermark frame
watermark_frame = tk.Frame(root, padx=10, pady=10)
watermark_frame.pack()

# Watermark text entry
watermark_text_label = tk.Label(watermark_frame, text="WATERMARK ")
watermark_text_label.grid(row=0, column=0)
watermark_text_entry = tk.Entry(watermark_frame)
watermark_text_entry.grid(row=0, column=1)

# Watermark position
watermark_position_label = tk.Label(watermark_frame, text="POSITION")
watermark_position_label.grid(row=1, column=0)
watermark_position_var = tk.StringVar()
watermark_position_var.set("Bottom Right")
watermark_position_menu = tk.OptionMenu(watermark_frame, watermark_position_var, "Top Left", "Top Right", "Bottom Left",
                                        "Bottom Right")
watermark_position_menu.grid(row=1, column=1)

# Watermark transparency
watermark_transparency_label = tk.Label(watermark_frame, text="TRANSPARENCY ")
watermark_transparency_label.grid(row=2, column=0)
watermark_transparency_scale = tk.Scale(watermark_frame, from_=0.0, to=1.0, resolution=0.1, orient="horizontal")
watermark_transparency_scale.set(0.5)
watermark_transparency_scale.grid(row=2, column=1)

# Watermark size
watermark_size_label = tk.Label(watermark_frame, text="SIZE ")
watermark_size_label.grid(row=3, column=0)
watermark_size_scale = tk.Scale(watermark_frame, from_=10, to=100, orient="horizontal")
watermark_size_scale.set(30)
watermark_size_scale.grid(row=3, column=1)

# Open image button
open_button = tk.Button(root, text="WATERMARK IMAGE", command=open_image)
open_button.pack()

root.mainloop()
