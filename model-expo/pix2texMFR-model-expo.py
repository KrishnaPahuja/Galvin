from transformers import Pix2StructProcessor, Pix2StructForConditionalGeneration
from PIL import Image
import torch

def extract_text_from_image(image_path):
   
    processor = Pix2StructProcessor.from_pretrained("google/pix2struct-docvqa-base")
    model = Pix2StructForConditionalGeneration.from_pretrained("google/pix2struct-docvqa-base")

 
    image = Image.open("fromCanvas.png").convert("RGB")

   
    inputs = processor(images=image, return_tensors="pt")

  
    outputs = model.generate(pixel_values=inputs.pixel_values)
    text = processor.decode(outputs[0], skip_special_tokens=True)

    return text

if __name__ == "__main__":
    image_path = "default.png"  
    extracted_text = extract_text_from_image("fromCanvas.png")


