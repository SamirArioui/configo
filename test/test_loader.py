from src.loader import *

DATA_DIR = "test/test_data/"
YAML_PATH = "test/test_data/test_loader.yaml"
JSON_PATH = "test/test_data/test_loader.json"
EMPTY_DIR_PATH = "test/test_data/empty_dir"
EXPECTED = {"test": "test"}

class TestSingleFileLoader:
    
    def test_load_yaml(self):
        loader = SingleFileLoader(YAML_PATH)
        assert loader.data() == EXPECTED
    
    def test_load_yaml(self):
        loader = SingleFileLoader(JSON_PATH)
        assert loader.data() == EXPECTED

def test_config_filepath_from_dir():
    dir_path = "test/test_data/"
    expected = [YAML_PATH, JSON_PATH]
    config_files = get_config_file_from_dir(dir_path)
    assert set(config_files) == set(expected)
