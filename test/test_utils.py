import pytest

from src.utils import *

EMPTY_FILE_PATH = "test/test_data/empty.txt"
YAML_PATH = "test/test_data/test_loader.yaml"
JSON_PATH = "test/test_data/test_loader.json"
EMPTY_DIR_PATH = "test/test_data/empty_dir"
DIR_PATH = "test/test_data"


def test_get_file_extension_str():
    expected = ".txt"
    result = get_file_extension(EMPTY_FILE_PATH)
    assert result == expected

def test_get_file_extension_path():
    path = Path(EMPTY_FILE_PATH)
    expected = ".txt"
    result = get_file_extension(path)
    assert result == expected

def test_get_extention_file_upper():
    path = "test/test_data/empty.TXT"
    expected = ".txt"
    result = get_file_extension(path)
    assert result == expected

def test_get_file_extension_folder():
    with pytest.raises(ValueError) as e_info:
        get_file_extension(DIR_PATH)
        
def test_is_file():
    assert is_file(EMPTY_FILE_PATH) == True

def test_is_file_dir():
    assert is_file(DIR_PATH) == False

def test_is_dir():
    assert is_dir(DIR_PATH) == True

def test_is_dir_file():
    assert is_dir(EMPTY_FILE_PATH) == False

def test_get_filelist_from_dir():
    expected = {EMPTY_FILE_PATH, YAML_PATH, JSON_PATH}
    assert get_file_list_from_dir(DIR_PATH) == expected