#!/usr/bin/env python

# diconvert.py - convert Dicom images to GIFs

import os
import numpy as np
import pydicom
from PIL import Image # PIL is provided by pillow
from pathlib import Path

dicom_dir = 'dicom'

# Interate through the files inside the dicom directory
for _, _, filenames in os.walk(dicom_dir):
  for filename in filenames:
    filepath = Path(os.path.join(dicom_dir, filename))
    if filepath.is_file() and not filepath.name.startswith('.'):
        print(filename)

        # Create a dicom file object
        ds = pydicom.dcmread(filepath)

        # Get the image data from the file
        img_data = ds.pixel_array.astype(float)
        if img_data.max() != 0: # we found image data
        # Dicom image pixels have values that aren't necessarily
        # right for us. Ensure the pixel values all lie in the
        # range 0-255
          scaled_img_data = (np.maximum(img_data, 0) / img_data.max()) * 255
          scaled_img_data = np.uint8(scaled_img_data)
          # Create an image object with this data
          output_image = Image.fromarray(scaled_img_data)

          # Now output the new images in three formats
          for fmt in ['JPG', 'PNG', 'GIF']:
              conv_subdir = os.path.join(dicom_dir, fmt)
              conv_file = filename + '.' + fmt.lower()
              # Following line creates the sub-subdir if needed
              Path(conv_subdir).mkdir(exist_ok=True)
              output_image.save(os.path.join(conv_subdir, conv_file))

print('Done.')
