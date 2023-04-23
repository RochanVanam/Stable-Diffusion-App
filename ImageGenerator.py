import tkinter as tk
import torch
from diffusers import StableDiffusionPipeline
from PIL import Image, ImageTk

class ImageGeneratorUI:
    def __init__(self):
        self.model_path = "CompVis/stable-diffusion-v1-4"
        self.device = 'cuda'

        self.pipe = StableDiffusionPipeline.from_pretrained(
        self.model_path,
        use_auth_token="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"
        ).to(self.device)
        
        self.root = tk.Tk()
        self.root.title("Image Generator")
        self.root.geometry("400x500")
        
        # Create three buttons for image type selection
        self.button_frame = tk.Frame(self.root, padx=10, pady=10)
        self.button_frame.pack()
        # self.generator = ImageGenerator()
        self.image_type = tk.StringVar(value="Hyperrealistic")
        tk.Button(self.button_frame, text="Hyperrealistic", command=lambda: self.set_image_type("Hyperrealistic")).pack(side=tk.LEFT, padx=5)
        tk.Button(self.button_frame, text="Fantasy", command=lambda: self.set_image_type("Fantasy")).pack(side=tk.LEFT, padx=5)
        tk.Button(self.button_frame, text="Futuristic", command=lambda: self.set_image_type("Futuristic")).pack(side=tk.LEFT, padx=5)
        
        # Display currently selected image type
        self.image_type_label = tk.Label(self.root, textvariable="Current Image Type: " + self.image_type.get())
        self.image_type_label.pack()
        
        # Create text input for image prompt
        self.prompt_frame = tk.Frame(self.root, padx=10, pady=10)
        self.prompt_frame.pack()
        tk.Label(self.prompt_frame, text="Enter image prompt: ").pack(side=tk.LEFT)
        self.prompt_entry = tk.Entry(self.prompt_frame)
        self.prompt_entry.pack(side=tk.LEFT)
        
        # Create button to display generated image
        self.generate_button = tk.Button(self.root, text="Generate Image", command=self.generate_image)
        self.generate_button.pack(pady=10)
        
        # Display generated image
        self.image_canvas = tk.Canvas(self.root, width=300, height=300)
        self.image_canvas.pack()
        
        self.root.mainloop()
        self.root.update()
    
    def set_image_type(self, image_type):
        self.image_type.set(image_type)
        self.image_type_label = tk.Label(self.root, textvariable="Current Image Type: " + self.image_type.get())
        self.image_type_label.pack()
        self.root.update()
        
    def generate_image(self):
        # Generate image based on selected type and prompt input
        # Update image_canvas with generated image

        # img = generator.generate(self.prompt_entry.get())

        prompt = self.prompt_entry.get()
        full_prompt = prompt

        if self.image_type.get() == "Hyperrealistic":
            full_prompt = "A hyperrealistic photo of " + prompt
        if self.image_type.get() == "Fantasy":
            full_prompt = prompt + ", fantasy theme"
        if self.image_type.get() == "Futuristic":
            full_prompt = "A futuristic photo of " + prompt

        img = self.pipe(full_prompt).images[0]
        img.save("result.png")
        tk_image = ImageTk.PhotoImage(Image.open("result.png"))
        self.image_canvas.create_image(300, 300, anchor='se', image=tk_image)
        self.root.mainloop()

if __name__ == "__main__":
    ImageGeneratorUI()
