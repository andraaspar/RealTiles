import os
import subprocess

def pack():
	for file in os.listdir():
		if file.endswith('.tpproj'):
			print('Packing:', file)
			result = subprocess.run(['java', '-jar', 'gdx-texture-packer.jar', '--batch', '--project', file], shell=True)
			if (result.returncode):
				raise Exception("[sta263]")