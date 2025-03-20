import math
import os
import re
import json

def find_sizes() -> list[int]:
	sizes: list[int] = []
	for file in os.listdir('.'):
		# print(file)
		if file.endswith('.tpproj'):
			result = re.match(r'^.*?(\d+)\.tpproj$', file)
			if result == None:
				print('[sta3hz] File name does not match Regex:', file)
			else:
				size_str = result.group(1)
				if type(size_str) is str and len(size_str) > 0:
					size = int(size_str)
					if size == math.nan:
						raise Exception(f'[sta2mv] NaN size: {json.JSONEncoder().encode(size_str)}')
					sizes.append(size)
	sizes.sort(reverse=True)
	print('Found sizes:', sizes)
	return sizes