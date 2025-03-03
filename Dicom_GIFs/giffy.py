#!/usr/bin/env python3

''' giffy.py

	This takes a folder of GIF files and turns them into an animated GIF.
'''

from PIL import Image
import glob
import contextlib
import subprocess

gifdir = 'dicom/GIF'

# use exit stack to automatically close opened images
with contextlib.ExitStack() as stack:
  # load images
  imgs = (stack.enter_context(Image.open(f)) for f in sorted(glob.glob(gifdir + '/*.gif')))
  # extract first image from iterator
  img = next(imgs)
  # save the animated GIF
  img.save(fp='movie.gif', format='GIF', append_images=imgs, save_all=True, duration=75, loop=0)

# Now create a compressed version of the file using gifsicle.
subprocess.run(['gifsicle', '-O2', '--lossy=200', 'movie.gif', '-o', 'movie-optimised.gif'])
print('Done.')
