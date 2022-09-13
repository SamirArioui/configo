import pytest

from configo.utils import *

TEST_FILE_PATH = "test/test_data/empty.txt"
TEST_DIR_PATH = "test/test_data"

def test_get_file_extension_str():
    expected = ".txt"
    result = get_file_extention(TEST_FILE_PATH)
    assert result == expected

def test_get_file_extension_path():
    path = Path(TEST_FILE_PATH)
    expected = ".txt"
    result = get_file_extention(path)
    assert result == expected

def test_get_extention_file_upper():
    path = "test/test_data/empty.TXT"
    expected = ".txt"
    result = get_file_extention(path)
    assert result == expected

def test_get_file_extension_folder():
    with pytest.raises(ValueError) as e_info:
        get_file_extention(TEST_DIR_PATH)
        
def test_is_file():
    assert is_file(TEST_FILE_PATH) == True

def test_is_file_dir():
    assert is_file(TEST_DIR_PATH) == False

def test_is_dir():
    assert is_dir(TEST_DIR_PATH) == True

def test_is_dir_file():
    assert is_dir(TEST_FILE_PATH) == False