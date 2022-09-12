from configo.loader import *

class TestYamlLoader:

    test_path = "test/test_data/test_loader_yaml.yaml"
    expected = {"test": "test"}
    loader = YamlLoader(test_path)

    def test_load(self):
        data = TestYamlLoader.loader.load()
        assert data == TestYamlLoader.expected
