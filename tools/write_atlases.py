import json

def write_atlases(sizes: list[int]):
	size_names: list[str] = []
	for size in sizes:
		size_names.append(f'game{size}')
	content = json.JSONEncoder().encode(size_names)
	with open('../Atlases.json', mode='w', encoding='utf-8') as file:
		file.write(content)
	print('Atlases.json written:', content)