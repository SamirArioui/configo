import pytest

from src.reader import *

DATA_DIR = "test/test_data/"
EMPTY_FILE = "test/test_data/empty.txt"
YAML_PATH = "test/test_data/test_loader.yaml"
JSON_PATH = "test/test_data/test_loader.json"
EMPTY_DIR_PATH = "test/test_data/empty_dir"
EXPECTED = {"test": "test"}

class TestConfigRe:
    # TODO: Use pytest fixture to avoid duplicated line of code
    def test_load_yaml(self):
        reader = ConfigReader(YAML_PATH)
        assert reader.data == EXPECTED
    
    def test_load_json(self):
        reader = ConfigReader(JSON_PATH)
        assert reader.data == EXPECTED
    
    def test_load_wrong_file(self):
        reader = ConfigReader(EMPTY_FILE)
        with pytest.raises(ValueError):
            reader.data
    
    def test_is_valid_extension(self):
        reader = ConfigReader(JSON_PATH)
        assert reader._is_valid_extension()
