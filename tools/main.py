from create_sizes import create_sizes
from expand_aliases import expand_aliases
from find_sizes import find_sizes
from pack import pack
from copy_json import copy_json
from remove import remove
from write_atlases import write_atlases

remove()

sizes = find_sizes()

create_sizes(sizes)

pack()

expand_aliases(sizes)

copy_json(sizes)

write_atlases(sizes)