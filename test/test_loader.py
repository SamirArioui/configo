from src.loader import *

YAML_PATH = "test/test_data/test_loader.yaml"
JSON_PATH = "test/test_data/test_loader.json"
EMPTY_DIR_PATH = "test/test_data/empty_dir"
EXPECTED = {"test": "test"}

class TestLoader:

    def test_init_yaml(self):
        loader = Loader(YAML_PATH)
        assert loader.path == YAML_PATH
        assert loader.extension == ".yaml"
    
    def test_init_json(sefl):
        loader = Loader(JSON_PATH)
        assert loader.path == JSON_PATH
        assert loader.extension == ".json"
    
    def test_load_yaml(self):
        loader = Loader(YAML_PATH)
        assert loader.load() == EXPECTED
    
    def test_load_json(self):
        loader = Loader(JSON_PATH)
        assert loader.load() == EXPECTED

def test_config_filepath_from_dir():
    dir_path = "test/test_data/"
    expected = [YAML_PATH, JSON_PATH]
    assert get_config_filepath_from_dir(dir_path) == expected
