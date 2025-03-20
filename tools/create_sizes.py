from pprint import pprint
import shutil
from glob import glob
import os
from PIL import Image
from constants import ORIGINAL_SIZE

SRC_PATH = '../src/Images/TileSets/RealTiles/'
TARGET_PATH = '../temp/Images/TileSets/'

def create_sizes(sizes: list[int]):
	pngs = glob(f'**/*.png', root_dir=SRC_PATH, recursive=True)
	for size in sizes:
		size_dir_name = f'RealTiles{size}'
		size_dir = TARGET_PATH + size_dir_name + '/'
		print(f'Creating {size_dir_name}...')
		for png in pngs:
			src_file = os.path.normpath(SRC_PATH + png)
			target_file = os.path.normpath(size_dir + png)
			target_dir = os.path.dirname(target_file)
			if not os.path.exists(target_dir):
				os.makedirs(target_dir)
			if size == ORIGINAL_SIZE:
				print('Copying:', target_file)
				shutil.copyfile(src_file, target_file)
			else:
				ratio = float(size) / float(ORIGINAL_SIZE)
				print('Creating:', target_file)
				with Image.open(src_file) as img:
					new_width = max(1, round(img.width * ratio))
					new_height = max(1, round(img.height * ratio))
					img_resized: Image.Image = img.resize((new_width, new_height), resample=Image.Resampling.BICUBIC)
				pixel_bl = img_resized.getpixel((0, -1))
				if type(pixel_bl) is tuple and pixel_bl[3] == 0:
					# print('Bottom left pixel modified.')
					img_resized.putpixel((0, -1), (255, 255, 255, 1))
				pixel_br = img_resized.getpixel((-1, -1))
				if type(pixel_br) is tuple and pixel_br[3] == 0:
					# print('Bottom right pixel modified.')
					img_resized.putpixel((-1, -1), (255, 255, 255, 1))
				img_resized.save(target_file)