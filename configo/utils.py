from pathlib import Path

def get_file_extention(path: str)->str:
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