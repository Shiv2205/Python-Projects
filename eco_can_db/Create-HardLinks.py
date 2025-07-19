import os
import shutil
import json
from pathlib import Path

build_repo_path = lambda name, parts: Path(os.sep.join(parts[:parts.index(name) + 1]))
build_interface_path = lambda path, ext: ([p for p in path.rglob(f"Interface*.{ext}") 
                                          if "Interface" in str(p.parent)][0].parent)
join_path = lambda path, leaf: Path(str(path) + os.sep + leaf)

FILE_EXT  = 'txt'
REPO_NAME = 'eco_can_db'
REPO_PATH = build_repo_path(REPO_NAME, Path(__file__).parts)
INTERFACE_PATH = build_interface_path(REPO_PATH, FILE_EXT)
INETRAFCE_VERSION = '_V2025'

def generate_interface_hardlinks():
  hardlinks_path = join_path(INTERFACE_PATH, 'HardLinks')
  git_keep_path  = join_path(hardlinks_path, '.gitkeep')
  link_map_path  = join_path(INTERFACE_PATH, 'Link_Map.json')

  if hardlinks_path.exists():
    shutil.rmtree(hardlinks_path)

  hardlinks_path.mkdir()
  git_keep_path.touch()
  link_map_path.touch()

  link_map = dict()
  interface_list = INTERFACE_PATH.glob(f"*.{FILE_EXT}")

  for dbc_path in interface_list:
    basename = dbc_path.parts[-1]
    hardlink_name = basename[:basename.index(INETRAFCE_VERSION)] + f".{FILE_EXT}"
    link_path = join_path(hardlinks_path, hardlink_name)

    link_path.hardlink_to(dbc_path)
    link_map[hardlink_name] = str(dbc_path)

  with open(str(link_map_path), 'w') as f_write:
    json.dump(link_map, f_write, indent=4)

if __name__ == "__main__":
  generate_interface_hardlinks()