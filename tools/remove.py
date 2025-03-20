import os
import shutil

def remove():
	print
	remove_folder('../jsons')
	remove_folder('../temp')
	for file in os.listdir('..'):
		if file.startswith('game'):
			remove_file('../' + file)
	remove_file('../Atlases.json')
	
def remove_folder(path: str):
	if os.path.exists(path):
		print('Deleting:', path)
		shutil.rmtree(path)
	else:
		print('Does not exist:', path)
		
def remove_file(path: str):
	if os.path.exists(path):
		print('Deleting:', path)
		os.unlink(path)
	else:
		print('Does not exist:', path)