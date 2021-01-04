import unittest
from yaml_pyconf import FlaskConfig
import pathlib
import os


class TestLocalConfig(unittest.TestCase):
    def setUp(self):
        FlaskConfig.destroy()
        os.environ["FLASK_ENV"] = "development"
        sample_conf = pathlib.Path(__file__).parents[1].joinpath("yaml_pyconf").\
            joinpath("samples").joinpath("sample-yaml").joinpath("flask-choose-env.yaml")
        with open("config.yaml", "w") as f:
            with open(sample_conf, "r") as r:
                f.write(r.read())

    def tearDown(self):
        os.environ.pop("FLASK_ENV")
        pathlib.Path("config.yaml").unlink()

    def test_local_config(self):
        conf = FlaskConfig()
