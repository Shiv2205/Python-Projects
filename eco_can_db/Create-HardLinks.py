import os
import shutil
import json
import subprocess
import sys
from pathlib import Path

build_repo_path = lambda name, parts: Path(os.sep.join(parts[:parts.index(name) + 1]))
build_interface_path = lambda path, ext: ([p for p in path.rglob(f"Interface*.{ext}") 
                                          if "Interface" in str(p.parent)][0].parent)
join_path = lambda path, leaf: Path(str(path) + os.sep + leaf)

FILE_EXT          = 'txt'
REPO_NAME         = 'eco_can_db'
INETRAFCE_VERSION = '_V2025'
REPO_PATH         = build_repo_path(REPO_NAME, Path(__file__).parts)
INTERFACE_PATH    = build_interface_path(REPO_PATH, FILE_EXT)
HARDLINKS_PATH    = join_path(INTERFACE_PATH, 'HardLinks')
LINK_MAP_PATH     = join_path(INTERFACE_PATH, 'Link_Map.json')


def generate_interface_hardlinks():
  """
    Generates the HardLinks directory and the interface hardlinks. 
    Also generates the .gitkeep and Link_Map.json. 
  """
  git_keep_path  = join_path(HARDLINKS_PATH, '.gitkeep')

  if HARDLINKS_PATH.exists():
    shutil.rmtree(HARDLINKS_PATH)

  HARDLINKS_PATH.mkdir()
  LINK_MAP_PATH.touch()
  git_keep_path.touch()

  link_map = dict()
  interface_list = INTERFACE_PATH.glob(f"*.{FILE_EXT}")

  for dbc_path in interface_list:
    basename = dbc_path.parts[-1]
    hardlink_name = basename[:basename.index(INETRAFCE_VERSION)] + f".{FILE_EXT}"
    link_path = join_path(HARDLINKS_PATH, hardlink_name)

    link_path.hardlink_to(dbc_path)
    link_map[hardlink_name] = str(dbc_path)

  with open(str(LINK_MAP_PATH), 'w') as f_write:
    json.dump(link_map, f_write, indent=4)


def test_linkage(target: str) -> bool:
  """
    Test if the hardlinks still point to the target they were created from.
  """
  if not LINK_MAP_PATH.exists():
    return False

  link_map = dict()
  with open(str(LINK_MAP_PATH), 'r') as f_read:
    link_map = json.load(f_read)

  if target not in link_map.keys():
    return False

  drive_letter = HARDLINKS_PATH.drive
  hardlinks = HARDLINKS_PATH.glob(f"*.{FILE_EXT}")
  hardlink_interface = join_path(HARDLINKS_PATH, target)
  original_interface = Path(link_map[target])

  if not original_interface.exists():
    return False

  return original_interface.stat().st_ino == hardlink_interface.stat().st_ino # Compare inode number


if __name__ == "__main__":
  target_dbc = sys.argv[1]

  if not target_dbc:
    generate_interface_hardlinks()
  else:
    is_link_valid = test_linkage(target_dbc)
    print(f"Links valid: {is_link_valid}")
    if not is_link_valid:
      generate_interface_hardlinks()