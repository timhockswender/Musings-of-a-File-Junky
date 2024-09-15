# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 09:56:58 2024

@author: timho
"""

from PIL import Image
from pathlib import Path

def combine_images(image1_path, image2_path, output_path):
  """Combines two images side-by-side.

  Args:
    image1_path: Path to the first image.
    image2_path: Path to the second image.
    output_path: Path to save the combined image.
  """

  # Open the images
  image1 = Image.open(image1_path)
  image2 = Image.open(image2_path)

  # Calculate the width of the combined image
  combined_width = image1.width + image2.width

  # Create a new image with the combined dimensions
  combined_image = Image.new('RGB', (combined_width, max(image1.height, image2.height)))

  # Paste the images into the combined image
  combined_image.paste(image1, (0, 0))
  combined_image.paste(image2, (image1.width, 0))

  # Save the combined image
  combined_image.save(output_path)

# Example usage:
#image1_path = 'Hbar_Files.png'
#image1_path  = Path('C:\\Python_Stuff\\rrWork') #Testing only
image1_path = Path ( "C:\\Python_Stuff\\Articles_Code_Ideas\\MFJ_1\\Hbar_Files.png")
#image2_path = 'Hbar_no_Python.png'
image2_path = Path("C:\\Python_Stuff\\Articles_Code_Ideas\\MFJ_1\\Hbar_no_Python.png" )

output_path = "C:\\Python_Stuff\\Articles_Code_Ideas\\MFJ_1\\File_count_Comparison.png"

combine_images(image1_path, image2_path, output_path)