import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import torch
import torchvision.transforms as transforms

def invert_colors_pytorch(input_path, output_path):
 
    img = Image.open(input_path).convert('RGB')

    # Convert the image to a PyTorch tensor
    transform = transforms.Compose([transforms.ToTensor()])
    img_tensor = transform(img).unsqueeze(0)

    # Invert the colors using PyTorch
    inverted_tensor = 1 - img_tensor

    
    inverted_img = transforms.ToPILImage()(inverted_tensor.squeeze())

    
    inverted_img.save(output_path, "PNG")

class ImageInvertApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Inversion App")

        self.frame = tk.Frame(root)
        self.frame.pack()

        self.label = tk.Label(self.frame, text="Select an image:")
        self.label.pack()

        self.image_path = None

        self.browse_button = tk.Button(self.frame, text="Browse", command=self.browse_image)
        self.browse_button.pack()

        self.process_button = tk.Button(self.frame, text="Process Image", command=self.process_image)
        self.process_button.pack()

        self.image_label = tk.Label(self.frame)
        self.image_label.pack()

    def browse_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png")])
        if self.image_path:
            
            img = Image.open(self.image_path)
            img = img.resize((300, 300), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            self.image_label.config(image=img)
            self.image_label.image = img

    def process_image(self):
        if self.image_path:
            output_path = 'output_inverted_pytorch.png'
            invert_colors_pytorch(self.image_path, output_path)
            
           
            img = Image.open(output_path)
            img = img.resize((300, 300), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            self.image_label.config(image=img)
            self.image_label.image = img

if __name__ == '__main__':
    root = tk.Tk()
    app = ImageInvertApp(root)
    root.mainloop()
