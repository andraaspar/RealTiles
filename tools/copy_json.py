import os
import shutil

def copy_json(sizes: list[int]):
	src_file = f'../src/jsons/TileSets/RealTiles.json'
	for size in sizes:
		target_file = f'../jsons/TileSets/RealTiles{size}.json'
		print('Copying:', target_file)
		os.makedirs(os.path.dirname(target_file), exist_ok=True)
		shutil.copyfile(src_file, target_file)