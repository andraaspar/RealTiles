from pprint import pprint
import os


def expand_aliases(sizes: list[int]):
	group__units = load_aliases("units.txt")
	src_edge__target_edges = load_aliases("edges.txt")
	src_tile__target_tiles = load_aliases("tiles.txt")
	# pprint(src_edge__target_edges)
	
	for size in sizes:
		atlas_file = f"../game{size}.atlas"
		print(f'Processing {atlas_file}...')
		
		with open(atlas_file, mode="r", encoding="utf-8") as atlas_file_read:
			lines = atlas_file_read.readlines()
			
		unit_path = f"TileSets/RealTiles{size}/Units/"
		edge_path = f"TileSets/RealTiles{size}/Edges/"
		tile_path = f"TileSets/RealTiles{size}/Tiles/"

		index = 0
		while index < len(lines):
			line = lines[index]
			if line.startswith(unit_path):
				file_name = os.path.basename(line.strip())
				group_name_and_suffix = file_name.split('-', maxsplit=1)
				group_name = group_name_and_suffix[0]
				suffix = '-' + group_name_and_suffix[1] if len(group_name_and_suffix) == 2 else ''
				if group_name in group__units:
					print('Found:', line.strip())
					properties = gather_properties(lines, index)
					next_index = index
					units = group__units[group_name]
					for unit in units:
						next_index = put_lines(lines, next_index, [unit_path + unit + suffix + '\n'] + properties)
						print(' → Expanded unit group:', group_name, '→', unit)
					index = next_index - 1
			elif line.startswith(edge_path):
				src_edge = os.path.basename(line.strip())
				if src_edge in src_edge__target_edges:
					properties = gather_properties(lines, index)
					next_index = index
					next_index = put_lines(lines, next_index, [edge_path + src_edge + '\n'] + properties)
					target_edges = src_edge__target_edges[src_edge]
					for target_edge in target_edges:
						next_index = put_lines(lines, next_index, [edge_path + target_edge + '\n'] + properties)
						print(' → Added edge:', src_edge, '→', target_edge)
					index = next_index - 1
			elif line.startswith(tile_path):
				src_tile = os.path.basename(line.strip())
				if src_tile in src_tile__target_tiles:
					properties = gather_properties(lines, index)
					next_index = index
					next_index = put_lines(lines, next_index, [tile_path + src_tile + '\n'] + properties)
					target_tiles = src_tile__target_tiles[src_tile]
					for target_tile in target_tiles:
						next_index = put_lines(lines, next_index, [tile_path + target_tile + '\n'] + properties)
						print(' → Added tile:', src_tile, '→', target_tile)
					index = next_index - 1
			index += 1

		with open(atlas_file, mode='w', encoding='utf-8') as atlas_file_write:
			atlas_file_write.writelines(lines)
			
		print('Written:', atlas_file)
		
def load_aliases(file_path: str) -> dict[str, list[str]]:
	with open(file_path, mode="r", encoding="utf-8") as file:
		src__targets: dict[str, list[str]] = dict()
		for line in file:
			words = line.split(' → ', maxsplit=1)
			src = words[0]
			target = words[1].strip()
			targets = src__targets[src] if src in src__targets else []
			targets.append(target)
			src__targets[src] = targets
	return src__targets

def gather_properties(lines: list[str], index: int) -> list[str]:
	lines.pop(index)
	properties: list[str] = []
	while (index < len(lines) and not lines[index].startswith('TileSets/')):
		properties.append(lines.pop(index))
	print(' → Properties:', len(properties))
	return properties

def put_lines(lines: list[str], index: int, lines_to_insert: list[str]) -> int:
	for line in lines_to_insert:
		lines.insert(index, line)
		index += 1
	return index