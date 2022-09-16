from pathlib import Path
from typing import Set

def get_file_extension(path: str)->str:
    if is_file(path):
        extension = Path(path).suffix.lower()
    else:
        raise ValueError(f"{path} is not a file")
    return extension

def is_file(path: str)->bool:
    path_obj = Path(path)
    return path_obj.is_file()

def is_dir(path: str)->bool:
    path_obj = Path(path)
    return path_obj.is_dir()

def get_file_list_from_dir(dir_path: str) -> Set[str]:
    path = Path(dir_path)
    file_list = set()
    for p in path.iterdir():
        if is_file(p):
            file_list.add(str(p))
    return file_list
